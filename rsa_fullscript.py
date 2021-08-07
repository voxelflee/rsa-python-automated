import sys, math, pathlib, random
from rsa_keygen_function import RSAKeygen
from rsa_gen_primes import findPrimes
def extractInfo(flag, extraction_range):    # Extract <extraction_range> items after <flag>
    return_list = []
    for argument in range(extraction_range):
        info_index = sys.argv.index(flag) + (argument + 1)
        return_list.append(sys.argv[info_index])
    return return_list

    
def cryptData(dkey, dpq, dmessage):
    key = int(dkey)
    pq = int(dpq)
    message = int(dmessage)
    power_crypt = message ** key
    crypt_data = power_crypt % pq
    return crypt_data

def helpInfo():    # If no arguments are passed along with --help
    print("Python RSA script version 0.1.2\n")
    print("This script will help you generate keys, encrypt and decrypt messages.")
    print("Type --help <command> to review required variables and see additional information.")
    print("\n")
    print("--gen-key <--gen-primes (see below)> or <--mod (see below)> - generate a new keypair\n")
    print("--gen-primes <start (minimum number of digits in primess [integer])> <end (maximum number of digits in primes [integer])> - generate primes for key derivation\n")
    print("--mod <prime one> <prime two> - pass two prime numbers to the key generator\n")

def helpPage(command):
    if (command == "--gen-key") or (command == "--generate-key"):
        print()
    elif (command == "--help"):
        print()
    elif (command == "--gen-primes") or (command == "--generate-primes"):
        print()
    elif (command == "--max-primes"):
        print()
    elif (command == "--mod"):
        print()
    elif (command == "-e") or (command == "--encrypt"):
        print("This variable takes in an integer that is then encrypted using the RSA function")
        print("Usage:", command, "<message (integer)>")
        print("Note: this does the same thing as -d")
    elif (command == "-d") or (command == "--decrypt"):
        print("This variable takes in an integer that is then decrypted using the RSA function")
        print("Usage:", command, "<message (integer)>")
        print("Note: this does the same thing as -e")
    elif (command == "-x"):
        print("This variable is used to modify the RSA generation multiplier")
        print("Usage: -x <integer>")    

def saveKeygenToFile(keygen_results, print_only, save_path=''):    # print_only is a boolean
    if not(print_only):
        save_path = extractInfo('--output', 1)[0]
        if save_path[0] != '/' and save_path[0] != '~':
            full_save_path = str(pathlib.Path().absolute()) + '/' + save_path
        else: full_save_path = save_path
        keygen_output_file = open(full_save_path, 'w')
        keygen_output_file.write(f'pub(x): {keygen_results[0]}\nsec(y): {keygen_results[1]}\nmod(primes): {keygen_results[2]}\n')
        return_sentence_filepath = "Saved to: " + full_save_path
        return return_sentence_filepath
    else:
        return_print_list = ['pub(x): ', str(keygen_results[0]), 'sec(y): ', str(keygen_results[1]), 'mod(primes): ', str(keygen_results[2])]
        return return_print_list



if len(sys.argv) < 2:
    print("Please provide at least one argument")
        
if '--help' in sys.argv:
    help_noargs = False
    try: help_command = extractInfo('--help', 1)[0]
    except IndexError: help_noargs = True
    if help_noargs: helpInfo()
    else: helpPage(help_command)

if '--gen-key' in sys.argv:
    if '--max-primes' in sys.argv:
        maximum_primes_set = True
        maximum_primes_passed = int(extractInfo('--max-primes', 1)[0])
    else: maximum_primes_set = False
    primes_generated = False
    if '--gen-primes' in sys.argv:
        primes_generated = True
        min_max_characters = extractInfo('--gen-primes', 2)
        if maximum_primes_set:
            extracted_primes_many = findPrimes(int(min_max_characters[0]), int(min_max_characters[1]), maximum_primes=maximum_primes_passed)
            extracted_primes = [random.choice(extracted_primes_many), random.choice(extracted_primes_many)]
        else:
            extracted_primes_many = findPrimes(int(min_max_characters[0]), int(min_max_characters[1]))
            extracted_primes = [random.choice(extracted_primes_many), random.choice(extracted_primes_many)]
        not_different = False
        if extracted_primes[0] == extracted_primes[1]: not_different = True
        while not_different:
            extracted_primes[1] = random.choice(extracted_primes_many)
            if not(extracted_primes[0] == extracted_primes[1]): not_different = True
    if '--mod' in sys.argv and primes_generated == True:
        raise ValueError('Conflicting commands! Halting...')
    if '--mod' in sys.argv and primes_generated == False:
        extracted_primes = extractInfo('--mod', 2)
    if '--mod' not in sys.argv and primes_generated == False:
        raise ValueError('No primes provided! Halting...')
    prime_one = int(extracted_primes[0])
    prime_two = int(extracted_primes[1])
    if '-x' in sys.argv: x = int(extractInfo('-x', 1)[0])
    if not '-x' in sys.argv: x = 1
    keygen_results = RSAKeygen(prime_one, prime_two, x)
    if type(keygen_results) == 'str':
        raise ValueError(keygen_results)
    #print('DEBUG: ', keygen_results, sep='')

    #print_file_path = False
    if ('--output' in sys.argv) and not('--print' in sys.argv):
        save_path_passed = extractInfo('--output', 1)[0]
        file_path_success = saveKeygenToFile(keygen_results, False, save_path_passed)
    elif ('--print' in sys.argv) and ('--output' in sys.argv):
        save_path_passed = extractInfo('--output', 1)[0]
        print_list = saveKeygenToFile(keygen_results, True)
        for output_item in range(len(print_list)):
            if output_item == 0:
                print(print_list[output_item], end='')
            elif output_item % 2 == 1 and output_item != 0:
                print(print_list[output_item], end='\n')
            else: print(print_list[output_item], end='')
        saveKeygenToFile(keygen_results, False, save_path_passed)
    elif (('--print' in sys.argv) and not('--output' in sys.argv)) or (not('--print' in sys.argv) and not('--output' in sys.argv)):
        print_list = saveKeygenToFile(keygen_results, True)
        for output_item in range(len(print_list)):
            if output_item == 0:
                print(print_list[output_item], end='')
            elif output_item % 2 == 1 and output_item != 0:
                print(print_list[output_item], end='\n')
            else: print(print_list[output_item], end='')
        
if '-e' in sys.argv or '-d' in sys.argv:
    if '-e' in sys.argv:
        message = extractInfo('-e', 1)[0]
    else: message = extractInfo('-d', 1)[0]
    if '--key' in sys.argv:
        key = extractInfo('--key', 1)[0]
    if '--key' not in sys.argv:
        raise ValueError('No key (--key) provided! Halting...')
    if '--mod' in sys.argv:
        pq = extractInfo('--mod', 1)[0]
    if '--mod' not in sys.argv:
        raise ValueError('No N (--mod) provided! Halting...')
    
    crypt_data = cryptData(key, pq, message)
    print(crypt_data)
    
    if '--output' in sys.argv:
        save_path_passed = extractInfo('--output', 1)[0]
        if save_path_passed[0] != '/' and save_path_passed[0] != '~':
            full_save_path = str(pathlib.Path().absolute()) + '/' + save_path_passed
        else: full_save_path = save_path_passed
        crypt_output_file = open(full_save_path, 'w')
        crypt_output_file.write(f'{crypt_data}\n')

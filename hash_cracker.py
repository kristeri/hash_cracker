import hashlib
import string
import itertools

def crack_password(hash, salt, filename):
    with open(filename) as f:
        for line in f:
            line_strip = line.strip('\n')
            guess = line_strip + salt

            available_algorithms = hashlib.algorithms_guaranteed
            for hashing_algorithm in available_algorithms:
                # Skip shake algorithms due to dynamic length outputs resulting in errors
                if hashing_algorithm.startswith('shake_'):
                    continue
                algorithm_guess = getattr(hashlib, hashing_algorithm)(guess.encode('utf-8')).hexdigest()
                if algorithm_guess == hash:
                    print("Found!")
                    print("Password is: " + line_strip)
                    print("Hashing algorithm used: " + hashing_algorithm)
                    return

                if line == '':
                    print("Password not found!")
                    return


hash = input('Enter hash: ')
salt = input('Enter salt (Press enter if no salt used): ')
filename = input('Enter filename containing guesses: ')
crack_password(hash, salt, filename)

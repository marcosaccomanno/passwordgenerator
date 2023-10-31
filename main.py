import random
from colorama import Fore

def shuffle(string):
    '''
    Takes a string and shuffles it.
    '''
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

def uppercaseCharacters(counter):
    '''
    Generates n random uppercase letters and appends them
    to the password list.
    '''
    while counter <= number_of_uppercase:
        password.append(chr(random.randint(65, 90)))
        counter += 1

def lowercaseCharacters(counter):
    '''
    Generates n random lowercase letters and appends them
    to the password list.
    '''
    while counter <= number_of_lowercase:
        password.append(chr(random.randint(97, 122)))
        counter += 1

def numberCharacters(counter):
    '''
    Generates n random numbers and appends them
    to the password list.
    '''
    while counter <= number_of_numbers:
        password.append(chr(random.randint(48, 57)))
        counter += 1

def specialCharacters(counter):
    '''
    Generates n random special characters and appends them
    to the password list.
    '''
    while counter <= number_of_special:
        password.append(chr(random.randint(33, 38)))
        counter += 1

if __name__ == "__main__":

    print(Fore.YELLOW + '-------------PASSWORD GENERATOR-------------' + Fore.RESET)

    # ask user for number of characters
    number_of_uppercase = int(input('Uppercase letters: '))
    number_of_lowercase = int(input('Lowercase letters: '))
    number_of_numbers = int(input('Numbers: '))
    number_of_special = int(input('Special characters: '))

    # sets initial counter
    character_counter = 1

    # initial password characters (empty)
    password = []

    # generates characters
    uppercaseCharacters(character_counter)
    lowercaseCharacters(character_counter)
    numberCharacters(character_counter)
    specialCharacters(character_counter)

    # shuffles password characters
    password = shuffle(password)

    print(Fore.YELLOW + '--------------------------------------------' + Fore.RESET)
    print(f'Password: {password}')
    print(f'Generated password is {len(password)} characters long.')
    print(Fore.YELLOW + '--------------------------------------------' + Fore.RESET)

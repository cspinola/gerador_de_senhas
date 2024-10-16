import random
import string

# This function ensures that users just insert numbers on characters password size
def only_interger_acceptance():

    words_or_strings = True

    while words_or_strings:
        
        try:
            number = int(input('Type a interger: '))
            words_or_strings = False

        except ValueError:

            print("Just numbers 0 to 9 are allowed, try again!")

            words_or_strings = True

    return number


# This function ensures that users just type y - for yes and n for no 
def answer_y_or_n_only():

    answer_not_expected = True
    
    while answer_not_expected:

        user_answer = str(input('Type (y/n): '))

        if (user_answer == 'y' ) or (user_answer == 'n' ):
            answer_not_expected = False

        else:

            print('Just (y/n) is allowed, try again!')
            answer_not_expected = True
    
    return user_answer




def password_characters():


    print('Should the password contain capital letters?')

    capital_letters  = answer_y_or_n_only()


    if (capital_letters == 'y'):

        characters = string.ascii_letters


    else: 

        characters = string.ascii_lowercase


    print('Should the password contain 0 to 9 numbers?')

    numbers = answer_y_or_n_only()


    if (numbers == 'y'):

        characters += string.digits
        

    print('Should the password contain special characters?')
    special_characters = answer_y_or_n_only()
    
    if (special_characters == 'y'):

        characters += string.punctuation

    return characters


def password_generator(pass_size, not_unique):

    # as senhas contém letras e números e caractres especiais
    caracteres = password_characters()
    
    # If the characters can repeat on password
    if (not_unique == 'y'):

        random_password = random.choices(caracteres, k = pass_size)

    elif (not_unique == 'n'):
        random_password = random.sample(caracteres, k = pass_size)

    # Change a list to string:
    password = ', '.join(random_password)
    password_str = password.replace(", ","")
    print(f'Your random password is: {password_str}')
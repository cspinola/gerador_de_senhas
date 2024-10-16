from funcoes import *
continue_answ = True

while continue_answ:

    print('Security Password Generator')

    print('Shoud password characters repeat?')
    unique_or_not = answer_y_or_n_only()

    print('Which is the password size?')
    password_size = only_interger_acceptance()
    
    password_generator(pass_size = password_size,not_unique = unique_or_not)

    print('Would you like to generate another random password?')

    generate_another_password = answer_y_or_n_only()

    if generate_another_password == 'n':

        continue_answ = False
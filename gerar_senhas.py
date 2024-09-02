import random
import string

random.seed(11)

caracteres = string.ascii_letters + string.digits + string.punctuation
sorteio = random.choices(caracteres, k=9)
senha = ', '.join(sorteio)
nova_senha = senha.replace(",","")
print(nova_senha.replace(" ",""))

'''
continuar = True
while continuar:
    print('Gerador de Senhas Seguras')

    a = input('Deseja que os caracteres da senha se repitam s/n: ')

    if (a == 's'):
        k = int(input('Qual o número de caracteres que a senha deve conter: '))
        print(random.choices(caracteres, k).replace(",",""))
   
    else:
        k = int(input('Qual o número de caracteres que a senha deve conter: '))
        print(random.sample(caracteres, k).replace(",",""))

    c = input('Deseja gerar outra senha (s/n): ')

    if c == 's':
        continuar = True
    elif c == 'n':
        continuar = False
    else:
        print('Entrada inválida!!!')

'''
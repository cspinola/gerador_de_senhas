
from funcoes import *

continuar = True

while continuar:
    print('Gerador de Senhas Seguras')

    print('Deseja que os caracteres da senha possam se repitir (s/n): ')
    a = resposta()
    print('Qual o número de caracteres que a senha deve conter: ')
    i = retornaInteiro()
    
    gera_senha(num_caracteres = i,repeticao = a)

    print('Deseja gerar outra senha (s/n): ')
    c = resposta()

    if c == 'n':
        continuar = False
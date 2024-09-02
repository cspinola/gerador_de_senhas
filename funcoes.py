import random
import string

def retornaInteiro():

    n_passou = True
    while n_passou:
        
        try:
            numero = int(input('Digite um número inteiro: '))
            n_passou = False
        except ValueError:
            print("O valor informado não é um inteiro!")
            n_passou = True
    
    return numero


def resposta():
    n_passou = True
    while n_passou:
        resposta = str(input('Digite (s/n): '))
        if (resposta == 's' ) or (resposta == 'n' ):
            n_passou = False
        else:
            print('O valor digitado não é s/n!')
            n_passou = True
    
    return resposta

# Como os valores gerados estão em uma lista com os caracteres separados por 
# vírgulas essa função organiza em um ínico string e tamanho k



def caracteres_senha():
    
    print('Deseja que a senha contenha letras maúsculas?')
    maiusculas = resposta()
    
    if (maiusculas== 's'):
        caracteres = string.ascii_letters
    else: 
        caracteres = string.ascii_lowercase
    
    print('Deseja que a senha contenha números?')
    numeros = resposta()
    
    if (numeros == 's'):
        caracteres += string.digits
        
    print('Deseja que a senha contenha caracteres especiais?')
    caracteres_especiais = resposta()
    
    if (caracteres_especiais== 's'):
        caracteres += string.punctuation

    return caracteres


def gera_senha(num_caracteres, repeticao):

    # as senhas contém letras e números e caractres especiais

    caracteres = caracteres_senha()
    
    if (repeticao == 's'):

        sorteio = random.choices(caracteres, k = num_caracteres)
    
    elif (repeticao == 'n'):
        sorteio = random.sample(caracteres, k = num_caracteres)
    
    # transformando lista em string:
    senha = ', '.join(sorteio)
    senha_str = senha.replace(", ","")

    print('Segue a senha segura gerada: ')
    print(senha_str)
    #return senha_str
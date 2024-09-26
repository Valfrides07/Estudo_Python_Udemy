# Uma função básica

def verificacao(nome):

    while True:
        
        if nome.isalpha():
            print(f'O nome: {nome} esta escrito corretamente.')
            break
        
        else:
            print(f'O nome: {nome} não contém letras, digite novamente.')
            if nome.isalpha() == False:
                nome = input('Digite o seu nome corretamente: ')
                continue 
            
nome = input('Digite o seu nome: ')
verificacao(nome)                

# nome = input('Digite o seu nome: ')
# verificacao(nome)

# Criar uma função de verificacao

def numeros_leitura():
    while True:
        numeros = input('Digite um número, sem conter caracteres especias: ')
        try:
            numeros = int(numeros)
            print (f'O número: {numeros}, está correto.')
            break
        except ValueError:
            try:
                while True:
                    numero_float = float(numeros)
                    print(f'O número {numero_float} é um número de ponto flutuante válido.')
                    break

            except ValueError:
                numeros = str(numeros)
                print('Entrada inválida! Por favor, insira um número válido (sem caracteres especiais).')

numeros_leitura()

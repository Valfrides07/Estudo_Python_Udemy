# Segundo tratamento de erros utiliznado 'raise'

arm_nome = []
def tratamento_nome(nome):
    if nome.isdigit():  # Se o nome for composto apenas por dígitos, levanta uma exceçãoif isinstance(nome, int): # Se nome nao for um int retorna raise  
        raise ValueError('Digite um nome que seja válido.')
    return nome.title() #A cada letra no inicio de cada palavra é iniciada com letra maíscula.
           

while True:
    try:
        nome = input('Digite o seu nome: ')         


        # Chama a função para a verificação do nome    
        verificacao_nome = tratamento_nome(nome)

       
        print(f'O nome {nome}, é válido e foi armazenado com sucesso!')
        arm_nome.append(verificacao_nome)
        break
    
    except ValueError:
        print('Digite um valor que seja válido.')
        continue
    
    
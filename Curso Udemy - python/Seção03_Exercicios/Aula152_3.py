# Validação de numero Par

def validacao_par(numero_par):
    while True:
        try:
            numero_par = int(numero_par)
            if numero_par % 2 == 0:
                print(f'O número {numero_par} é Par.')
                return numero_par
            
            else:
                print(f'O {numero_par} não é um número Par')
                numero_par = int(input('Digite novamente o número:')) #O uso da mesma variavel é para atribuir o novo valor digitado pelo usuario         
            
        except ValueError:
            print('O dado digitado não é válido.')
            numero_par = int(input('Digite novamente o número:'))

numero_par = input("Digite um número para verificação: ")
validacao_par(numero_par)
        

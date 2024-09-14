# Tratamento de erros utiliznado 'raise'. Validação se o numero digitado está entre o requisito.

def tratamento_erros_numero(numero):
    if numero < 1 or numero >= 11:
        # raise é usado para lançar a exceção personalizada se o número estiver fora do intervalo permitido.
        raise ValueError("Numero digitado não atende aos parametros esabelecidos.") #

    else:
        return print(f"O número {numero} digitado, está dentro dos parametros estabelecidos.")

    
while True:
    entrada_numero = input(" Digite um número que esteja entre 1-10: ")
    
    try:
        # Converte o dado digitado pelo usuario para inteiro    
        numero = int(entrada_numero)
        
        try:
            # Essa função é responsável por verificar se o número esta de acordo. Se o número não estiver, ela levantará uma exceção ValueError.
            tratamento_erros_numero(numero)
            break
        
        except ValueError :
            print('Valor digitado maior que o permitido.')
    
    except ValueError:
        print('Os dados digitados não são validos.Por favor, insira um número válido.')
    
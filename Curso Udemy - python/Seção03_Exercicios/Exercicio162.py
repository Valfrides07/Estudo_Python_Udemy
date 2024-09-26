# Adiando execução de funções

def soma(x, y):
    return x + y

def divisao(x, y):
    return x/y

# Criar um função que execute as duas
def criar_funcao(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna

soma_num = criar_funcao(soma, 10)
divisao_num = criar_funcao(divisao, 50)

print (soma_num(10))
print(divisao_num(4))
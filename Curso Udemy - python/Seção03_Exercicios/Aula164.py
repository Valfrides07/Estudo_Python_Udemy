# utilizanção de uma palavra-chave (keyword)=  nonlocal

def concatenar(string_inicial):
    valor_final = string_inicial


    def interna(valor_p_concatenar):
        nonlocal valor_final
        valor_final += valor_p_concatenar
        return valor_final
    return interna

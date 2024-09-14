# Isinstace para verificar se um item é de determinado tipo

tipo_lista = [
    1,'a', 200,32,'2hrs',{'nome': 'Val'},True,['Nome'],[2,0,0], {1, 2, 3},
]

for item in tipo_lista:
    if isinstance(item, set): # 'isinstance' verifica se o 'item' é do tipo 'set'
        print(item, isinstance(item, set))
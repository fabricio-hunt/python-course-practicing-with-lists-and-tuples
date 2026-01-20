"""Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado."""


lista_despensa = ['leite', 'arroz', 'feijão', 'macarrão', 'açúcar', 'sal', 'óleo', 'café', 'chá', 'biscoitos']

def verificar_item(item):
    if item in lista_despensa:
        return f"O item '{item}' já está na despensa."
    else:
        return f"O item '{item}' não está na despensa e precisa ser comprado."
    
# Exemplo de uso
item_desejado = input("Digite o item que você deseja verificar na despensa: ")
resultado = verificar_item(item_desejado)
print(resultado)
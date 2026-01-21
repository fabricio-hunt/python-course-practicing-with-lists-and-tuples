"""Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada? """

convidados = ['Ana', 'Pedro', 'Carlos']

novo_convidado = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição (0, 1, 2, ...) onde deseja inserir o novo convidado: "))
convidados.insert(posicao, novo_convidado)
print("Lista atualizada de convidados:", convidados)

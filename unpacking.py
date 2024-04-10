lista_compras = ["Arroz", "Feijão", "Cebola", "Alho", "Tomate"]

a, *rest = lista_compras

a, *middle, c = lista_compras

print(a, rest)
print(a, middle, c)

for index, item in enumerate(lista_compras):
    print(index, item)
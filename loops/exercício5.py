lista = []

quantidade = int(input("Digite a quantidade de numeros que ira digitar "))

for i in range(quantidade):
    numero_usuario = int(input("Digite numero "))
    lista.append(numero_usuario)

lista_ordenada = sorted(lista)
ordem = quantidade-1
print(lista_ordenada[ordem])
lista = []
quantidade_usuario = int(input("Digite a quantidade de numeros que ira digitar "))

for i in range(quantidade_usuario):
    numero_usuario = int(input("Digite o numero "))

    lista.append(numero_usuario)

for verifica in (lista):
    if verifica%2==0:
        print(f'{verifica} é par')
    elif verifica%2!=0:
        print(f'{verifica} é impar')


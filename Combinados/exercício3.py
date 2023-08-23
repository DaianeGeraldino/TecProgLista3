import random
acerto = True

numero_aleatorio = random.randint(1,100)

while acerto:
    usuario = int(input("Digite um número "))
    if numero_aleatorio == usuario:
        print("Você acertou")
        acerto = False
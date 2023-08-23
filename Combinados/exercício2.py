numero_usuario = []
parar = True

while parar:
    numero_usuario.append(int(input("Digite um número ")))
    cod_parada = int(input("Digite 1 para continuar e 2 para parar "))
    if cod_parada==2:
        parar = False

numero_ordenado = sorted(numero_usuario)

print(numero_ordenado[0])


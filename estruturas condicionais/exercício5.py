lado_um = float(input("Digite o primeiro lado do triângulo "))
lado_dois = float(input("Digite o segundo lado do triângulo "))
lado_tres = float(input("Digite o terceiro lado do triângulo "))

if lado_um == lado_dois and lado_dois == lado_tres:
    print('O triângulo é equilátero')
elif lado_um == lado_dois or lado_dois == lado_tres or lado_tres == lado_um:
    print("O triângulo é isósceles")
elif lado_um != lado_dois and lado_dois != lado_tres:
    print("O triângulo é escaleno")
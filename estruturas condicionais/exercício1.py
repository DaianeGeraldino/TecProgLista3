numero_usuario = int(input("Digite um numero "))

if numero_usuario<0:
    print(f'O número {numero_usuario} é negativo')
elif numero_usuario>0:
    print(f'O número {numero_usuario} é positivo')
elif numero_usuario==0:
    print(f'O número {numero_usuario} é zero')
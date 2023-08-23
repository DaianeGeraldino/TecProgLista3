ano = input("Digite um ano ")
ano_calculo = int(ano[2:])

if ano_calculo%4==0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} é normal')
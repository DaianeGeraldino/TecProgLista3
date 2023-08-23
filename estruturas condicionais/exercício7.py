ponto_x = float(input("Digite o ponto x do plano cartesiano"))
ponto_y = float(input("Digite o ponto y do plano cartesiano"))

if ponto_x>0 and ponto_y >0:
    print("primeiro quadrante")
elif ponto_x<0 and ponto_y>0:
    print('segundo quadrante')
elif ponto_x<0 and ponto_y<0:
    print('terceiro quadrante')
elif ponto_x>0 and ponto_y<0:
    print('quarto quadrante')
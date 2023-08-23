parar = True
nota_aluno = []

while parar:
    nota_aluno.append(float(input("Digite a nota do aluno ")))
    cod_parada = int(input("Digite 1 para continuar digitando e 2 para parar "))
    if cod_parada==2:
        parar = False

tamanho = len(nota_aluno)
soma = 0

for i in nota_aluno:
    soma += i

media = soma/tamanho
print(media)


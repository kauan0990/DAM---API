Saque = input("Insira o valor do saque min 3 digitos?")
posição1 = int(Saque[0])
posição2 = int(Saque[1])
posição3 = int(Saque[2])

moeda = 0
nota5 = 0
nota10 = 0
nota50 = 0

if posição1 != 0:
    nota100 = posição1
else:
    nota100 = 0

if posição2 == 5:
    nota50 +=1
elif posição2 < 5:
    nota10 += posição2
else:
    nota50 += 1
    nota10 += posição2 - 5

if posição3 == 5:
    nota5 +=1
elif posição3 < 5:
    moeda += posição3
else:
    nota5 += 1
    moeda += posição3 - 5

print(f"O valor do saque será de {Saque}, sendo {nota100} notas de R100, {nota50} notas de R50, {nota10} notas de R10, {nota5} notas de R5 e {moeda} moedas")
lista = []
var_Soma = 0
Media = 0
valor = int(input("Infome um numero: "))

while valor != -1:
    lista.append(valor)
    valor = int(input("Infome um numero: "))


print(len(lista))
print (lista)
for i in range(len(lista) - 1, -1, -1):
    print(lista[i], end= " ")
    var_Soma += (lista[i])

print(f"\n{var_Soma}")    

media = var_Soma/len(lista)

print(f"{media} Media")

for i in range(len(lista)):
    if lista[i] > media:
        print(lista[i], end= " ")
Nota1 = float(input("Nota 1 :"))
Nota2 = float(input("Nota 2 :"))

Media = (Nota1+Nota2)/2

if Media >= 9:
    notaF = "A"
    Mens = "APROVADO"

elif Media >=7.5:
    notaF = "B"
    Mens = "APROVADO"

elif Media >= 6:
    notaF = "C"
    Mens = "APROVADO"

elif Media >= 4:
    notaF = "D"
    Mens = "REPROVADO"  

else:
    notaF = "E"
    Mens = "REPROVADO"

print(f"Media: {Media:.2f} - Nota Final: {notaF} - {Mens}")
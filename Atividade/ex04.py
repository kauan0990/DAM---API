# gabarito

resposta1 = 'B'
resposta2 = 'D'
resposta3 = 'A'
resposta4 = 'E'
resposta5 = 'C'
resposta6 = 'B'
resposta7 = 'C'
resposta8 = 'E'
resposta9 = 'C'
resposta10 = 'E'

alunos = 0
Notas = []

# Questões
NovoAluno = input(f'Deseja conferir a prova? ')
while NovoAluno == "sim":
    alunos += 1
    questão1 = input(f'Insira a resposta da questão1: (A,B,C,D,E)')
    questão2 = input(f'Insira a resposta da questão2: (A,B,C,D,E)')
    questão3 = input(f'Insira a resposta da questão3: (A,B,C,D,E)')
    questão4 = input(f'Insira a resposta da questão4: (A,B,C,D,E)')
    questão5 = input(f'Insira a resposta da questão5: (A,B,C,D,E)')
    questão6 = input(f'Insira a resposta da questão6: (A,B,C,D,E)')
    questão7 = input(f'Insira a resposta da questão7: (A,B,C,D,E)')
    questão8 = input(f'Insira a resposta da questão8: (A,B,C,D,E)')
    questão9 = input(f'Insira a resposta da questão9: (A,B,C,D,E)')
    questão10 = input(f'Insira a resposta da questão10: (A,B,C,D,E)')

    pontos = 0

    if questão1 == resposta1:
        pontos += 1
    if questão2 == resposta2:
        pontos +=1
    if questão3 == resposta3:
        pontos +=1
    if questão4 == resposta4:
        pontos +=1
    if questão5 == resposta5:
        pontos +=1
    if questão6 == resposta6:
        pontos +=1
    if questão7 == resposta7:
        pontos +=1
    if questão8 == resposta8:
        pontos +=1
    if questão9 == resposta9:
        pontos +=1
    if questão10 == resposta10:
        pontos +=1
    
    Notas.append(pontos)
    
    NovoAluno = input(f'Quer conferir a nota de outro aluno? ')

maior = 0
menor = 0
soma = 0
for i in range(len(Notas)):
    soma += Notas[i - 1]
    if i == 1:
        if Notas[i -1] > Notas[i]:
            maior = Notas[i - 1]
            menor = Notas[i]
        else:
            maior = Notas[i]
            menor = Notas[i - 1]
    else:
        if Notas[i] > maior:
            maior = Notas[i]
        if Notas[i] < menor:
            menor = Notas[i]
        
media = soma / len(Notas)

print(f'O maior numero de acertos foi de {maior};\n O menor numero de acertos foi de {menor};\n O total de alunos foi de {alunos};\n A media da turma é de {media}')
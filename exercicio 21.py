import random

aluno1 = input("Insira o nome do primeiro aluno: ")
aluno2 = input("Insira o nome do segundo aluno: ")
aluno3 = input("Insira o nome do terceiro aluno: ")
aluno4 = input("Insira o nome do quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

print("A ordem de apresentação dos trabalhos será:")
for i, aluno in enumerate(alunos):
    print(i + 1, aluno)
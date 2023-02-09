import random

aluno1 = input("Insira o nome do primeiro aluno: ")
aluno2 = input("Insira o nome do segundo aluno: ")
aluno3 = input("Insira o nome do terceiro aluno: ")
aluno4 = input("Insira o nome do quarto aluno: ")
aluno5 = input("Insira o nome do cinco aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
sorteado = random.choice(alunos)

print("O aluno escolhido para apagar o quadro é:", sorteado)
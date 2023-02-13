frase = str(input("Insira uma frase: ")).strip()

frase = frase.upper()
contagem = frase.count("A")
primeira_posicao = frase.find('A')+1
ultima_posicao = frase.rfind('A')

print("A letra 'A' aparece", contagem, "vezes na frase.")
print("A primeira ocorrência de 'A' está na posição", primeira_posicao)
print("A última ocorrência de 'A' está na posição", ultima_posicao)
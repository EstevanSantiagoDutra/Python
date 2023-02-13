#FATIAMENTO DE STRING:
#O ultimo valor não entra na contagem, ex: 9:20 (vai selecionar as letras do 9 até o 19
#Para saltar de 2 em 2, ex: 9:20:2
#Omitir o inicio começa do 0, ex: frase(:5) vai fatiar do 0 até o 4
#Omitir o final começa e não tem fim, ex: frase(15:) vai fatiar do 15 até o fim
#ANALISE:
#len(frase) comprimento de frase > ver informar o espaço total ou comprimento total da frase.
#frase.count('o') > vai contar quantas letras 'o' tem na frase
#frase.count('o',0,13) > conta do 0 até o 12 e conta quantos 'o' tem
#frase.find('deo') > conta quantos 'deo' tem e onde ele começou
#frase.find('Android') > se não encontrar ela mostra -1
#'curso' in frase > existe a palavra 'curso' dentro da frase?
#TRANSFORMAÇÃO:
#frase.replace('Python','Android') > Substitui 'Python' por 'Android'
#frase.upper() > transforma tudo em maisculo
#frase.lower() > transforma tudo em minusculo
#frase.capitalize() > joga todos os caracteres para minusculo deixando somente o primeiro caracter em maiusculo
#frase.title() > vai analisar quantas palavras tem e colocar todas as letras iniciais das palavras em maiusculo
#frase.strip() > remoção de espaços excedentes no inicio da frase
#frase.rstrip() > vai remover somente os ultimos espaços
#frase.lstrip() > remove somente os espaços do inicio
#DIVISÃO:
#frase.split() > onde tem espaço vai criar uma divisão, criando um espaço entre as palavras e enumerando elas ex: Curso em video 0,1,2,3,4 | 0,1 | 0,1,2,3,4
#JUNÇÃO:
#'-'.join(frase) > junta a frase em divisão colocando o que está dentro da ''
import random
nome = (input('Insira seu nome completo: '))
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()

tamanho_total = len(nome.replace(' ', ''))
primeiro_nome = nome.split()[0]
tamanho_primeiro_nome = len(primeiro_nome)

print("Seu nome em maiúsculas é:", nome_maiusculo)
print("Seu nome em minúsculas é:", nome_minusculo)
print("Seu nome tem ao todo", tamanho_total, "letras.")
print("Seu primeiro nome é", primeiro_nome, "e ele tem", tamanho_primeiro_nome, "letras.")



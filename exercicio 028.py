nome_completo = str(input("Insira seu nome completo: "))

nomes = nome_completo.split()

primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print("Seu primeiro nome é", primeiro_nome)
print("Seu último nome é", ultimo_nome)
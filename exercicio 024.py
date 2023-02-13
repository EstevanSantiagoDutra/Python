num = int(input("Digite um número entre 0 e 9999: "))

num_str = str(num).zfill(4)

milhar = num_str[0]
centena = num_str[1]
dezena = num_str[2]
unidade = num_str[3]

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)

#Você pode utilizar a função str para transformar o número em uma string e
# Em seguida, utilizar o método zfill para adicionar zeros à esquerda, se necessário, para que tenha exatamente 4 dígitos.
# Depois disso, você pode usar indexação para separar cada dígito e exibi-los na tela.
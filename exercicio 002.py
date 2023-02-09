nome = input ('Qual o seu nome?')
peso = float (input ('Qual o seu peso?'))
altura = float (input ('Qual sua altura?'))
imc = peso/altura**2
print('{}, seu IMC é de: {}'.format(nome, imc))

if imc < 16:
    print('Magreza grave')
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")

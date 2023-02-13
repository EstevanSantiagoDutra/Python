velocidade = int(input("Qual é a velocidade do carro em Km/h? "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado! A multa será de R$%d." % multa)
else:
    print("Você está dentro do limite de velocidade.")
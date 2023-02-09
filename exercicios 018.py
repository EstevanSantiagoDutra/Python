def hipotenusa(a, b):
    return (a**2 + b**2)**0.5

cateto_a = float(input("Insira o comprimento do primeiro cateto: "))
cateto_b = float(input("Insira o comprimento do segundo cateto: "))

resultado = hipotenusa(cateto_a, cateto_b)
print("A hipotenusa é {:.2f}".format(resultado))
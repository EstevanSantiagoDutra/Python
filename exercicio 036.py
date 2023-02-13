print("Verificador de Triângulos")
lado1 = float(input("Insira o comprimento do primeiro lado: "))
lado2 = float(input("Insira o comprimento do segundo lado: "))
lado3 = float(input("Insira o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados formam um triângulo.")
else:
    print("Os lados não formam um triângulo.")
p = float(input("Insira o preço do produto para realizar o reajuste: "))
d = float(p*0.05)
r = float(p-d)
print('O valor com desconto de 5% é de R${:.2f}'.format(r))
p = float(input("Insira o salario para realizar o reajuste: "))
d = float(p*0.15)
r = float(p+d)
print('O valor do novo salario é de R${:.2f}'.format(r))
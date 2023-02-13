salario = float(input('Informe o salário do funcionario? '))

if salario > 1250.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento

    print("O aumento foi de R$%.2f." % aumento)
    print("O novo salário é de R$%.2f." % novo_salario)

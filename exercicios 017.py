#como foi utilizado somente a função trunc da biblioteca math, então foi direcionado somente a trunc
#math.trunc(num)= numero truncado ou seja o numero cortado ele é impresso inteiramente.
'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi{} e a sua porção inteira é {}'.format(num, trunc(num)))'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))


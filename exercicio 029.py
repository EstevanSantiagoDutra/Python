import random
from time import sleep
def main():
    number = random.randint(0, 5)
    guess = int(input("Tente adivinhar o número inteiro escolhido pelo computador (entre 0 e 5): "))
    print('PROCESSANDO...')
    sleep(2)
    if guess == number:
        print("Você venceu!")
    else:
        print("Você perdeu! O número escolhido pelo computador era", number)


if __name__ == '__main__':
    main()
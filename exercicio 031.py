def main():
    number = int(input("Digite um número inteiro: "))

    if number % 2 == 0:
        print("O número", number, "é PAR.")
    else:
        print("O número", number, "é ÍMPAR.")


if __name__ == '__main__':
    main()
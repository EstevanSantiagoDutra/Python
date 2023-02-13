def main():
    distance = int(input("Qual é a distância da viagem em km? "))

    if distance <= 200:
        price = distance * 0.5
        print("O preço da passagem será de R$", price)
    else:
        price = distance * 0.45
        print("O preço da passagem será de R$", price)


if __name__ == '__main__':
    main()
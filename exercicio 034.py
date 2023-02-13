def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    numbers = [num1, num2, num3]
    max_num = max(numbers)
    min_num = min(numbers)

    print("O maior número é", max_num)
    print("O menor número é", min_num)


if __name__ == '__main__':
    main()
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Digite um ano: "))

    if is_leap(year):
        print(year, "é um ano bissexto.")
    else:
        print(year, "não é um ano bissexto.")


if __name__ == '__main__':
    main()
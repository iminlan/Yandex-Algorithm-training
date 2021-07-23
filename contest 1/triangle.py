def main():
    a, b, c = int(input()), int(input()), int(input())

    if (a+b) > c and (a+c) > b and (b+c) > a:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    print(main())

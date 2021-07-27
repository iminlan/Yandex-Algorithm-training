def main():
    A, B, C = int(input()), int(input()), int(input())      # кирпичи
    D, E = int(input()), int(input())                       # стороны отверстия в стене

    def fit(x, y):                                          # пройдет ли кирпич этим боком?
        h = (E >= x) and (D >= y)
        l = (E >= y) and (D >= x)
        if h or l:
            return True

    if fit(A, B) or fit(A, C) or fit(B, C):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    print(main())

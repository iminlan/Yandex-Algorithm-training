def main():
    data = input().split()
    a, b, c, d = [int(x) for x in data]

    s1 = [max(a, c), b + d, max(a, c) * (b + d)]
    s2 = [max(a, d), c + b, max(a, d) * (c + b)]

    s3 = [max(b, c), a + d, max(b, c) * (a + d)]
    s4 = [max(b, d), a + c, max(b, d) * (a + c)]

    table = [s1, s2, s3, s4]
    dictionary = {1: s1[2], 2: s2[2], 3: s3[2], 4: s4[2]}
    a = sorted(dictionary.items(), key=lambda t: t[1])

    n = a[0][0] - 1                                 # номер варианта расстановки с наименьшей площадью
    print(table[n][0], table[n][1])


if __name__ == "__main__":
    main()

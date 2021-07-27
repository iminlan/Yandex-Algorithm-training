def master(n, k, m):
    if n < k or k < m:
        return 0
    else:
        zag = n // k                                # сколько заготовок получилось из массы металла
        izd = zag * (k // m)                        # сколько деталей получилось из этих заготовок
        delta = zag * k - izd * m                   # сколько обрезков металла осталось
        n = n % k + delta                           # считаем сколько со всех заготовок остаток + металл остался
        return izd + master(n, k, m)


def main():
    data = input().split()
    ni, ki, mi = [int(x) for x in data]             # масса металла, заготовки и детали

    return master(ni, ki, mi)


if __name__ == "__main__":
    print(main())

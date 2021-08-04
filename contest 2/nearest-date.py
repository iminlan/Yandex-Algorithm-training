def main():
    N = int(input())
    mass = [int(x) for x in input().split()]
    num = int(input())

    mass.append(num)
    mass.sort()

    idx = mass.index(num)
    if idx == 0:
        return mass[1]
    elif idx == len(mass) - 1:
        return mass[-2]
    else:
        a1 = abs(mass[idx - 1] - num)  # модуль числа - расстояние до него
        a2 = abs(mass[idx + 1] - num)
        if min(a1, a2) == a1:
            return mass[idx - 1]
        else:
            return mass[idx + 1]


if __name__ == "__main__":
    print(main())

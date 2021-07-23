def main():
    a, b, c = int(input()), int(input()), int(input())
    result = []

    if a != 0:
        x1 = (-(c ** 2) - b) / a
        x2 = (c ** 2 - b) / a
        if c >= 0 and (x1 * a + b >= 0 or x2 * a + b >= 0):     # исключили варианты, когда под корнем минус или с<0
            if (x1 * a + b >= 0) and round(x1) == x1:
                result.append(x1)
            if (x2 * a + b >= 0) and round(x2) == x2:
                result.append(x2)
            result.sort()
            if x1 == x2:
                if round(x1) == x1:
                    return int(x1)
                else:
                    return"NO SOLUTION"                         # если есть один корень, но он не целый
            else:
                if result:
                    for i in result:
                        return int(i)
                else:
                    return "NO SOLUTION"                        # если не нашлось целых корней
        else:
            return "NO SOLUTION"
    else:
        if c >= 0 and c**2 == b:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"


if __name__ == "__main__":
    print(main())

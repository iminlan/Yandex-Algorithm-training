def main():
    a, b, n, m = int(input()), int(input()), int(input()), int(input())

    min_a = n + (n - 1) * a
    max_a = n + (n + 1) * a
    min_b = m + (m - 1) * b
    max_b = m + (m + 1) * b

    if min(max_a, max_b) < max(min_a, min_b):
        print(-1)
    else:
        print(max(min_a, min_b), min(max_a, max_b))


if __name__ == "__main__":
    main()

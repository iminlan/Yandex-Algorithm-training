def main():
    s = list(input().split())
    last = s[0]
    growth = 'YES'
    for elem in s[1:]:
        if elem > last:
            last = elem
        else:
            growth = 'NO'
    return growth


if __name__ == "__main__":
    print(main())

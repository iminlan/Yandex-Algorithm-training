def main():
    s = []
    while True:
        elem = int(input())
        if elem == -2000000000:
            break
        s.append(elem)

    last = s[0]
    growth = []
    for i in s[1:]:
        if i > last:
            growth.append('ASCENDING')
            last = i
        elif i == last:
            growth.append('CONSTANT')
            last = i
        elif i < last:
            growth.append('DESCENDING')
            last = i

    growth = set(growth)
    if len(growth) == 1:
        return list(growth)[0]
    elif len(growth) == 3:
        return 'RANDOM'
    elif ('ASCENDING' in growth) and ('CONSTANT' in growth):
        return 'WEAKLY ASCENDING'
    elif ('DESCENDING' in growth) and ('CONSTANT' in growth):
        return 'WEAKLY DESCENDING'


if __name__ == "__main__":
    print(main())

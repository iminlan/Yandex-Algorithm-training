def main():
    number = input()
    nums = [input(), input(), input()]

    number = number.replace('-', '')
    nums = [x.replace('-', '') for x in nums]
    number = number.replace('(', '')
    nums = [x.replace('(', '') for x in nums]
    number = number.replace(')', '')
    nums = [x.replace(')', '') for x in nums]
    number = number.replace('+7', '8')
    nums = [x.replace('+7', '8') for x in nums]

    if number and nums:
        if len(number) == 7:
            number = "8495" + number

        for i, my_number in enumerate(nums):
            if len(my_number) == 7:
                nums[i] = "8495" + my_number
            if nums[i] == number:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()

target = int(input())

result = 0

if target > 0 and target < 1000:
    for number in range(0, target + 1, 2):
        result += number
    print(result)
else:
    print("Number is not between 0 and 1000")

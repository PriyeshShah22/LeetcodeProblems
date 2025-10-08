test_cases = int(input())


def count_enemies(numbers):
    output = 0
    for number in numbers:
        if number % 56 == 0:
            output += 1
    print(output)


for _ in range(test_cases):
    lol = int(input())
    num = input()
    numbers = [int(num) for num in num.split()]
    output = count_enemies(numbers)
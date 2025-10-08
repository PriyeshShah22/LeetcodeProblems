def calculate_points(string):
    points = 0
    for medal in string:
        if medal == 'G':
            points += 3
        elif medal == 'S':  
            points += 2
        elif medal == 'B':
            points += 1
    return points


test_cases = int(input())
for _ in range(test_cases):
    string = input().strip()
    total_points = calculate_points(string)
    print(total_points)
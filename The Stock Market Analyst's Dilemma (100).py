def calculate_performance_window(prices):
    N = len(prices)
    performance_window = [0] * N
    stack = []

    for i in range(N):
        count = 1
        while stack and prices[stack[-1]] <= prices[i]:
            count += performance_window[stack.pop()]

        performance_window[i] = count
        stack.append(i)

    return performance_window


test_cases = int(input())
for _ in range(test_cases):
    Num = int(input())
    num = input()
    prices = [int(num) for num in num.split()]
    result = calculate_performance_window(prices)
    print(' '.join(map(str,result)))
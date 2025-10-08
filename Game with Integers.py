def winner(n):
    return n % 3 == 0

t = int(input())
for _ in range(t):
    n = int(input())
    print("Second") if winner(n) else print("First")
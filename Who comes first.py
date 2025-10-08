def optimal_game_score(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = arr[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(arr[i] - dp[i + 1][j], arr[j] - dp[i][j - 1])
    return 1 if dp[0][n - 1] <= 0 else 0


test_name = int(input())
for _ in range(test_name):
    num = int(input())
    arr = list(map(int, input().split()))
    print(optimal_game_score(arr))
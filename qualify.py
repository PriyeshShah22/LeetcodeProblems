def find_qualified_players(arr):
    n = len(arr)
    qualified_count = 0
    highest_qualified_score = float('-inf')
    highest_qualified_index = -1

    for i in range(n):
        if i == 0:
            if n == 1 or arr[i] > arr[i + 1]:
                qualified_count += 1
                if arr[i] > highest_qualified_score:
                    highest_qualified_score = arr[i]
                    highest_qualified_index = i
        elif i == n - 1:
            if arr[i] > arr[i - 1]:
                qualified_count += 1
                if arr[i] > highest_qualified_score:
                    highest_qualified_score = arr[i]
                    highest_qualified_index = i
        else:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                qualified_count += 1
                if arr[i] > highest_qualified_score:
                    highest_qualified_score = arr[i]
                    highest_qualified_index = i

    if qualified_count == 0:
        return 0, -1
    else:
        return qualified_count, highest_qualified_index


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        qualified_count, highest_qualified_index = find_qualified_players(arr)
        print(qualified_count, highest_qualified_index)

if __name__ == "__main__":
    main()


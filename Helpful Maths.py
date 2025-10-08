def helpful(word):
    numbers = list(map(int, word.split("+")))  # Convert all to integers
    numbers.sort()                             # Sort once
    return "+".join(map(str, numbers))         # Convert back to string and join


t = int(input())
for _ in range(t):
    word = input().strip()    # .STRIP REMOVES EXTRA SPACES OR SPECIAL CHARACTERS AND RETURN CLEAN INPUT
    answer = helpful(word)
    print(answer)
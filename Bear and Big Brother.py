def bearbro(word):
    a, b = map(int, word.strip().split())  # split the input into two integers
    count = 0       # initialize count = 0
    while a <= b:   # check bob <=  limak
        a *= 3      # multiply bob by 3
        b *= 2      # multiply limak by 2
        count += 1  # count a year
    return count


word = input()
answer = bearbro(word)
print(answer)
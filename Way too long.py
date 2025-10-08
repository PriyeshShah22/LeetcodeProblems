def waytoolong(word):
    if(len(word)>10):   # check for len word and if len is greater than 10
        shorten = word[0] + str(len(word)-2) + word[-1]  # take 0th word and last word and then do len of word - 2
        return shorten
    else:
        return word

t = int(input())
for _ in range(t):
    word = input().strip()    # .STRIP REMOVES EXTRA SPACES OR SPECIAL CHARACTERS AND RETURN CLEAN INPUT
    answer = waytoolong(word)
    print(answer)
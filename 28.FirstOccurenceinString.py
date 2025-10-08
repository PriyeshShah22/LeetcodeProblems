haystack = input("Enter string:")
needle = input("Enter string:")
for i in range(len(haystack)-len(needle)):
    if haystack[i:i + len(needle)] == needle:
        print(i)
        exit()
print(-1)
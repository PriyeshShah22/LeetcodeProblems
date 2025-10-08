strs = input("Give list of strings:")
str = strs.split(",")
output = ""
s = min(str, key=len)  # smallest string amongst all
flag = False
for i in range(len(s)):
    for word in str:
        if word[i] != s[i]:
            flag = True
            break
    if flag:
        break
    output += s[i]

print(output)
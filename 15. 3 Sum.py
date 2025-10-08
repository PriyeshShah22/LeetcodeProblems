nums = input("Enter the numbers:")
num = nums.split(",")
result = []
uniques = []
n = len(num)
for i in range(n-2): #[-1,0,1,2,-1,-4]
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if int(num[i]) + int(num[j]) + int(num[k]) == 0:
                result.append([int(num[i]), int(num[j]), int(num[k])])
for list in result:
    list.sort()
    if list not in uniques:
        uniques.append(list)
print(uniques)

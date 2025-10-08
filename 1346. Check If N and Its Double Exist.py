nums = input()
num = [int(num) for num in nums.split(',')]
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] == num[j]*2 and i!=j:
            print("True")
            exit()
print("False")
import math
num = int(input("Enter a number:"))
rev = 0
'''if num < 0:
    num = (abs(num))'''
while num:
    rem = int(math.fmod(num,10))
    num = int(num / 10)
    if rev >= 2147483647 or rev <= -2147483648:
        print("0")
        exit()
    rev = (rev * 10) + rem
print(f"{rev}")
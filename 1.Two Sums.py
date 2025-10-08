nums = input("Give list of numbers:")
num = nums.split(',')
num_dup = nums.split(',')
for i in enumerate(num): #makes a loop and goes through every element in the list. and gives index and number itself
    num[i[0]] = int(i[1])
    num_dup[i[0]] = int(i[1])
target = int(input("Input the target now:"))
def calculate_twosum(num, target):
    num2 = num
    num.sort()
    first, last = 0, len(num2)-1
    while first < last:
        calc_sum = num[first] + num[last]
        if calc_sum == target:
            number1, number2 = num[first], num[last]
            l = [number1, number2]
            print(f"{number1} + {number2} = {target}")
            return l
        elif calc_sum < target:
            first += 1
        else:
            last -= 1
    return False

Lol = calculate_twosum(num,target)
if Lol == False:
    print("No Two Numbers Add up to the Target :(")
    exit()
print("Indices of the Numbers equal to the Target Are : ", end="")
print(num_dup.index(Lol[0]), end=", ")
print(num_dup.index(Lol[1]))
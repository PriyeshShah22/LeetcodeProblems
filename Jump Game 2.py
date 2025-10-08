numbers = input()
num = [int(num) for num in numbers.split(',')]
currEndJumps = 0
maxEndJump = 0
jumps = 0

if len(num) < 1:
    print("0")
    
if num[0] == 0:
    print("0")

for i in range(len(num)-1):
    maxEndJump = max(maxEndJump, i + num[i])

    if maxEndJump >= len(num) - 1:
        jumps +=1
        break

    if i == currEndJumps:
        jumps += 1
        currEndJumps = maxEndJump

print(jumps)
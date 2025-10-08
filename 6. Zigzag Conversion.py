s = input("Enter the string:").upper()
num_rows = int(input("Enter num rows:"))
zigzag = ""
if num_rows == 1:
    zigzag = s
    print(zigzag)
    exit()

lines = [[] for i in range(num_rows)]
counter = 0
bottom = False
for letter in s:
    lines[counter].append(letter)
    if counter+1 == num_rows:
        bottom = True
    if counter == 0:
        bottom = False
    if bottom:
        counter -= 1
    else:
        counter += 1

for line in lines:
    for letter in line:
        zigzag += letter
print(zigzag)
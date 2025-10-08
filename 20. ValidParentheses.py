parentheses = input("Enter Parentheses: ")
stack = []
closeforOpen = {")": "(", "]": "[", "}": "{"}

for c in parentheses:
    if c in closeforOpen:
        if stack and stack[-1] == closeforOpen[c]:
            stack.pop()
    else:
        stack.append(c)

if not stack:
    print("This is a Valid Parentheses")
else:
    print("Invalid Parentheses")

'''not stack to see if stack is empty'''
'''stack and stack[-1]= (last added value)'''
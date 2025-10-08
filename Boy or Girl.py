def boyorgirl(check):
    return len(set(check)) % 2 == 0  # set to get only unique numbers and % 2 to check even or odd


check = input().strip()    # .STRIP REMOVES EXTRA SPACES OR SPECIAL CHARACTERS AND RETURN CLEAN INPUT
answer = boyorgirl(check)
if answer:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

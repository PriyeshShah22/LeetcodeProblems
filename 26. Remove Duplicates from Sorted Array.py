list = input("Enter the numbers:")
lists = list.split(",")
uniques = []
for number in lists:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
for i, number in enumerate(uniques):
    uniques[i] = int(number)
l = len(uniques)
u = len(lists) - len(uniques)
for underscore in range(u):
    uniques.append("_")
print(uniques)
print(f"Output = {l} ")
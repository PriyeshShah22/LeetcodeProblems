details = []
while True:
    detail = input("Enter the details:")
    if detail == "E":
        break
    details.append(detail)
count = 0
for age_str in details:
    age = int(age_str[11:13])
    if age > 60:
        count = count + 1
print(count)
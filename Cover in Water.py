def cost(containers):
    if "..." in containers:      # CHECK FOR ... BCZ WE WILL DIRECTLY RETURN 2 BECAUSE THAT BECOMES OUR INFINITE SOURCE THEN
        return 2
    else:
        price = 0
        for i in containers:    # FOR OTHER CASE ITS SIMPLE NO INFINITE SOURCE GET THAT MANY NO. OF BUCKETS
            if i == ".":
                price += 1
        return price

t = int(input())
for _ in range(t):
    n = int(input())
    containers = input()
    answer = cost(containers)
    print(answer)
def knapsackFractional(items, maxCapacity):
    totalValue = 0
    ratioList = []

    for weight, value in items:
        ratioList.append((value/weight, weight, value))

    ratioList.sort(reverse=True)

    print(f"Initial heap sorted by ratio",ratioList)

    for ratio, weight, value in ratioList:
        if maxCapacity >= weight:
            maxCapacity -= weight
            totalValue += value
            print(f"Added full item with {weight} and {value}")
        else:
            totalValue += ratio * maxCapacity
            print(f"Added fractional item with weight {maxCapacity} and value {ratio * maxCapacity}")
            break
    print("Total value obtained: ",totalValue)

items = []
n = int(input("Enter number of iems"))

for _ in range(n):
    weight = int(input("Enter weight"))
    value = int(input("Enter value"))
    items.append((weight,value))

maxCapacity = int(input("Enter maximum capacity of the knapsack: "))
knapsackFractional(items,maxCapacity)


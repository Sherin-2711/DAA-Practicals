def knapSack(items,maxCap):
    dp = [[0]*(maxCap+1) for _ in range(len(items)+1)]

    # Fill the DP table
    for i in range(1,len(items)+1):
        weight = items[i-1][0]
        value = items[i-1][1]
        for j in range(1,maxCap+1):
            dp[i][j] = dp[i-1][j]
            if weight <= j :
                dp[i][j] = max(dp[i][j],value+dp[i-1][j-weight])

    select = []
    cap = maxCap
    while i > 0 and cap > 0:
        if dp[i][cap] != dp[i-1][cap]:
            select.append(i-1)
            cap -= items[i-1][0]
        i -= 1

    return dp[len(items)][maxCap], select

items = []
n = int(input("Enter the number of items: "))
for _ in range(n):
    weight = int(input("Enter weight of item: "))
    value = int(input("Enter value of item: "))
    items.append((weight, value))

maxCapacity = int(input("Enter the maximum capacity of the knapsack: "))
result, selected_items = knapSack(items, maxCapacity)
print("Maximum value:", result)
print("Selected items:", selected_items)
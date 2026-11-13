def iterative(n):
    a,b = 0,1
    result = []
    for i in range(n):
        result.append(a)
        a,b = b,a+b
    return result

def recursion(n):
    if n<=1:
        return n
    return recursion(n-1) + recursion(n-2)

def recursive(n):
    result = []
    for i in range(n):
        result.append(recursion(i))
    return result


n = int(input("Enter n"))

print("Iterative Algorithm: ", iterative(n))
print("Recursive Algorithm: ", recursive(n))

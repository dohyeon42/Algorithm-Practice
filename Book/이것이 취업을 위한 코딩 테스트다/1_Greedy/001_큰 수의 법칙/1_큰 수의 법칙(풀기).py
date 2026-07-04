n, m, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0

array.sort(reverse = True)
while m:
    result += array[0]*k
    m -= k
    if not m:
        break;
    result += array[1]
    m -= 1
    
print(result)
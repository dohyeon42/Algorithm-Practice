n, m = map(int, input().split())

# for i in range(n):
#     result.append(list(map(int, input().split())))
result = [list(map(int, input().split())) for i in range(n)]

result = max([min(result[i]) for i in range(n)])

print(result)
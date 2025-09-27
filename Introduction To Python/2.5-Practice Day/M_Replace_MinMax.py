n = int(input())

arr = list(map(int, input().split()))

mn = min(arr)
mx = max(arr)

mnIndex = arr.index(mn)
mxIndex = arr.index(mx)

arr[mnIndex] = mx
arr[mxIndex] = mn

print(*arr)
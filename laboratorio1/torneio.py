casos = int(input())

for i in range(casos):
    n, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    mxEl = 0
    for i in range(n):
        if arr[mxEl] < arr[i]:
            mxEl = i
    
    if arr[mxEl] == arr[j-1]:
        mxEl = j-1
    
    cnt = n
    for i in range(n):
        if i == j-1 or i == mxEl:
            continue
        if arr[i] <= arr[j-1] or arr[i] <= arr[mxEl]:
            cnt -= 1
    
    if cnt <= k:
        print("YES")
    else:
        print("NO")
        


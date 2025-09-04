# fairdivision
t = int(input())

for _ in range(t):
    
    candy = int(input())
    w = list(map(int, input().split()))
    w.sort()
    w.reverse()
    
    aliceSum = 0
    bobSum = 0
    
    for i in w:
        if aliceSum < bobSum:
            aliceSum += i
        else:
            bobSum += i
    
    if aliceSum != bobSum:
        print("NO")
    else:
        print("YES")
        
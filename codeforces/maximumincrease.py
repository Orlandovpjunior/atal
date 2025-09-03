c = int(input())

nums = list(map(int, input().split()))

count = 1
max_count = 1

for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        count += 1
        max_count = max(count, max_count)
    else:
        count = 1

print(max_count)

nums = [i+1 for i in range(1, 10000)]
for n in nums:
    for m in nums[1:]:
        if n!=m and m % n == 0:
            nums.remove(m)

print(nums)
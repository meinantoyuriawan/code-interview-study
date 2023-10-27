def prodArray(nums):
    prod = []

    m = 1
    for i in range(len(nums)):
        prod.append(m)
        m = m*nums[i]

    m = 1
    for j in range(len(nums)-1, -1, -1):
        prod[j] = prod[j] * m
        m = m*nums[j]

    return prod

nums = [2,4,3,5]

print(prodArray(nums))
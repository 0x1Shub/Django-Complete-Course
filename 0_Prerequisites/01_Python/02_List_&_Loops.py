# List [] & Tuples ()

nums = [10, 20, 30, 40]

def square():
    i = 0
    while i < len(nums):
        nums[i] = nums[i] * nums[i]
        i += 1
    
    print(nums)


square()


# Better Approach

nums = [10, 20, 30, 40]
squared = [num ** 2 for num in nums]  # List comprehension (cleaner)
print(squared)


for num in nums:
    print(num ** 2)  # Print squared values without modifying the list
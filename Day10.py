import numpy as np

# 1. Create an array
arr = np.array([10,20,30,40,50])

# 2. Print the array
print(arr)
# 3. Add 10 to every element
print(arr+10)
# 4. Multiply every element by 3
print(arr*3)
# 5. Print:
# Sum
print(np.sum(arr))
# Mean
print(np.mean(arr))
# Maximum
print(np.max(arr))
# Minimum
print(np.min(arr))
# Standard Deviation
print(np.std(arr))

# 6. Create a 3×3 matrix
arr1=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# 7. Print:
# First row
print(arr1[0])
# Second column
print(arr1[:,1])
# Shape of matrix
print(arr1.shape)
# 8. Create:
# np.zeros(5)
arr2=np.zeros(5)
# np.ones(5)
arr3=np.ones(5)
# np.arange(1,11)
arr4=np.arange(1,11)
print(arr2)
print(arr3)
print(arr4)
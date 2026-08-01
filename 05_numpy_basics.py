"""
Day 12 – NumPy Basics

Topics Covered:
- Creating Arrays
- Vectorized Operations
- Statistical Functions
- Matrix Operations
- Array Shape
- Special Arrays (Zeros, Ones, Arange)

Author: Anshu Chourasia
"""

import numpy as np

# ==========================================
# Problem 1: Create a NumPy Array
# ==========================================

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

# ==========================================
# Problem 2: Add 10 to Every Element
# ==========================================

print("\nArray After Adding 10:")
print(arr + 10)

# ==========================================
# Problem 3: Multiply Every Element by 3
# ==========================================

print("\nArray After Multiplying by 3:")
print(arr * 3)

# ==========================================
# Problem 4: Basic Statistical Functions
# ==========================================

print("\nSum:")
print(np.sum(arr))

print("\nMean:")
print(np.mean(arr))

print("\nMaximum Value:")
print(np.max(arr))

print("\nMinimum Value:")
print(np.min(arr))

print("\nStandard Deviation:")
print(np.std(arr))

# ==========================================
# Problem 5: Create a 3×3 Matrix
# ==========================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n3×3 Matrix:")
print(matrix)

# ==========================================
# Problem 6: Matrix Indexing
# ==========================================

print("\nFirst Row:")
print(matrix[0])

print("\nSecond Column:")
print(matrix[:, 1])

print("\nShape of Matrix:")
print(matrix.shape)

# ==========================================
# Problem 7: Create Special Arrays
# ==========================================

zeros_array = np.zeros(5)

ones_array = np.ones(5)

range_array = np.arange(1, 11)

print("\nArray of Zeros:")
print(zeros_array)

print("\nArray of Ones:")
print(ones_array)

print("\nArray Using arange():")
print(range_array)
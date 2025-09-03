#simplify the code by removing unnecessary parts
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)
#Output
# 0
# 1
# 2                         
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# The function prints numbers from 0 to n-1 twice, resulting in 2n outputs.
# The time complexity is O(n) because the two loops are sequential, not nested.
# The space complexity is O(1) since no additional space is used that scales with input size.

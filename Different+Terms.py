
def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)
#Output
# 0
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
# The function prints numbers from 0 to a-1 and then from 0 to b-1, resulting in a + b outputs.
# The time complexity is O(a + b) because the two loops are sequential, not nested.
# The space complexity is O(1) since no additional space is used that scales with input size.       
# If a and b are independent variables, we cannot simplify O(a + b) to O(n).
# However, if we assume a and b are of similar magnitude, we can denote both as n, leading to a simplified time complexity of O(n).
# The space complexity remains O(1) in either case. 
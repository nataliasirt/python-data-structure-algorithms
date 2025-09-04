def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
#separate loop
    for k in range(n):
        print(k)

print_items(10)
#Output
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5
# 0 6
# 0 7
# 0 8
# 0 9
# 1 0
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 2 0
# 2 1
# 2 2
# 2 3
#....
# 9 9
# 0
# 1
# 2
# 3 ect
# The function prints n^2 pairs of numbers from the nested loops, resulting in n^2 outputs, followed by n additional numbers from the separate loop, resulting in a total of n^2 + n outputs.
# The time complexity is O(n^2) because the nested loops dominate the time complexity.
# The space complexity is O(1) since no additional space is used that scales with input size.   
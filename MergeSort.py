a = [5,7,3,8,1,4,9,2,6]

def merge_sort(arr):

    if len(arr) > 1:
    
        mid = len(arr) // 2 # find the middle of the array
        left = arr[:mid] # first half
        right = arr[mid:] # second half

        left = merge_sort(left) # recursively sort the first half
        right = merge_sort(right) # recursively sort the second half


        arr = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                val = left.pop(0)
                arr.append(val)
            else:
                val = right.pop(0)
                arr.append(val)
            
        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)
        
    return arr


print(merge_sort(a))


# Running time: How many times you have to press enter in the debugger for algorithm to complete

# pop() from end of list is O(1) but pop(n) due to shifting of all other items in O(n). So its better to use pointers.

# MergeSort has upper bound of 6nlog(n) + 6n

# GUIDING PRINCIPLES
# A
# 3 methods of analysis:
# 1- Worst-Case Analysis
# 2- Average-Case
# 3- Benchmarks
# 2,3 require domain knowledge

# B
# We don't pay much attention to constant factors (lower order terms)
# justification: 1- its easier 2- constants depend on architecture,compiler,programmer 3- Lose very little predictive power

# C
# Asymptotic analysis: focus on running time for large input sizes
#


# Asymptotic analysis:
# High level idea: suppress constant factors and lower-order terms
# lower-order terms become irrelevant with large inputs
# constant factors are too system dependent

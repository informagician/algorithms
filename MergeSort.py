arr = [5,7,3,8,1,4,9,2,6]

def mergeSort(arr):

    if len(arr) > 1:
    
        mid = len(arr) // 2 # find the middle of the array
        left = arr[:mid] # first half
        right = arr[mid:] # second half

        mergeSort(left) # recursively sort the first half
        mergeSort(right) # recursively sort the second half

        # pointers
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr.append(j)
                j += 1
            k += 1

        while i < len(left): # check if anything is left in left
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right): # check if anything is left in right
            arr[k] = right[j]
            j += 1
            k += 1
        
    return arr

print(mergeSort(arr))
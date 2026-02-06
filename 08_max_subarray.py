# Maximum Sum
def max_sum(arr):
    max_sum = 0
    for i in range(0,len(arr)-1):
        curr_sum = arr[i]+arr[i+1]
        max_sum = max(curr_sum,max_sum)
    return max_sum
print(max_sum([4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]))

# Maximum Sum SubArray. From the array, pick a continuous chunk (subarray) whose elements add up to the largest possible sum. (Kadane’s algorithm) 
def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
print(max_subarray_sum([4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]))

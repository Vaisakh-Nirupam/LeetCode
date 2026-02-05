def rain_trap(lst):
    n = len(lst)
    left = [0]*n
    right = [0]*n

    # Left
    left[0] = lst[0]
    for i in range(1,n):
        left[i] = max(left[i-1],lst[i])
    print("Left:",left)

    # Right
    right[-1] = lst[-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1],lst[i])
    print("Right:",right)

    # Water
    water = 0
    for i in range(n):
        water += min(left[i],right[i]) - lst[i]
    return water

A = [1, 0, 2, 0, 1, 0, 3, 1, 0, 2]
print("Water:",rain_trap(A)) 

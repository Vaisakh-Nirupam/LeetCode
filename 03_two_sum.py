# Given an array and a target, return indices of two distinct elements whose sum equals the target. You may not use the same element twice.

lst = [2,7,11,15]
target = 9

# Mine
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j] == target:
            print(i,j)

# GPT
dit = {}
for i,num in enumerate(lst):
    sub = target - num
    if sub in dit:
        print(dit[sub],i)
        break
    dit[num] = i
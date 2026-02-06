# Find out Common Letters 
str1 = set(input("Enter First String: "))
str2 = set(input("Enter Second String: "))
def common(s1,s2):
    return s1 & s2
print(common(str1,str2))
# or
common = lambda s1,s2 : s1 & s2
print(common(str1,str2))


# Word Frequency
sen = "Sheena loves eating apple and mango. Her sister also loves eating apple and mango" 
dit = {}
for i in sen.split():
    if i not in dit:
        dit[i] = 0
    dit[i] += 1
print(dit)


# Merge 2 List as Key Value of Dict
l1 = ['hi','how','hey']
l2 = [1,2,3]
dit = dict(zip(l1,l2))
print(dit)


# Find the Missing Number
num = [1,2,4,5,7]
for i in range(len(num)-1):
    if num[i]+1 != num[i+1]:
        print(num[i]+1)
# or
ms = [i for i in range(1,num[-1]) if i not in num]
print(ms)


# Find Index of Numbers with Target Sum 
lst = [5,7,4,3,9,8,19,21,12]
tar = 17
dit = {}
for i,num in enumerate(lst):
    sub = tar - num
    if sub in dit:
        print(f"{dit[sub]},{i}")
    dit[num] = i


# Minimum Difference bw each Elements
lst = [5,32,45,4,12,18,25]
print("List:",lst)
lst.sort()
print("Sorted List:",lst)
min_val = float('inf')
for i in range(len(lst)-1):
    diff = lst[i+1] - lst[i] 
    if diff < min_val:
        min_val = diff
print("Minimum Difference:",min_val)
# or
min_diff = min(b - a for a, b in zip(lst, lst[1:]))
print("Minimum Difference:", min_diff)


# Maximum Difference bw each Elements
lst = [5,32,45,4,12,18,25]
print("List:",lst)
lst.sort()
print("Sorted List:",lst)
max_val = float('-inf')
for i in range(len(lst)-1):
    diff = lst[i+1] - lst[i] 
    if diff > max_val:
        max_val = diff
print("Maximum Difference:",max_val)
# or
max_diff = max(b - a for a, b in zip(lst, lst[1:]))
print("Maximum Difference:", max_diff)


# Stack Push, Pop and Operate
def stack_operate(lst):
    op = ["+","-","*","/","%"]
    stk = [] 
    for i in lst:
        if i not in op:
            stk.append(int(i))
        else:
            n1, n2 = stk.pop(), stk.pop()
            if i == '+':
                stk.append(n1+n2)
            elif i == '-':
                stk.append(n1-n2)
            elif i == '*':
                stk.append(n1*n2)
            elif i == '/':
                stk.append(n1/n2)
            elif i == '%':
                stk.append(n1%n2)
    return stk[-1]
print(stack_operate(["1","2","+","3","*"]))


# Create Wave Array from Normal Arrays
def waves(arr):
    for i in range(0,len(arr)-1,2):
        if arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr
arr = [3,5,12,2,6,10,7,9,8]
print("Before Wave:",arr)
print("After Wave:",waves(arr))


# Find the Indexes of the Anagrams
def anagram(lst):
    dit = {}
    for i in range(len(lst)):
        word = "".join(sorted(lst[i]))
        if word in dit:
            dit[word].append(i)
        else:
            dit[word] = [i]
    return dit 
lst = ["cat","god","dog","act","tac"]
print(anagram(lst))


# 
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
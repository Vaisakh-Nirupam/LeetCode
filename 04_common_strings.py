# Find out common letters between two strings Using Python
str1 = set(input("Enter First String: "))
str2 = set(input("Enter Second String: "))

# method 1
def common(s1,s2):
    return s1 & s2
print(common(str1,str2))

# method 2
common = lambda s1,s2 : s1 & s2
print(common(str1,str2))
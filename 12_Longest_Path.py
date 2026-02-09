# Find the Longest Path

# Mine
def max_length_finder(inp):
    path = inp[0]
    max_length = []
    for i in range(len(path)):
        k = inp[1]
        length = 0
        for j in range(i,len(path)):
            if path[j] == 'clear':
                length += 1
            elif path[j] == 'mud' and k > 0:
                length += 1
                k-=1 
            else:
                break
        max_length.append(length)
    return max(max_length)
inp = [['mud','mud','clear','clear','mud'],1]
print(max_length_finder(inp))

# GPT
def max_length_finder(path, k):
    left = 0
    mud_count = 0
    max_len = 0
    for right in range(len(path)):
        if path[right] == 'mud':
            mud_count += 1
        while mud_count > k:
            if path[left] == 'mud':
                mud_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
path = ['mud','mud','clear','clear','mud']
k = 1
print(max_length_finder(path, k))
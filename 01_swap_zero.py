# Swap Zeroes to the last without changing the orders of the non-zero numbers

lst = [0,1,0,3,12]
print("Before: ",lst)

# Mine
mysol = lst.copy()
for i in mysol:
    if i == 0:
        mysol.remove(0)
        mysol.append(0)
print("Mine After: ",mysol)

# GPT
gptsol = lst.copy()
zero_count = gptsol.count(0)
gptsol = [i for i in gptsol if i != 0] + [0]*zero_count
print("GPT After: ",gptsol)

# Yt
ytsol = lst.copy()
prev = 0
for i in range(0,len(ytsol)):
    if ytsol[i] != 0:
        # swap
        ytsol[prev],ytsol[i] = ytsol[i],ytsol[prev]
        # increment
        prev += 1
print("Yt After: ",ytsol)

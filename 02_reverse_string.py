# Reverse a String without string indexing

sen = "Python Programming"
print("Before: ",sen)
# sen_rev = sen[::-1]
# print(sen_rev)

# Mine
mysen = []
for i in range(len(sen)-1,-1,-1):
    mysen.append(sen[i])
mysen = "".join(mysen)
print("Mine After: ",mysen)

# GPT
gptlst = [i for i in sen]
gptsen = ""
while gptlst:
    gptsen += gptlst.pop()
print("GPT After: ",gptsen)

# Yt
ytsen = list(sen)
left = 0
right = len(ytsen)-1
while left < right:
    ytsen[left], ytsen[right] = ytsen[right], ytsen[left]
    left+=1
    right-=1
ytsen = "".join(ytsen)
print("Yt After: ",ytsen)

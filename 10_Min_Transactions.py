# Find the Minimum Transaction needed to Complete the Debts 

# Mine
def minTransfers(balances):
    l1 = len([i for i in balances if i < 0])-1
    l2 = len([i for i in balances if i > 0])-1
    if l1 and l2 == -1:
        return 0
    return l1 + l2 + 1
print(minTransfers([30,30,-20,-40]))

# Mine
def minTransfers(balances):
    lst = [i for i in balances if i != 0]
    lst.sort()
    count = 0
    while len(lst) > 1:
        s = lst[0] + lst[-1]
        if s < 0:
            lst[0] = s
            lst.pop()
        elif s > 0:
            lst[-1] = s
            lst.pop(0)
        else:
            lst.pop(0)
            lst.pop()
        count += 1
    return count
print(minTransfers([30,30,-20,-40]))

# GPT
def minTransfers(balances):
    debts = [b for b in balances if b != 0]
    def settle(i):
        while i < len(debts) and debts[i] == 0:
            i += 1
        if i == len(debts):
            return 0
        ans = float('inf')
        for j in range(i + 1, len(debts)):
            if debts[i] * debts[j] < 0:
                debts[j] += debts[i]
                ans = min(ans, 1 + settle(i + 1))
                debts[j] -= debts[i]
        return ans
    return settle(0)
print(minTransfers([30,30,-20,-40]))

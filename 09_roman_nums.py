# Roman Numerals to INT

def roman_int(rm):
    dit = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":100}
    total = 0
    prev = 0
    for i in reversed(rm):
        value = dit[i]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total
print(roman_int("XIVL"))
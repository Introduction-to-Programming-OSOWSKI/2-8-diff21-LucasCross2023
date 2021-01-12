def diff21(n):
    if abs(21-n): 
        return abs(21-n)
    elif abs(n>21):
        return abs(n*2)
    elif abs(n==21):
        return 0 


print(diff21(21))
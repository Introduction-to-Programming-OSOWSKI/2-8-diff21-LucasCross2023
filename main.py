def diff21(n):
    if 21>=n: 
        return abs(21-n)
    elif 21<n:
        return abs(21-n)*2 
    elif abs(n==21):
        return 0 


print(diff21(31))
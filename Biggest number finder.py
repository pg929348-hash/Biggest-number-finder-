def comp(a,b,c):
    if a>b and c<a:
        return a
    elif a<b and c<b:
        return b
    elif a<c and b<c:
        return c
    else :
        return "none"
result=comp(-3,6,0)
print(result)

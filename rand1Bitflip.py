import random
def BinCShift(x,n):
    i = x[:n]
    return x[n:]+x[:n]

def BinXor(x,y,m):
    c = bin(int(x,2) ^ int(y,2))
    return c[2:].zfill(m)
def random1bitflip(a):
    ''' binary strin a --> binary string a'''
    m = len(a)
    bs='1'.zfill(m)
    bs = BinCShift(bs,random.randint(0,m-1))
    a = BinXor(a,bs,m)
    return a




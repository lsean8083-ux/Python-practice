# add some comments

a = ['4','b','7','8','s']
b = ['4','7','3','#']


def cha_ji (a,b):
    c=[]
    for o in a:
        c.append(o)
        for k in b:
            if o == k:
                c.remove(k)
                

    return c

def jiao_ji(a,b):
    num= []
    for p in a:
        for e in b:
            if p == e:
               num.append(p)

    return num
            
            
def bing_ji(a,b):
    jun = []
    aa = []
    bb=[]
    
    for p in a:
        aa.append(p)
       
    for e in b:
       bb.append(e)
       
    for t in aa:
        for s in bb:
            if t == s:
                aa.remove(t)
                
    for o in aa:
        jun.append(o)
    for l in bb:
        jun.append(l)    
    return jun

print("a: ",a)
print("b: ",b)


print("cha a,b: ",cha_ji(a,b))
print("jiao a,b:",jiao_ji(a,b))
print("bing a,b:",bing_ji(a,b))

f=['4','t']
print("f: ",f)
print("bing a,f",bing_ji(a,f))





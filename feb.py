
feb = [0, 1]
num = 100
for i in range(0,num):
    x= feb[i] + feb[i+1]
    feb.append(x)

num= 1
n = 0 

for i in range(0, len(feb), 2):
    n += feb[i]  
    if len(str(n)) == num:
        print(i)
        print(n)
        break




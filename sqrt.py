a = int(input())
b=False
i= 1
while i**2 <= a:    
    if i**2 == a:
        b = True
        rt = i
        break
    
        
    elif i**2 != a:
        i+=1
        b = False
        
if b:
    print("是, sqrt is ", rt)
else:
    print("不是")
    
    

        
        

        


        
    
        
nums = [12, 7, 9, 20, 33, 40, 55]
ev=[]
od=[]

for i in nums:
    if i%2==0:
        ev[i]=ev+1

    else:
       od[i]=od+1
    
print("Even: ", ev) 
print("odd: ", od)   
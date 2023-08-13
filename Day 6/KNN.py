import math
cigarettes=[7,7,3,1,3]
weights=[70,40,40,40,70]
heartAttack=['Bad','Bad','Good','Good','Bad',]

c2=int(input('Enter number of cigarettes: '))
w2=int(input('Enter your weight: '))
dis=[] # empty list

for i in range (len(cigarettes)):
    x=math.sqrt((c2-cigarettes[i])**2+(w2-weights[i])**2)
    dis.append(x) #to add in the list
m=min(dis)
z=dis.index(m) #finding the index  
print('You are: ', heartAttack[z] )
    
   
    
    

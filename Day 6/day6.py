"""
Imagine you have a model with Forecast & Observation 
Find MSE:

"""

O=[7,5,2,0,1,8]
F=[6,5,0,-1,0,7]
sum=0

for i in range(len(O)):
    sum= sum+ (F[i]- O[i])**2
MSE=sum/len(O)
print(MSE)

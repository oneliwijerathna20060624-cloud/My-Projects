L=[1,2]
sum=0
while True:
    x=L[-1]+L[-2]
    if x<4000000:
     L.append(x)
    
    else:
       break
       
for i in L:
    if i%2==0 :
        sum = sum+i
print(sum)
print(L)
    


#input

x = int(input())
y = int(input())
z = int(input())
n = int(input())
res=[]
    
    
for i in range(x+1):           # will travers till give value of x,y,z
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k==n:       # if the sum of x,y and z are equal to n then will continue loop
                continue
            else:
                res.append([i,j,k])   #inserting values in res list
    
                
print(res)
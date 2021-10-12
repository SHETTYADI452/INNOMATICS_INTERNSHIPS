#Raw Input 
n = int(input())

if(n % 2 == 1):                       #odd no
    print("Weird")
else:                                 #even no
    if(2 <= n <= 5):                  # if n is even and in range 2 to 5
        print("Not Weird")
    elif(6 <= n <= 20):               # if n is even and in range 6 to 20
        print("Weird")
    else:                             # if n is even and more than 20
        print("Not Weird")
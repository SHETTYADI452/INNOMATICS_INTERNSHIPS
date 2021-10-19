def swap_case(s):
    
    #first let find the length
    n=len(s)              
    #initialize res as a list for storing changed elements
    res=[] 
    for i in range(n):
        if(s[i].isupper()==True):
            res.append(s[i].lower())
        elif(s[i].islower()==True):
            res.append(s[i].upper())
        else:
            res.append(s[i])  
            
    #def String for storing changed elements
    string=''
    
    #converting list into string
    return string.join(res)

    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
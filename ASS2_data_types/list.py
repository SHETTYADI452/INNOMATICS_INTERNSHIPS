if __name__ == '__main__':
    N = int(input())
    
    # out put  list
    out_list=[]
    
    for i in range(0,N): # will traverse through all input
        
    # now let us split the input the index 0 will contain commands and the otherindex contains values
        ip = input().split();  
        if ip[0] == "print":
            print(out_list)
        elif ip[0] == "insert":
            out_list.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            out_list.remove(int(ip[1]))
        elif ip[0] == "pop":
            out_list.pop();
        elif ip[0] == "append":
            out_list.append(int(ip[1]))
        elif ip[0] == "sort":
            out_list.sort();
        else:
            out_list.reverse();
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

inp = int(input())

for i in range(inp):
    num = input()
    if(len(num)==10 and num.isdigit()):
        output = re.findall(r"^[789]\d{9}$",num)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
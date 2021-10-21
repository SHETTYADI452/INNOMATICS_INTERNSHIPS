# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

n = int(input().strip())
for _ in range(n):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))
    
    

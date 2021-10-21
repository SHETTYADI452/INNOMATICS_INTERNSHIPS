# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
res = False
for _ in range(N):
    s = input()
    if '{' in s:
        res = True
    elif '}' in s:
        res = False
    elif res:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)
# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = input()
a = set(int(x) for x in input().split(' '))

n = int(input())
for inp in range(n):
    op, inp = input().split(' ')
    b = set(int(x) for x in input().split(' '))
    if op == "update":
        a |= b
    elif op == "intersection_update":
        a &= b
    elif op == "difference_update":
        a -= b
    elif op == "symmetric_difference_update":
        a ^= b

print(sum(a))
                    

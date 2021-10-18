# Enter your code here. Read input from STDIN. Print output to STDOUT

a = input()
b = set()
for i in xrange(a):
    b.add(raw_input())

print len(b)
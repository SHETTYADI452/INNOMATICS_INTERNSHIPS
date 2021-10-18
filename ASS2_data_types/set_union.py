
e = input()
english = set(map(int,raw_input().split()))
f = input()
french = set(map(int,raw_input().split()))

u = english.union(french)

print len(u)
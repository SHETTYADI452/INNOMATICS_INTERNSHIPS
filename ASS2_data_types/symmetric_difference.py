# Enter your code here. Read input from STDIN. Print output to STDOUT

int(raw_input())
N = raw_input().split()
N_int = set(list(map(int, N)))
int(raw_input())
M = raw_input().split()
M_int = set(list(map(int, M)))
result = []
for i in list(N_int.difference(M_int)):
    result.append(i)
for j in list(M_int.difference(N_int)):
    result.append(j)
for k in sorted(result):
    print k
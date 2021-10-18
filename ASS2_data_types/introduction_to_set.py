from __future__ import division

def average(array):
    # your code goes here
    total = sum(set(array))
    n = len(set(array))
    avg = total/n 
    return format(avg,".3f") 

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
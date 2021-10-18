n = int(input())
arr = map(int, input().split())

#lets Convert array to list and getting its set and then converting to list.
arr = list(set(list(arr)))

new_len = len(arr)

#sorting the list by using sorted and getting second last element.

arr = sorted(arr)
print(arr[new_len-2])


            

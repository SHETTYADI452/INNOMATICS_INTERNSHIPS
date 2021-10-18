#let us declare an empty list
result = []
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    #append record of each student name,score in a for loop
    result.append([name, score])
    
# will sort the list in increasing order of thier score and remove duplicates
scores = sorted(list(set([x[1]for x in result ]))) 
second_lowest_score = scores[1]     #as index 1 will have second lowest score

#let us create a new list which stores students having 2 lowest score
second_lowest_students=[]
for student in result:
    if second_lowest_score == student[1]:
        second_lowest_students.append(student[0])

#sort names in alphabetical order
second_lowest_students.sort()
#loop through each name and print
for name in second_lowest_students:
    print(name)

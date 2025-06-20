# From a list, find all elements that appear more than once
# Input: [1,2,3,2,1,4,5,6,4]
# Output: [1, 2, 4]

list1 = [1,2,3,2,1,4,5,6,4]
list2 = []
for n1 in list1:
    count = 0
    for n2 in list1:
        if(n1 == n2):
            count = count+1
    if(count >1 and not list2.__contains__(n1)):
        list2.append(n1)
        
        
print(list2)
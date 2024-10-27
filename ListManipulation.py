### Part Three -- your code goes here. 
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list.sort()

n = 2
newList = list[n:]

extendedList = newList
extendedList.extend([7, 8])

print(extendedList)

### Part Four -- your code goes here. 
import random
randomList = []
for i in range(10):
    n = random.randint(1, 100)
    randomList.append(n)
print("The random numbers are:", randomList)

x = 0
while x < len(randomList):
    if randomList[x] % 2 == 0:
        randomList.pop(x)
    else:
        x += 1
print("Odd numbers in the list are:", randomList)





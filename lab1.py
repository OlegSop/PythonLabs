import random

list = []
iter = 0
lsize = 0
sum = 0
avg = 0

lsize = int(input("Enter a list size:"))
while iter < lsize:
    list.append(random.randint(0,50))
    iter += 1
for x in list:
    sum += x
avg = sum / lsize

print("List = "+str(list))
print("List sum = "+str(sum))
print("List average = "+str(avg))
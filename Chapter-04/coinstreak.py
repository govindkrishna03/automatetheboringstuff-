import random
numberOfStreaks = 00
for experimentNumber in range(10000):
    lst=[random.randint(0,1) for x in range(100)]
    count=0
    for x in range(100):
        if x==0:
            continue
        if lst[x]==lst[x-1]:
            count=count+1
        else:
            count=0
        if count==6:
            numberOfStreaks=numberOfStreaks+1
            count=0
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))


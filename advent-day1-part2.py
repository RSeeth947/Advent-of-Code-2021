newList = test.split()
addList = []
i = 0
while (i < len(newList)):
    try:
        addNum = int(newList[i]) + int(newList[i + 1]) + int(newList[i + 2])
        addList.append(addNum)
        i += 1
    except:
        break



count = 0
i = 1
lastMax = int(addList[0])
for i in range(len(addList)):
    

    if (int(addList[i]) > lastMax):
        count += 1
        lastMax = int(addList[i])

    elif (int(addList[i]) < lastMax):
        lastMax = int(addList[i])
        
print(count)

depths_list = depths.split()



count = 0
i = 1
lastMax = int(depths_list[0])


for i in range(len(depths_list)):
    

    if (int(depths_list[i]) > lastMax):
        count += 1
        lastMax = int(depths_list[i])

    elif (int(depths_list[i]) < lastMax):
        lastMax = int(depths_list[i])
        
print(count)

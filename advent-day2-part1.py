file = open('forward.txt', 'r')
data = file.read()
file.close()

moveIndex = data.split()




forward = 0
depth = 0

for i in range(len(moveIndex)):

    if (i % 2 == 0):
        if (moveIndex[i] == "forward"):
            forward += int(moveIndex[i + 1])
        
        elif (moveIndex[i] == "down"):
            depth += int(moveIndex[i + 1]) 
            
        elif (moveIndex[i] == "up"):
            depth -= int(moveIndex[i + 1]) 

print(forward * depth)  

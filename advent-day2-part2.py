file = open('forward.txt', 'r')
data = file.read()
file.close()

moveIndex = data.split()

forward = 0
depth = 0
newDepth = 0
aim = 0


for i in range(len(moveIndex)):

    if (i % 2 == 0):
        if (moveIndex[i] == "forward"):
            forward += int(moveIndex[i + 1])
            depth = depth + ((int(moveIndex[i + 1]) * aim)) 
            
            
        
        if (moveIndex[i] == "down"):
            aim += int(moveIndex[i + 1])

        if (moveIndex[i] == "up"):
            aim -= int(moveIndex[i + 1])

print(forward * depth)

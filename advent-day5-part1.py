file = open('coords.txt', 'r')
data = file.read()
file.close()
original_coords = data.split()






file = open('coords.txt', 'r')
data = file.read()
file.close()
original_coords = data.split()

startpoint = []
endpoint = []

for i in range(len(original_coords)):
    if (i % 3 == 0):
        test = original_coords[i].split(",")
        startpoint.append(test[0])
        startpoint.append(test[1])

for i in range(len(original_coords)):
    if (i % 3 == 0):
        test = original_coords[i + 2].split(",")
        endpoint.append(test[0])
        endpoint.append(test[1])


start_coords = []
end_coords = []

for i in range(len(startpoint)):
    if (i % 2 == 0):
        start_coords.append((int(startpoint[i]), int(startpoint[i + 1])))

for i in range(len(endpoint)):
    if (i % 2 == 0):
        end_coords.append((int(endpoint[i]), int(endpoint[i + 1])))



def fill_lines(line_list, start, end):
    for i in range(len(start)):

        if (start[i][0] == end[i][0]):
            for j in range(abs(end[i][1] - start[i][1]) + 1):
                if (start[i][1] > end[i][1]):
                    line_list.append((start[i][0], start[i][1] - j))
                elif (start[i][1] < end[i][1]):
                    line_list.append((start[i][0], start[i][1] + j))

        elif (start[i][1] == end[i][1]):
            for j in range(abs(end[i][0] - start[i][0]) + 1):
                if (start[i][0] > end[i][0]):
                    line_list.append((start[i][0] - j, start[i][1]))
                elif (start[i][0] < end[i][0]):
                    line_list.append((start[i][0] + j, start[i][1]))
                   

               

    return line_list

filled_lines = []

fill_lines(filled_lines, start_coords, end_coords)



grid = []

length = 1000
i = 0

while (i < length):
    width = []
    for j in range(length):
        width.append(0)
    grid.append(width)
   
    
    i += 1

def fill_grid(grid, lines, length):
    for i in range(len(lines)):
        grid[lines[i][0]][lines[i][1]] += 1

    count = 0
    for i in range(length):
        for j in range(length):
            if (grid[i][j] > 1):
                count += 1
    return count

print(fill_grid(grid, filled_lines, 1000))

file = open('inputs.txt', 'r')
data = file.read()
file.close()
raw_inputs = data.split()


inputs = []
for i in range(len(raw_inputs)):
    for j in range(len(raw_inputs[0])):
        inputs.append(raw_inputs[i][j])




input_map = []
row = []
i = 0
while i < len(inputs):
    row.append(int(inputs[i]))
    if len(row) == 10:
        input_map.append(row)
        row = []

    i += 1








def check_min(inputs):
    values = []
    location = []
    row_len = 0
    col_len = len(inputs[0])
    
    
            
    for i in inputs:
        for j in range(len(i)):
            if j == 0:
                row_len += 1

    for row in range(len(inputs)):
        for col in range(col_len):

            if row == 0 and col == 0:
                mins = inputs[row][col]

                if mins < inputs[row + 1][col] and mins < inputs[row][col + 1]:
                    values.append(mins)
                    location.append((row, col))


            elif row == row_len - 1 and col == 0:
                mins = inputs[row][col]

                if mins < inputs[row - 1][col] and mins < inputs[row][col + 1]:
                    values.append(mins)
                    location.append((row, col))



            elif row == 0 and col == col_len - 1: 
                mins = inputs[row][col]

                if mins < inputs[row][col - 1] and mins < inputs[row + 1][col]:
                    values.append(mins)
                    location.append((row, col))




            elif row == row_len - 1 and col == col_len - 1:
                mins = inputs[row][col]

                if mins < inputs[row - 1][col] and mins < inputs[row][col - 1]:
                    values.append(mins)
                    location.append((row, col))



            elif row == 0:
                mins = inputs[row][col]
                if mins < inputs[row][col - 1] and mins < inputs[row + 1][col] and mins < inputs[row][col + 1]:
                    values.append(mins)
                    location.append((row, col))

            elif row == row_len - 1:
                mins = inputs[row][col]
                if mins < inputs[row][col - 1] and mins < inputs[row - 1][col] and mins < inputs[row][col + 1]:
                    values.append(mins)
                    location.append((row, col))

            elif col == 0:
                mins = inputs[row][col]

                if mins < inputs[row - 1][col] and mins < inputs[row][col + 1] and mins < inputs[row + 1][col]:
                    values.append(mins)
                    location.append((row, col))


            elif col == col_len - 1:
                mins = inputs[row][col]   
                
                if mins < inputs[row - 1][col] and mins < inputs[row][col - 1] and mins < inputs[row + 1][col]:
                    values.append(mins)
                    location.append((row, col))

            else:
                mins = inputs[row][col]

                if mins < inputs[row][col - 1] and mins < inputs[row - 1][col] and mins < inputs[row][col + 1] and mins < inputs[row + 1][col]:
                    values.append(mins)
                    location.append((row, col))
    return location


locations = check_min(input_map)
#print(input_map)



def find_basins(map, low_points):
    searched = []
    unsearched = low_points


    for i in range(len(low_points)):
        x = low_points[i][0]
        y = low_points[i][1]

        low = map[x][y]
        print(low)

        while (unsearched != 0):
            pass
            

#find_basins(input_map, locations)

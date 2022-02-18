file = open('input.txt', 'r')
data = file.read()
file.close()
raw_inputs = data.split(",")

inputs = [int(x) for x in raw_inputs]



fuel_costs = []
fuel_average = 4501500000000000

i = 0
while i < len(inputs):
    for j in range(len(inputs)):
        distance = abs(i - inputs[j])
        total = int((distance * (distance + 1)) / 2)
        
        fuel_costs.append(total)
       

    total = 0
    for j in range(len(fuel_costs)):
        total += fuel_costs[j]

    if total < fuel_average:
        fuel_average = total
    
    fuel_costs = []
    i += 1
    


print(fuel_average)

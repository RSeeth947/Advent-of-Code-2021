file = open('input.txt', 'r')
data = file.read()
file.close()
raw_inputs = data.split(",")

inputs = [int(x) for x in raw_inputs]

fuel_costs = []
fuel_average = 100000000

i = 0
while i < len(inputs):
    compare = inputs[i]
    for j in range(len(inputs)):
        fuel_costs.append(abs(i - inputs[j]))

    total = 0
    for j in range(len(fuel_costs)):
        total += fuel_costs[j]

    if total < fuel_average:
        fuel_average = total    

    fuel_costs = []
    i += 1

print(fuel_average)
print(len(inputs))


file = open('input.txt', 'r')
data = file.read()
file.close()
inputs = data.split()

outputs = []
output = ""

count = 0
for i in range(len(inputs)):

    if len(inputs[i]) == 2:
        output += "1"
    elif len(inputs[i]) == 3:
        output += "7"
    elif len(inputs[i]) == 4:
        output += "4"
    elif len(inputs[i]) == 7:
        output += "8" 

    elif len(inputs[i]) == 5:
        if ("e" or "b") not in inputs[i]:
            output += "2"
        elif ("e" or "g") not in inputs[i]:
            output += "5"
        else:
            output += "3"

    elif len(inputs[i]) == 6:
        if "g" not in inputs[i]:
            output += "6"
        elif "f" not in inputs[i]:
            output += "0"
        elif "a" not in inputs[i]:
            output += "9"

    if len(output) == 4:
        outputs.append(output)
        output = ""


count = 0
for i in range(len(outputs)):
    count += int(outputs[i])

print(outputs)

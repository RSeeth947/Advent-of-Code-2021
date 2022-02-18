file = open('binary.txt', 'r')
data = file.read()
file.close()


binary = data.split()
myList = []
gammaRate = []
epsilonRate = []



j = 0
while (j <= 11):
    zeroCount = 0
    oneCount = 0
    for i in range(len(binary)):
        if (binary[i][j] == "1"):
            zeroCount += 1
        if (binary[i][j] == "0"):
            oneCount += 1

    if (zeroCount > oneCount):
        gammaRate.append("1")
        epsilonRate.append("0")
    elif (zeroCount < oneCount):
        gammaRate.append("0")
        epsilonRate.append("1")

    j += 1

gamma = ''.join(gammaRate)
epsilon = ''.join(epsilonRate)

print(gamma)
print(epsilon)

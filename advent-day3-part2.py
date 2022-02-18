file = open('binary.txt', 'r')
data = file.read()
file.close()


binary = data.split()
oxyBinary =  data.split()
carBinary = data.split()

myList = []


for i in range(len(binary[0])):
    zeroCount = 0
    oneCount = 0

    for j in range(len(oxyBinary)):
        if oxyBinary[j][i] == "0":
            oneCount += 1
        elif oxyBinary[j][i] == "1":
            zeroCount += 1




    if zeroCount > oneCount:
        for k in range(len(oxyBinary)):
            if oxyBinary[k][i] == "0":
                oxyBinary[k] = "fiverfiver123"

    if zeroCount < oneCount:
        for k in range(len(oxyBinary)):
            if oxyBinary[k][i] == "1":
                oxyBinary[k] = "fiverfiver123"

    if zeroCount == oneCount:
        for k in range(len(oxyBinary)):
            if oxyBinary[k][i] == "0":
                oxyBinary[k] = "fiverfiver123"




    for x in range(len(oxyBinary)):
        if (oxyBinary[x][0] == "0"):
            print(oxyBinary[x])
        elif (oxyBinary[x][0] == "1"):
            print(oxyBinary[x])

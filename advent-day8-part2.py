file = open('code_input.txt', 'r')
data = file.read()
file.close()
inputs = data.split()

file = open('output_code.txt', 'r')
data = file.read()
file.close()
outputs = data.split()

class Code:
    def __init__(self):
        self.uni0 = "" 
        self.uni1 = ""
        self.uni2 = ""
        self.uni3 = ""
        self.uni4 = ""
        self.uni5 = ""
        self.uni6 = ""
        self.uni7 = ""
        self.uni8 = ""
        self.uni9 = ""

    def decode(self, info):

        

        for i in range(len(info)):
            if len(info[i]) == 2:
                self.uni1 = info[i]
            elif len(info[i]) == 4:
                self.uni4 = info[i]
            elif len(info[i]) == 3:
                self.uni7 = info[i]
            elif len(info[i]) == 7:
                self.uni8 == info[i]



        

        for word in info:
            if len(word) == 5:
                if self.uni1[0] in word and self.uni1[1] in word:
                    self.uni3 = word
                    info.remove(word)



        for word in info:
            if len(word) == 6:
                if self.uni1[0] not in word or self.uni1[1] not in word:
                    self.uni6 = word
                    info.remove(word)

                    

        for word in info:
            if len(word) == 5:
                count = 0
                for letter in word:
                    if letter in self.uni6:
                        count += 1

                if count == 5:
                    self.uni5 = word
                elif count != 5:
                    self.uni2 = word

        for word in info:
            if len(word) == 6:
                count = 0
                for letter in word:
                    if letter in self.uni4:
                        count += 1
                if count == 4:
                    self.uni9 = word
                elif count != 4:
                    self.uni0 = word
                

    def decipher(self, info):
        key = []
        for word in info:
            if len(word) == 2:
                key.append("1")
            elif len(word) == 4:
                key.append("4")
            elif len(word) == 3:
                key.append("7")
            elif len(word) == 7:
                key.append("8")

            if len(word) == 5:
                count1 = 0
                for letter in word:
                    if letter in self.uni2:
                        count1 += 1
                if count1 == 5:
                    key.append("2")

                count2 = 0
                for letter in word:
                    if letter in self.uni3:
                        count2 += 1
                if count2 == 5:
                    key.append("3")

                count3 = 0
                for letter in word:
                    if letter in self.uni5:
                        count3 += 1
                if count3 == 5:
                    key.append("5")

            if len(word) == 6:
                count1 = 0
                for letter in word:
                    if letter in self.uni0:
                        count1 += 1
                if count1 == 6:
                    key.append("0")

                count2 = 0
                for letter in word:
                    if letter in self.uni6:
                        count2 += 1
                if count2 == 6:
                    key.append("6")

                count3 = 0
                for letter in word:
                    if letter in self.uni9:
                        count3 += 1
                if count3 == 6:
                    key.append("9")

        return "".join(key)

codes = Code()

input_code = []
code = []

i = 0
while i < len(inputs):
    code.append(inputs[i]) 
    if len(code) == 10:
       input_code.append(code)
       code = []

    i += 1

output_code = []
code = []
i = 0
while i < len(outputs):
    code.append(outputs[i])
    if len(code) == 4:
        output_code.append(code)
        code = []

    i += 1


keys = []

i = 0
while i < 200:
    codes.decode(input_code[i])
    keys.append(codes.decipher(output_code[i]))
    i += 1



count = 0
for num in keys:
    count += int(num)
            


print(count)

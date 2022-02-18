file = open('input.txt', 'r')
data = file.read()
file.close()
lantern_input = data.split(",")


class Lantern:
    def __init__(self, counter):
        self.counter = counter
        if self.counter < 7:
            self.just_born = False
            self.life_cycles = 1

        else:
            self.just_born = True
            self.life_cycles = 0

    def spawn(self):
        if self.just_born == False:
            self.just_born == True


lanterns = []

for i in range(len(lantern_input)):
    lanterns.append(Lantern(int(lantern_input[i])))

i = 0
while i < 256:
    for lantern in lanterns:
        lantern.counter -= 1
        if lantern.counter == 0:
            lanterns.append(Lantern(10))

        if lantern.counter == -1:
            lantern.counter = 6

    i += 1

        
print(len(lanterns))



#for i in range(len(lanterns)):
    #print(lanterns[i].counter)

count = 0
for i in range(len(lanterns)):
    if lanterns[i].counter == 9:
        count += 1

print(count)
print(len(lanterns) - count)

lantern = {
    9:0,
    8:0,
    7:0,
    6:0,
    5:29,
    4:28,
    3:20,
    2:25,
    1:198,
    0:0,
    
    
}

i = 0
while i < 256:

    
    lantern[0] = lantern[1]
    lantern[1] = lantern[2]
    lantern[2] = lantern[3]
    lantern[3] = lantern[4]
    lantern[4] = lantern[5]
    lantern[5] = lantern[6]
    lantern[6] = lantern[7] + lantern[9]
    lantern[7] = lantern[8]
    lantern[8] = lantern[9]
    lantern[9] = lantern[0]


    
   
    i += 1



print(lantern)
print(lantern[0] + lantern[1] + lantern[2] + lantern[3] + lantern[4] + lantern[5] + lantern[6] + lantern[7] + lantern[8])

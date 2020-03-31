spiral = []
length = 1001
for i in range(length):
    row = []
    for j in range(length):
        row.append(1)
    spiral.append(row)
    #print(spiral[i])

x = int(length/2)
y = int(length/2)

adder = 1
negative = 1
for i in range(len(spiral)):
    for j in range (i):
        y -= (1 * negative)
        spiral[x][y] += adder
        adder += 1 
    for j in range(i):
        x -= (1 * negative)
        spiral[x][y] += adder
        adder += 1
    

    if negative == 1:
        negative = -1
    elif negative == -1:
        negative = 1

for i in range(1, len(spiral[0])):
    spiral[0][i] += adder
    adder += 1
        
#spiral is created
answer = -1 #number 1 in the middle will be used twice
for diag in range(len(spiral)):
    answer += spiral[diag][diag]
    answer += spiral[diag][(length-1) - diag]
print(answer)
    

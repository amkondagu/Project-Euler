data = open('p067_triangle.txt', 'r') #opening the huge triangle file

tri = []
for lines in data:
    lines = lines.rstrip()
    lines = lines.split()
    lines = list(lines)
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    tri.append(lines)

data.close()

#fancy alg
while len(tri) != 1: #breaking down the triangle to one line
    for i in range(len(tri[-2])): #loop thru the 2nd to last row
        tri[-2][i] += max(tri[-1][i], tri[-1][i+1]) #add the greater of the two adjacent numbers
        
    tri.pop(-1) #delete the last row
    for j in range(len(tri)):
        print(tri[j])  #print the triangle just for fun
    print("\n")

print(tri)

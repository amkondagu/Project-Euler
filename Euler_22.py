data = open('p022_names.txt', 'r') #opening the huge names file
names = None
chars = data.readline()
#names.append(chars)
chars = chars.replace('"', "")
names = chars.split(',')
data.close()
ans = 0
names = sorted(names)
for place in range(len(names)):
    tempAns = 0
    for letter in names[place]:
        tempAns += (ord(letter)-64)
    tempAns *= (place+1)
    ans += tempAns
print(ans)
    
    
    
        
        



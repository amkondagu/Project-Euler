'''
ans = 1
combo = []
def pickNumber(oldNum):
    global combo
    global ans
    values = [100, 50, 20, 10, 5, 2, 1]
    newNum = oldNum
    for i in enumerate(values):
        if i[1] > newNum:
          continue
        combo.append(i[1])
        newNum -= i[1]
        print(i[1])
        if values[i[0]] + newNum > oldNum:
          values.pop[i[0]]
          print(combo)
        if sum(combo) == 200:
            ans += 1
            print(combo)
            combo = []
            print('yayyy')
            print(values)
            pickNumber(200)
        print(combo)
        pickNumber(newNum)
        
pickNumber(200)

'''

DP = [0 for i in range(0, 10 + 1)]
print(DP)
        

import math
import sys
#sys.exit()
print('started')
num = 1
tri = 0
factors = 0
while factors < 500:
    factors = 0
    tri += num
    num += 1
    for i in range(1, int(math.sqrt(tri))+ 1):
        if tri % i == 0:
            factors += 2
        if math.sqrt(tri) == int(math.sqrt(tri)):
            factors -= 1


print('answer: ' + str(tri))

    

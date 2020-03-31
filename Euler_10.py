import math
print('code has started')
prime = None
def checkPrime(number):
    global prime
    if number == 2:
        prime = True
        
    for factor in range(2 , int(math.sqrt(number))+1):
        if number % factor == 0:
            prime = False
            break
        elif number % factor != 0:
            prime = True

    return prime
count = 0
answer = 0
while count < 2_000_000:
    count += 1
    if checkPrime(count) == True:
        answer += count
        print(count)

print(answer)
        
    


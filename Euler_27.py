from math import sqrt, ceil
def checkPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for factor in range(3, ceil(sqrt(number))+1, 2):
        if number % factor == 0:
            return False
            break
    return True
count = 1
primes = []
while count <= 1000:
    if checkPrime(count):
        primes.append(count)
        primes.append(count * -1)
    count += 1
#print(len(primes))
#print(primes)
highest = 0
for a in primes:
    for b in primes:
        count = 0
        while True:
            possible = count**2 + (a*count) + b
            if possible in primes:
                count += 1
            else:
                if count > highest:
                    highest = count
                    highest_a = a
                    highest_b = b
                break
#print(highest)
#print(highest_a, highest_b)
print('Answer: ' + str(highest_a*highest_b))
        
            

prime = None
def checkPrime(number):
    global prime
    if number == 2:
        prime = True
        
    for factor in range(2, number):
        if number % factor == 0:
            prime = False
            break
        elif number % factor != 0:
            prime = True

    return prime
count = 0
primes = 0
while primes < 10001:
    count += 1
    if checkPrime(count) == True:
        primes += 1
        

print(count)
        
    


from math import sqrt, ceil
print('code is running')
def checkPrime(number): 
    global prime
    for factor in range(2, ceil(sqrt(number))):
        if number % factor == 0:
            return False
    return True
problem = 600851475143    
for i in range(1,ceil(problem/2),2):
    if problem % i == 0:
        if checkPrime(i):
       # print(str(i) + " is a factor")
           # print(str(i) + " is prime")
            answer = i
            print(answer)
print(answer)
print('done')

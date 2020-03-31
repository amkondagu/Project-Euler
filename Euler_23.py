from math import ceil, sqrt
def addFactors(num):
    numSum = 0
    numRange = ceil(sqrt(num))
    if int(sqrt(num)) == sqrt(num):
           numRange += 1
    for i in range(1, numRange):
        if num % i == 0 and i != num:
            numSum += i + num/i
            if i == 1 or i == num/i:
                numSum -= num/i    
    if numSum == num:
        return 'perfect'
    elif numSum < num:
        return 'deficient'
    elif numSum > num:
        return 'abundant'
    
def sum_of_2_abundants(num):
    for num1 in range(1, num):
        num2 = num - num1
        if addFactors(num1) == 'abundant' and addFactors(num2) == 'abundant':
            return True
    return False

ans = 0
for number in range(1, 28124):
    if sum_of_2_abundants(number) == False:
        ans += number
        #print(number)
    if number % 1000 == 0:
        print(number)
print(ans)






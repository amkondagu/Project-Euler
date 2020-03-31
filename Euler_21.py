def checkAmicable(num1):
    sum1 = 0
    sum2 = 0
    for i in range(1, int(num1/2)+1):
        if num1 % i == 0:
            sum1 = sum1 + i + (num1%i)
            if i == num1/i or i == 1:
                sum1 -= num1%i
    num2 = sum1
    if num1 == num2:
        return False
    if num1 == 1 or num2 == 1:
        return False
    for j in range(1, int(num2/2)+1):
        if num2 % j == 0:
            sum2 += j + num2 % 2
            if j == num2/i or j == 1:
                sum2 -= num2%j
    if sum1 == num2 and sum2 == num1:
        return True
    else:
        return False
ans = 0
for a in range(1, 10000):
    if checkAmicable(a):
        print(a)
        ans += a

print('Answer: ' + str(ans))
        

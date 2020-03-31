count1 = 10
for n in range(1, 1_000_000):
    count = 1
    origN = n
    while n != 1:        
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    if count > count1:
        count1 = count
        answer = origN
        print(answer)

    
print('answer: '+ str(answer), str(count1) + " loops")
        
        

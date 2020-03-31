def fib(terms):
    oldnum = 0
    newnum = 1
    if terms == 0:
        return oldnum
    elif terms == 1:
        return newnum
    else:
        for x in range(0,terms-1):
            newnum = oldnum + newnum
            oldnum = newnum - oldnum
        return newnum

counter = 12
while True:
    if len(str(fib(counter))) == 1000:
        print(counter)
        break
    counter += 1
    
    


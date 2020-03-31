number = 20
while True:
    for factor in range(1,21):
        if number % factor == 0:
            multiple = True
        else:
            multiple = False
            break
    if multiple == True:
        break
    number += 20
print(number)
        
        

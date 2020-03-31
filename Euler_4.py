highestpal = 0
def pal(number):
  checkDigit = 0
  digits = (len(str(number)))
  if digits % 2 == 1:
    odd = True
  elif digits % 2 == 0:
    odd = False
  else:
    print('invalid input')

  if odd == True:
    repeats = (digits-1)/2

  elif odd == False:
    repeats = digits/2

  for i in range(int(repeats)):
    if str(number)[checkDigit] == str(number)[-checkDigit-1]:
      pallendrome = True
    else:
      
      pallendrome  = False
      break
    checkDigit += 1  

  if pallendrome == True:
    #print(str(number) + " is a pallendrome")
    global highestpal
    if number > highestpal:
      highestpal = number

for number1 in range(100,1000):
  for number2 in range(100,1000):
    number = number1 * number2
    pal(number)

print(highestpal)



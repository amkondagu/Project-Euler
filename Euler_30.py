number = 2
answer = 0
while number < 200_000:
    fifth = 0
    for digit in str(number):
        fifth += int(digit) ** 5
    if fifth == number:
        print(fifth, number)
        answer += number
    number += 1
print('Answer: ' + str(answer))

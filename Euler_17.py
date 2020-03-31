letters = "- one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
letters = letters.split(' ')
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#print(letters)
def wordNum(num):
    if 0 < num < 20:
        return letters[num]
    elif len(str(num)) == 2:
        if int(str(num)[1]) == 0:
            return tens[int(str(num)[0])]
        else:
            return tens[int(str(num)[0])]+letters[int(str(num)[1])]
    elif len(str(num)) == 3:
        if int(str(num)[1:3]) == 00:
            return letters[int(str(num)[0])] + 'hundred'
        return letters[int(str(num)[0])] + 'hundredand' + wordNum(int(str(num)[1:3]))
    elif num == 1000:
        return 'onethousand'
   
ans = 0
for num in range(1 ,1001):
    ans += len(wordNum(num))
    print(wordNum(num))
print(ans)



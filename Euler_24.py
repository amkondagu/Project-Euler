from itertools import permutations
numbers = []
for i in range(10):
    numbers.append(i)
perms = list(permutations(numbers))
ans = []
for index in range(len(perms)):
    num = ''
    for digits in perms[index]:
        num += str(digits)
    ans.append(int(num))

#ans.sort()
print(ans[999_999])
    
    

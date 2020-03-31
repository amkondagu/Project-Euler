import itertools
perms = []
ans = 0
for i in range(20):
    perms.append(1)
    perms.append(0)
all = itertools.permutations(perms)
ansList = []
for i in (all):
    if i not in ansList:
        ansList.append(i)
        ans += 1
        print(i)
print('hi')
print(ans)
    

import calendar
ans = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if calendar.monthrange(i, j)[0] == 6:
            ans += 1
print(ans)
            

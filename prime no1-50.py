i = 2
while i <= 50:
    j = 2
    while j < 50:
        if i%j == 0:
            break
        j += 1
    if i == j:
        print(i,end=',')
    i += 1

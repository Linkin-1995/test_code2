def sum():
    mul=2
    for i in range(3,100001):
        for o in range(2,i):
            if i % o == 0:
                break
        else:
	    mul += i
    return mul
print(sum())

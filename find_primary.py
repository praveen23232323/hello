n = 55

flat = False
for i in range(2,n):

    for j in range(i+1,n):
        if n % j == 0:
            flat = True
            break 
if not flat:
    print("primary")

else:
    print("not primary")    

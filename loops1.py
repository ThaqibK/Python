while True:
    n = int(input("Value of n: "))
    if n > 0:                            # It reduces the code to only check if its greater then breaks.
        break

'''
# also written as 

while True:
    n = int(input("Value of n: "))
    if n < 0:
        continue
    else:
        break
        
'''

for _ in range(n):
    print ("Baka!")
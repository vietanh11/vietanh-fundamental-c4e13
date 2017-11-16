numbers = [10,11,26,85,11,25,56,100,98,63,10,11]
x = int(input("enter your number ?"))
count_number = 0

for i in numbers :
    if x ==i:
        count_number += 1
print ("number", x, "appear", count_number, "times in this list")

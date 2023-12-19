import time
import math
start = time.time()

def sum_of_list():
    sum = 0
    for y in mylist:
        sum=sum + y
    return sum
print(sum)
mylist = []
def split(number, parts):
    if number > parts:
        number2 = number / parts
        for t in range(parts-1):
            mylist.append(int(number2))
            number2 = (number- (number - round(number2)))
        mylist.append(number - sum_of_list())

    else:
        for i in range(parts - number):
            mylist.append(0)
        for a in range(parts - (parts-number)):
            mylist.append(1)
    print(mylist)


split(99999987, 50)






end = time.time()

print(end - start)
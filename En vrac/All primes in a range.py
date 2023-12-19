from math import ceil

nbr_of_prime = 0
nbr_of_prime2 = 0
prime_list = {}
listofnumbers = []
listofprimes = []

def creer_variable(nmbr):
    while f'prime{nmbr}' not in prime_list:
        variable_name = f'prime{nmbr}'
        prime_list[variable_name] = 0


def changer_variable(nmbr):
    prime_list[f'prime{nmbr}'] += 1


def nombrepremier(nombre):
    global nbr_of_prime
    o = 2
    for n in range(2, ceil(int(nombre)/2)):
        if n > o:
            break

        trynombre = int(nombre)/n
        if trynombre == int(trynombre):
            creer_variable(n)
            prime_list[f'prime{n}'] += 1
            break
        elif trynombre != int(trynombre):
            o += 1
            if o > round(int(nombre)/2)-1:
                creer_variable(nombre)
                prime_list[f'prime{nombre}'] += 1
                listofprimes.append(nombre)
                nbr_of_prime += 1
                break
        else :
            print("what ???")



import time
import turtle as tu
from collections import deque
from_ = 0            # int(input("primes from : "))
to = 100             # int(input("to : "))


'''tu.speed(50000)
tu.penup()
tu.backward(200)'''

mylist = deque()

loops = int(input("Number of loops : "))
for t in range(loops):
    if from_ < 4:
        if from_ < 3:
            listofprimes.append(2)
            listofprimes.append(3)
            nbr_of_prime += 2
        else:
            listofprimes.append(3)
            nbr_of_prime += 1

    for y in range(from_, to):
        nombrepremier(y)
    nbr_of_prime3 = nbr_of_prime - nbr_of_prime2
    # print(nbr_of_prime3)
    nbr_of_prime2 = nbr_of_prime
    mylist.append(nbr_of_prime3)


    '''tu.pendown()
    tu.left(90)
    tu.forward((nbr_of_prime3 - (nbr_of_prime3/10)*5) * 10)
    tu.backward((nbr_of_prime3 - (nbr_of_prime3/10)*5) * 10)
    tu.right(90)
    tu.penup()
    tu.forward((50 / (loops/5)))
    tu.pendown()'''
    from_ += 100
    to += 100
#   print(t)
prime_list['prime2'] += 3
print(prime_list)


kills = 0
for key, value in prime_list.items():
    kills += prime_list[key]

print(kills)
print(listofprimes)

for y in listofprimes:
    if y / 31 == int(y / 31):
        print(y)


# à faire: montrer le nombre de kills de chaque prime number (26 est kill par 3, on fait donc +1 au nombre de kills de 2)



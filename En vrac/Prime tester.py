def nombrepremier(nombre):
    o = 2
    for n in range(2, int(int(nombre)/2)):
        if n > o:
            print("ce nombre n'est pas premier, car il est divisible par " + str(n))
            break
        trynombre = int(nombre)/n
        if trynombre == int(trynombre):
            print("ce nombre n'est pas premier, car il est divisible par " + str(n))
            break
        elif trynombre != int(trynombre):
            o += 1
            if o > round(int(nombre)/2)-1:
                print("ce nombre est premier")
                break
        else :
            print("what ???")
        

import time

while True:
    nombre1 = input("quel nombre voulez-vous tester ? ")
    start = time.time()
    nombrepremier(nombre1)
    end = time.time()
    print(end - start)
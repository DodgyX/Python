# from 10 000 to dix mille


unitdec = "non"
dizdec = "non plus"

def unitée(nbrrandom):
    global unitdec
    global unitnbr
    unitnbr = int(nbrrandom[-1:])
    if unitnbr == 1:
        unitdec = ["un", "onze", "et onze", "et un"]
    elif unitnbr == 2:
        unitdec = ["deux", "douze"]
    elif unitnbr == 3:
        unitdec = ["trois", "treize"]
    elif unitnbr == 4:
        unitdec = ["quatre", "quatorze"]
    elif unitnbr == 5:
        unitdec = ["cinq", "quinze"]
    elif unitnbr == 6:
        unitdec = ["six", "seize"]
    elif unitnbr == 7:
        unitdec = ["sept"]
    elif unitnbr == 8:
        unitdec = ["huit"]
    elif unitnbr == 9:
        unitdec = ["neuf"]
    else:
        unitdec = [""]


def dizaine(nbrrandomdix):
    dizaine = int(nbrrandomdix[-2:])
    unitée(nbrrandomdix)
    global unitdec
    global unitnbr
    global dizdec
    if 20 > dizaine >= 10:
        if 6 >= unitnbr > 0:
            unitdec = unitdec[1]
        else:
            unitdec = "dix " + unitdec[0]

    elif 30 > dizaine >= 20:
        dizdec = "vinght "
        unitdec = dizdec + unitdec[0]

    elif 40 > dizaine >= 30:
        dizdec = "trente "
        unitdec = dizdec + unitdec[0]

    elif 50 > dizaine >= 40:
            dizdec = "quarante "
            unitdec = dizdec + unitdec[0]

    elif 60 > dizaine >= 50:
            dizdec = "cinquante "
            unitdec = dizdec + unitdec[0]

    elif 70 > dizaine >= 60:
            dizdec = "soixante "
            unitdec = dizdec + unitdec[0]

    elif 80 > dizaine >= 70:
        dizdec = "soixante-dix "
        if 6 >= unitnbr > 1:
            unitdec = "soixante " + unitdec[1]
        elif unitnbr == 1:
            unitdec = "soixante " + unitdec[2]
        else:
            unitdec = dizdec + unitdec[0]

    elif 90 > dizaine >= 80:
        dizdec = "quatre-vinght "
        unitdec = dizdec + unitdec[0]

    elif dizaine >= 90:
        dizdec = "quatre-vinght-dix "
        if 6 >= unitnbr > 0:
            unitdec = dizdec[:14] + unitdec[1]
        else:
            unitdec = dizdec + unitdec[0]

    else:
        dizdec = ""
        unitdec = unitdec[0]

    dizdec = unitdec


millenbr = ""

def centaine(a):
    dizaine(a)
    a = int(a)
    if 200 > a >= 100:
        cendec = "cent "
    elif 300 > a >= 200:
        cendec = "deux cent "
    elif 400 > a >= 300:
        cendec = "trois cent "
    elif 500 > a >= 400:
        cendec = "quatre cent "
    elif 600 > a >= 500:
        cendec = "cinq cent "
    elif 700 > a >= 600:
        cendec = "six cent "
    elif 800 > a >= 700:
        cendec = "sept cent "
    elif 900 > a >= 800:
        cendec = "huit cent "
    elif a >= 900:
        cendec = "neuf cent "
    else:
        cendec = ""
    
    global millenbr
    millenbr = cendec + dizdec




def milliers(nombreint):
    moin = 0
    global nombredec
    nombredec = ""
    while len(nombre)-moin  > 3:
        if 6 >= len(nombre)-moin > 3:
            nombrecut = nombreint[-6:len(nombre)-3]
            centaine(nombrecut)
            nombredec = nombredec + millenbr + " mille  "

        elif  9 >= len(nombre)-moin > 6:
            nombrecut = nombreint[-9:len(nombre)-6]
            centaine(nombrecut)
            nombredec = nombredec + millenbr + " million  "

        elif  12 >= len(nombre)-moin > 9:
            nombrecut = nombreint[-12:len(nombre)-9]
            centaine(nombrecut)
            nombredec = nombredec + millenbr + " milliard  "
        
        elif  15 >= len(nombre)-moin > 12:
            nombrecut = nombreint[-15:len(nombre)-12]
            centaine(nombrecut)
            nombredec = nombredec + millenbr + " billion  "

        elif  18 >= len(nombre)-moin > 15:
            nombrecut = nombreint[-18:len(nombre) - 15]
            centaine(nombrecut)
            nombredec = nombredec + millenbr + " billiard  "

        else:
            print("le nombre est trop grand")
            moin += 999999
            return
        
        moin += 3
    nombrecut = nombreint[-3:]
    centaine(nombrecut)
    nombredec = nombredec + millenbr

    print(nombredec)


nombre = input("choisissez un nombre : ")
milliers(nombre)
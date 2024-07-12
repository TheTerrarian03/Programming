def option1(b1, b2, b3):
    b = "".join(b1)
    ca = "".join(b2)
    try:
        c = float(ca)
    except ValueError:
        return "error"
    d = "".join(b3)

    answer = False

    if b == 'mm' and d == 'mm':
        answer = c
    if b == 'mm' and d == 'cm':
        answer = c / 10
    if b == 'mm' and d == 'm':
        answer = c / 1000
    if b == 'mm' and d == 'km':
        answer = c / 1000000
    if b == 'mm' and d == 'inches':
        answer = c / 25.4
    if b == 'mm' and d == 'feet':
        answer = c / 304.8
    if b == 'mm' and d == 'yards':
        answer = c / 914.4
    if b == 'mm' and d == 'miles':
        answer = c / 1609344
    if b == 'mm' and d == 'ly':
        answer = c / 9460730472580800000
    if b == 'cm' and d == 'mm':
        answer = c * 10
    if b == 'cm' and d == 'cm':
        answer = c
    if b == 'cm' and d == 'm':
        answer = c / 100
    if b == 'cm' and d == 'km':
        answer = c / 100000
    if b == 'cm' and d == 'inches':
        answer = c / 2.54
    if b == 'cm' and d == 'feet':
        answer = c / 30.48
    if b == 'cm' and d == 'yards':
        answer = c / 91.44
    if b == 'cm' and d == 'miles':
        answer = c / 160934.4
    if b == 'cm' and d == 'ly':
        answer = c / 946073047258080000
    if b == 'm' and d == 'mm':
        answer = c * 1000
    if b == 'm' and d == 'cm':
        answer = c * 100
    if b == 'm' and d == 'm':
        answer = c
    if b == 'm' and d == 'km':
        answer = c / 1000
    if b == 'm' and d == 'inches':
        answer = c * 39.3701
    if b == 'm' and d == 'feet':
        answer = c * 3.28084
    if b == 'm' and d == 'yards':
        answer = c * 1.094
    if b == 'm' and d == 'miles':
        answer = c / 1609
    if b == 'm' and d == 'ly':
        answer = c / 9460730472580800
    if b == 'km' and d == 'mm':
        answer = c * 1000000
    if b == 'km' and d == 'cm':
        answer = c * 100000
    if b == 'km' and d == 'm':
        answer = c * 1000
    if b == 'km' and d == 'km':
        answer = c
    if b == 'km' and d == 'inches':
        answer = c * 39370.1
    if b == 'km' and d == 'feet':
        answer = c * 3281
    if b == 'km' and d == 'yards':
        answer = c * 1094
    if b == 'km' and d == 'miles':
        answer = c / 1.609
    if b == 'km' and d == 'ly':
        answer = c / 9460730472580.8
    if b == 'inches' and d == 'mm':
        answer = c * 25.4
    if b == 'inches' and d == 'cm':
        answer = c * 2.54
    if b == 'inches' and d == 'm':
        answer = c / 39.37
    if b == 'inches' and d == 'km':
        answer = c / 39370
    if b == 'inches' and d == 'inches':
        answer = c
    if b == 'inches' and d == 'feet':
        answer = c / 12
    if b == 'inches' and d == 'yards':
        answer = c / 36
    if b == 'inches' and d == 'miles':
        answer = c / 63360
    if b == 'inches' and d == 'ly':
        answer = c / 372469703644913408
    if b == 'feet' and d == 'mm':
        answer = c * 304.8
    if b == 'feet' and d == 'cm':
        answer = c * 30.48
    if b == 'feet' and d == 'm':
        answer = c / 3.281
    if b == 'feet' and d == 'km':
        answer = c / 3281
    if b == 'feet' and d == 'inches':
        answer = c * 12
    if b == 'feet' and d == 'feet':
        answer = c
    if b == 'feet' and d == 'yards':
        answer = c / 3
    if b == 'feet' and d == 'miles':
        answer = c / 5280
    if b == 'feet' and d == 'ly':
        answer = c / 31039141970409448
    if b == 'yards' and d == 'mm':
        answer = c * 914.4
    if b == 'yards' and d == 'cm':
        answer = c * 91.44
    if b == 'yards' and d == 'm':
        answer = c / 1.094
    if b == 'yards' and d == 'km':
        answer = c / 1094
    if b == 'yards' and d == 'inches':
        answer = c * 36
    if b == 'yards' and d == 'feet':
        answer = c * 3
    if b == 'yards' and d == 'yards':
        answer = c
    if b == 'yards' and d == 'miles':
        answer = c / 1760
    if b == 'yards' and d == 'ly':
        answer = c / 10346380656803150
    if b == 'miles' and d == 'mm':
        answer = c * 1609344
    if b == 'miles' and d == 'cm':
        answer = c * 160934.4
    if b == 'miles' and d == 'm':
        answer = c / 1609.344
    if b == 'miles' and d == 'km':
        answer = c / 1.609344
    if b == 'miles' and d == 'inches':
        answer = c * 63360
    if b == 'miles' and d == 'feet':
        answer = c * 5280
    if b == 'miles' and d == 'yards':
        answer = c * 1760
    if b == 'miles' and d == 'miles':
        answer = c
    if b == 'miles' and d == 'ly':
        answer = c / 5878625373183.6074219
    if b == 'ly' and d == 'mm':
        answer = c * 9460730472580800000
    if b == 'ly' and d == 'cm':
        answer = c * 946073047258080000
    if b == 'ly' and d == 'm':
        answer = c * 9460730472580800
    if b == 'ly' and d == 'km':
        answer = c * 9460730472580.8
    if b == 'ly' and d == 'inches':
        answer = c * 372469703644913408
    if b == 'ly' and d == 'feet':
        answer = c * 31039141970409448
    if b == 'ly' and d == 'yards':
        answer = c * 10346380656803150
    if b == 'ly' and d == 'miles':
        answer = c * 5878625373183.6074219
    if b == 'ly' and d == 'ly':
        answer = c

    if not answer:
        answer = "error"

    return answer


def option2(b1, b2, b3):
    f = "".join(b1)
    ga = "".join(b2)
    try:
        g = float(ga)
    except ValueError:
        return "error"
    h = "".join(b3)

    answer = False

    if f == "c" and h == "c":
        answer = g
    if f == "c" and h == "f":
        answer = (g * 9 / 5) + 32
    if f == "c" and h == "k":
        answer = g + 273.15
    if f == "f" and h == "c":
        answer = (g - 32) * 5 / 9
    if f == "f" and h == "f":
        answer = g
    if f == "f" and h == "k":
        answer = ((g - 32) * 5 / 9) + 273.15
    if f == "k" and h == "c":
        answer = g - 273.15
    if f == "k" and h == "f":
        answer = ((g - 273.15) * 9 / 5) + 32
    if f == "k" and h == "k":
        answer = g

    if not answer:
        answer = "error"

    return answer


def option3(b1, b2, b3):
    b = "".join(b1)
    ca = "".join(b2)
    try:
        c = float(ca)
    except ValueError:
        return "error"
    d = "".join(b3)

    answer = False

    # units: milliseconds (ms), seconds (s), minutes (m), hours (h), days (d), weeks (w), years (y),
    # decades (dec.), centuries (cent.)
    # based on 365 days per year and 52 weeks per year

    if b == "ms" and d == "ms":
        answer = c
    if b == "ms" and d == "s":
        answer = c / 1000
    if b == "ms" and d == "m":
        answer = c / 60000
    if b == "ms" and d == "h":
        answer = c / 3600000
    if b == "ms" and d == "d":
        answer = c / 86400000
    if b == "ms" and d == "w":
        answer = c / 604800000
    if b == "ms" and d == "y":
        answer = c / 31536000000
    if b == "ms" and d == "dec.":
        answer = c / 315360000000
    if b == "ms" and d == "cent.":
        answer = c / 3153600000000
    if b == "s" and d == "ms":
        answer = c * 1000
    if b == "s" and d == "s":
        answer = c
    if b == "s" and d == "m":
        answer = c / 60
    if b == "s" and d == "h":
        answer = c / 3600
    if b == "s" and d == "d":
        answer = c / 86400
    if b == "s" and d == "w":
        answer = c / 604800
    if b == "s" and d == "y":
        answer = c / 31536000
    if b == "s" and d == "dec.":
        answer = c / 315360000
    if b == "s" and d == "cent.":
        answer = c / 315360000
    if b == "m" and d == "ms":
        answer = c * 60000
    if b == "m" and d == "s":
        answer = c * 60
    if b == "m" and d == "m":
        answer = c
    if b == "m" and d == "h":
        answer = c / 60
    if b == "m" and d == "d":
        answer = c / 1440
    if b == "m" and d == "w":
        answer = c / 10080
    if b == "m" and d == "y":
        answer = c / 525600
    if b == "m" and d == "dec.":
        answer = c / 5256000
    if b == "m" and d == "cent.":
        answer = c / 52560000
    if b == "h" and d == "ms":
        answer = c * 3600000
    if b == "h" and d == "s":
        answer = c * 3600
    if b == "h" and d == "m":
        answer = c * 60
    if b == "h" and d == "h":
        answer = c
    if b == "h" and d == "d":
        answer = c / 24
    if b == "h" and d == "w":
        answer = c / 168
    if b == "h" and d == "y":
        answer = c / 8760
    if b == "d" and d == "ms":
        answer = c * 86400000
    if b == "d" and d == "s":
        answer = c * 86400
    if b == "d" and d == "m":
        answer = c * 1440
    if b == "d" and d == "h":
        answer = c * 24
    if b == "d" and d == "d":
        answer = c
    if b == "d" and d == "w":
        answer = c / 7
    if b == "d" and d == "y":
        answer = c / 365
    if b == "d" and b == "dec.":
        answer = c / 3650
    if b == "d" and b == "cent.":
        answer = c / 36500
    if b == "w" and d == "ms":
        answer = c * 604800000
    if b == "w" and d == "s":
        answer = c * 604800
    if b == "w" and d == "m":
        answer = c * 10080
    if b == "w" and d == "h":
        answer = c * 168
    if b == "w" and d == "d":
        answer = c * 7
    if b == "w" and d == "w":
        answer = c
    if b == "w" and d == "y":
        answer = c / 2555
    if b == "w" and d == "dec.":
        answer = c / 25550
    if b == "w" and d == "cent.":
        answer = c / 255500
    if b == "y" and d == "ms":
        answer = c * 31536000000
    if b == "y" and d == "s":
        answer = c * 31536000
    if b == "y" and d == "m":
        answer = c * 525600
    if b == "y" and d == "h":
        answer = c * 8760
    if b == "y" and d == "d":
        answer = c * 365
    if b == "y" and d == "w":
        answer = c * 52
    if b == "y" and d == "y":
        answer = c
    if b == "y" and d == "dec.":
        answer = c / 10
    if b == "y" and d == "cent.":
        answer = c / 100
    if b == "dec." and d == "ms":
        answer = c * 315360000000
    if b == "dec." and d == "s":
        answer = c * 315360000
    if b == "dec." and d == "m":
        answer = c * 5256000
    if b == "dec." and d == "h":
        answer = c * 87600
    if b == "dec." and d == "d":
        answer = c * 3650
    if b == "dec." and d == "w":
        answer = c * 520
    if b == "dec." and d == "y":
        answer = c * 10
    if b == "dec." and d == "dec.":
        answer = c
    if b == "dec." and d == "cent.":
        answer = c / 10
    if b == "cent." and d == "ms":
        answer = c * 3153600000000
    if b == "cent." and d == "s":
        answer = c * 3153600000
    if b == "cent." and d == "m":
        answer = c * 52560000
    if b == "cent." and d == "h":
        answer = c * 876000
    if b == "cent." and d == "d":
        answer = c * 36500
    if b == "cent." and d == "w":
        answer = c * 5200
    if b == "cent." and d == "y":
        answer = c * 100
    if b == "cent." and d == "dec.":
        answer = c * 10
    if b == "cent." and d == "cent.":
        answer = c

    if not answer:
        return "error"

    return answer


def option4(b1, b2, b3):
    if b1 and not b2 and not b3:
        a = "".join(b1)
        return a
    elif b2 and not b1 and not b3:
        a = "".join(b2)
        return a
    elif b3 and not b1 and not b2:
        a = "".join(b3)
        return a
    elif b1 and b2 and not b3:
        a = "".join(b1)
        b = "".join(b2)

        if a == b:
            return a
        elif a == "1" or b == "1":
            return "haha nice try"
        else:
            aa = []
            ab = []
            i = 1

            # writing
            for _ in range(5000):
                aa.append(int(a) * i)
                ab.append(int(b) * i)
                i += 1

            # checking
            for num1 in aa:
                for num2 in ab:
                    if num1 == num2:
                        return num1
            return "none"
    else:
        return "wassup my dude"


def option7(old):
    string = "".join(old)
    list = []
    listRev = []
    num = int(string)
    while True:
        num += 1
        for item in str(num):
            list.append(item)
        for item in range(len(list)):
            listRev.append(list[-(item + 1)])
        if list == listRev:
            print(*list, sep="")
            print("The difference was " + str((num - int(string))))
            return list
        else:
            list.clear()
            listRev.clear()


"""if __name__ == '__main__':
    print("PLEASE RUN MAIN.PY")"""

if __name__ == '__main__':
    ia = input()
    ib = input()
    ic = input()
    print(option4(ia, ib, ic))

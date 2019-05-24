def __main__():
    print("Pls input your math expression:")
    b = input()
    validate(b)


def conv(b):
    b = b.replace(' ', '')
    splitters = ['+', '-', '*', '=', '/']
    spli = ['plus', 'minus', 'um', 'eq', 'del']
    ini = ''
    wsr = ''
    uni = []

    for i in splitters:
        s_index = splitters.index(i)
        b = b.replace(i, spli[int(s_index)])


    i = 0
    for s in b:
        if i:
            if s.isdigit():
                ini += s
                    # print(ini)
                if wsr:
                    uni.append(wsr)
                    wsr = ''
            else:
                    # print(ini)
                wsr += s
                if ini:
                    uni.append(ini)
                    ini = ''
        else:
            if s.isdigit():
                ini += s
            else:
                wsr += s
        i += 1
    if ini:
            uni.append(ini)
    elif wsr:
        uni.append(wsr)


    for n in uni:
        if n.isdigit():
            b = uni.index(n)
            uni[b]= num2Word(n)
    print(' '.join(uni))


def num2Word(n):
    n3 = []
    r1 = ""

    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k

        if q < -2:
            break
        else:
            if q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r

    sp = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100) // 10
        b3 = (x % 1000) // 100

        if x == 0:
            continue
        else:
            t = thousands[i]
        if b2 == 0:
            sp = ones[b1] + t + sp
        elif b2 == 1:
            sp = tens[b1] + t + sp
        elif b2 > 1:
            sp = twenties[b2] + ones[b1] + t + sp
        if b3 > 0:
            sp = ones[b3] + "hundred " + sp
    return sp



ones = ["", "one ", "two ", "three ", "four ", "five ",
        "six ", "seven ", "eight ", "nine "]
tens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ",
            "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
thousands = ["", "thousand ", "million ", "billion ", "trillion ",
             "quadrillion ", "quintillion ", "sextillion ", "septillion ", "octillion ",
             "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ",
             "octodecillion ", "novemdecillion ", "vigintillion "]


def validate(b):
    if not b.isalpha():
         conv(b)
    else:
        print("Invalid input")


__main__()
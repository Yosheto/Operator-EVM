def poisk_podmassiva(glav, pod):
    """poisk podmassiva"""
    len1 = len(glav)
    len2 = len(pod)
    if len2 == 0:
        return -2
    if len2 > len1:
        return -1
    for start in range(len1 - len2 + 1):
        ok = True
        for k in range(len2):
            if glav[start + k] != pod[k]:
                ok = False
                break
        if ok:
            return start
    return -1

def vse_podmassivy(glav, pod):
    """vse vhozhdeniya"""
    res = []
    len1 = len(glav)
    len2 = len(pod)
    if len2 > len1 or len2 == 0:
        return res
    i = 0
    while i <= len1 - len2:
        if glav[i:i+len2] == pod:
            res.append(i)
        i += 1
    return res

def pokazat(poz, glav, pod):
    """pokazyvaet rezultat"""
    if poz == -1:
        print("[-] Podmassiv dlinnee osnovnogo")
    elif poz == -2:
        print("[-] Pustoy podmassiv")
    elif poz == -3:
        print("[-] Nichego ne naydeno")
    else:
        print(f"[+] Naydeno na pozicii {poz}")
        print(f"Osnovnoy: {glav}")
        print(f"Iskomiy:  {pod}")
        stroka = " " * (poz * 3 + 2) + "^" * len(pod)
        print(stroka)

def test1():
    d1 = [5, 5, 5, 5, 5]
    d2 = [5, 5]
    print("Test 1:")
    r1 = poisk_podmassiva(d1, d2)
    pokazat(r1, d1, d2)

def test2():
    e1 = [1, 2, 3, 1, 2, 3, 1]
    e2 = [2, 3]
    print("\nTest 2:")
    r2 = vse_podmassivy(e1, e2)
    print(f"Vse vhozhdeniya: {r2}")

def test3():
    f1 = [10, 20, 30, 40]
    f2 = [25, 30]
    print("\nTest 3:")
    r3 = poisk_podmassiva(f1, f2)
    pokazat(-3 if r3 < 0 else r3, f1, f2)

def vvod():
    """ruchnoy vvod"""
    print("\n" + "-"*30)
    print("Ruchnoy vvod")
    print("-"*30)
    try:
        a = input("Massiv: ").strip().split()
        b = input("Podmassiv: ").strip().split()
        if not a or not b:
            print("Oshibka: pustoy vvod")
            return
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        res = poisk_podmassiva(a, b)
        if res >= 0:
            print(f"Rezultat: indeks {res}")
            print(f"Naydennyy kusok: {a[res:res+len(b)]}")
        else:
            print("Rezultat: ne naydeno")
    except ValueError:
        print("Oshibka: nuzhno vvodit chisla")
    except Exception as e:
        print(f"Oshibka: {e}")

def poisk_elementa(massiv, element):
    """poisk elementa"""
    for i in range(len(massiv)):
        if massiv[i] == element:
            return i
    return -1

def vse_elementy(massiv, element):
    """vse pozicii elementa"""
    res = []
    for i in range(len(massiv)):
        if massiv[i] == element:
            res.append(i)
    return res

def max_min(massiv):
    """maksimum i minimum"""
    if not massiv:
        return None, None, -1, -1
    max_z = min_z = massiv[0]
    max_p = min_p = 0
    for i in range(1, len(massiv)):
        if massiv[i] > max_z:
            max_z = massiv[i]
            max_p = i
        if massiv[i] < min_z:
            min_z = massiv[i]
            min_p = i
    return max_z, min_z, max_p, min_p

def summa_srednee(massiv):
    """summa i srednee"""
    if not massiv:
        return 0, 0
    s = 0
    for x in massiv:
        s += x
    return s, s / len(massiv)

def chetnye(massiv):
    """chetnye chisla"""
    res = []
    for x in massiv:
        if x % 2 == 0:
            res.append(x)
    return res

def nechetnye(massiv):
    """nechetnye chisla"""
    res = []
    for x in massiv:
        if x % 2 != 0:
            res.append(x)
    return res

def start():
    print("="*40)
    print("POISK V MASSIVE")
    print("="*40)
    test1()
    test2()
    test3()
    vvod()
    x = [1, 1, 1, 2, 1, 1]
    y = [1, 1]
    print("\nDopolnitelno:")
    print(f"Massiv: {x}")
    print(f"Poisk: {y}")
    all_pos = vse_podmassivy(x, y)
    if all_pos:
        print(f"Nayden na poziciyah: {all_pos}")
    else:
        print("Ne nayden")
    
   
    print("\n" + "="*40)
    input("Press Enter to exit...")

if __name__ == "__main__":
    start()

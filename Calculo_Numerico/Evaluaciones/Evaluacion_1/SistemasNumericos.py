n = 520987

def decimal_binario(n,ls = []):
    while n > 0:
        ls.append(n % 2)
        n = n // 2
    return ls[::-1]
a = decimal_binario(n)
cadena = ''.join(str(i) for i in a)

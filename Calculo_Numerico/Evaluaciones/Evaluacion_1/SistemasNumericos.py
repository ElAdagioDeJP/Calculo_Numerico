
class SistemasNumericos:
    def __init__(self,entrada,desde,hacia):
        self.entrada = entrada
        self.desde = desde
        self.hacia = hacia
        print(self.entrada)
"""n = 24
def decimal_binario(n,ls = []):
    while n > 0:
        ls.append(n % 2)
        n = n // 2
    return ls[::-1]
a = decimal_binario(n)
cadena = ''.join(str(i) for i in a)
print(cadena)

def decimal_terceario(n,ls = []):
    while n > 0:
        ls.append(n % 3)
        n = n // 3
    return ls[::-1]
a = decimal_terceario(n)
cadena = ''.join(str(i) for i in a)

def decimal_cuaternario(n,ls = []):
    while n > 0:
        ls.append(n % 4)
        n = n // 4
    return ls[::-1]
a = decimal_cuaternario(n)
cadena = ''.join(str(i) for i in a)

def decimal_octal(n,ls = []):
    while n > 0:
        ls.append(n % 8)
        n = n // 8
    return ls[::-1]
a = decimal_octal(n)
cadena = ''.join(str(i) for i in a)

def decimal_hexadecimal(n,ls = []):
    while n > 0:
        ls.append(n % 16)
        n = n // 16
    return ls[::-1]
a = decimal_hexadecimal(n)
cadena = ''.join(str(i) for i in a)
"""

numero = input('Introduce un número:\n')
sistema = int(input('Introduce un sistema de conversión:\n'))
a =int(numero, sistema)
print(a)
b = hex(a)
print(b)
c = int(b, 16)

bin(a)
oct(a)

class SistemasNumericos:
    def __init__(self, entrada, desde, hacia):
        self.entrada = entrada
        self.desde = desde
        self.hacia = hacia

    def Comprobacion(self):
        if self.desde == 'Hexadecimal':
            for i in self.entrada:
                if i not in '0123456789ABCDEF':
                    return 'Número no válido'
        elif self.desde == 'Decimal':
            for i in self.entrada:
                if i not in '0123456789':
                    return 'Número no válido'
        elif self.desde == 'Octal':
            for i in self.entrada:
                if i not in '01234567':
                    return 'Número no válido'
        elif self.desde == 'Cuaternario':
            for i in self.entrada:
                if i not in '0123':
                    return 'Número no válido'
        elif self.desde == 'Terceario':
            for i in self.entrada:
                if i not in '012':
                    return 'Número no válido'
        elif self.desde == 'Binario':
            for i in self.entrada:
                if i not in '01':
                    return 'Número no válido'
        elif self.desde == self.hacia:
            return 'Sistema no válido'
        else:
            return 'Sistema no válido'

    def set_validacion(self):
        a = self.Comprobacion()
        if a == 'Número no válido' or a == 'Sistema no válido':
            return False
        else:
            return True

    def Resolver(self):
        def decimal_terceario(a,ls = []):
            while a > 0:
                ls.append(a % 3)
                a = a // 3
            return ''.join(map(str, ls[::-1]))
        def decimal_cuaternario(a,ls = []):
            while a > 0:
                ls.append(a % 4)
                a = a // 4
            return ''.join(map(str, ls[::-1]))
        
        if self.desde == 'Hexadecimal':
            a = int(self.entrada, 16)
            if self.hacia == 'Decimal':
                return a
            elif self.hacia == 'Octal':
                return oct(a)[2:]
            elif self.hacia == 'Cuaternario':
                return decimal_cuaternario(a)
            elif self.hacia == 'Terceario':
                return decimal_terceario(a)
            elif self.hacia == 'Binario':
                return bin(a)[2:]
            
        elif self.desde == 'Decimal':
            if self.hacia == 'Hexadecimal':
                return hex(int(self.entrada))[2:]
            elif self.hacia == 'Octal':
                return oct(int(self.entrada))[2:]
            elif self.hacia == 'Cuaternario':
                return decimal_cuaternario(int(self.entrada))
            elif self.hacia == 'Terceario':
                return decimal_terceario(int(self.entrada))
            elif self.hacia == 'Binario':
                return bin(int(self.entrada))[2:]
            
        elif self.desde == 'Octal':
            a = int(self.entrada, 8)
            if self.hacia == 'Hexadecimal':
                return hex(a)[2:]
            elif self.hacia == 'Decimal':
                return a
            elif self.hacia == 'Cuaternario':
                return decimal_cuaternario(a)
            elif self.hacia == 'Terceario':
                return decimal_terceario(a)
            elif self.hacia == 'Binario':
                return bin(a)[2:]
        
        elif self.desde == 'Cuaternario':
            a = int(self.entrada, 4)
            if self.hacia == 'Hexadecimal':
                return hex(a)[2:]
            elif self.hacia == 'Decimal':
                return a
            elif self.hacia == 'Octal':
                return oct(a)[2:]
            elif self.hacia == 'Terceario':
                return decimal_terceario(a)
            elif self.hacia == 'Binario':
                return bin(a)[2:]
        
        elif self.desde == 'Terceario':
            a = int(self.entrada, 3)
            if self.hacia == 'Hexadecimal':
                return hex(a)[2:]
            elif self.hacia == 'Decimal':
                return a
            elif self.hacia == 'Octal':
                return oct(a)[2:]
            elif self.hacia == 'Cuaternario':
                return decimal_cuaternario(a)
            elif self.hacia == 'Binario':
                return bin(a)[2:]
        
        elif self.desde == 'Binario':
            a = int(self.entrada, 2)
            if self.hacia == 'Hexadecimal':
                return hex(a)[2:]
            elif self.hacia == 'Octal':
                return oct(a)[2:]
            elif self.hacia == 'Decimal':
                return a
            elif self.hacia == 'Cuaternario':
                return decimal_cuaternario(a)
            elif self.hacia == 'Terceario':
                return decimal_terceario(a)
                
    

        
    
        
        
        
        
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

# numero = input('Introduce un número:\n')
# sistema = int(input('Introduce un sistema de conversión:\n'))
# a =int(numero, sistema)
# print(a)
# b = hex(a)
# print(b)
# c = int(b, 16)

# bin(a)
# oct(a)

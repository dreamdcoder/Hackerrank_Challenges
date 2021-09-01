import math


class Complex:
    def __init__(self, a, b):
        self.real = a
        self.img = b

    def __add__(self, other):
        result = Complex(0, 0)
        result.real = self.real + other.real
        result.img = self.img + other.img
        return result

    def __sub__(self, other):
        result = Complex(0, 0)
        result.real = self.real - other.real
        result.img = self.img - other.img
        return result

    def __mul__(self, other):
        result = Complex(0,0)
        result.real = self.real*other.real-self.img*other.img
        result.img = self.real*other.img + self.img*other.real
        return result

    def __truediv__(self, other):
        Conjugate = Complex(0, 0)
        Conjugate.real = other.real
        Conjugate.img = -other.img
        result = self*Conjugate
        result_denominator = Conjugate.real**2+Conjugate.img**2
        result.real /= result_denominator
        result.img /= result_denominator
        return result

    def mod (self):
        result = Complex (0, 0)
        result.real = math.sqrt(self.real**2+self.img**2)
        return result

    def __str__(self):
        return F"{self.real:.2f}{self.img:+.2f}i"


if __name__ == "__main__":
    ar, ai = map(float, input().split())
    a = Complex(ar, ai)
    br, bi = map(float, input().split())
    b = Complex(br, bi)
    print(a + b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a.mod())
    print(b.mod())

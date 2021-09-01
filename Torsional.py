import math


class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        result =Points(0,0,0)
        result.x = no.x-self.x
        result.y = no.y-self.y
        result.z = no.z-self.z
        return  result

    def dot(self, no):
     return self.x*no.x+self.y*no.y+self.z*no.z

    def cross(self, other):
        return Points(self.y * other.z - self.z * other.y
                     , self.z * other.x - self.x * other.z
                     , self.x * other.y - self.y * other.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    A = Points(*map(int,input().split()))
    B = Points(*map(int, input().split()))
    C = Points(*map(int, input().split()))
    D = Points(*map(int, input().split()))

    AB = B - A
    BC = C - B
    CD = D - C

    X = AB.cross(BC)
    Y = BC.cross(CD)

    torsional =X.dot(Y)/(X.absolute()*Y.absolute())

    print(f"{math.degrees(math.acos(torsional)):.2f}")

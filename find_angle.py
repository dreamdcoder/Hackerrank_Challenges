import math

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    degree = round(math.degrees(math.atan2(ab,bc)))
    print(str(degree) + chr(176))

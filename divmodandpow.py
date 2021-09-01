if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())

    print(a // b)
    print(a % b)
    print(divmod(a, b))

    print(pow(a,b))
    print(pow(a,b,m))
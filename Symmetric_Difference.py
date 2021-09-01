

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    set_A = set(list(map(int, (input().split()))))
    set_B = set(list(map(int, (input().split()))))
    set_difference = sorted(set_A.symmetric_difference(set_B))
    for i in set_difference:
        print(i)




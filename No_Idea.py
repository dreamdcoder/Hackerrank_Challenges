# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pursuitofHappyness(n, m, arr, setA, setB):
    # calculate happyness
    happyness = 0

    for i in arr:
        if setA.__contains__(i):
            happyness += 1
        elif setB.__contains__(i):
            happyness -= 1
        else:
            pass
    return happyness


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [i for i in list(map(int, input().split()))]
    set_a = set([i for i in list(map(int, input().split()))])
    set_b = set([i for i in list(map(int, input().split()))])
    final_happyness = pursuitofHappyness(n, m, arr, set_a, set_b)
    print(final_happyness)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

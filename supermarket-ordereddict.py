from collections import OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

if __name__ == "__main__":
    n= int(input())

    bill = OrderedDict()
    for _ in range(n):
        item_details = input()
        if item_details.count(" ") == 1:
            item, price = item_details.split()
        elif item_details.count(" ") == 2:
            part_a, part_b, price = item_details.split()
            item = " ".join([part_a, part_b])
        if not bill.__contains__(item):
            bill[item] = int(price)
        else:
            bill[item] += int(price)

    for k, v in bill.items():
        print(k, v)


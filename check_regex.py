import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


if __name__ == "__main__":
    M = int(input())
    for _ in range(M):
        regex = input()
        print(is_valid_regex(regex))

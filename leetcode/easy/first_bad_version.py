version = ['G', 'G', 'G', 'G', 'G', 'G', 'B', 'B', 'B']

def isBadVersion(position):
    if version[position] == 'G':
        return False
    else:
        return True

def check_bad(start, end):
    while start < end:
        if not isBadVersion(end - 1):
            print(end - 1)
        elif not isBadVersion(start + 1):
            print(start + 1)
        check_bad(int(start / 2), int(end / 2))

if __name__ == "__main__":
    print(check_bad(0, len(version)))

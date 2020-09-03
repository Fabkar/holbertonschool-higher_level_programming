#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    for i in range(1, len(sys.argv)):
        x += int(sys.argv[i])
    print(x)

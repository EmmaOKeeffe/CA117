import sys

def diamond(n):
    i = 1
    while i < n:
        print (" " * (n - i) + "* " * i)
        i += 1
    while i > 0:
        print (" " * (n - i) + "* " * i)
        i -= 1
        

def main():
    n = int(sys.argv[1])
    diamond(n)

if __name__ == "__main__":
    main()

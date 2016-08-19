import sys

d = {}

def main():
    f = open(sys.argv[1], "r")
    for line in f:
       details = line.split(" ")
       names = details[1].strip("\n")
       d[details[0]] = names
    
    for l in sys.stdin:
       l = l.strip()
       if l in d:
          print ("Phone: {}".format(d[l]))

       else:
          print("No such contact")


if __name__ == "__main__":
   main()

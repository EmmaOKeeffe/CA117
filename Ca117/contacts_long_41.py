import sys

d = {}

def main():
    f = open(sys.argv[1], "r")
    for line in f:
       details = line.split(" ")
       names = details[0]
       d[details[0]] = names
       details[2] = details[2].strip("\n")
       d[names] = (details[1], details[2])

    for l in sys.stdin:
       l = l.strip()
       if l in d:
          print ("Phone: {}".format(d[l][0]))
          print ("Email: {}".format(d[l][1]))

       else:
          print("No such contact")


if __name__ == "__main__":
   main()

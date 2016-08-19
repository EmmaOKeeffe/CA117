import sys

def plural(s):
   vowels = ["a", "i", "e", "o", "u"]
   if s[-2: ] == "ch" or s[-2: ] == "sh":
      return (s + "es") 
   elif s[-1] == "x" or s[-1] == "s" or s[-1] == "z":
      return (s + "es")
   elif s[-1] == "y" and s[-2] not in vowels:
      return (s[:-1] + "ies") 
   elif s[-1] == "f":
      return (s[:-1] + "ves")
   elif s[-2:] == "fe":
      return (s[:-2] + "ves")
   elif s[-1] == "o":
      return (s + "es")
   else:
      return (s + "s")

def main():
   print (plural(sys.argv[1]))
   
if __name__ == "__main__":
   main()

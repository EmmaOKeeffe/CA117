import sys


def swap_keys_values(d):
   new_dict = dict((v,k) for k,v in d.items())
   return (new_dict)

def main():
   d = {"a" : 1, "b" : 2, "c" : 3}
   print (swap_keys_values(d))


if __name__ == "__main__":
   main()

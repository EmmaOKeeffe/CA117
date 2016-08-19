import sys

def main():
   numbers = list(range(1, 31))
   three_mults = [n for n in numbers if not n % 3]
   print ("Multiples of 3: {}".format(three_mults))
   three_squares = [n**2 for n in three_mults]
   print ("Multiples of 3 squared: {}".format(three_squares))
   four_mults = [n for n in numbers if not n % 4]
   four_roots = [n*2 for n in four_mults if not n % 4]
   print ("Multiples of 4 doubled: {}".format(four_roots))
   either_mults = [n for n in numbers if not n % 4 or not n % 3]
   print ("Multiples of 3 or 4: {}".format(either_mults))
   both_mults = [n for n in numbers if not n % 4 and not n % 3]
   print ("Multiples of 3 and 4: {}".format(both_mults))
   three_replaced = [n if n % 3 else "X" for n in numbers]
   print ("Multiples of 3 replaced: {}".format(three_replaced))
   

if __name__ == "__main__":
   main()

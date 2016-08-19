import sys

count = [0] * 10

def poker(n):
   count[n] += 1

def main():
   f = sys.stdin.readlines()

   for line in f:
      poker(int(line[-2]))

   print (count)
   print("The probability of nothing is {:.4f}%".format(count[0]/1000000))
   print("The probability of one pair is {:.4f}%".format(count[1]/1000000))
   print("The probability of two pairs is {:.4f}%".format(count[2]/1000000))
   print("The probability of three of a kind is {:.4f}%".format(count[3]/1000000))
   print("The probability of straight is {:.4f}%".format(count[4]/1000000))
   print("The probability of flush is {:.4f}%".format(count[5]/1000000))
   print("The probability of full house is {:.4f}%".format(count[6]/1000000))
   print("The probability of four of a kind is {:.4f}%".format(count[7]/1000000))
   print("The probability of straight flush is {:.4f}%".format(count[8]/1000000))
   print("The probability of royal flush is {:.4f}%".format(count[9]/1000000))

if __name__ == "__main__":
   main()



#9	Royal flush	{Ace, king, queen, jack, ten} + flush
#8	Straight flush	Straight + flush
#7	Four of a kind	Four equal ranks within five cards
#6	Full house	Pair + different rank three of a kind
#5	Flush	Five cards of same suit
#4	Straight	Five cards sequentially ranked (no gaps)
#3	Three of a kind	Three equal ranks within five cards
#2	Two pairs	Two pairs of equal ranks within five cards
#1	One pair	One pair of equal ranks within five cards
#0	Nothing	 

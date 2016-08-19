import sys


def most_es(wordlist):
   biggest = 0
   for w in wordlist:
      if w.count("e") > biggest:
         biggest = w.count("e")

   most = [w for w in wordlist if w.count("e") == biggest]

   print ("Words with most e's: {}".format(most))



def main():
   wordlist = [w.strip() for w in sys.stdin]
   seventeens = [w for w in wordlist if len(w) == 17]
   print ("Words containing 17 letters: {}".format(seventeens))
   over_eighteen = [w for w in wordlist if len(w) >= 18]
   print ("Words containing 18+ letters: {}".format(over_eighteen))
   shortest_vowel = [w for w in wordlist if all(c in w for c in ["a", "e", "i", "o", "u"])]
   print ("Shortest word containing all vowels: {}".format(min (shortest_vowel, key = len)))
   fouras = [w for w in wordlist if w.lower().count("a") == 4]
   print ("Words with 4 a's: {}".format(fouras))
   many_qs = [w for w in wordlist if w.count("q") >= 2]
   print ("Words with 2+ q's: {}".format(many_qs))
   has_cie = [w for w in wordlist if "cie" in w]
   print ("Words containing cie: {}".format(has_cie))
   anagram = [w for w in wordlist if all(c.lower() in w.lower() for c in ["a", "n", "g", "l", "e"]) and len(w) == 5 and w != "angle"]
   print ("Anagrams of angle: {}".format(anagram))
   count_iary = [w for w in wordlist if "iary" in w]
   print ("Words ending in iary: {}".format(len(count_iary)))
   has_q_not_u = [w for w in wordlist if "q"in w.lower() and "u" not in w]
   print ("Words with q but no u: {}".format(has_q_not_u))
   most_es(wordlist)

if __name__ == "__main__":
   main()

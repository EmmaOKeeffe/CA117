import sys
import calendar

def date(l):
   details = l.split(" ")
   day = details[0]
   month = details[1]
   year = details[2]

   months = list(calendar.month_abbr)

   if month[:3] in months:
      monthnum = str(months.index(month[:3]))

   dob = day + "/" + monthnum + "/" + year[2:]

   print(dob.strip("\n"))


def main():
   for line in sys.stdin:
      date(line)

if __name__ == "__main__":
   main()

import random



def quote():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=27
  rnd=random.randint(0,last)

  print(quotes[rnd])

if __name__== "__main__":
  quote()

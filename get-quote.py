import random



def quote():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last=27
  rnd=random.randint(0,last)
  rnd2=random.randint(0,last)
  rnd3=random.randint(0,last)
  rnd4=random.randint(0,last)

  print(quotes[rnd], end = ' ')
  print(quotes[rnd2], end = ' ')
  print(quotes[rnd3], end = ' ')
  print(quotes[rnd4], end = ' ')

if __name__== "__main__":
  quote()

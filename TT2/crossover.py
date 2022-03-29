import random


def guessNumber(usern):
  n = random.randint(1, 10)
  while n != "usern":
      if usern > n:
          print ("Guess Lower!")
          usern = int(input("Enter an number from 1 to 10: "))
      elif usern < n:
          print ("Guess Higher!")
          usern = int(input("Enter an number from 1 to 10: "))
      elif usern == n:
          print ("Nice! That's the score you got out of 10 this week!")
          quit()
      

  
def tester():
  usern = int(input("Enter an number from 1 to 10: "))
  guessNumber(usern)

tester()
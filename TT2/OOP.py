class OddorEven:
  def __init__(self):
    print("The number is", end=" ")
  def __call__(self, n):
    if(n % 2 == 0):
      print(n)
      print("which is even!")
    else:
      print(n)
      print("which is odd!")

def OddorEvenfinder():
  print("Odd or Even")
  n = int(input("Enter any Number to determine if it is even or odd: "))
  oddoreven = OddorEven()
  oddoreven(n)

# OddorEvenfinder()
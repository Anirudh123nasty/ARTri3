

def swap(age1, age2):
  if age1 > age2:
      temp1 = age1
      temp2 = age2
      age1 = temp2
      age2 = temp1
      return age1, age2
  if age1 < age2:
      return age1, age2

def testSwap():
  firstAge = int(input("Enter a number for age 1:"))
  secondAge = int(input("Enter a number for age 2:"))
  x, y = swap(firstAge, secondAge)
  print(x, y)
      





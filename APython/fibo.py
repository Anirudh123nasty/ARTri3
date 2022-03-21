#creates set conditions that values with eventually become
#values get subtracted until they are 0, 1, or 2
def fibo(n):
    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibo(n-1) + fibo(n-2)

#print end statement, checks for entering letters or negative numbers with try accept and if else
def fibotester():
  try:
    n = int(input("Enter the term number: "))
    if n < 0:
      print("Please enter positive number!")
    else: 
      for i in range(n):
                print(fibo(i), end=', ')
      print ("are the fibonacci terms!")
  except: 
    print("Please enter number!")

# fibotester()
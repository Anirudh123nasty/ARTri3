
def fibo(n):
    if n < 0:
        print("Please enter valid input!")
 
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibo(n-1) + fibo(n-2)




def fibotester():
  n = int(input("Enter the term number: "))
  for i in range(n):
          print(fibo(i))

# fibotester()
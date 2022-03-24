class Fibonacci:
    def __init__(self):
        self.fiboSeq = [1]
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = n * self(n - 1) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]
def facttester():
  fibo_of = Fibonacci() # object instantiation and run __init__ method
  l = int(input('What number: '))
  print(fibo_of(l)) # object running __call__ method
  


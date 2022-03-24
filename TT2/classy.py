class Factorial:
    def __init__(self):
        self.factSeq = [1]
    def __call__(self, n):
        if n < len(self.factSeq):
            return self.factSeq[n]
        else:
            # Compute the requested Fibonacci number
            fact_number = n * self(n - 1) # two recursive calls to self (__call__(self, n))
            self.factSeq.append(fact_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factSeq[n]
def facttester():
  fact_of = Factorial() # object instantiation and run __init__ method
  l = int(input('What number: '))
  print(fact_of(l)) # object running __call__ method
  


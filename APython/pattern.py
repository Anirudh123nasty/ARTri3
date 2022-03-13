def christmaspattern(n):
    for i in range(n):
        for c in range(n-i):
            print(' ', end=' ')
        for c in range(2*i+1):
            print('*',end=' ')
        print()

def testPattern():
  row = int(input('How many rows: '))
  christmaspattern(row)

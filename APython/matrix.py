def write(matrix):
    length = len(matrix)
    for i in range(length):
        row = len(matrix[i])
        for order in range(row):
            print(matrix[i][order], end='')
        print()

def swap_tester():
    age1 = 1
    age2 = 9
    swap(age1, age2)

if __name__ == "__main__":
    swap_tester()



matrix = [[1,2,3],[4,5,6],[7,8,9]]

write(matrix)

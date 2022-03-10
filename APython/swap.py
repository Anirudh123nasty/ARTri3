def swap(age1, age2):
    if age1 > age2:
        temp1 = age1
        temp2 = age2
        age1 = temp2
        age2 = temp1
        return age1, age2

x,y= swap(21, 16)

print(x,y)



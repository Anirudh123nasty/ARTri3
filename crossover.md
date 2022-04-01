{% include navigation.html %}

**Cross over codes**

1. Code for rock paper scissors

```
import random
def game():
    # Print multiline instruction
    # performstring concatenation of string
    print()
    print("Rules of Rock Paper Scissors: \n"
          +"1. Paper > Rock \n"
          +"2. Rock > Scissors \n"
          +"3. Scissors > Paper \n")

    while True:
        print("Enter your choice: \n 1. Rock \n 2. paper \n 3. scissor \n")


        #user input
        choice = int(input("Make your choice: "))


        # does not allow the user to continue if the input is invalid
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))

        #print("your choice is: ", choice)

        # initialize value of choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'

        # print user choice
        print("user choice is: " + choice_name)

        # Computer chooses randomly any number among 1 , 2 and 3. Using randint method of random module
        comp_choice = random.randint(1, 3)

        #in case the user had the same choice as the computer
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'

        print("Computer choice is: ", comp_choice_name)

        print(choice_name, " v.s. ", comp_choice_name)

        # condition for winning
        if((choice == 1 and comp_choice == 2) or
                (choice == 2 and comp_choice ==1 )):
            print("paper wins => ", end = "")
            result = "paper"

        elif((choice == 1 and comp_choice == 3) or
             (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end = "")
            result = "Rock"
        else:
            print("scissor wins =>", end = "")
            result = "scissor"

        # Printing either user or computer wins
        if result == choice_name:
            print(" User wins!!")
        else:
            print(" Computer wins!!")

        print("Do you want to play again? (Y/N)")
        ans = input()


        # if user input n or N then condition is True

        if ans == "n" or ans == "N":
            break
        #if user input is not n, N, y, or Y
        elif ans != "n" or "N" or "Y" or "y":
            print("invalid input. Please Try Again")
            print("Do you want to play again? (Y/N)")
            ans = input()

    # after coming out of the while loop
    # we print thanks for playing
    print("\nThanks for playing")
```

2. Code to convert decimal to binary

```
def binary():
    decimal = int(input("Please enter a number: "))
    print("Your choice is: ", decimal)
    def convert(num):
        if num >= 1:
            convert(num // 2)
        print(num % 2, end = "")
    convert(decimal)
    print()

```

3. Code to find average

```

def findAverage():
    list = []
    n = int(input("How many numbers are you entering? "))
    count = 0
    while count < n:
        number = int(input("Enter a number: "))
        list.append(number)
        count = count + 1
    print("the list of numbers you inputted is: ", list)

    def average(i):
        avg = sum(i) / len(i)
        return avg
    average = average(list)
    print("the average of the numbers ", list, " is ", average)
```

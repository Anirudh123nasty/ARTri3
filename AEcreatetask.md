{% include navigation.html %}



<!-- # Create Task Project
## Me and Ethan are planning on working together to make a math function page for the create a task project. -->

## Runtime
[Video Showing Runtime](https://loom.com/share/b12746083af449339ffe4ef3e44d0ce1)

# General Requirements # 
[Link to Requirements](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)

<!-- # Submission Requirements
## PROGRAM CODE (CREATED INDEPENDENTLY OR COLLABORATIVELY)
Submit one PDF file that contains all of your program code (including
comments). Include comments or acknowledgments for any part of the
submitted program code that has been written by someone other than you
and/or your collaborative partner(s).

### In your program, you must include student-developed program code that
### contains the following:
* Instructions for input from one of the following:
  *  the user (including user actions that trigger events)
  a device
  * an online data stream
  * a file
* Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
* At least one procedure that contributes to the program’s intended purpose, where you have defined:
  *  the procedure’s name
  *  the return type (if necessary)
  *  one or more parameters
* An algorithm that includes sequencing, selection, and iteration that is in the
body of the selected procedure
* Calls to your student-developed procedure
* Instructions for output (tactile, audible, visual, or textual) based on input and
program functionality

## VIDEO (CREATED INDEPENDENTLY)
Submit one video file that demonstrates the running of your program as
described below. Collaboration is not allowed during the development of
your video.

* Your video must demonstrate your program running, including:
  * Input to your program
  * At least one aspect of the functionality of your program
  * Output produced by your program

* Your video may NOT contain:
  * Any distinguishing information about yourself
  * Voice narration (though text captions are encouraged)

* Your video must be:
  * Either .mp4, .wmv, .avi, or .mov format
  * No more than 1 minute in length
  * No more than 30MB in file size

## How we meet requirements
* sequencing is seen through the if/then statements, where if conditions aren't met the code is skipped. 
```js
function tri () {
    const one = document.getElementById("one").value;
    const two = document.getElementById("two").value;
    if (one > 0 && two >0) {
        let area = (parseInt(one) * parseInt(two)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
}
```

* selection is met through the while statements, which only carry out functions if conditions are met.
```js
function factorial () {
    var e = document.getElementById("e").value;
    let count = 1;
    let ans = 1;
    while (count <= e-1) {
        count += 1;
        ans= count * ans
    }
    console.log(ans);
    document.getElementById("ans").innerHTML = "Answer is " + ans;
}
```

* iteration is met through for loop, that repeats code in a function
```js
def aecreatetask_index():
    try:
        if request.form:
            a = int(request.form.get("f")) #user input
            x = 0
            y = 1
            z = 0
            for i in range(a):
                z = x + y
                x = y
                y = z
                i += 1
        return render_template("aecreatetaskIndex.html", z=z)
    except:
        return render_template("aecreatetaskIndex.html", z="")
```
* the user input is a number of odd math functions they might not have on their calculator.
* the return type is specified as a numeric value with parseInt() to perform addition function.
* various functions created like tri, fibo, and factorial- and they are called with button presses
* parameters of the user input are provided to math functions.

* Calls to student procedure
```html
    <input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
```
* The button calls the JavaScript function factorial(), which is our procedure for finding the factorial of a number

* At least one procedure that contributes to the program’s intended purpose:
```js
function tri () {
    const base = document.getElementById("base").value;
    const height = document.getElementById("height").value;
    if (one > 0 && two >0) {
        let area = (parseInt(one) * parseInt(two)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
}
```
  *  the procedure’s name is tri, short for triangle, which finds the area of a triangle given a base and height
  *  parseInt converts the string input into an integer output, so by having it we are specifying the program to return an integer
  *  two parameters, "one" and "two" are taken from the user input from the frontend. They represent the base and height of the triangle the user wants the area of

* Instructions for input from the user
```html
        <input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
        <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 id="response"></h1>
```
* The placeholder inside of the text box notifies the user of the parameters for the function
* The button also gives directions to the user as to what button prompts what function.

* Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
```py
fs = [1,]
            if b == 1:
                z = 1
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", z=z)
            else:
                for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", fs=fs)
```
* The list stores all the numbers of the Fibonacci sequence
* When the user inputs how many times the loop runs, the list will store each new value created in the sequence

## Code Comments
![image](https://user-images.githubusercontent.com/89223726/162528720-7dabb0f6-54d0-4ee9-9443-e16415c1d319.png)
[Commit with code comments](https://github.com/NastyAwakened/NastyAwakened/commit/bc64c68f0ed0725f3601349c8d502f5b0df34c9f)

## Design Ideas and Usage
* our main idea was to create a unique math page that the user couldn't find on a standard calculator
* in general, our design idea is to have multiple lines and buttons on the page, with the results being displayed right to the submit button
* these math functions meet many of CB's create a task requirements for iteration, selection, sequencing, calling functions, and the use of lists
 -->
# End of what Ethan and I wrote together for CSP. Here is Anirudh's INDIVIDUAL responses for create task questions.

## Describes the overall purpose of the program:

The purpose of our program was to provide odd math functions one a single page that users might not be able to access with a scientific calculator.

## Describes what functionality of the program is demonstrated in the video:

The programs iteration, selection, and sequencing was met through the three major functions was finding all the fibonacci terms, the area of a triangle, and generating the factorial of any given number. Additionally, functions are being called, parameters are provided for functions by getelementbyID, and lists are used. The functions that I wrote are 'factorial()' and 'tri()', and the function my partner Ethan Vo wrote are 'factdriver()' and 'aecreatetask_index()'.

## Describes the input and output of the program demonstrated in the video

The input of the program are numbers, and the output is the area of a triangle with given dimensions, a factorial value, or a list of fibonacci terms. The inputs of all functions are limited to numbers only, meaning users can't enter letters of symbols. Additionally, the output of the program is shown on the page through a ID for javascript and try/accept method for python.

##  The first program code segment must show how data have been stored in the list:
``` python
 try:
        if request.form:
            a = request.form.get("f") #user input
            print("The number is " + a)
            x = 0
            y = 1
            z = 0
            b = int(a)
            fs = [1,]
```
The list comes from Ethan Vo's function, who I worked with on my create task project when writing code. Here, the list is created, and is specified to start from 1 with no defined end value yet. This allows us to add on to the list by appending values.
## The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose:
``` python
 if b == 1:
                z = 1
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", z=z)
            else:
                for i in range(b-1):
                    z = x + y
                    x = y
                    y = z
                    i += 1
                    fs.append(z)
                return render_template("aecreatetaskIndex.html", a="The Fibonaci sequence up to term " + a + " is: ", fs=fs)
        return render_template("aecreatetaskIndex.html", a="")
    except:
        return render_template("aecreatetaskIndex.html", a="Something went wrong try again")
```
Again, this comes from Ethan Vo's function. b is set to the number that equals the user's input value. The for loop then carries out the code for the fibonacci sequence (which adds variables x and y and sets that value to z, then sets x to y and y to z, and finally incremantally increases the value of i by 1. z (which represents the term value for each interation of 'i') is then appended to the list 'fs'.
## Identifies the name of the list being used in this response:
The name of the list is fs, which stands for fibonacci sequence.
## Describes what the data contained in the list represent in your program:
The data in the list represents all the terms of the fibonacci sequence from 1 to the user entered term number. This value is specifically set to z, while other variables x and y change with every iteration of i and are added to get variable z.
## Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list:
The program could be written to javascript similar to the factorial function, where terms and generated based on whether conditions are met (which as using a while loop to continally add numbers together until the user's numerical input value is reached. However, this wouldn't give all the values of the fibonacci sequence. To show all the terms, a list (where terms can be stored) has to be used.
## The first program code segment must be a student-developed procedure that
### *  Defines the procedure’s name and return type (if necessary)
### *  Contains and uses one or more parameters that have an effect on the functionality of the procedure
### *  Implements an algorithm that includes sequencing, selection, and iteration
``` javascript
{#Takes parameter e, which is user input. Count is incremented up by one until it reachs the input number value.#}
function factorial (e) {
    let count = 1;
    let ans = 1;
    if (e > 0 || /[0-99999999]/.test(e)) {
        while (count <= e-1) {
            count += 1;
            ans = count * ans
        }
        console.log(ans);
        document.getElementById("ans").innerHTML = "Answer is " + ans;
    } else {
        document.getElementById("responsef").innerHTML = "Please enter positive, numerical inputs only!"
    }
}
{#allows factorial function to make parameter#}
function factdriver () {
    e = document.getElementById("e").value;
    factorial(e)
}
{#Sets base and height to user input, then accounts for invalid inputs with if else statement.#}
function tri () {
    const base = document.getElementById("base").value;
    const height = document.getElementById("height").value;
    if (base > 0 && height >0) {
        let area = (parseInt(base) * parseInt(height)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
}
```
I wrote both functions 'tri' and 'factorial'. My partner Ethan Vo wrote the function 'factdriver()' to add a parameter to our createtask project. Sequencing is met since each line of code is run line by line until the end. Selection is met through the 'if else' method in javascript, which as used in both functions. This runs the first segment of the function to generate the factorial value or triangle area. If there is a error (which likely would be caused by a failure of meeting the conditions in the 'if' statement), when the second segment of code would run. This sets the element that is displayed under the input box to a failure message that alerts the user that their inputs aren't valid. Iteration is met through the use of a while loop in the 'factorial' function, which repeats the lines of code used to generate the factorial value until the conditions are no longer met. The procedures names are defined when the functions are created with the format 'function tri () {}' and 'function factorial (e) {}'. The return type is specified using document.getElementById, where the displayed element is set equal to an element that stores answer following the phrase "Answer is ". Here is an example: document.getElementById("ans").innerHTML = "Answer is " + ans;. Finally, parameters are passed into the function 'factorial()' with the use of another function 'factdriver()' that sets the user input value to the element 'e', and then calls the function factorial with 'e' passed inside as a parameter. 
## The second program code segment must show where your student-developed procedure is being called in your program:
```html
    <div class="center">
    <h1 style="text-align:center; font-size: 90px; color:white">Odd Math Functions!</h1>
        <input id="e" placeholder="Number">
        <button onclick="factdriver()">Factorial!</button>
        <h1 style="color:white" id="ans"></h1>
        <h1 style="color:white" id="responsef"></h1>
        <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 style="color:white" id="response"></h1>
        <form action="{{ url_for('aecreatetask_index') }}" id="enter" method="POST" >
            <input type="number" name="f" placeholder="Number of Terms" id="f">
            <button type="submit" value="Fibonacci!">Fibonacci!</button>
            <h1 style="color:white" >{{ a }}  {{ fs }}</h1>
        </form>
    </div>
```
The javascript function 'factdriver' is called using html, with the button on click method since the user clicks a button to determine the factorial value. This is the same case with the javascript function 'tri' since the user also clicks a button to determine the area of an triangle.

## Describes in general what the identified procedure does and how it contributes to the overall functionality of the program:


The identified procedures 'tri' and 'factorial' generates and displays the area of the triangle with the user specified height and base and generates the factorial value of the user inputted number. Overall, this function gives users access to odd math functions that they may not have on their calculators/or may take them too much time to compute.

## Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it:
First, for the function 'factorial', the element 'e' which stores the user inputted value is passed into the function as a parameter through the use of the function 'factdriver'. The variables 'count' and 'ans' are both set to 1. Then, the user input is tested if it meets the requirements. This is done with the use of an 'if else' statement. If the value of e is either positive or within the values of 0 to 99999999, then the algorithm to generate the value for the factorial is started. The value is generating using a while loop, which carried out a specific procedure as long as the conditions are met. These different conditions require the 'count' to be less than or equal to the user inputted value minus one. While this condition is met, count is incrementally increased by one and the element 'ans' is set equal to the updated value of the element 'count' times the current value of element 'ans'. The element 'ans' is set to the value of constant 'ans' to dispolay the final value. Error is accounted for with the 'else' statement that sets element 'resopnsef' to an error message. This only runs if the conditions in the if statement aren't met.

For the function 'tri', first constants base and height are set equal to elements 'base' and 'height'. Then another 'if else' statement is used to test conditions that determine whether the user inputs are valid. If both the base and the height are larger than 0, then a new variable 'area' is set equal to the base times the height divided by two. parseInt is used here to mathematical calculations by returning a numeric value from the strings stored in 'base' and 'height'. Finally, document.getElementById is used to display the answer by setting element 'response' to constant 'area. There is also an else statement here that sets 'response' to an error message, and this displays if the conditions in the 'if statement' aren't met.

## Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of ## code in the algorithm to execute.
### First call:
```html
        <input id="e" placeholder="Number">
        <button onclick="factdriver()">Factorial!</button>
        <h1 style="color:white" id="ans"></h1>
        <h1 style="color:white" id="responsef"></h1>
```
Here the javascript function 'factorial()' which I wrote that is being called with the click of a button. This function generates the factorial for any number the user inputs. 'ans' is an element that is the factorial value of the number the user inputted, and 'responsef' is another element that is used to account for error like invalid inputs.
### Second call:
```html
        <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 style="color:white" id="response"></h1>
```
Here is a similar call in html for another function 'tri()' with the button onclick method, which I also wrote. This function generates the area of a triangle when the user inputs numerical values for the length and base.
## Describes what condition(s) is being tested by each call to the procedure: 
### Condition(s) tested by the first call:
```javascript
function factorial (e) {
    let count = 1;
    let ans = 1;
    if (e > 0 || /[0-99999999]/.test(e)) {
```
The function 'factorial' (which I wrote) only starts its algorithm to generate the factorial of the number the user inputted 'if' the condition is met that 'e' (or the user input) is greater than zero or was in the range 0-99999999.
### Condition(s) tested by the second call:
```javascript
function tri () {
    const base = document.getElementById("base").value;
    const height = document.getElementById("height").value;
    if (base > 0 && height >0) {
```
The function 'tri' (which I wrote) only starts the algorithm to generate the area of an triangle with user inputs for height and base if the value for height is positive and the value for base is positive.
## Identifies the result of each call
### Result of the first call:
```javascript
         while (count <= e-1) {
            count += 1;
            ans = count * ans
        }
        console.log(ans);
        document.getElementById("ans").innerHTML = "Answer is " + ans;
    } else {
        document.getElementById("responsef").innerHTML = "Please enter positive, numerical inputs only!"
    }
}
```
This is the actual algorithm the function 'factorial' (which I wrote) uses the generate the factorial of the user inputted number runs while the value for 'count' is less than or equal to the user inputted number minus one. The 'count' is set equal to its value incrementally increased by one. The 'ans' (answer or value for the factorial) is then set equal to the 'ans' times the 'count' Essentially, this performs the work neccesary for finding the factorial, but in a reverse manner, since it starts from 1 and multiplies incrementally increasing numbers until the final value for the factorial is reached. The final factorial value is displayed through the use of document.getElementById- which displays 'ans'. There is also an else statement that also uses document.getElementById to set new variable 'responsef' to account for invalid user inputs like negative values.
### Result of the second call:
```javascript
 if (base > 0 && height >0) {
        let area = (parseInt(base) * parseInt(height)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
```
This is the actual algorithm the function 'tri'(which I wrote) uses to generate the area of the triangle with the values of height and base the user inputted. If both the user inputted base and height are positive, then a new variable called 'area' is set equal to the value of the base and height multiplied together and divided by 2. Additionally, 'parseInt' is used to return integer values from the positive user inputs (which previously were stored as strings). Finally, the element 'response' is set equal to the area using document.getElementById. In this whole procedure, an if else statement was used to take care of errors. If the base wasn't greater than zero or the height wasn't greated than zero, then the element 'response' is set equal to a phrase that reminds the user to only enter appropriate values (positive numerial numbers).


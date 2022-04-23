{% include navigation.html %}



# Create Task Project
## Me and Ethan are planning on working together to make a math function page for the create a task project.

## Runtime
[Video Showing Runtime](https://www.loom.com/share/42a83665a0b64a1192f4d168568f98a6?sharedAppSource=personal_library)

# General Requirements # 

[Link to Requirements](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)

# Submission Requirements
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

# End of Ethan and I wrote together for CSP. Here is Anirudh's INDIVIDUAL responses for create task questions.

## Describes the overall purpose of the program:

The purpose of our program was to provide odd math functions one a single page that users might not be able to access with a scientific calculator.

## Describes what functionality of the program is demonstrated in the video:

The programs iteration, selection, and sequencing was met through the three major functions was finding all the fibonacci terms, the area of a triangle, and generating the factorial of any given number. Additionally, functions are being called, parameters are provided for functions by getelementbyID, and lists are used.

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
``` python
def aecreatetask_index():
    try:
        if request.form:
            a = request.form.get("f") #user input, parameter that is passed into the function
            print("The number is " + a)
            x = 0
            y = 1
            z = 0
            b = int(a)
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
        return render_template("aecreatetaskIndex.html", a="")
    except:
        return render_template("aecreatetaskIndex.html", a="Something went wrong try again")
```
This function was written by Ethan Vo. Sequencing is met since each line of code is run line by line until the end. Selection is met through the 'try except' method in python, which runs the first segment of the function to generate fibonacci terms. If there is a error (which likely would be caused by the progam not able to get the user input 'f', set it to 'a', and then set 'b' to the integer value of 'a'), when the second segment of code would run. This displays the same page, and sets 'a' to an error message that displays below the user input area.
## The second program code segment must show where your student-developed procedure is being called in your program:
```html

    <body style="background-color: rebeccapurple">
    <div class="center">
    <h1 style="text-align:center; font-size: 90px">Odd Math Functions!</h1>
        <input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
        <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 id="response"></h1>
        <form action="{{ url_for('aecreatetask_index') }}" id="enter" method="POST" >
            <input type="number" name="f" placeholder="Number of Terms" id="f">
            <button type="submit" value="Fibonacci!">Fibonacci!</button>
            <p>{{ a }}  {{ fs }} </p>
        </form>
    </div>

</body>
```
The python function 'aecreatetask_index()' is called using html, with the form action method. The url with the name of the function, the id for the user's input, and POST method is used to call the function (which was written in python) in a javascript file. In the next line of code, html with 'button' is used to run function 'aecreatetask_index()' when pressed. Finally, the format of output is specified with the user entered value specified as 'a' and the list specified as 'fs'.
## Describes in general what the identified procedure does and how it contributes to the overall functionality of the program:
The identified procedures both generates and displays all the fibonacci terms until the user inputted term number. Overall, this function gives users access to an odd math sequence that they may not have on their calculators.
## Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else ## to recreate it:
First, the value is obtained from the user input with request.form.get, since 'f' is just the ID of the input. Then, three variables are used: x, y and z. Variables a (which is set to the user input) and b (the integer of a) are additionally used to take care of the first term, which follows no pattern. Then, a list is created that's named 'fs'. A for loop is used that repeats until i is one less than b, where i iterates and increases by 1 every time the loop is carried out. The loop adds variables x and y to z, sets x and y equal, and then sets z equal to y. z is then appended to the list fs.

## Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of ## code in the algorithm to execute.
### First call:
```html
<input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
```
Here the javascript function 'factorial()' which I wrote that is being called with the click of a button. This function generates the factorial for any number the user inputs.
### Second call:
```html
 <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 id="response"></h1>
```
Here is a similar call in html for another function 'tri()' with the button onclick method, which I also wrote. This function generates the area of a triangle when the user inputs numerical values for the length and base.
## Describes what condition(s) is being tested by each call to the procedure: 
### Condition(s) tested by the first call:
```javascript
function factorial () {
    var e = document.getElementById("e").value;
    let count = 1;
    let ans = 1;
    while (count <= e-1) {
```
The function 'factorial' (which I wrote) only starts its algorithm to generate the factorial of the number the user inputted 'while' the condition is met that the 'count' is less than or equal to the user inputted number minus one.
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
        ans= count * ans
    }
    console.log(ans);
    document.getElementById("ans").innerHTML = "Answer is " + ans;
```
This is the actual algorithm the function 'factorial' (which I wrote) uses the generate the factorial of the user inputted number runs while the value for 'count' is less than or equal to the user inputted number minus one. The 'count' is set equal to its value incrementally increased by one. The 'ans' (answer or value for the factorial) is then set equal to the 'ans' times the 'count' Essentially, this performs the work neccesary for finding the factorial, but in a reverse manner, since it starts from 1 and multiplies incrementally increasing numbers until the final value for the factorial is reached. The final factorial value is displayed as a result of the first function being called.
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
<!--  IN ETHAN'S RESPONSE DON'T USE-->
<!-- The final triangle value is displayed as a result of the second function being called.
### Function with passed in parameter
```javascript
function factorial (e) {
    let count = 1;
    let ans = 1;
    while (count <= e-1) {
        count += 1;
        ans = count * ans
    }
    console.log(ans);
    document.getElementById("ans").innerHTML = "Answer is " + ans;
}

function factdriver () {
    e = document.getElementById("e").value;
    factorial(e)
}
``` -->


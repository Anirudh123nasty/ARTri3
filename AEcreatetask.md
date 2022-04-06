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
## Identifies the name of the list being used in this response:
The name of the list is fs.
## Describes what the data contained in the list represent in your program:
The data in the list represents all the terms of the fibonacci sequence from 1 to the user entered term number.
## Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list:
The program could be written to javascript similar to the factorial function, where terms and generated based on whether conditions are met. However, this wouldn't give all the values of the fibonacci sequence. To show all the terms, a list (where terms can be stored) has to be used.
## The first program code segment must be a student-developed procedure that
### *  Defines the procedure’s name and return type (if necessary)
### *  Contains and uses one or more parameters that have an effect on the functionality of the procedure
### *  Implements an algorithm that includes sequencing, selection, and iteration
``` python
def aecreatetask_index():
    try:
        if request.form:
            a = request.form.get("f") #user input
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
## The second program code segment must show where your student-developed procedure is being called in your program:
```html
{% endblock %}
{% block body %}
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



{% endblock %}
</body>
```
## Describes in general what the identified procedure does and how it contributes to the overall functionality of the program:
The identified procedures both generates and displays all the fibonacci terms until the user inputted term number. Overall, this function gives users access to an odd math sequence that they may not have on their calculators.
## Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else ## to recreate it:
First, the value is obtained from the user input with request.form.get, since 'f' is just the ID of the input. Then, three variables are used: x, y and z. Variables a (which is set to the user input) and b (the integer of a) are additionally used to take care of the first term, which follows no pattern. Then, a list is created that's named fs. A for loop is used that repeats until i is one less than b, where i iterates and increases by 1 every time the loop is carried out. The loop adds variables x and y to z, sets x and y equal, and then sets z equal to y. Z is then appended to the list fs.

## Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of ## code in the algorithm to execute.
### First call:
```html
<input id="e" placeholder="Number" type="number">
        <button onclick="factorial()">Factorial!</button>
        <h1 id="ans"></h1>
```
### Second call:
```html
 <input id="base" placeholder="Length of Base" type="number">
        <input id="height" placeholder="Length of Height" type="number">
        <button onclick="tri()">Find the area of an triangle!</button>
        <h1 id="response"></h1>
```
## Describes what condition(s) is being tested by each call to the procedure: 
### Condition(s) tested by the first call:
```javascript
function factorial () {
    var e = document.getElementById("e").value;
    let count = 1;
    let ans = 1;
    while (count <= e-1) {
```
### Condition(s) tested by the second call:
```javascript
function tri () {
    const base = document.getElementById("base").value;
    const height = document.getElementById("height").value;
    if (base > 0 && height >0) {
```
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
The final factorial value is displayed as a result of the first function being called.
### Result of the second call:
```javascript
 if (base > 0 && height >0) {
        let area = (parseInt(base) * parseInt(height)) / 2;
        document.getElementById("response").innerHTML = "Answer is " + area;
    } else {
        document.getElementById("response").innerHTML = "Please enter valid inputs!"
    }
```
The final triangle value is displayed as a result of the second function being called.
## Design Ideas and Usage
* our main idea was to create a unique math page that the user couldn't find on a standard calculator
* in general, our design idea is to have multiple lines and buttons on the page, with the results being displayed right to the submit button
* these math functions meet many of CB's create a task requirements for iteration, selection, sequencing, calling functions, and the use of lists

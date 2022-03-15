{% include navigation.html %}



# Create Task Project
## Me and Ethan are planning on working together to make a math function page for the create a task project.

## Runtime
[Video Showing Runtime](https://www.loom.com/share/42a83665a0b64a1192f4d168568f98a6?sharedAppSource=personal_library)

## Snippets
``` javascript
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
``` javascript
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
```

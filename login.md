{% include navigation.html %}
# Login
### Hack 1
```html
 <div class="container py-4 text-light bg-success">

        <div class="container bg-secondary py-4">
            <div class="p-5 mb-4 bg-light text-dark rounded-3">
                <form method="POST" ID="authUser" action={{url_for('crud.crud_authorize')}} >
                    <table>
                        <tr><th><label for="user_name">Username</label></th></tr>
                        <tr><td><input type="text" id='user_name' name="user_name" size="20" required></td></tr>
                        <tr><th><label for="email">Email</label></th></tr>
                        <tr><td><input type="email" id="email" name="email" size="20" required></td></tr>
                        <tr><th><label for="phone">Phone Number</label></th></tr>
                        <tr><td><input type="tel" id="phone" name="phone" placeholder="1234567890" required></td></tr>
                        <tr><th><label for="password1">Password</label></th></tr>
                        <tr><td><input type="password" id='password1' name="password1" size="20" required></td></tr>
                        <tr><th><label for="password2">Password Confirmation</label></th></tr>
                        <tr><td><input type="password" id='password2' name="password2" size="20" required></td></tr>
                        <tr><th><input type="submit" value="Submit"></th></tr>
                        <tr><td><a href={{url_for('crud.crud_login')}}>Log In</a></td></tr>
                    </table>
                </form>
            </div>
        </div>

    </div>
```
```python
# Authorise new user requires user_name, email, password
def authorize(name, email, password, phone):
    if is_user(email, password):
        return False
    else:
        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone=phone,  # this should be added to authorize.html
        )
        # encrypt their password and add it to the auth_user object
        auth_user.create()
        return True
```
```python
@app_crud.route('/authorize/', methods=["GET", "POST"])
def crud_authorize():
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        phone = request.form.get("phone")
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password1")           # password should be verified
        if authorize(user_name, email, password1, phone):    # zero index [0] used as user_name and email are type tuple
            return redirect(url_for('crud.crud_login'))
    # show the auth user page if the above fails for some reason
    return render_template("authorize.html")
```
![image](https://user-images.githubusercontent.com/89223726/162532879-05fd4bda-77f1-4156-9e0c-2a718493a59d.png)

### Hack 2
```python
@app_crud.route('/logout/', methods=["POST"])
@login_required
def logout():
    logout()
    return redirect(url_for('crud.crud'))
```
```html
<a href={{url_for('crud.crud_login')}}>Log Out</a>
            <p>{{current_user.name}}</p>
```
![image](https://user-images.githubusercontent.com/89223726/162533111-a5d0064f-debc-469b-963d-12e1d703582d.png)

### Hack 3
```python
@app_frontend.route('/life')
@login_required
def life():
    return render_template("life.html")
```
```python
from flask_login import login_required
```
![image](https://user-images.githubusercontent.com/89223726/162533274-00550646-ea35-4fb8-8b87-aafd228d452e.png)

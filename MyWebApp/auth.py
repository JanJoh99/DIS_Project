from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth',__name__)

# Sets all the user interactions 
@auth.route("/login", methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    
    return "<p> Logout<p>"


# Get and Post are HTTP mehtods that get and retrieve data 
@auth.route("/sign-up",  methods = ['GET', 'POST'])
def sign_up():    
    if request.method == 'POST': 
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        ## Message flashing
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category = 'success')
    return  render_template("signup.html")

 
### Chceck Password Fucntion 
def checkPassword():
    pass
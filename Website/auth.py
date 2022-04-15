from flask import Blueprint, render_template,request,flash,redirect, url_for
from .models import User
from . import db
#this is to import the classes for the database
from werkzeug.security import generate_password_hash,check_password_hash
#this is a way to secure a password so the password is not stored in plain text 
#hashing function is a one way function which doesn't have an inverse
#we can generate a hash, we pass password through hashing function and we cannot find the password through any other method aside from entering the original password
#so like we cannot find the password if we just know the hash
#explanation of inverse 
#x -> y
#f(x) = x+1
#f'(x) = x-1
from flask_login import login_user, login_required, logout_user,current_user
#current_user can be used to access all the information about the user

auth = Blueprint('auth',__name__) 

@auth.route('/login',methods=['GET','POST'])
#setting up the route url so like localhost:5000/login
#methods set to get and post, now we can use any element to Get or Post data and stuff

def login():#function to run when this page comes up
    data = request.form
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #getting the data from the text box and storing in variable
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                #it will hash the password in the db and compare with what the user entered
                flash("Logged in Successfully!",category='success')
                login_user(user,remember = True) #this remembers the fact that the user is logged in until the session is cleared or history is cleared or something
                #this is for when the user doesn't need to login every single time
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password, Try Again ",category= "error")
        else:
            flash("email does not exist ",category="error")
    return render_template("login.html",user = current_user)

@auth.route('/logout')#localhost:5000/logout
@login_required
def logout():   #functino to run when this page comes up
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods = ['GET','POST']) #localhost:5000/sign-up
def sign_up():#function to run when this page comes up
    if request.method=='POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email = email).first()
        if user:
            flash("email already exists ",category="error")
        elif len(email) < 4:
            flash('Email must be greater than 3 characters!',category='error')
        elif len(first_name)<2:
            flash('First name must be greater than 1 character!',category = 'error')
        elif password1 != password2:
            flash('Passwords do not match!',category = 'error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters!',category='error')
        else:
            #add user to database
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password1, method="sha256"))
            db.session.add(new_user) #to add the data to the table
            db.session.commit() #committing the data

            flash('Account Created!',category='success')
            #to redirect to home page after successfully created account
            
            return redirect(url_for('views.home'))#url_for('blueprintname.functionname)
    return render_template("signup.html",user = current_user)


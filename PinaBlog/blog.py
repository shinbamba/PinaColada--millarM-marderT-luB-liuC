from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import sqlite3

DB_FILE="blogger.db"

app = Flask(__name__)

app.secret_key = os.urandom(32)

errors = False

@app.route('/')
def render_test():
    if 'user' in session:
        username = session['user']
    else:
        return redirect("/login")
    return "Hey, you logged in!"

@app.route('/login')
def login():
    #print('user' in session)
    if 'user' in session:
        flash("You are already logged in.")
        return redirect("/")
    return render_template("login.html")
    
@app.route('/auth')
def authenticate():
    errors = False
    u_name = request.args.get("username")
    u_pass = request.args.get("password")
    try:
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("SELECT password FROM login where username='" + str(u_name) + "';")
        password = c.fetchall()
        db.commit()
        db.close()
        #print(u_pass)
        #print(password)
        if u_pass != password[0][0]:
            flash("Incorrect password.")
            errors = True
    except:
        flash("Incorrect username or password.")
        errors = True
    if not errors:
        session['user'] = u_name
        flash("Success!")
        return redirect("/")
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    if 'user' not in session:
        return redirect("/login")
    session.pop('user')
    flash("Successfully logged out")
    return redirect("/login")

@app.route('/register')
def register():
    if 'user' in session:
        flash("You must log out to create a new account.")
        return redirect("/")
    return render_template("register.html")

@app.route('/makereg')
def makereg():
    if 'user' in session:
        flash("You must log out to create a new account.")
        return redirect("/")
    u_name = request.args.get("username")
    u_pass = request.args.get("password")
    if u_name == None or u_pass == None:
        return redirect("/")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT username FROM login WHERE username='" + str(u_name) + "';")
    check_u = c.fetchall()
    #print(check_u)
    #print(u_name)
    if check_u != []:
        db.commit()
        db.close()
        flash("Username taken.")
        return redirect("/login")
    else:
        c.execute("INSERT INTO login VALUES('" + str(u_name) + "', '" + str(u_pass) + "');")
        db.commit()
        db.close()
        session['user'] = u_name
        flash("Account successfully created!")
        return redirect("/")

if __name__ == '__main__':
    app.debug = True
    app.run()

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


if __name__ == '__main__':
    app.debug = True
    app.run()

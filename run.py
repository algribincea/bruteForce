from flask import Flask, render_template, url_for, request, redirect, session, abort
from config import user


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form)
        if request.form['login'] != user['login']:

            error = 'Invalid username'
        elif request.form['password'] != user['password']:
            print('------------------', request.form['password'])
            error = 'Invalid password'
        else:
            print('------------')
            # session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/home')
def home():
    # if not session.get('logged_in'):
    #     abort(401)
    return render_template('index.html')


@app.route('/')
def main():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.debug = True
    app.run()
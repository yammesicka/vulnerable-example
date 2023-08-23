from flask import Flask, redirect, request, render_template_string, session

import install
import leaderboard
import login
import points
import register


app = Flask(__name__)
app.secret_key = "RQwefsaseTA4Y^AwAWrA"
install.database()


@app.route('/hi')
def hi():
    user = session.get('user')
    if not user:
        return redirect('/')
    return (
        f"Hello, {user['name']}!<br>"
        f"Points: {user['points']}<br>"
        f"<a href='/add_point'>Add Point</a><br>"
        f"<a href='/leaderboard'>Go to leaderboard</a><br>"
    )


@app.route('/login', methods=['POST'])
def login_page():
    username = request.form['username']
    password = request.form['password']

    user = login.vulnerable(username, password)
    if user:
        session['user'] = user
        return redirect('/hi')
    else:
        return "Login failed!"


@app.route('/add_point')
def add_point_endpoint():
    user = session.get('user')
    if not user:
        return "Not logged in!"

    points.add(user["id"])
    user = login.secure(user["name"], user["password"])
    session['user'] = user

    return redirect('/hi')


@app.route('/leaderboard')
def show_leaderboard():
    limit = request.args.get('limit', '10')

    best_users = leaderboard.vulnerable(limit)

    leaderboard_html = '<ol>'
    for user in best_users:
        leaderboard_html += f"<li>{user[0]}: {user[1]} points</li>"
    leaderboard_html += '</ol>'
    return (
        f"<h1>Leaderboard (Top {limit})</h1>"
        f"{leaderboard_html}"
        f"<a href='/hi'>Back to the main page</a>"
    )


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register.user(username, password):
            return "Registration successful! <a href='/'>Login</a>"
        else:
            return "Username already exists. Please choose a different username."
    return render_template_string('''
    <form action="/register" method="post">
        Username: <input type="text" name="username" autocomplete="off"><br>
        Password: <input type="password" name="password" autocomplete="off"><br>
        <input type="submit" value="Register">
    </form>
    <a href='/'>Back to Login</a>
    ''')


@app.route('/')
def home():
    return render_template_string('''
    <form action="/login" method="post">
        Username: <input type="text" name="username" autocomplete="off"><br>
        Password: <input type="password" name="password" autocomplete="off"><br>
        <input type="submit" value="Login">
    </form>
    <a href='/register'>Register</a>
    ''')


if __name__ == '__main__':
    app.run(debug=True)

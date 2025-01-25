from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    
    # Check if username and password match the predefined values
    if username == 'Belkacem Chemlal' and password == '32009138':
        return redirect('/profile')  # Redirect to static profile page
    else:
        return 'Incorrect username or password'

@app.route('/profile')
def profile():
    # Render the profile directly
    return render_template('profile.html', username='Belkacem Chemlal')

if __name__ == '__main__':
    app.run(debug=True)

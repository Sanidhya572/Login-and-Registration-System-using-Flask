from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form['email']
    password = request.form['password']
    
    # Perform login validation (this is a basic example, you should implement proper validation)
    if email == 'example@example.com' and password == 'password':
        return redirect(url_for('home'))
    else:
        return "Invalid credentials"  # You can also render a template for displaying error messages


@app.route('/create_expense')
def create_expense():
    return render_template('create_expense.html')


if __name__ == '__main__':
    app.run(debug=True)

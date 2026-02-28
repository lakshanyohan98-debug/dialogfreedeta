from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('htmlc.html')

@app.route('/register', methods=['POST'])
def register():
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['password']
    mobile = request.form['mobile']

    print("Name:", fullname)
    print("Email:", email)
    print("Password:", password)
    print("Mobile:", mobile)

    return "Registration Successful!"

if __name__ == '__main__':
    app.run(debug=True)


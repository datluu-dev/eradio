from flask import Flask, render_template

eradio_client = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@eradio_client.route('/')
@eradio_client.route('/Account/Login')
def login():
	return render_template('login.html', title='Sign In', isBackground=True)

@eradio_client.route('/Account/SignUp')
def sign_up():
	return render_template('signup.html', title='Sign Up', isBackground=True)

@eradio_client.route('/Account/Verify')
def verify():
	return render_template('verify.html', isBackground=True)
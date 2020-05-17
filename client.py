from flask import Flask, render_template

eradio_client = Flask(__name__)

@eradio_client.route('/')
@eradio_client.route('/Account/Login')
def login():
	return render_template('login.html', title='Sign In')

@eradio_client.route('/Account/SignUp')
def sign_up():
	return 'SignUp'
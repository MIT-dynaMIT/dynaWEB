# all the imports
import os
import sqlite3
import smtplib
import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



app = Flask(__name__) # create the application instance :)

#primary views
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/board.html')
def generic():
	return render_template('board.html')

@app.route('/donate.html')
def elements():
	return render_template('donate.html')

@app.route('/apply_main.html')
def apply():
	return render_template('apply_main.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/publicity.html')
def publicity():
	return render_template('publicity.html')

@app.route('/faq.html')
def faq():
	return render_template('faq.html')

#secondary views
@app.route('/typical_day.html')
def typical_day():
	return render_template('typical_day.html')

@app.route('/outreach.html')
def outreach():
	return render_template('outreach.html')

@app.route('/testimonials.html')
def testimonials():
	return render_template('testimonials.html')

@app.route('/sponsors.html')
def sponsors():
	return render_template('sponsors.html')

@app.route('/student_app.html')
def student_app():
	return render_template('student_app.html')

@app.route('/mentor_app.html')
def mentor_app():
	return render_template('mentor_app.html')

@app.route('/board_app.html')
def board_app():
	return render_template('board_app.html')

#backend for now
@app.route('/contact_us.html')
def contact_us():
    return render_template('board_app.html')
# 	if request.method == "POST":
#
# 		now = datetime.datetime.now()
# 		msg = MIMEMultipart()
# 		msg['Subject'] = request.form['name'] + ": dynaMIT Contact Email " + now.strftime("%Y/%m/%d")
# 		msg['From'] = 'dynamit.mit@gmail.com'
# 		msg['To'] = 'dynamit_board@mit.edu'
# 		msg['reply-to'] = request.form['email']
# 		body = MIMEText(request.form['message'])
# 		msg.attach(body)
#
# 		server = smtplib.SMTP('smtp.gmail.com', 587)
# 		server.starttls()
# 		server.login("dynamit.mit@gmail.com", "dynaROCKdynaTHIS") #eventually change this to a config variable set in the heroku instance for security reasons
# 		server.sendmail("dynamit.mit@gmail.com", "dynamit_board@mit.edu", msg.as_string())
# 		server.quit()
# 	return render_template('after_send_email.html')

def create_app():
    # Create the Flask application
    return app

if __name__ == '__main__':
    app.run(debug=True)

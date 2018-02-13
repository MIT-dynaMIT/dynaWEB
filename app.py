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

@app.route('/board')
def generic():
	return render_template('board.html')

@app.route('/donate')
def elements():
	return render_template('donate.html')

@app.route('/apply')
def apply():
	return render_template('apply.html')

@app.route('/about')
def about():
	return render_template('about.html')


#secondary views
@app.route('/typical_day')
def typical_day():
	return render_template('typical_day.html')

@app.route('/outreach')
def outreach():
	return render_template('outreach.html')

@app.route('/testimonials')
def testimonials():
	return render_template('testimonials.html')

@app.route('/sponsors')
def sponsors():
	return render_template('sponsors.html')


#backend for now
@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
	if request.method == "POST":

		now = datetime.datetime.now()
		msg = MIMEMultipart()
		msg['Subject'] = request.form['name'] + ": dynaMIT Contact Email " + now.strftime("%Y/%m/%d")
		msg['From'] = 'dynamit.mit@gmail.com'
		msg['To'] = 'dynamit_board@mit.edu'
		msg['reply-to'] = request.form['email']
		body = MIMEText(request.form['message'])
		msg.attach(body)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("dynamit.mit@gmail.com", "Dynamitemail")
		server.sendmail("dynamit.mit@gmail.com", "andytsai14@gmail.com", msg.as_string())
		server.quit()
	return render_template('after_send_email.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, flash, redirect, url_for, session, logging,request, session
from flask_mysqldb import MySQL
from form import RegisterForm
from twilio.rest import Client
from helpers import sendmail,sendmsg
import smtplib
import yaml

mysql = MySQL()
app = Flask(__name__)

db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = db['mysql_cursorclass']

mysql = MySQL(app)

@app.route('/')

def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])


def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        #get form fields
        guestname,guestphone,guestemail,checkin,checkout = form.guestname.data, form.guestphone.data, form.guestemail.data, form.checkin.data,form.checkout.data
        hostname, hostphone, hostemail   = form.hostname.data, form.hostphone.data, form.hostemail.data

        # check to make sure time in particular format
        if(form.checkin.data[2]==':' and (form.checkin.data[6:]=='AM' or form.checkin.data[6:]=='PM')):
            checkin = checkin
        else:
            flash('Time should be in HH:MM AM')
            render_template('register.html', form=form)
        if(form.checkout.data[2]==':' and (form.checkout.data[6:]=='AM' or form.checkout.data[6:]=='PM')):
            checkout = checkout
        else:
            flash('Time should be in HH:MM AM')
            render_template('register.html', form=form)


        session['guestphone'], session['guestemail'],session['guestname'],session['hostname'],session['checkin'] = guestphone, guestemail, guestname, hostname, checkin
        visitedaddress = 'ABCD'

        #visitor details to be sent to host
        msg_host = 'Visitor Details' + '\n'+'Name - '+guestname+'\n' + 'Email - ' +guestemail + '\n' + 'Phone - ' + guestphone + '\n' + 'Checkin Time - ' + checkin + '\n' + 'Checkout Time - ' + checkout 
        db = mysql.connection.cursor()

        # Execute query to save data to database
        db.execute("INSERT INTO visitor2(guestname,guestemail,guestphone,hostname,hostemail,hostphone,checkin,checkout,visitedaddress) VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s)",(guestname,guestemail,guestphone,hostname,hostemail,hostphone,checkin,checkout,visitedaddress))
        mysql.connection.commit()
        db.close()
        #sending message to host
        sendmsg(msg_host, '+91'+ hostphone)

        #sending mail to host
        sendmail(msg_host, 'yashnavlakha.1@gmail.com', hostemail, '123pawan123')
        flash('Registration Succesful! Have a Good Day')

        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/checkout' , methods = ['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Get Form Fields
        guestphone, guestemail, checkout1, visitedaddress = request.form['guestphone'],request.form['guestemail'], request.form['checkout'], 'ABCD'

        if(checkout1[2]==':' and (checkout1[6:]=='AM' or checkout1[6:]=='PM')):
            checkout = checkout1
        else:
            flash('Time should be in this format HH:MM_AM')
            return render_template('login.html')

        cur = mysql.connection.cursor()

        result = cur.execute("SELECT * FROM visitor2 WHERE guestphone = %s", [guestphone])
        result1 = cur.execute("SELECT * FROM visitor2 WHERE guestemail = %s", [guestemail])

        if result > 0 and result1 > 0:
            cur.execute("UPDATE visitor2 SET checkout = checkout WHERE guestemail = guestemail")
            session['msg_guest'] = 'Meeting Details' + '\n' + 'Name - '+ session['guestname']  +'\n' + 'Email - ' + session['guestemail'] + '\n' + 'Phone - ' + session['guestphone'] + '\n' + 'Check Time - ' + session['checkin'] +'\n'+'checkout Time - ' + checkout +'\n' + 'Host Name - ' + session['hostname'] +'\n' + 'Address Visited - ' + visitedaddress   
            sendmsg(session['msg_guest'], '+91'+ session['guestphone'])

            sendmail(session['msg_guest'], 'yashnavlakha.1@gmail.com' ,session['guestemail'], '123pawan123' )
            flash('Succesfully Checked Out')
            cur.close()
            return render_template('home.html')
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
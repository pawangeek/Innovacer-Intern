# Innovacer-Intern

# Approach
I defined a model that contains all the attributes stored in the MySQL table. Then I created two forms, one for the submission and another to get the details of the checkout time. In helpers.py file, there are two functions defined mainly, one to craete template and all necessary details for sending sms and another is to create template for sending mail to host. It also takes care of certain errors and exceptions. Then used HTML, Bootstrap for the frontend integrated with the backend.

# Tech Stack

* Flask
* Twilio API
* SMTP library for Mail services
* Mysql (For Database Purpose)
* Jinja2 (Templating Engine)
* Bootstrap 

# Steps for Deployment

* Clone this repository by `git clone https://github.com/pawangeek/Innovacer-Intern.git`
* Change directory by `cd Innovaccer-Intern`
* Install `python 3.7` on your local machine
* Install Mysql 5.5 Client on you machine
* Create `Virtual Environment` and activate it
* Use `pip install -r requirements.txt` to install dependencies
* Create Account on twilio to get auth_id and token
* Create a Phone number for machine based sms to mobile from twilio. Check them at `https://www.twilio.com/console/`
* Create database `myflaskapp` using mysql client by `create database myflaskapp;`
* Create table `visitors2` after `use myflaskapp;` and you able to create something like this<br>
![Database](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Database.png)

* Set your mysql cresentials and an email+password for smtplib. After completion of all these steps you will see something like this<br>
![Setup](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Directory.png)

* Start the sever fo to `http://127.0.0.1:5000/` and you will see something like this<br>
![Home](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Home.png)

* Go to About Me and you will see something like this<br>
![About](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/About.png)

* Navigate to Register page and fill all necessary checkin details there<br>
![Register](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Register.png)

* After filling Details under Register Section. Host will get mail and message regarding visitor's checkin like this<br>
![Mail](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Mail.png)
![Message](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Message.png)

* Further you can checkout from this software leaving deatials about host to visitor via mail and message<br>
![Checkout](https://github.com/pawangeek/Innovacer-Intern/blob/master/Images/Checkout.png)

# Conatact Details
Name: Pawan Kumar Jain
Phone: +91 9079250835
Email: pawanjain.432@gmail.com
altEmail: 17ucs108@lnmiit.ac.in

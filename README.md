# Innovacer-Intern

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
* Create table `visitors2` after `use myflaskapp;`
![Database](https://github.com/pawangeek/Innovacer-Intern/Images/Database.png)

* Set your mysql cresentials and an email+password for smtplib. After completion of all these steps you will see something like this
![Setup](https://github.com/pawangeek/Innovacer-Intern/Images/Directory.png)

* Start the sever fo to `http://127.0.0.1:5000/` and you will see something like this
![Home](https://github.com/pawangeek/Innovacer-Intern/Images/Home.png)

* Go to About Me and you will see something like this
![About](https://github.com/pawangeek/Innovacer-Intern/Images/About.png)

* Navigate to Register page and fill all necessary checkin details there
![Register](https://github.com/pawangeek/Innovacer-Intern/Images/Register.png)

* After filling Details under Register Section. Host will get mail and message regarding visitor's checkin like this
![Mail](https://github.com/pawangeek/Innovacer-Intern/Images/Mail.png)
![Message](https://github.com/pawangeek/Innovacer-Intern/Images/Message.png)

* Further you can checkout from this software leaving deatials about host to visitor via mail and message
![Checkout](https://github.com/pawangeek/Innovacer-Intern/Images/Checkout.png)

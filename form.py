from wtforms import Form, StringField, TextAreaField, PasswordField, validators,DateTimeField,IntegerField

class RegisterForm(Form):
    guestname  = StringField('Guest Name', [validators.Length(min=1, max=100)])
    guestphone = StringField('Guest Contact',[validators.Length(10)])
    guestemail = StringField('Guest Email', [validators.Length(min=6, max=100)])
    hostname   = StringField('Host Name', [validators.Length(min=1, max=100)])
    hostphone  = StringField('Host Contact', [validators.Length(10)])
    hostemail  = StringField('Host Email', [validators.Length(min=6, max=100)])
    checkin    = StringField('Check In Time', [validators.Length(8)])
    checkout   = StringField('Check Out Time', [validators.Length(8)])
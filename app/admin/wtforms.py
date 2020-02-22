from wtforms import Form, BooleanField, TextField, validators

class RegistrationForm (Form):
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])
    surname = TextField('Surname', [ validators.DataRequired() ])   
    firstname = TextField('First name', [ validators.DataRequired() ])
    year = TextField('Year', [ validators.DataRequired() ])

class Results1(Form):
    english = TextField('English Language', [ validators.DataRequired() ]) 
    mathematics = TextField('Mathematics', [ validators.DataRequired() ])
    economics = TextField('Economics', [ validators.DataRequired() ])
    physics = TextField('Physics', [ validators.DataRequired() ])   
    chemistry = TextField('Chemistry', [ validators.DataRequired() ])
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])

class Delete1(Form):
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])

class Update1(Form):
    english = TextField('English Language', [ validators.DataRequired() ]) 
    mathematics = TextField('Mathematics', [ validators.DataRequired() ])
    economics = TextField('Economics', [ validators.DataRequired() ])
    physics = TextField('Physics', [ validators.DataRequired() ])   
    chemistry = TextField('Chemistry', [ validators.DataRequired() ])
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])

class RegistrationUpdate (Form):
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])
    surname = TextField('Surname', [ validators.DataRequired() ])   
    firstname = TextField('First name', [ validators.DataRequired() ])
    year = TextField('Year', [ validators.DataRequired() ])

class ClassCombo(Form):
    year = TextField('Year', [ validators.DataRequired() ])
    subjectone = TextField('Subject One', [ validators.DataRequired() ])   
    subjecttwo = TextField('Subject Two', [ validators.DataRequired() ])
    subjectthree = TextField('Subject Three', [ validators.DataRequired() ])
    subjectfour = TextField('Subject Four', [ validators.DataRequired() ])   
    subjectfive = TextField('Subject Five', [ validators.DataRequired() ])

class Search(Form):
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])
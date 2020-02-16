from wtforms import Form, BooleanField, TextField, validators

class RegistrationForm (Form):
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])
    surname = TextField('Surname', [ validators.DataRequired() ])   
    firstname = TextField('First name', [ validators.DataRequired() ])
    year = TextField('Year', [ validators.DataRequired() ])

class Results(Form):
    computerscience = TextField('Computer Science', [ validators.DataRequired() ])
    physics = TextField('Physics', [ validators.DataRequired() ])   
    chemistry = TextField('Chemistry', [ validators.DataRequired() ])
    biology = TextField('Biology', [ validators.DataRequired() ])
    english = TextField('English Language', [ validators.DataRequired() ])   
    mathematics = TextField('Mathematics', [ validators.DataRequired() ])
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])

class Search(Form):
    matricNo = TextField('Matriculation Number', [ validators.DataRequired() ])
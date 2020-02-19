from . import admin_blueprint
import traceback

from .wtforms import RegistrationForm, Results, Search

from flask import Flask, render_template, redirect, url_for, flash, request, session
from app.classes.InsertQuery import InsertQuery
from app.classes.SelectQuery import SelectQuery

from functools import wraps

InsertQuery = InsertQuery()
SelectQuery = SelectQuery()


@admin_blueprint.route('/dashboard/')
def dashboard():
    return render_template('admin/dashboard.html')


@admin_blueprint.route('/register/', methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    
    if request.method == "POST" and form.validate():

        try:

            matricNo = form.matricNo.data

            surname = form.surname.data

            firstname = form.firstname.data

            year = form.year.data

            is_user_exist = SelectQuery._findUserByMatricNo(matricNo)

            if is_user_exist:

                flash('Matric No already exist', category = 'danger')
                return redirect(url_for('admin.register'))

            else:

                addUsers = InsertQuery._addUser(matricNo, surname, firstname, year)

                if addUsers == True:

                    flash('Registration Successful', category = 'success')
                    return redirect(url_for('admin.register'))

                else:
                    flash('Error During Registration', category = 'danger')
                    return redirect(url_for('admin.register'))


        except Exception as e:
            return str(traceback.format_exc())

    return render_template('admin/register.html', form=form)
    

@admin_blueprint.route('/result/', methods = ['GET','POST'])
def result():
    form = Results(request.form)
    
    if request.method == "POST" and form.validate():

        try:

            computerscience = form.computerscience.data

            physics = form.physics.data

            chemistry = form.chemistry.data

            biology = form.biology.data

            english = form.english.data

            mathematics = form.mathematics.data

            matricNo = form.matricNo.data

            is_user_exist = SelectQuery._findUserByMatricNo(matricNo)

            addResult = InsertQuery._addResult(computerscience, physics, chemistry, biology, english, mathematics, matricNo)

            if addResult == True:

                flash('Result Upload Successful', category = 'success')
                return redirect(url_for('admin.result'))
            
            else:
                flash('Error During Registration', category = 'danger')
                return redirect(url_for('admin.result'))


        except Exception as e:
            return str(self.traceback.format_exc())

    return render_template('admin/result.html', form=form)


@admin_blueprint.route('/checkresult/', methods=['GET','POST'])
def search():
    form = Search(request.form)
    
    if request.method == "POST" and form.validate():

        try:

            matricNo = form.matricNo.data

            results = SelectQuery._checkResult(matricNo)

            if results:
                
                for result in results:
                    post = result
                    return render_template('admin/course.html', post=post)

            else:
                flash ('No Records' , category='danger')

        except Exception as e:

            #since this is not inside a class use return str(traceback.formatexc()), you will have to import traceback
            #if it is inside a class, use return str(self.traceback.format_exc())
            return str(traceback.format_exc())

    return render_template('admin/search.html', form=form)
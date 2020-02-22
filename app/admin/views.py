from . import admin_blueprint
import traceback

from .wtforms import RegistrationForm, Results1, Delete1, Search, ClassCombo, Update1, RegistrationUpdate

from flask import Flask, render_template, redirect, url_for, flash, request, session
from app.classes.InsertQuery import InsertQuery
from app.classes.SelectQuery import SelectQuery
from app.classes.DeleteQuery import DeleteQuery
from app.classes.UpdateQuery import UpdateQuery

from functools import wraps

InsertQuery = InsertQuery()
SelectQuery = SelectQuery()
DeleteQuery = DeleteQuery()
UpdateQuery = UpdateQuery()


@admin_blueprint.route('/dashboard/')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_blueprint.route('/yearone/')
def yearone():
    return render_template('admin/yearone.html')

@admin_blueprint.route('/yeartwo/')
def yeartwo():
    return render_template('admin/yeartwo.html')

@admin_blueprint.route('/yearthree/')
def yearthree():
    return render_template('admin/yearthree.html')

@admin_blueprint.route('/addclasscombo/')
def addclasscombo():
    return render_template('admin/addclasscombo.html')

@admin_blueprint.route('/updateclasscombo/')
def updateclasscombo():
    return render_template('admin/updateclasscombo.html')

@admin_blueprint.route('/deleteclasscombo/')
def deleteclasscombo():
    return render_template('admin/deleteclasscombo.html')


@admin_blueprint.route('/register1/', methods=['GET','POST'])
def register1():
    form = RegistrationForm(request.form)
    
    if request.method == "POST" and form.validate():

        try:

            matricNo = form.matricNo.data

            surname = form.surname.data

            firstname = form.firstname.data

            year = form.year.data

            is_user_exist = SelectQuery._findUserByMatricNo1(matricNo)

            if is_user_exist:

                flash('Matric No already exist', category = 'danger')
                return redirect(url_for('admin.register1'))

            else:

                addUsers = InsertQuery._addUser1(matricNo, surname, firstname, year)

                if addUsers == True:

                    flash('Registration Successful', category = 'success')
                    return redirect(url_for('admin.register1'))

                else:
                    flash('Error During Registration', category = 'danger')
                    return redirect(url_for('admin.register1'))


        except Exception as e:
            return str(traceback.format_exc())

    return render_template('admin/register1.html', form=form)


@admin_blueprint.route('/uploadresults1/', methods = ['GET','POST'])
def uploadresults1():
    form = Results1(request.form)
    
    if request.method == "POST" and form.validate():

        try:

            english = form.english.data

            mathematics = form.mathematics.data
            
            economics = form.economics.data

            physics = form.physics.data

            chemistry = form.chemistry.data

            matricNo = form.matricNo.data

            addResult = InsertQuery._addResult1(english, mathematics, economics, physics, chemistry, matricNo)

            if addResult == True:

                flash('Result Upload Successful', category = 'success')
                return redirect(url_for('admin.uploadresults1'))
            
            else:

                flash('Error', category = 'danger')
                return redirect(url_for('admin.uploadresults1'))


        except Exception as e:
            return str(self.traceback.format_exc())

    return render_template('admin/result1.html', form=form)


@admin_blueprint.route('/deleteresults1/', methods = ['GET','POST'])
def deleteresults1():
    form = Delete1(request.form)

    if request.method == "POST" and form.validate():

        try:
            
            matricNo = form.matricNo.data

            delete = DeleteQuery._deleteresults1(matricNo)

            flash('Result Deleted', category= 'success')
            return redirect(url_for('admin.deleteresults1'))
                

        except Exception as e:
            return str(self.traceback.format_exc())
        
    return render_template('admin/deleteresults1.html', form=form)


@admin_blueprint.route('/updateresults1/', methods = ['GET','POST'])
def updateresults1():
    form = Update1(request.form)

    if request.method == 'POST' and form.validate():

        try:

            english = form.english.data

            mathematics = form.mathematics.data
            
            economics = form.economics.data

            physics = form.physics.data

            chemistry = form.chemistry.data

            matricNo = form.matricNo.data

            update = UpdateQuery._updateresult1 (english, mathematics, economics, physics, chemistry, matricNo)

            if update == True:

                flash('Result Updated', category= 'success')
                return redirect(url_for('admin.updateresults1'))

        except Exception as e:
            return str(self.traceback.format_exc())

    return render_template('admin/updateresults1.html', form=form)


@admin_blueprint.route('/updatedetails1/', methods = ['GET','POST'])
def updatedetails1():
    form = RegistrationUpdate(request.form)

    if request.method == 'POST' and form.validate():

        try:

            matricNo = form.matricNo.data

            surname = form.surname.data

            firstname = form.firstname.data

            year = form.year.data

            update = UpdateQuery._updatedetails1(matricNo, surname, firstname, year)

            if update == True:

                flash("Details updated successfully.")
                return redirect(url_for(admin.updatedetails1))

        except Exception as e:
            return str(traceback.format_exc())
    
    return render_template('admin/updatedetails1.html', form = form)


@admin_blueprint.route('/deletedetails1/', methods = ['GET','POST'])
def deletedetails1():
    form = Delete1(request.form)

    if request.method == "POST" and form.validate():

        try:
            
            matricNo = form.matricNo.data

            delete = DeleteQuery._deletedetails1(matricNo)

            flash("Student's Details Deleted", category= 'success')
            return redirect(url_for('admin.deletedetails1'))
                

        except Exception as e:
            return str(self.traceback.format_exc())
        
    return render_template('admin/deleteresults1.html', form=form)


@admin_blueprint.route('/checkresult1/', methods=['GET','POST'])
def search():
    form = Search(request.form)
    
    if request.method == "POST" and form.validate():

        try:

            matricNo = form.matricNo.data

            results = SelectQuery._checkResult1(matricNo)

            if results:
                
                for result in results:
                    post = result
                    return render_template('admin/course1.html', post=post)

            else:
                flash ('No Records' , category='danger')

        except Exception as e:

            return str(traceback.format_exc())

    return render_template('admin/search.html', form=form)


@admin_blueprint.route('/checkstudentdetails1/', methods = ['GET','POST'])
def checkstudentdetails1():
    form = Search(request.form)

    if request.method == "POST" and form.validate():

        try:

            matricNo = form.matricNo.data

            details = SelectQuery._checkstudentdetails1(matricNo)

            if details:

                for detail in details:
                    post = detail
                    return render_template('admin/studentdetails1.html', form = form, post = post)
                    
            else:
                flash ('No Records' , category='danger')

        except Exception as e:

            return str(traceback.format_exc())

    return render_template('admin/studentdetails1.html', form=form)


@admin_blueprint.route('/classcombo/', methods=['GET','POST'])
def classcombo():
    form = ClassCombo(request.form)

    if request.method == 'POST' and form.validate():

        try:

            year = form.year.data

            subjectone = form.subjectone.data 

            subjecttwo = form.subjecttwo.data

            subjectthree = form.subjectthree.data

            subjectfour = form.subjectfour.data  

            subjectfive = form.subjectfive.data

            subjectsix = form.subjectsix.data

        except Exception as e:
            return str(traceback.format_exc())
    
    return render_template('admin/classcombo.html', form=form)
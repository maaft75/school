from .function_db import Dbfunctions

update = Dbfunctions()

class UpdateQuery():
    def _updateresult1(self, english, mathematics, economics, physics, chemistry, matricNo):

        try:

            query = "UPDATE resultyear1 SET english = '%s', mathematics = '%s', economics = '%s', physics = '%s', chemistry = '%s' WHERE matricNo = '%s'" %(english, mathematics, economics, physics, chemistry, matricNo)

            update._Initiatedb()

            update.cursor.execute(query)

            update._Commitdb()

            return True
        
        except Exception as e:

            return str(self.traceback.format_exc())

        finally:

            update._Closedb()

    def _updatedetails1(self, matricNo, surname, firstname, year):

        try:

            query = "UPDATE studentinfo1 SET  surname = '%s', firstname = '%s', year = '%s' WHERE matricNo = '%s'" %(surname, firstname, year, matricNo)

            update._Initiatedb()

            update.cursor.execute(query)

            update._Commitdb()

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            update._Closedb()

    def _updatesubjectcombo(self, year, subjectone, subjecttwo, subjectthree, subjectfour, subjectfive):
    
        try:

            query = "UPDATE subjectcombo SET subject1 = '%s', subject2 = '%s', subject3 = '%s', subject4 = '%s', subject5 = '%s' WHERE year = '%s'" %(subjectone, subjecttwo, subjectthree, subjectfour, subjectfive, year)

            update._Initiatedb()

            update.cursor.execute(query)

            update._Commitdb()

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            update._Closedb()
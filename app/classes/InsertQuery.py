from .function_db import Dbfunctions

import traceback

dbFunctions = Dbfunctions()

class InsertQuery():
    def _addUser1(self, matricNo, surname, firstname, year):

        try:

            query = "INSERT INTO studentinfo1(matricNo, surname, firstname, year) VALUES ('%s', '%s', '%s', '%s')" %(matricNo, surname, firstname, year)
            
            dbFunctions._Initiatedb()
            
            dbFunctions.cursor.execute(query)
            
            dbFunctions._Commitdb()
            
            return True

        except Exception as e:

            return str(self.traceback.format_exc())

        finally:

            dbFunctions._Closedb()

    def _addResult1(self, english, mathematics, economics, physics, chemistry, matricNo):
        try:

            query = "INSERT INTO resultyear1(english, mathematics, economics, physics, chemistry, matricNo) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(english, mathematics, economics, physics, chemistry, matricNo)
            
            dbFunctions._Initiatedb()

            dbFunctions.cursor.execute(query)

            dbFunctions._Commitdb()

            return True

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            dbFunctions._Closedb()

    def _addClass(self, year, subjectone, subjecttwo, subjectthree, subjectfour, subjectfive):

        try:

            query = "INSERT INTO subjectcombo(year, subject1, subject2, subject3, subject4, subject5) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(year, subjectone, subjecttwo, subjectthree, subjectfour, subjectfive)

            dbFunctions._Initiatedb()

            dbFunctions.cursor.execute(query)

            dbFunctions._Commitdb()

            return True

        except Exception as e:

            return str(self.traceback.format_exc())

        finally:

            dbFunctions._Closedb()
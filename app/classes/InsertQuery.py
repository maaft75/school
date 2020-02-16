from .function_db import Dbfunctions

import traceback

dbFunctions = Dbfunctions()

class InsertQuery():
    def _addUser(self, matricNo, surname, firstname, year):

        try:

            query = "INSERT INTO studentinfo(matricNo, surname, firstname, year) VALUES ('%s', '%s', '%s', '%s')" %(matricNo, surname, firstname, year)
            
            dbFunctions._Initiatedb()
            
            dbFunctions.cursor.execute(query)
            
            dbFunctions._Commitdb()
            
            return True

        except Exception as e:

            return str(self.traceback.format_exc())

        finally:

            dbFunctions._Closedb()

    def _addResult(self, computerscience, physics, chemistry, biology, english, mathematics, matricNo):
        try:

            query = "INSERT INTO studentresult(computerscience, physics, chemistry, biology, english, mathematics, matricNo) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(computerscience, physics, chemistry, biology, english, mathematics, matricNo)
            
            dbFunctions._Initiatedb()

            dbFunctions.cursor.execute(query)

            dbFunctions._Commitdb()

            return True

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            dbFunctions._Closedb()
from .function_db import Dbfunctions

dbfunctions = Dbfunctions()

class DeleteQuery():
    def _deleteresults1(self, matricNo):

        try:

            query = "DELETE FROM resultyear1 WHERE matricNo = '%s'" %(matricNo)

            dbfunctions._Initiatedb()
            
            dbfunctions.cursor.execute(query)

            dbfunctions._Commitdb()

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            dbfunctions._Closedb()
    
    def _deletedetails1(self, matricNo):

        try:

            query = "DELETE FROM studentinfo1 WHERE matricNo = '%s'" %(matricNo)

            dbfunctions._Initiatedb()
            
            dbfunctions.cursor.execute(query)

            dbfunctions._Commitdb()

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            dbfunctions._Closedb()

    def _deletesubjectcombo(self, year):

        try:
            query = "DELETE FROM subjectcombo WHERE year = '%s'" %(year)

            dbfunctions._Initiatedb()

            dbfunctions.cursor.execute(query)

            dbfunctions._Commitdb()

        except Exception as e:

            return str(self.traceback.format_exc())
        
        finally:

            dbfunctions._Closedb()

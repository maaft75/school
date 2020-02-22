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
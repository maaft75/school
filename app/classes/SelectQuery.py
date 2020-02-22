from .function_db import Dbfunctions

select = Dbfunctions()

class SelectQuery():

    def _findUserByMatricNo1(self, matricNo):

        try:
            query = "SELECT matricNo FROM studentinfo1 WHERE matricNo = '%s'" %(matricNo)

            select._Initiatedb()

            select.cursor.execute(query)

            data = select.cursor.fetchone()

            if data:
                return data
            else:
                return False
            
        except Exception as e:
            return str(self.traceback.format_exc)
            raise e
        
        finally:
            select._Closedb()

    def _checkResult1(self, matricNo):
        
        try:
            query = "SELECT english, mathematics, economics, physics,chemistry, matricNo FROM resultyear1 WHERE matricNo = '%s'" %(matricNo)

            select._Initiatedb()

            select.cursor.execute(query)

            data = select.cursor.fetchall()

            if data:
                return data
            else:
                return False
        
        except Exception as e:
            return str(self.traceback.format_exc())
            raise e
        
        finally:
            select._Closedb()
    

    def _checkstudentdetails1(self, matricNo):

        try:

            query = "SELECT matricNo, surname, firstname, year FROM studentinfo1 WHERE matricNo = '%s'" %(matricNo)

            select._Initiatedb()

            select.cursor.execute(query)

            data = select.cursor.fetchall()

            if data:
                return data
            else:
                return False

        except Exception as e:
            return str(self.traceback.format_exc())
            raise e

        finally:
            select._Closedb()
from .function_db import Dbfunctions

select = Dbfunctions()

class SelectQuery():

    def _findUserByMatricNo(self, matricNo):

        try:
            query = "SELECT matricNo FROM studentinfo WHERE matricNo = '%s'" %(matricNo)

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

    def _checkResult(self, matricNo):
        
        try:
            query = "SELECT computerscience,physics,chemistry, biology, english, mathematics, matricNo FROM studentresult WHERE matricNo = '%s'" %(matricNo)

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
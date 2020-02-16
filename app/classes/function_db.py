from .config_db import connection

#DEFINE FUNCTION THAT INITIATES, COMMITS AND CLOSES DB

class Dbfunctions():
    
    def __init__(self):

        self.db = connection()
        self.cursor = self.db.cursor()


    def _Closedb(self):

        self.cursor.close()
        self.db.close()


    def _Commitdb(self):

        self.db.commit()

    def _Initiatedb(self):

        self.db = connection()
        self.cursor = self.db.cursor()
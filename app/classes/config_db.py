import MySQLdb
import gc

def connection():

    db = MySQLdb.connect(host='localhost',user='root',password='tygertyger',database='school')

    gc.collect()

    return db

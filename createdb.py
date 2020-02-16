import MySQLdb

db = MySQLdb.connect(host='localhost', user='root',password='tygertyger')
cursor = db.cursor()

#DROP DATABASE IF IT EXISTS AND CREATE DATABASE
#cursor.execute('DROP DATABASE school')
#cursor.execute('CREATE DATABASE school')
cursor.execute('USE school')

#CREATE TABLES
#cursor.execute('CREATE TABLE studentinfo(matricNo INT(4) PRIMARY KEY, surname VARCHAR(255), firstname VARCHAR(255), year INT(4))')
cursor.execute('CREATE TABLE studentresult(computerscience VARCHAR(255) NOT NULL,physics VARCHAR(255) NOT NULL,chemistry VARCHAR(255) NOT NULL, biology VARCHAR(255) NOT NULL, english VARCHAR(255) NOT NULL, mathematics VARCHAR(255) NOT NULL, matricno INT(4) NOT NULL, FOREIGN KEY (matricno) REFERENCES studentinfo(matricno))')

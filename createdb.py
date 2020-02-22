import MySQLdb

db = MySQLdb.connect(host='localhost', user='root',password='tygertyger')
cursor = db.cursor()

#DROP DATABASE IF IT EXISTS AND CREATE DATABASE
cursor.execute('DROP DATABASE school')
cursor.execute('CREATE DATABASE school')
cursor.execute('USE school')

#CREATE TABLES

cursor.execute('CREATE TABLE studentinfo1(matricNo INT(4) PRIMARY KEY, surname VARCHAR(255), firstname VARCHAR(255), year INT(4))')
cursor.execute('CREATE TABLE studentinfo2(matricNo INT(4) PRIMARY KEY, surname VARCHAR(255), firstname VARCHAR(255), year INT(4))')
cursor.execute('CREATE TABLE studentinfo3(matricNo INT(4) PRIMARY KEY, surname VARCHAR(255), firstname VARCHAR(255), year INT(4))')
cursor.execute('CREATE TABLE subjectcombo(year INT(3) NOT NULL, subject1 VARCHAR(255) NOT NULL, subject2 VARCHAR(255) NOT NULL, subject3 VARCHAR(255) NOT NULL, subject4 VARCHAR(255) NOT NULL, subject5 VARCHAR(255) NOT NULL)')
cursor.execute('CREATE TABLE resultyear1(english INT(3) NOT NULL, mathematics INT(3), economics INT(3) NOT NULL, physics INT(3) NOT NULL, chemistry INT(3) NOT NULL, matricNo INT(4) NOT NULL, FOREIGN KEY (matricNo) REFERENCES studentinfo1(matricNo))')
cursor.execute('CREATE TABLE resultyear2(english INT(3) NOT NULL, mathematics INT(3), economics INT(3) NOT NULL, history INT(3) NOT NULL, government INT(3) NOT NULL, matricNo INT(4) NOT NULL, FOREIGN KEY (matricNo) REFERENCES studentinfo2(matricNo))')
cursor.execute('CREATE TABLE resultyear3(english INT(3) NOT NULL, mathematics INT(3), economics INT(3) NOT NULL,  accounting INT(3) NOT NULL, commerce INT(3) NOT NULL, matricNo INT(4) NOT NULL, FOREIGN KEY (matricNo) REFERENCES studentinfo3(matricNo))')

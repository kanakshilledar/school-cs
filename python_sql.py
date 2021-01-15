# 1. Create database School, Create table Student with
#    fields rno, name, dob, total. w/ 3 records

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',)

mycrsr = mydb.cursor()
mycrsr.execute("create database School")
mycrsr.execute('use School')
mycrsr.execute('create table Student (rno int, name varchar(255), dob date, total float)')

query = 'insert into Students (rno, name, dob, total) values (%d, %s, %s, %f)'
values = (1, 'a', '01-01-2001', 99.5)
mycrsr.execute(query, values)
values = (2, 'b', '02-02-2002', 99.5)
mycrsr.execute(query, values)
values = (3, 'c', '03-03-2003', 99.5)
mycrsr.execute(query, values)

# writing data to table
mydb.commit()

# displaying contents
mycrsr.execute('select * from Students')
output = mycrsr.fetchall()
print(output)



# 2. create database company, table employee fields eno, ename, doj, basic_salary. insert 3 records, increament salary by 2000

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',)

mycrsr = mydb.cursor()
mycrsr.execute('create database company')
mycrsr.execute('use company')
mycrsr.execute('create table employee (eno int, ename varchar(255), doj date, basic_salary float)')

query = 'insert into employee (eno, ename, doj, basic_salary) values (%d, %s, %s, %f)'
values = [
        (1, 'peter', '01-01-2001', 2000),
        (2, 'meter', '02-02-2002', 2000),
        (3, 'liter', '03-03-2003', 2000),]
mycrsr.execute(query, values)
mydb.commit()

mycrsr.execute('select * from employee')

# updating table
mycrsr.execute('update employee set salary = salary + 2000')
mydb.commit()



# 3. Create database library, table book fields ano, bname, author, price, qty. insert 3 records, display contents, increment price by 10

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',)

mycrsr = mydb.cursor()
mycrsr.execute('create database library')
mycrsr.execute('use library')
mycrsr.execute('create table book (ano int, bname varchar(255), author varchar(255), price int, qty int)')

query = 'insert into book (ano, bname, author, price, qty) values (%d, %s, %s, %d, %d')
values = [(1, 'a', 'x', 123, 1),
        (2, 'b', 'y', 123, 1),
        (3, 'c', 'z', 123, 1),]
mycrsr.execute(query, values)
mydb.commit()

mycrsr.execute('select * from book')
mycrsr.execute('update book set price = price + 10')
mydb.commit()



# 4. Insert data into table

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',
        database = 'school',)

mycrsr = mydb.cursor()
mycrsr.execute('create table student(sno varchar(4), sname varchar(10), age int, fees int, address varchar(22)')

sql = 'insert into student (sno, sname, age, fees, address) values (%s, %s, %d, %d, %s')
values = [('s101', 'heena', 18, 9880, 'nagpur'),
        ('s102', 'rahul', 21, 10000, 'jaipur'),
        ('s103', 'happy', 25, 12000, 'bhopal'),
        ('s104', 'jasmine', 16, 7777, 'delhi'),
        ('s105', 'visha', 22, 2222, 'jaipur'),]
mycrsr.execute(sql, values)
mydb.commit()



# 5. Delete records with city nagpur

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',
        database = 'school',)

mycrsr = mydb.cursor()
mycrsr.execute('delete from student where address = \'nagpur\'')
mydb.commit()



# 6. Display records of student table

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',
        database = 'school',)

mycrsr = mydb.cursor()
mycrsr.execute('select * from student')



# 7. set age of heena as 12 instead of 18

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',
        database = 'school',)

mycrsr = mydb.cursor()
mycrsr.execute('update student set age = 20 where sname = \'heena\'')



# 8. display records whose name doesnt start with 'h'

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'user_name',
        password = 'user_password',
        database = 'school',)

mycrsr = mydb.cursor()
mycrsr.execute('select * from student where sname rlike \'^H\'')


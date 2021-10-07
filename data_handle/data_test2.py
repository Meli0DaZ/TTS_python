import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)
mycursor = db.cursor()

sql = 'CREATE DATABASE no_data;'
try:
    mycursor.execute(sql)
except:
    pass
db.close()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="no_data"
)
mycursor = db.cursor()
sql = "CREATE TABLE custormer(" \
      "customerid INT(10) UNSIGNED PRIMARY KEY," \
      "firstname VARCHAR(20),lastname VARCHAR(20)," \
      "companyname VARCHAR(50)," \
      "billingaddress1 VARCHAR(225), billingaddress2 VARCHAR(25)," \
      "city VARCHAR(20), state VARCHAR(20)," \
      "postalcode VARCHAR(20) ,country VARCHAR(20)," \
      "phonenumber VARCHAR(20)," \
      "emailaddress VARCHAR(50)," \
      "createddate DATETIME);"
try:
    mycursor.execute(sql)
except:
    pass
# mycursor.execute('DESCRIBE custormer')

f = open('customer.csv','r')
people =[]
person ={}

lines = f.readlines()[1:]
for line in lines:
    a=line.split(',')
    # print(a)
    person['customerid'] = a[0]
    person['firstname'] = a[1]
    person['lastname'] = a[2]
    person['companyname'] = a[3]
    person['billingaddress1'] = a[4]
    person['billingaddress2'] = a[5]
    person['city'] = a[6]
    person['state'] = a[7]
    person['postalcode'] = a[8]
    person['country'] = a[9]
    person['phonenumber'] = a[10]
    person['emailaddress'] = a[11]
    person['createddate'] = a[12][:-1]
    print(person)

    sql = "INSERT INTO custormer SET " \
          "customerid='{}', firstname='{}', lastname='{}'," \
          "companyname='{}', billingaddress1='{}', billingaddress2='{}', " \
          "city='{}', state='{}', postalcode='{}', country='{}', " \
          "phonenumber='{}', emailaddress='{}', createddate='{}'".\
        format(person['customerid'],person['firstname'],person['lastname'],
                person['companyname'],person['billingaddress1'],person['billingaddress2'],
                person['city'],person['state'],person['postalcode'],person['country'],
                person['phonenumber'],person['emailaddress'],person['createddate'])
    mycursor.execute(sql)
    db.commit()
db.close()

import cx_Oracle as orcl

import sys
con=None
try:
    print "Making connection"
    con=orcl.connect('system/Jyoti2113')
    print "Connection Made"

    cur = con.cursor()
    print "cur made"
    querystring="select * from STOCK"
    cur.execute(querystring)
    ver = cur.fetchall()
    print ver
    cur.execute("insert into STOCK values(20, \"C20\", \"STOCK 20\")")

    cur.execute("SELECT * from STOCK")
    ver = cur.fetchall()
    print "Database values : ", ver

    cur.execute("update STOCK set STOCK_CODE=\"C20_1\" where STOCK_ID=20")
    cur.execute("SELECT * from STOCK")
    ver = cur.fetchall()
    print "After Update Database values : ", ver

    cur.execute("insert into STOCK values(30,\"C30\", \"Stock 30\")")
    cur.execute("insert into STOCK values(40,\"C40\", \"Stock 40\")")
    cur.execute("SELECT * from STOCK")
    ver = cur.fetchall()
    print "After Insert Database values : ", ver
    con.commit()

    
    #cur.execute("SELECT VERSION()")
    #ver = cur.fetchone()
    #print "Database values : ", ver
   
    '''cur.execute("create table if not exists employee (eid int primary key , ename varchar(25), age int)");
    cur.execute("insert into employee values(1, \"Chetan\", 25)")

    cur.execute("SELECT * from employee")
    ver = cur.fetchall()
    print "Database values : ", ver

    cur.execute("update employee set ename=\"Vinod\" where eid=1")
    cur.execute("SELECT * from employee")
    ver = cur.fetchall()
    print "After Update Database values : ", ver

    cur.execute("insert into employee values(6,\"Chetan\", 25)")
    cur.execute("insert into employee values(2,\"Vishwa\", 32)")
    cur.execute("SELECT * from employee")
    ver = cur.fetchall()
    print "After Insert Database values : ", ver
    con.commit()
    '''
except orcl.Error, e:
    print e
    print "Error %d" % (e.args[0])
    sys.exit(1)
finally:           
    if con:    
        con.close()

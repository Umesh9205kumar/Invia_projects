import pymysql
def connection():
    return pymysql.connect(host='localhost',database='employ',user='root',port=3306,password='')
def check_Employe(employe_id):
    sql="select * from empd where id=%s"
    conn=connection()
    c=conn.cursor()
    data=(employe_id)
    c.execute(sql,data)
    r=c.rowcount
    
    if r==1:
        return True
    else:
        return False

def Add_employ():
    id=input("Enter the employ id")
    if(check_Employe(id)==True):
        print("This employe already exists:")
        menu()
    else:
        Name=input("Enter the name:")
        post=input("Enter the post:")
        salary=input("Enter the salary:")
        data=(Name,post,salary,id)
        sql="insert into empd values(%s,%s,%s,%s)"
        conn=connection()
        c=conn.cursor()
        c.execute(sql,data)
        conn.commit()
        print("Employee Data added successfully:")
        conn.close()
def Display_employee():
    sql="select * from empd"
    conn=connection()
    c=conn.cursor()
    c.execute(sql)
    r=c.fetchall()
    for i in r:
        print("Employee Name:",i[0])
        print("Employee post:",i[1])
        print("Employee salar:",i[2])
        print("Employee ID:",i[3])
    menu()

def Remove_employee():
    id=input("Enter the employee ID:")
    if(check_Employe(id)==False):
        print("This employee does not exist:")
        menu()
    else:
        sql="delete from empd where id=%s"
        data=(id)
        conn=connection()
        c=conn.cursor()
        c.execute(sql,data)
        conn.commit()
        print("Employee Removed")
def Employee_promotion():
    Id=int(input("Enter the employee id:"))
    if(check_Employe(Id)==False):
        print("This employee does not exist:")
        menu()
    else:
        sql="select salary from empd where id=%s"
        data=(Id)
        conn=connection()
        c=conn.cursor()
        c.execute(sql,data)
        Amount=int(input("Enter the update salary"))
        r=c.fetchone()
        t=r[0]+Amount
        sql="update empd set salary=%s where id=%s"
        d=(t,Id)
        c.execute(sql,d)
        conn.commit()
        print("Employee has promoted")
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
    ch=int(input("Enter your the operation number"))
    if ch==1:
        Add_employ()
    elif ch==2:
        Remove_employee()
    elif ch==3:
        Employee_promotion()
    elif ch==4:
        Display_employee()
    elif ch==5:
        exit(0)
    else:
        print("Invalid operation")
menu()
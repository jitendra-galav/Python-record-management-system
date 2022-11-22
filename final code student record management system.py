import pymysql as mq
conn=mq.connect(host="localhost",user="root",passwd="")
mycursor=conn.cursor()

mycursor.execute("create database if not exists studentrecord")
mycursor.execute("use studentrecord")
mycursor.execute("create table if not exists signup(username varchar(30) , password varchar(30))")


print("-----------------------------------------------------------------")
print("---------------->>>TOPIC OF PROJECT<<<--------------------------")
print("----------->>> STUDENT RECORD MANAGEMENT SYSTEM <<<---------")
print()

print(" 1. signup    2. login")
character=int(input("  signup \ login ( 1 , 2 ) : "))
if character == 1:
   signup()
elif character ==2 :
     login()
else:
     print("wrong enter")
     print("please enter the correct userid and paswword")




def signup():
    username=input("ENTER THE USERNAME -->>")
    password=input("ENTER THE PASSWORD-->>")
    mycursor.execute("insert into signup values("+username+","+password+")")
    conn.commit()                                                            #please check these once
    print("************SIGN UP SUCCESSFULLY****************")
    print("Now Pleasse Login To Continue")
    login()


def login():
    username=input("ENTER THE USERNAME -->>")
    password=input ("ENTER THE PASSWORD-->>")
    mycursor=conn.cursor()
    mycursor.execute("select username from signup")
    all_user_name=mycursor.fetchall()
    user2=[]
    for i in range (len (all_user_name)):
        user2.append(all_user_name[i][0])  #jo pehla hoga wo user hoga isliye 0

    mycursor=conn.cursor()
    mycursor.execute("select password from signup")
    paswrd=mycursor.fetchall()
    pwd=[]
    for i in range (len(paswrd)):
        pwd.append(paswrd[i][0])
    conn.commit()

    if (username not in user2) or (password not in pwd):
       print("*****WRONG USERNAME OR PASSWORD********")
       f = 1
       while True:
            if f==1:
                login()
            else:
                 exit()
    else:
        mycursor=conn.cursor()
        mycursor.execute("select username from signup where username="+username+"")
        user=mycursor.fetchone()
        mycursor.execute("select password from signup where password="+password+"")
        print("****************LOGIN SUCCESSFULLY************************")
        mycursor.execute("create table if not exists students(rollno integer , Name varchar(20) ,Class varchar(5),Fee integer)")
        conn.commit()
        while True:
            print("-------------------------------------------------------------")
            print("*************MAIN MENU***************************************")
            print("-------------------------------------------------------------")
            print(" 1. add record" )
            print(" 2. display record" )
            print(" 3. search record" )
            print(" 4. delete record" )
            print(" 5. update record" )
            print(" 6. exit" )
            print("-------------------------------------------------------------")


            a=int(input(" enter  no :-> "))                      # add record
            if ( a == 1 ) :
               print("----------------------------------------------------------")
               print("************ENTER  DETAILS OF STUDENT*********************")
               print("----------------------------------------------------------")
               roll = input(" enter roll no :->")
               name = input(" enter name :->")
               clas = input(" enter class :->")
               fee  = input (" enter fee :->")
               mycursor=conn.cursor()
               sql="insert into student (rollno,name,clas,fee) values (%s,%s,%s,%s)"
               value = [( roll , name ,  clas  ,  fee )]
               mycursor.executemany( sql , value)
               conn.commit()
               print("\t\t\t\tINFORMATION SAVED")
               print("----------------------------------------------------------")
            elif( a == 2 ) :
                mycursor=conn.cursor()
                mycursor.execute( " select * from student " )
                myresult=mycursor.fetchall()
                for record in myresult:
                     print("{:<20}{:<15}{:<20}{:<5}".format(record[0],record[1],record[2],record[3]))

            elif ( a == 3 ) :                                                #search student by roll number
              print("----------------------------------------------------------")
              print("***********SEARCH STUDENT BY ROLL NO *********************")
              print("----------------------------------------------------------")


              roll_1=input( " enter student roll no :-> " )
              mycursor=conn.cursor()
              mycursor.execute( " select * from student where rollno = ' " +roll_1+" ' ")
              myresult=mycursor.fetchall()
              for record in myresult:
                        print("{:<20}{:<15}{:<20}{:<5}".format(record[0],record[1],record[2],record[3]))


            elif  ( a == 4 ):                                                 #delte student record by roll number
                 print("---------------------------------------------------------")
                 print("***************DELETE RECORD BY ROLL NO *****************")
                 print("---------------------------------------------------------")
                 roll_1=input("enter student rollno whoes information you want to delete :-->")
                 mycursor=conn.cursor()
                 mycursor.execute("delete from student where rollno = " +roll_1)
                 conn.commit()
                 print("\t\t\t!!!!Record deleted successfully !!!!")
                 print("---------------------------------------------------------")


            elif (a == 5):                                                   #update and correction student fee name and other information by roll

                rollno = input ( " enter student rollno whoes fees you want to update = " )
                fee = input ( " new fee :-> " )
                name = input(" enter name :->")
                clas = input(" enter class :->")

                mycursor=conn.cursor()
                sql="UPDATE student SET name = %s ,fee = %s , clas = %s where rollno = %s "
                data=(rollno ,fee ,name ,clas )
                mycursor.execute(sql,data)
                conn.commit()
                print("information updated susccessfully..")


                mycursor.execute( " select * from student where rollno = ' " +rollno+" ' ")
                myresult=mycursor.fetchall()
                for record in myresult:
                    print("{:<20}{:<15}{:<20}{:<5}".format(record[0],record[1],record[2],record[3]))









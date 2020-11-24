import mysql.connector
mydb = mysql.connector.connect(
    host="host ip address",
    user="username",
    password="your password",
    database="name of your database"

)
mycursor=mydb.cursor()



while True:
   print(" 1.insert  \n 2.view \n 3.retrive\n 4.delete\n 5.update password \n 6.exit \n")
   user_choice=int(input())
   print(user_choice)
   if user_choice == 1 :
       weba=input("enter the website address\n")
       user=input("enter the user name if not type - ")
       email=input("enter the email address\n")
       password=input("enter the password address\n")
       sql="insert into passwordmanager(weba,username,emailid,password) values(%s,%s,%s,%s)"
       val=(weba,user,email,password)
       mycursor.execute(sql,val)
       mydb.commit()
       print(mycursor.rowcount,"record inserted")
   if user_choice == 2: 
     mycursor.execute("select * from passwordmanager")
     myresult=mycursor.fetchall()
     for x in myresult:
       print(x)  

   if user_choice == 3:
      print("enter the website address \n")
     
      cmd1="select * from passwordmanager where weba = %s"
      email=str(input())
      val=(email,)
      mycursor.execute(cmd1,val)
      myresult=mycursor.fetchall()
      for x in myresult:
         print("the website is : " + x[0])
         print("the username is : "+ x[1])
         print("the emailid is : " + x[2])
         print("the password is : " + x[3])
      
   if user_choice ==4 :
      print("Enter the user name or any information regarding the record\n")
      delete = input()
      sql = "delete from passwordmanager where emailid= %s"
      val =(delete,)
      mycursor.execute(sql,val)
      mydb.commit()
      print("the record has been deleted\n")  
   if user_choice == 5:
      print("enter the website address\n")
      website=input()
      print("enter the updated password\n")
      password =input()
      sql="update passwordmanager SET password = %s where weba = %s"
      val=(password, website)
      mycursor.execute(sql, val)
      mydb.commit()
      print("the password has been updated\n")

   if user_choice == 6:
      break;
      break;
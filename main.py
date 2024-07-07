import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="mydatabase"

)
user_password="Da@9141525275"

mycursor=mydb.cursor()

def get_multiple_records(website):
    sql="select * from passwordmanager where weba=%s"
    val=(website,)
    mycursor.execute(sql,val)
    x=mycursor.fetchall()
    for a in x:
     print(a)
def number_of_records(website):
         sql="select count(*) from passwordmanager where weba = %s"
         val =(website,)
         mycursor.execute(sql,val)
         x=mycursor.fetchall()
         get_multiple_records(website)
         return int(x[0][0])

def updatedata(changedValue,website,emailid,field):
     sql="update passwordmanager SET "+field+" = %s where weba = %s and emailid=%s"
     val=(changedValue, website,emailid)
     mycursor.execute(sql, val)
     mydb.commit()
     print("the "+field+" has been updated\n")  

user_input_password = input("Enter the master password ")
if user_password == user_input_password :
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
         cmd1="select * from passwordmanager where weba = %s"
         email=str(input("Enter the website address\n"));
         val=(email,)
         mycursor.execute(cmd1,val)
         myresult=mycursor.fetchall()
         num=0
         print("the number of results are:" + str(len(myresult)))
         for x in myresult:
            num = num+1
            print(str(num))
            print(x[0])
            print("the website is : " + x[1])
            print("the username is : "+ x[2])
            print("the emailid is : " + x[3])
            print("the password is : " + x[4] + "\n")
         
      if user_choice ==4 :
         print("Enter the website address or any information regarding the record\n")
         delete =str(input())
         a=number_of_records(delete)
         if a>1:
            print("the number of the multiple records is",str(a))   
            print("there are " + str(a) + " identical records so please provide more info regarding your email address")
            deletee = input()
            sql="delete from passwordmanager where emailid = %s and weba = %s"
            val =(deletee,delete)
            mycursor.execute(sql,val)
            mydb.commit()
            print("the record has been deleted ")
               
         elif a == 1 :
            sql = "delete from passwordmanager where weba= %s"
            val =(delete,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("the record has been deleted\n") 
         else :
            print("There are no records with specified names sorry!")
                   
      if user_choice == 5:
         print("enter the website address\n")
         website=input()
         a= number_of_records(website)
         if a>1:
          print("Since there are multiple records please provide the email address")
          emailid=input()
          print("select fromt the following\n 1. update website name \n 2. update username \n 3. update password \n 4. update email address \n")
          choice=int(input())
          if choice==1:
              print("enter the updated website address\n")
              newwebsite = input()
              updatedata(newwebsite,website,emailid,"weba")
              
          if choice == 2:
              print("enter the updated username \n")
              newusername =input()
              updatedata(newusername,website,emailid,"username")          
          if choice == 3:
              print("enter the updated password\n")
              newpassword =input()
              updatedata(newpassword,website,emailid,"password")
              
          if choice == 4 :
              print("enter the updated email address\n")
              newemail =input()
              updatedata(newemail,website,emailid,"emailid")
              
         if a==1:    
          print("select fromt the following\n 1. update website name \n 2. update username \n 3. update password \n 4. update email address \n")
          choice=int(input())
          if choice==1:
              print("enter the updated website address\n")
              newwebsite = input()
              sql="update passwordmanager SET weba = %s where weba =%s"
              val=(newwebsite, website)
              mycursor.execute(sql, val)
              mydb.commit()
              print("the website name has been updated\n")
              
          if choice == 2:
              print("enter the updated username \n")
              newusername =input()
              sql="update passwordmanager SET username = %s where weba=%s"
              val=(newusername, website)
              mycursor.execute(sql, val)
              mydb.commit()
              print("the username has been updated\n")
          
          if choice == 3:
              print("enter the updated password\n")
              newpassword =input()
              sql="update passwordmanager SET password = %s where weba = %s"
              val=(newpassword, website)
              mycursor.execute(sql, val)
              mydb.commit()
              print("the password has been updated\n")
          if choice == 4 :
              print("enter the updated email address\n")
              newemail =input()
              sql="update passwordmanager SET emailid = %s where weba = %s"
              val=(newemail, website)
              mycursor.execute(sql, val)
              mydb.commit()
              print("the email address has been updated\n")  
              

        

      if user_choice == 6:
         break;
         break;
else:
   print("You are an theif !")
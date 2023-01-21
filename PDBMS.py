from datetime import date
def start():
  global mydb
  global mycursor
  import mysql.connector
  mydb=mysql.connector.connect(host='localhost',\
                              user='root',\
                              passwd='8933',\
                              database='policerecord')
  mycursor=mydb.cursor()

def firt():
  start()
  from datetime import date
  k=date.today()
  q="select * from casedetails where DOC='{}'".format(k)
  mycursor.execute(q)
  results=mycursor.fetchall()
  if len(results)==0:
    print('NO CASES TODAY')
  else:
    for row in results :
      print('..............')
      print('STATION:',row[10])
      print('CASE NO :',row[0])
      print('ACCUSED NAME:',row[1])
      print('AADHAR NO:',row[5])
      print('VICTIM NAME:',row[7])
      print('INVESTIGATION OFFICER:',row[9])
      print('CASE STATUS:',row[14])
      print('CRIME CATEGORY:',row[15])
      print('ACCUSED STATUS:',row[16])
      print('...............')
    print('TOTAL CASES TODAY:',len(results))
  print('...............')
     
def accused():
    start()
    q="select * from casedetails"
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('................')
    for row in results:
       print('CASE NO :',row[0])
       print('AADHAR NO:',row[5])
       print('ACCUSED NAME :',row[1])
       print('.........................')  
    mydb.commit()
    mycursor.close()
    
def victim():
    start()
    q="select * from victimlist"
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('...................')
    for row in results:
       print('CASE NO :',row[0])
       print('VICTIM NAME :',row[1])
       print('VICTIMS AADHARNO:',row[3])
       print('ALIVEorDEAD:',row[5])
       print('.........................')  
    mydb.commit()
    mycursor.close()

def emplist():
    start()
    q="select* from employeelist"
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('.................')
    for row in results:
       print('EMPLOYEE NO :',row[0])
       print('EMPLOYEE NAME :',row[1])
       print('DESIGNATION :',row[3])
       print('SALARY :',row[4])
       print('STATION :',row[5])
       print('AADHAR NO :',row[2])
       print('CASE ON DUTY :',row[6])
       print('.........................')  
    mydb.commit()
    mycursor.close()

def deleteemp():
    start()
    e=int(input('ENTER EMPID:'))
    q="DELETE FROM EMPLOYEELIST WHERE EMPID='{}'".format(e)
    mycursor.execute(q)
    mydb.commit()
    mycursor.close()
    print('Successfully deleted employee :',e)
    
def addemp():
    start()
    E=int(input('Enter the Employee ID:'))
    N=input('Enter the Employees Name:')
    Ad=int(input('Enter Employees AdharNo :'))
    D=input('Enter the Designation:')
    S=input('Enter the Salary:')
    St=input('Enter the Station:')
    c=int(input('Enter Employees Current Case:'))
    mycursor=mydb.cursor()
    mycursor.execute("insert into employeelist values('{}','{}','{}','{}','{}','{}','{}')".format(E,N,Ad,D,S,St,c))
    mydb.commit()
    mycursor.close()
    print(E,':Employee added successfully')

def getcase():
    start()
    q="select * from casedetails"
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('..................')
    for row in results:
            print('CASE NO :',row[0])
            print('FATHERS NAME:',row[2])
            print('ACCUSED NAME:',row[1])
            print('ADDRESS:',row[3])
            print('DOB:',row[4])
            print('AADHAR NO:',row[5])
            print('CONTACT NO:',row[6])
            print('VICTIM NAME:',row[7])
            print('VICTIMs AADHAR NO:',row[8])
            print('INVESTIGATION OFFICER:',row[9])
            print('STATION:',row[10])
            print('EYE WITNESS:',row[11])
            print('EVIDENCES COLLECTED:',row[12])
            print('SECTIONS VIOLATED:',row[13])
            print('CASE STATUS:',row[14])
            print('CRIME CATEGORY:',row[15])
            print('ACCUSED STATUS:',row[16])
            print('DATE OF CRIME:',row[17])
            print('..........................')
    print('TOTAL CASEs REGISTERED =',mycursor.rowcount)
    mydb.commit()
  
def searchemp():
  while True :
      start()
      print('                                         +++SEARCH EMPLOYEE BY+++')
      print('                                            1.CASE')
      print('                                            2.EMPLOYEE ID')
      print('                                            3.DESIGNATION')
      print('                                            4.BACK TO MENU')
      print('                                              +++++++ ')
      o=int(input('CHOOSE AN OPTION:'))
      if o==1:
        C=int(input('ENTER CASENO:'))
        q='select * from employeelist where caseno="{}"'.format(C)
        mycursor.execute(q)
        results=mycursor.fetchall()
        for row in results :
                print('EMPID:',row[0])
                print('EMPLOYEE NAME:',row[1])
                print('EMPLOYEE AADHARNO:',row[2])
                print('DESIGNATION:',row[3])
                print('SALARY:',row[4])
                print('STATION:',row[5])
                print('........................')
        mydb.commit()
        mycursor.close()
      elif o==2:
        C=int(input('ENTER EMPID:'))
        q='select * from employeelist where EMPID="{}"'.format(C)
        mycursor.execute(q)
        results=mycursor.fetchall()
        for row in results :
                print('EMPLOYEE NAME:',row[1])
                print('EMPLOYEE AADHARNO:',row[2])
                print('DESIGNATION:',row[3])
                print('SALARY:',row[4])
                print('STATION:',row[5])
                print('CASE NO :',row[6])
                print('........................')
        mydb.commit()
        mycursor.close()
      elif o==3:
        C=input('ENTER EMPLOYEEs DESIGNATION:')
        q="select * from employeelist where DESIGNATION='{}'".format(C)
        mycursor.execute(q)
        results=mycursor.fetchall()
        for row in results :
                print('CASE NO:',row[0])
                print('EMPLOYEE NAME:',row[1])
                print('EMPLOYEE AADHAR NO:',row[2])
                print('SALARY:',row[4])
                print('STATION:',row[5])
                print('CASE NO :',row[6])
                print('........................')
        mydb.commit()
        mycursor.close()
      elif o==4:
        break 
      else:
       print('CHOOSE A VALID OPTION')
  
def criminal():
    start()
    k=input("ENTER CRIMINAL NAME:")
    q="select * from casedetails where ACCUSED_NAME ='{}'".format(k)
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('..................')
    for row in results:
            print('CASE NO :',row[0])
            print('STATION:',row[10])
            print('CASE STATUS:',row[14])
            print('CRIME CATEGORY:',row[15])
            print('ACCUSED STATUS:',row[16])
            print('DATE OF CRIME:',row[17])
            print('.........................') 
    mydb.commit()
    mycursor.close()
        
def updateemp():
  while True :
        start()
        E=int(input('ENTER EMPID:'))
        print('                                +++UPDATE EMPLOYEE+++')
        print('                                    1.STATION')
        print('                                    2.CASE')
        print('                                    3.SALARY')
        print('                                    4.BACK TO MENU')
        print('                                     +++++++')
        o=int(input('CHOOSE AN OPTION:'))
        if o==1:
            St=input('ENTER NEW STATION:')
            q="update employeelist set station='{}' where empid='{}'".format(St,E)
            mycursor.execute(q)
            mydb.commit()
            mycursor.close()
            print('Successfully updated employee:',E)
        elif o==2:
            C=int(input('ENTER NEW CASENO:'))
            q="update employeelist set caseno='{}' where empid='{}'".format(C,E)
            mycursor.execute(q)
            mydb.commit()
            mycursor.close()
            print('Successfully updated employee:',E)
        elif o==3:
            S=input('ENTER NEW SALARY:')
            q="update employeelist set salary='{}' where empid='{}'".format(S,E)
            mycursor.execute(q)
            mydb.commit()
            mycursor.close()
            print('Successfully updated employee:',E)
        elif o==4:
          break
        else:
            print('ENTER A VALID OPTION')
  
def searchcase():
    while True:
           start()
           print('                                   +++SEARCH CASES BY+++')
           print('                                       1.DATE OF CRIME')
           print('                                       2.VICTIM')
           print('                                       3.CRIME CATEGORY')
           print('                                       4.SOLVED CASES')
           print('                                       5.PENDING CASES')
           print('                                       6.CASES IN PROGRESS')
           print('                                       7.CASE NO')
           print('                                       8.BACK TO MENU')
           print('                                         ++++++++++')
           o=int(input('CHOOSE AN OPTION:'))
           if o==1:
                c=input('ENTER DATE OF CRIME:')
                q="select * from casedetails where DOC='{}'".format(c)
                mycursor.execute(q)
                results=mycursor.fetchall()
                print('......................')
                for row in results:
                    print('CASE NO :',row[0])
                    print('FATHERS NAME:',row[2])
                    print('ACCUSED NAME:',row[1])
                    print('ADDRESS:',row[3])
                    print('DOB:',row[4])
                    print('AADHAR NO:',row[5])
                    print('CONTACT NO:',row[6])
                    print('VICTIM NAME:',row[7])
                    print('VICTIMs AADHAR NO:',row[8])
                    print('INVESTIGATION OFFICER:',row[9])
                    print('STATION:',row[10])
                    print('EYE WITNESS:',row[11])
                    print('EVIDENCES COLLECTED:',row[12])
                    print('SECTIONS VIOLATED:',row[13])
                    print('CASE STATUS:',row[14])
                    print('CRIME CATEGORY:',row[15])
                    print('ACCUSED STATUS:',row[16])
                    print('.........................')
                mydb.commit()
                mycursor.close()
           elif o==2:
                vn=input('ENTER VICTIM NAME:')
                q="select * from casedetails where victim_NAME='{}'".format(vn)
                mycursor.execute(q)
                results=mycursor.fetchall()
                print('......................')
                for row in results:
                            print('CASE NO :',row[0])
                            print('FATHERS NAME:',row[2])
                            print('ACCUSED NAME:',row[1])
                            print('ADDRESS:',row[3])
                            print('DOB:',row[4])
                            print('AADHAR NO:',row[5])
                            print('CONTACT NO:',row[6])
                            print('VICTIMs AADHAR NO:',row[8])
                            print('INVESTIGATION OFFICER:',row[9])
                            print('STATION:',row[10])
                            print('EYE WITNESS:',row[11])
                            print('EVIDENCES COLLECTED:',row[12])
                            print('SECTIONS VIOLATED:',row[13])
                            print('CASE STATUS:',row[14])
                            print('CRIME CATEGORY:',row[15])
                            print('ACCUSED STATUS:',row[16])
                            print('DATE OF CRIME:',row[17])
                            print('.........................')
                mydb.commit()
                mycursor.close()
           elif o==3:
                    c=input('ENTER CRIME CATEGORY:')
                    q="select * from casedetails where CRIME_CATEGORY='{}'".format(c)
                    mycursor.execute(q)
                    results=mycursor.fetchall()
                    print('......................')
                    for row in results:
                        print('CASE NO :',row[0])
                        print('FATHERS NAME:',row[2])
                        print('ACCUSED NAME:',row[1])
                        print('ADDRESS:',row[3])
                        print('DOB:',row[4])
                        print('AADHAR NO:',row[5])
                        print('CONTACT NO:',row[6])
                        print('VICTIM NAME:',row[7])
                        print('VICTIMs AADHAR NO:',row[8])
                        print('INVESTIGATION OFFICER:',row[9])
                        print('STATION:',row[10])
                        print('EYE WITNESS:',row[11])
                        print('EVIDENCES COLLECTED:',row[12])
                        print('SECTIONS VIOLATED:',row[13])
                        print('CASE STATUS:',row[14])
                        print('ACCUSED STATUS:',row[16])
                        print('DATE OF CRIME:',row[17])
                        print('.........................')
                    mydb.commit()
                    mycursor.close()
           elif o==4:
                    q="select * from casedetails where case_status='SOLVED'"
                    mycursor.execute(q)
                    results=mycursor.fetchall()
                    print('......................')
                    for row in results:
                        print('CASE NO :',row[0])
                        print('FATHERS NAME:',row[2])
                        print('ACCUSED NAME:',row[1])
                        print('ADDRESS:',row[3])
                        print('DOB:',row[4])
                        print('AADHAR NO:',row[5])
                        print('CONTACT NO:',row[6])
                        print('VICTIM NAME:',row[7])
                        print('VICTIMs AADHAR NO:',row[8])
                        print('INVESTIGATION OFFICER:',row[9])
                        print('STATION:',row[10])
                        print('EYE WITNESS:',row[11])
                        print('EVIDENCES COLLECTED:',row[12])
                        print('SECTIONS VIOLATED:',row[13])
                        print('ACCUSED STATUS:',row[16])
                        print('CRIME CATEGORY:',row[15])
                        print('DATE OF CRIME:',row[17])
                        print('.........................')
                    mydb.commit()
                    mycursor.close()
           elif o==5:
                    q="select * from casedetails where case_status='PENDING'"
                    mycursor.execute(q)
                    results=mycursor.fetchall()
                    print('......................')
                    for row in results:
                        print('CASE NO :',row[0])
                        print('FATHERS NAME:',row[2])
                        print('ACCUSED NAME:',row[1])
                        print('ADDRESS:',row[3])
                        print('DOB:',row[4])
                        print('AADHAR NO:',row[5])
                        print('CONTACT NO:',row[6])
                        print('VICTIM NAME:',row[7])
                        print('VICTIMs AADHAR NO:',row[8])
                        print('INVESTIGATION OFFICER:',row[9])
                        print('STATION:',row[10])
                        print('EYE WITNESS:',row[11])
                        print('EVIDENCES COLLECTED:',row[12])
                        print('SECTIONS VIOLATED:',row[13])
                        print('ACCUSED STATUS:',row[16])
                        print('CRIME CATEGORY:',row[15])
                        print('DATE OF CRIME:',row[17])
                        print('.........................')
                    mydb.commit()
                    mycursor.close()
           elif o==6:
                    q="select * from casedetails where case_status='PROGRESS'"
                    mycursor.execute(q)
                    results=mycursor.fetchall()
                    print('......................')
                    for row in results:
                        print('CASE NO :',row[0])
                        print('FATHERS NAME:',row[2])
                        print('ACCUSED NAME:',row[1])
                        print('ADDRESS:',row[3])
                        print('DOB:',row[4])
                        print('AADHAR NO:',row[5])
                        print('CONTACT NO:',row[6])
                        print('VICTIM NAME:',row[7])
                        print('VICTIMs AADHAR NO:',row[8])
                        print('INVESTIGATION OFFICER:',row[9])
                        print('STATION:',row[10])
                        print('EYE WITNESS:',row[11])
                        print('EVIDENCES COLLECTED:',row[12])
                        print('SECTIONS VIOLATED:',row[13])
                        print('ACCUSED STATUS:',row[16])
                        print('CRIME CATEGORY:',row[15])
                        print('DATE OF CRIME:',row[17])
                        print('.........................')
                    mydb.commit()
                    mycursor.close()
           elif o==7:
                    c=int(input('ENTER CASENO:'))
                    q="select * from casedetails where CASENO='{}'".format(c)
                    mycursor.execute(q)
                    results=mycursor.fetchall()
                    print('......................')
                    for row in results:
                        print('CASE NO :',row[0])
                        print('FATHERS NAME:',row[2])
                        print('ACCUSED NAME:',row[1])
                        print('ADDRESS:',row[3])
                        print('DOB:',row[4])
                        print('AADHAR NO:',row[5])
                        print('CONTACT NO:',row[6])
                        print('VICTIM NAME:',row[7])
                        print('VICTIMs AADHAR NO:',row[8])
                        print('INVESTIGATION OFFICER:',row[9])
                        print('STATION:',row[10])
                        print('EYE WITNESS:',row[11])
                        print('EVIDENCES COLLECTED:',row[12])
                        print('SECTIONS VIOLATED:',row[13])
                        print('CASE STATUS:',row[14])
                        print('CRIME CATEGORY:',row[15])
                        print('ACCUSED STATUS:',row[16]) 
                        print('DATE OF CRIME:',row[17])
                        print('.........................')
                    mydb.commit()
                    mycursor.close()
           elif o==8:
                 break
           else:
                 print('CHOOSE A VALID OPTION')
                      
def filefir():
  start()
  C=int(input('ENTER CASENO:'))
  AN=input('ENTER ACCUSED NAME:')
  FA=input('ENTER ACCUSED FATHERs NAME')
  AA=input('ENTER ACCUSED ADDRESS:')
  DOB=input('ENTER ACCUSED DOB:')
  AD=int(input('ENTER ACCUSED AADHAR NO:'))
  CN=int(input('ENTER ACCUSED CONTACT NO:'))
  VN=input('ENTER VICTIMs NAME:')
  VAD=int(input('ENTER VICTIMs AADHAR NO:'))
  E=int(input('ENTER EMPID OF OFFICER:'))
  S=input('ENTER STATION:')
  EW=int(input('ENTER NO OF EYE WITNESSES:'))
  EV=input('ENTER EVIDENCES COLLECTED:')
  SEC=input('ENTER SECTIONS VIOLATED:')
  CS=input('ENTER CASE STATUS:')
  CC=input('ENTER CRIME CATERGORY:')
  AS=input('ENTER STATUS OF ACCUSED')
  DOC=input('ENTER DATE OF CRIME:')
  VA=input('ENTER VICTIMs ADDRESS:')
  VDOB=input('ENTER VICTIMS DOB:')
  AoD=input('ENTER ALIVE or DEAD:')
  q1="insert into casedetails values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(C,AN,FA,AA,DOB,AD,CN,VN,VAD,E,S,EW,EV,SEC,CS,CC,AS,DOC)
  q2="insert into victimlist values('{}','{}','{}','{}','{}','{}')".format(C,VN,VAD,VA,VDOB,AoD)
  mycursor.execute(q1)
  mycursor.execute(q2)
  print('CASE FILED SUCCESSFULLY')
  mydb.commit()
  mycursor.close()
  
def empst():
  start()
  q="select * from employeelist where station='{}'".format(S)
  mycursor.execute(q)
  results=mycursor.fetchall()
  print('.................')
  for row in results:
    print('EMPID:',row[0])
    print('EMPLOYEE NAME:',row[1])
    print('EMPLOYEE AADHAR NO:',row[2])
    print('DESIGNATION:',row[3])
    print('SALARY:',row[4])
    print('CASE NO:',row[6])
    print('...........................')
  mycursor.close()
  mydb.commit()
            
def victimst():
    start()
    q="select CASENO,VICTIM_NAME from casedetails where station='{}'".format(S)
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('...............')
    for row in results:
       print('CASE NO :',row[0])
       print('VICTIM NAME :',row[1])
       print('.........................')  
    mydb.commit()
    mycursor.close()

def stgetcase():
  start()
  q="select * from casedetails where station='{}'".format(S)
  mycursor.execute(q)
  results=mycursor.fetchall()
  if len(results)==0:
      print("NO CASES TODAY")
  else:
   for row in results:
    print('CASE NO :',row[0])
    print('ACCUSED NAME:',row[1])
    print('FATHERS NAME:',row[2])
    print('ADDRESS:',row[3])
    print('DOB:',row[4])
    print('AADHAR NO:',row[5])
    print('CONTACT NO:',row[6])
    print('VICTIM NAME:',row[7])
    print('VICTIMs AADHAR NO:',row[8])
    print('INVESTIGATION OFFICER:',row[9])
    print('EYE WITNESS:',row[11])
    print('EVIDENCES COLLECTED:',row[12])
    print('SECTIONS VIOLATED:',row[13])
    print('CASE STATUS:',row[14])
    print('CRIME CATEGORY:',row[15])
    print('ACCUSED STATUS:',row[16])
    print('DATE OF CRIME:',row[17])
    print('.........................') 
   print('TOTAL CASES IN STATION = ', len(results))
  mydb.commit()
  mycursor.close()       
     
def staccused():
    start()
    q="select * from casedetails where station='{}'".format(S)
    mycursor.execute(q)
    results=mycursor.fetchall()
    print('..............')
    for row in results:
       print('CASE NO :',row[0])
       print('AADHAR NO:',row[5])
       print('ACCUSED NAME :',row[1])
       print('.........................')  
    mydb.commit()
    mycursor.close()        
    
def graph():
    import matplotlib.pyplot as plt
    import numpy as np
    c=[]
    d=[]
    start()
    q=("select DOC,count(DOC) from casedetails group by DOC ")
    mycursor.execute(q)
    results=mycursor.fetchall()
    for row in results:
        c.append(row[0])
        d.append(row[1])
    print(c)
    print(d)
    plt.plot(c,d)
    plt.xlabel('DOC')
    plt.ylabel('NO OF CASEES:')
    plt.title('CRIME RATING')
    plt.show()
    mydb.commit()
    mycursor.close()    
            
def firstation():
    start()
    k=date.today()
    q="select*from casedetails where station='{}' and DOC='{}'".format(S,k)
    mycursor.execute(q)
    results=mycursor.fetchall()
    if len(results)==0:
        print('NO CASE FILLED TODAY')
    else:
        for row in results:
            print('CASE NO :',row[0])
            print('FATHERS NAME:',row[2])
            print('ACCUSED NAME:',row[1])
            print('ADDRESS:',row[3])
            print('DOB:',row[4])
            print('AADHAR NO:',row[5])
            print('CONTACT NO:',row[6])
            print('VICTIM NAME:',row[7])
            print('VICTIMs AADHAR NO:',row[8])
            print('INVESTIGATION OFFICER:',row[9])
            print('STATION:',row[10])
            print('EYE WITNESS:',row[11])
            print('EVIDENCES COLLECTED:',row[12])
            print('SECTIONS VIOLATED:',row[13])
            print('CASE STATUS:',row[14])
            print('CRIME CATEGORY:',row[15])
            print('ACCUSED STATUS:',row[16])
            print('DATE OF CRIME:',row[17])
            print('.........................') 
    mydb.commit()
    mycursor.close()   
    
def updatecasestatus():
            start()
            C=int(input('ENTER CASENO:'))
            E=input('ENTER NEW CASE STATUS:')
            q="update casedetails set case_status='{}' where caseno={}".format(E,C)
            mycursor.execute(q)
            mydb.commit()
            mycursor.close()
            print("CASE STATUS UPDATED")

def criminalstation():
    start()
    d=input('ENTER STATION NAME:')
    q='select caseno,accused_name from casedetails where station="{}"'.format(d)
    mycursor.execute(q)
    results=mycursor.fetchall()
    if len(results)==0:
        print('NO CASE FILLED TODAY')
    else:
        for row in results:
            print('CASE NO :',row[0])
            print('CRIMINAL NAME:',row[1])
    mydb.commit()
    mycursor.close() 

c='y'
while c=='y':
        print('******POLICE RECORD MANAGEMENT SYSTEM******')
        print("       ****MAIN MENU****")
        print('         1.HEADQUATERS LOGIN')
        print('         2.STATION LOGIN')
        print('         3.EXIT')
        print('          *******')
        pH='bharath'
        pS='alan'
        m=int(input('CHOOSE AN OPTION:'))
        if m==1:
            P=input('ENTER THE PASSWORD:')
            while P==pH:
                print("             *****HEADQUATERS LOGIN****")
                print('                1.FIRs FILLED TODAY')
                print("                2.EMPLOYEE LIST")
                print("                3.REGISTERED CASES")
                print('                4.SEARCH FOR A CASE')
                print('                5.ACCUSED LIST')
                print('                6.VICTIM LIST')
                print('                7.SEARCH FOR A CRIMINAL')
                print('                8.GRAPH')
                print("                9.LOGOUT")
                print('                  ***********')
                h=int(input('Choose an Option:'))
                if h==1:
                    firt()
                elif h==2:
                    while True:
                        print('                 +++EMPLOYEE LIST+++')
                        print('                   1.ALL EMPLOYEES')
                        print('                   2.SEARCH AN EMPLOYEE')
                        print('                   3.UPDATE  EMP DATA')
                        print('                   4.ADD AN EMPLOYEE')
                        print('                   5.DELETE EMPLOYEE DETAILS')
                        print('                   6.BACK TO HQ MAIN')
                        print('                     ++++++++++++++')                  
                        e=int(input('CHOOSE AN OPTION:'))
                        if e==1:
                            emplist()
                        elif e==2:
                            searchemp()
                        elif e==3:
                            updateemp()
                        elif e==4:
                            addemp()
                        elif e==5:
                            deleteemp()
                        elif e==6:
                            break
                        elif e>6:
                            print('ENTER A VALID OPTION')    
                elif h==3:
                    getcase()  
                elif h==4:
                    searchcase()
                elif h==5:
                    accused()
                elif h==6:
                    victim()
                elif h==7:
                    criminal()
                elif h==8:
                    graph()
                elif h==9:
                    break
                else:
                    print('ENTER A VALID OPTION') 
            else:
                print('WRONG PASSWORD!')             
        if m==2 :
            S=input('ENTER YOUR STATION:')
            P=input("ENTER THE PASSWORD:")
            if P==pS:
              while True:
                print("           *****STATION LOGIN*****")
                print('             1.FILE AN FIR')
                print('             2.FIRS FILLED TODAY')
                print('             3.REGISTERED CASES')
                print('             4.EMPLOYEES IN STATION')
                print('             5.CRIMINAL LIST OF STATION')
                print('             6.VICTIM LIST')
                print('             7.ACCUSED LIST')
                print('             8.UPDATE CASE DETAILS')
                print('             9.LOGOUT')
                print('                **********')
                s=int(input('CHOOSE AN OPTION:'))
                if s==1:
                    filefir()
                elif s==2:
                    firstation()
                elif s==3:
                    stgetcase()
                elif s==4:
                    empst()
                elif s ==5:
                    criminalstation()
                elif s==6:
                    victimst()
                elif s==7:
                    staccused()
                elif s==8:
                    updatecasestatus()
                elif s==9:
                    break
                else :
                    print('ENTER A VALID OPTION')      
            else:
                print('WRONG PASSWORD!')
        if m==3 :
            print("""                                                                        DEVELOPED AND MANAGED BY : ALAN & BHARATH""")
            break      
        elif m>3:
            print('ENTER A VALID OPTION')

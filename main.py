from getpass import getpass
import os 
import emp_lib as emp
import cus_lib as cus
import GUI as g



#___________________________________________________AUTHENTICATION_________________________________________________________________________________________

def auth():
 while True:    
  pas=getpass(g.password) 

  if pas=="amith":
    print(g.login)  
    main()
  else:
   print("""
   ***INCORRECT PASSWORD TRY AGAIN***
   """)
#________________________________________________________MAIN_EMPLOYEE_____________________________________________________________________________________
def main():
  while True:
   os.system("cls")
   print(g.spl_scr2)
   i=input(g.sel_opt)
   
   if i=='1':
     emp.search()
   elif i=='2':
     emp.ad()
   elif i=='3':
     emp.dl()
   elif i=='4':
     spl() 
   else:
     print(g.vld_opt)
  
#_______________________________________________________MAIN_CUSTOMER____________________________________________________________________________________________________
def main_cus():
  while True:
   os.system("cls")
   print(g.spl_scr2)
   i=input(g.sel_opt_cus)
   
   if i=='1':
     emp.search()
   elif i=='2':
     cus.check_out()
   elif i=='3':
     cus.check_in()
   elif i=='4':
     spl() 
   else:
     print(g.vld_opt)   

#______________________________________________________SPLASH-SCRN_____________________________________________________________________________________
def spl():
 os.system("cls")
 print(g.sp_scr)
 while True:

   i=input(g.e_c)
   
   if i=='1':
     auth()
     break
   elif i=='2':
     main_cus()
     break  
   else:
     print(g.vld_opt)
spl()

    

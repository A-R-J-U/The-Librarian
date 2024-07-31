import os
import GUI as g
import csv

#_______________________________________________________CHECK-OUT____________________________________________________________________
def check_out():
 while True :
   t=input(g.nm_bk).lower()
   dat=[]
   with open("library.csv", "r",newline='') as lib:  
      robj=csv.reader(lib)
      for k in robj:
           dat.append(k)
      lib.seek(0)
      nm=[x[0] for x in dat]
      
      if t in nm :
        n=input(g.yr_nam).lower()    
        e=[]
        for k in robj:
          if k[0]==t:
            k[3]=n
          e.append(k)
        with open('library.csv','w',newline='') as lib:
          wobj=csv.writer(lib)
          wobj.writerows(e)

        print(g.ck_suc)       
        return
      else :
        print("""
    ***BOOK NOT IN LIBRARY***
    """)
        while True :
         i=input(g.ck_ag).lower()
         if i=='y':
            break       
         elif i=='n':
           return         
         else:
          print("""
      ***INVAID INPUT***
      """)
      
 

#_____________________________________________________CHECK-IN___________________________________________________________________________________

def check_in():
 while True :
   t=input(g.nm_bk).lower()
   dat=[]
   with open("library.csv", "r",newline='') as lib:  
      robj=csv.reader(lib)
      for k in robj:
           dat.append(k)
      lib.seek(0)
      nm=[x[0] for x in dat]
      
      if t in nm :
        n=input(g.en_shl).lower()    
        e=[]
        for k in robj:
          if k[0]==t:
            k[3]='0'
            k[2]=n
          e.append(k)
        with open('library.csv','w',newline='') as lib:
          wobj=csv.writer(lib)
          wobj.writerows(e)

        print(g.ci_suc)       
        break
      else :
        print("""
    ***BOOK NOT IN LIBRARY***
    """)
        while True :
         i=input(g.ck_ag).lower()
         if i=='y':
            break       
         elif i=='n':
           return
         else:
          print("""
      ***INVAID INPUT***
      """)      


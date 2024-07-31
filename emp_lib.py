
import csv 
import GUI as g

 #_______________________________________________________Search____________________________________________________________
def search():
   def sg():
     while True :
      i=input(g.search_again).lower()
      if i=='y':
       search()
       break 
      elif i=='n':        
       return       
      else:
       print(g.in_err)
   print(g.shel)    
   bk=input(g.name_book).lower()
   dat=[]
   with open("library.csv", "r",newline='') as lib:  
       robj=csv.reader(lib)
       for k in robj:
           dat.append(k)
   nm=[ x[0] for x in dat]   
   if bk in nm :
     for x in range(0,len(dat)):
       if bk==dat[x][0]:

         if dat[x][3]=='0':
           print(g.room_no,dat[x][1])
           print(g.shelf_pos,dat[x][2] )
           sg()
         else:
           print (g.bk_taken,dat[x][3]) 
           sg()
   else :
    print("""
    ***BOOK NOT IN LIBRARY***
    """)
    sg()
            
  
 #__________________________________________________________Addition________________________________________________________           
def ad():
  with open('library.csv','a',newline='') as lib :
   wobj=csv.writer(lib)
   
   row=list()
   try:
    n=int(input(g.Hm_en))

    for i in range(n):
        
      N=input(g.nm_bk).lower()
      r=int(input(g.en_rmn))
      sp=input(g.en_shl)
      lc="0"
      entry=[N,r,sp,lc]
      row.append(entry)
   except ValueError:
     print(g.in_err)
     ad()  
   wobj.writerows(row)
  print(g.bk_suc)
  return
  
 #_____________________________________________________REMOVAL____________________________________________________________  
def dl():
    def sd():
     while True :
      i=input(g.rm_ag).lower()
      if i=='y':
       dl()
       break 
      elif i=='n':
       return
      else:
       print(g.in_err)
    li=[]

    t=input(g.nb_dl).lower()

    with open('library.csv','r',newline='') as lib:
     robj=csv.reader(lib)

     for row in robj:
        li.append(row)

        for field in row:

            if field==t:
                li.remove(row)
    lib.close()

    with open('library.csv','w',newline='') as lib :

        wobj=csv.writer(lib)
        wobj.writerows(li)
    lib.close()

    print(g.rm_sc)
    sd()     


search_again="""+---------------------------+
|    SEARCH AGAIN ? (Y/N)   |
+---------------------------+ >> """

e_c="""+------------------------------------------------+
|     EMPLOYEE MODE[1]--(or)CUSTOMER MODE[2]     |
+------------------------------------------------+ >> """

name_book="""+-------------------------------+
|     ENTER NAME OF THE BOOK    |
+-------------------------------+ >> """

room_no="""+------------------------+
| THE BOOK IS IN ROOM NO |
+------------------------+ >>"""

shelf_pos="""+------------------------+
|   SHELF AND POSITION   |
+------------------------+ >>"""                  

bk_taken="""+------------------------+
|  THE BOOK IS TAKEN BY  |
+------------------------+ >>"""

Hm_en="""+------------------------+
|    HOW MANY ENTRIES    |
+------------------------+ >> """

nm_bk="""+------------------------+
|   NAME OF THE BOOK     |
+------------------------+ >> """         

en_rmn="""+------------------------+
|   ENTER THE ROOM NO    |
+------------------------+ >> """         

en_shl="""+------------------------------+
| ENTER THE SHELF AND POSITION |
+------------------------------+ >> """

bk_suc="""
.-/|                  \ /                  |\-.
||||                   |                   ||||
||||                   |       ~~*~~       ||||
|||| |   THE BOOK   |  |                   ||||
|||| |     WAS      |  |                   ||||
|||| |    ADDED     |  |                   ||||
|||| |  SUCESSFULLY |  |     --==*==--     ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||__________________ | __________________||||
||/===================\|/===================\||
`--------------------~___~-------------------''"""

shel="""
_________________________________________________________
||-------------------------------------------------------||
||.--.    .-._                        .----.             ||
|||==|____| |H|___            .---.___|====|_____.--.___ ||
|||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
|||==|    | | |   | \         |   |   |_\/_|Black|  | ^ |||
|||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
|||  |    | | |   |_\ \_( oo )|   |   |    |Magus|  | ^ |||
|||==|====| |H|xxx|  \ \ |''| |+++|=-=|====|-=+=-|==|---|||
||`--^----'-^-^---'   `-' ==  '---^---^----^-----^--^---^||
||-------------------------------------------------------||
||-------------------------------------------------------||
||               ___                   .-.__.-----. .---.||
||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
||      _a'{ / (|===|+|   |++|  |==|   | |  |Illum| | R |||
||       '/\\/ _(|===|-|   |  |''|  |:x:|=|  |inati| | Y |||
||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
||-------------------------------------------------------||
||_______________________________________________________||
"""

rm_ag="""+---------------------------+
|    REMOVE AGAIN ? (Y/N)   |
+---------------------------+ >> """         

nb_dl="""+-----------------------------+
| NAME OF BOOK TO BE DELETED :|
+-----------------------------+ >> """

rm_sc="""
.-/|                  \ /                  |\-.
||||                   |                   ||||
||||                   |       ~~*~~       ||||
|||| |   THE BOOK   |  |                   ||||
|||| |     WAS      |  |                   ||||
|||| |    REMOVED   |  |                   ||||
|||| |  SUCESSFULLY |  |     --==*==--     ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||                   |                   ||||
||||__________________ | __________________||||
||/===================\|/===================\||
`--------------------~___~-------------------''"""

sel_opt="""         +-------------------------------+
         |       SELECT OPTION :         |
         +-------------------------------+
         | 1) Search For a Book          |
         | 2) Add a Book to Library      |
         | 3) Delete a Book From Library |
         | 4) Change Mode                |
         +-------------------------------+ >> """

sel_opt_cus="""         +-------------------------------+
         |       SELECT OPTION :         |
         +-------------------------------+
         | 1) Search For a Book          |
         | 2) Check Out Book             |
         | 3) Return Book                |
         | 4) Change Mode                |
         +-------------------------------+ >> """


password="""         +-----------------------+
         |   ENTER THE PASSWORD  |
         +-----------------------+ >>"""

login="""+------------------------+
|----LOGIN SUCCESSFUL----|
+------------------------+ """

yr_nam="""+-------------------------------+
|       ENTER YOUR NAME    :    |
+-------------------------------+ >> """         

ck_suc="""
        _________   _________
   ____/     690 \ /     700 \____
 /| ------------- |  ------------ |\
||| ------------- | ------------- |||
||| ------------- | ------------- |||
||| ------- ----- | ------------- |||
||| -----BOOOK----| ----HAPPY---- |||
||| --CHECKED-OUT-| ---READING----|||
||| -SUCCESSFULLY-| ----------    |||
||| ------------- |  ------------ |||
||| ------------- | ------------- |||
||| ------------- | ------ -----  |||
||| ------------  | ------------- |||
|||_____________  |  _____________|||
L/_____/--------\\_//W-------\_____\J"""    

ck_ag="""+--------------------+
|-----TRY AGAIN ?----|
+--------------------+ >>"""              

ci_suc="""       
        _________   _________
   ____/     420 \ /     421 \____
 /| ------------- |  ------------ |\
||| ------------- | ------------- |||
||| ------------- | ------------- |||
||| ------- ----- | ------------- |||
||| -----BOOOK----| --THANK YOU-- |||
||| --CHECKED-IN--| ----FOR-----  |||
||| -SUCCESSFULLY-| ---TIMELY---  |||
||| ------------- | ---RETURN---- |||
||| ------------- | ------------- |||
||| ------------- | ------ -----  |||
||| ------------  | ------------- |||
|||_____________  |  _____________|||
L/_____/--------\\_//W-------\_____\J""" 

in_err="""
      ***INVAID INPUT***
      """
vld_opt="""
     ***Please choose a valid option***
     """

sp_scr="""____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |"""


spl_scr2=""" ____________________________________________________
|____________________________________________________|
| __     __   ____   ___ ||  ____    ____     _  __  |
||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
||_______________________||__________________________|
| _____________________  ||      __   __  _  __    _ |
||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
|| | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
|____________________ /\~()/()~//\ __________________|
| __   __    _  _     \_  (_ .  _/ _      _     _____|
||~~|_|..|__| || |_ _   \ //\\ /  |=|_  /) |___| | | |
||--|+|^^|==|1||2| | |__/\ __ /\__| |(\/((\ +|+|=|=|=|
||__|_|__|__|_||_|_| /  \ \  / /  \_|_\___/|_|_|_|_|_|
|_________________ _/    \/\/\/    \_ /   /__________|
| _____   _   __  |/      \../      \/   /   __   ___|
||_____|_| |_|##|_||   |   \/ __\       /=|_|++|_|-|||
||______||=|#|--| |\   \   o     \_____/  |~|  | | |||
||______||_|_|__|_|_\   \  o     | |_|_|__|_|__|_|_|||
|_________ __________\___\_______|____________ ______|
|__    _  /    ________     ______           /| _ _ _|
|\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
| \/\ |*/  .//____// //   /__/__/ (_)      /  ||=|=|=|
|  \/\|/   /(____|/ //                    /  /||~|~|~|__
|___\_/   /________//   ________         /  / ||_|_|_|
|___ /   (|________/   |\_______\       /  /| |______|
    /                  \|________)     /  / | |
"""      
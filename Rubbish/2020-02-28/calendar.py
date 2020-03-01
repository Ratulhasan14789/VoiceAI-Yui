import datetime

allmonths=  [["January", "Jan", "01", "1", "one", "january", "jan"],["February", "Feb", "02", "2", "two", "february", "feb"], ["March", "Mar", "03", "3", "march", "mar"], ["April", "Apr", "04", "4", "april", "apr"], ["May", "may", "05", "5"], ["June", "Jun", "06", "6","june","jun"], ["July", "Jul", "07", "7", "july", "jul"], ["August", "Aug", "08", "8", "august", "aug"], ["September", "Sep", "09", "9", "september", "sep"], ["October", "Oct", "10", "ten", "october", "oct"], ["November", "Nov", "11", "noveember", "nov"], ["December", "Dec", "12", "december", "dec"]]

jan=allmonths[0]
feb=allmonths[1]
mar=allmonths[2]
apr=allmonths[3]
may=allmonths[4]
jun=allmonths[5]
jul=allmonths[6]
aug=allmonths[7]
sep=allmonths[8]
oct =allmonths[9]
nov=allmonths[10]
dec=allmonths[11]
leap=jan+feb
enmonth=jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
xday=jan+mar+may+jul+aug+oct+dec
yday=apr+jun+sep+nov
yes=["y","yes","yeah","Yes","Yeah","sure","Sure","ok","Ok","lets go","Lets go","let's go","Let's go","start","Start"]
no=["n","no","No","na","Na","nah","Nah","nope","Nope","stop","Stop","quit","Quit","exit","Exit"]
condition=yes+no
escape=["exit","close","shut down","quit"]
retry=1
reply=0
opt=0
year="ok"

while retry==1:
    while year=="ok":
        try:
            year=input("Enter the year (YYYY): ")
            if int(year)/1==int(year) or int(year)==0:
                year=int(year)
                while year<=0 or year>=10000:
                    print("I can't calculate before the year 1 or after 9999, yet.'")
                    year="ok"
        except:
            if year in escape:
                opt="quit"
                retry=0
            else:
                 print("**error_code:001**\nYou have entered an invalid year. Please re-enter the year in Number or digits.\nIf you wanna exit type: quit\n")
                 year="ok"
        
          
    if year not in escape:
        month=input("Enter the month (MM): ")

        if month in escape:
            break

        while month not in enmonth:
            print("**error_code:002**\nYou have entered an invalid month. Please ensure that the month is entered as name or number.")
            opt = input("1. Need help? Type: help\n2. Want to quit, type: quit\n3. Want to try again, just re-enter the month. ")
            if opt in escape:
                break
            elif opt in enmonth: month = opt
            elif opt == "help":
                print("Here are the options for the English Months: \n\nJanuary: ",jan,"\n\nFebruary: ",feb,"\n\nMarch: ",mar,"\n\nApril: ",apr,"\n\nMay: ",may,"\n\nJune:",jun,"\n\nJuly",jul,"\n\nAugust:",aug,"\n\nSeptember:",sep,"\n\nOctober: ",oct,"\n\nNovember: ",nov,"\n\nDecember: ",dec)

    day=1
    y0=year
    y1=y0//4
    
    x=0
    y=0
    z=0

    if month in jan: MM=1
    elif month in feb: MM=2
    elif month in mar: MM=3
    elif month in apr: MM=4
    elif month in may: MM=5
    elif month in jun: MM=6
    elif month in jul: MM=7
    elif month in aug: MM=8
    elif month in sep: MM=9
    elif month in oct: MM=10
    elif month in nov: MM=11
    else: MM=12
    name = datetime.datetime(year, MM, day)
    nod= int(name.strftime("%w"))
    xtab= 6-nod
    print(' Sat | Sun | Mon | Tue | Wed | Thu | Fri ')
    tab=(nod+1)%7
    print('      '*tab, end='')
    for i in range(1,10):
        print("  ",i,"   ",sep="",end="")
        if i%7==xtab: print()
    if month in xday: daterange=31
    elif month in feb:
        if y1==0: daterange=29
        else: daterange=28
    else: daterange=30
    for i in range(10,daterange+1):
        print(" ",i,"   ",sep="", end="")
        if i%7==xtab: print()
        
        retry=0
    print()
    reply=input("Wanna try again? ")

    while reply not in condition:
        try:
            if int(reply)/1==int(reply):
                year=int(reply)
                retry=1
                reply="y"
        except ValueError:
            print("I don't get it. Answer in yes or no")
            reply=input("Try to write clearly.  ")
    if reply in condition:
        if reply in yes and year!="ok":
             retry=1
             year="ok"
        elif reply in no or reply in escape:
             retry=0




print("\n\nBye!")

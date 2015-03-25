import sqlite3
import datetime
import balloontip as bt

t = datetime.datetime.now()

conn = sqlite3.connect('C:\\Users\\YourName\\bday.db')
c = conn.cursor()

qString = 'SELECT * FROM birthdays WHERE month IS '+ str(t.month) +' AND day IS ' + str(t.day)

try:
    btMessage = ""
    c.execute (qString)
    allrows = c.fetchall()
    if (allrows != None):
        for row in allrows:
            
            if (t.year-row[1] > 200):
                age = "N/A"
            else:
                age = str(t.year-row[1])

            btStr = ("Today is %s's birthday (%s years)" % (row[0], age))
            btMessage = btMessage + btStr + "\n"
    else:
        btMessage = ("No birthdays today :-( ")

except:
    e = sys.exc_info()[0]
    btMessage = ("Something went wrong!" % e )

bt.balloon_tip('Birthday notification', btMessage)

conn.close()

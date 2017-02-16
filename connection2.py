import sqlite3
import pandas as pd
import os

sqlitedb = 'viber_messages2'
#Messages table containing all of the messages
#_id = Message ID
#Address =
#Date = Date a message was sent, UNIX time, convert using http://www.epochconverter.com/ for human time.
#Read = 0 means read, 1 means unread.
#Opened = 0 means opened, 1 means unopened.
#Status =
#Type = 1 means it is sent from the phone you have gotten the database from 0 means it was sent to this phone.
#Body = Message sent.
#Number = contact number for saved contact
#Display_name = contacts display name on viber
#Contact_name = contact name for contact saved in the phone.
#Contact_id = ID which can be used to cross reference the contact in the messages table. The users phone will always be 0!!!!

#Connect to the Sqlite3 database
connect = sqlite3.connect(sqlitedb)
df = pd.read_sql_query("""SELECT m._id,m.body, participants_info.number, participants_info.display_name, participants_info._id
        FROM messages m, participants_info
        JOIN participants
        ON participants_info._id = participants.participant_info_id
        WHERE m.conversation_id IS NOT NULL;""", connect)
df.to_html(open('messages.html', 'w'))
base_filename = 'test.txt'
with open(os.path.join(base_filename),'w') as outfile:
        df.to_string(outfile)
print (df)

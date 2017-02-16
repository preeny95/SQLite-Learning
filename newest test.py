import sqlite3
import pandas as pd

conn = sqlite3.connect('viber_messages2')

cur = conn.cursor()
#Adapted from Stackoverflow.com by Parfait
cur.execute("""SELECT m._id, m.body, pp.number, pp.display_name, pp._id
        FROM messages m, participants p
        INNER JOIN participants_info pp
        ON m.participant_id = pp._id;""")

query = "SELECT m._id, m.date, m.body, m.conversation_id," + \
         "     pp.number, pp.display_name, pp._id" + \
         " FROM messages m, participants p" + \
         " INNER JOIN participants_info pp " + \
         "         ON m.participant_id = pp._id"
        # " WHERE m.conversation_id = ?"

with open('messages.html', 'w') as h, open('test.txt', 'w') as t:
    for convo in cur.fetchall():
        df = pd.read_sql_query(query, conn, params=convo)

        # HTML WRITE
        h.write(df.to_html())
        h.write('<br/>')

        # TXT WRITE
        t.write(df.to_string())
        t.write('\n\n')

cur.close()
conn.close()

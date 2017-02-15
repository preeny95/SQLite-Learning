import sqlite3
import pandas as pd

conn = sqlite3.connect('viber_messages2')

cur = conn.cursor()
#Adapted from Stackoverflow.com by Parfait
cur = cur.execute("SELECT DISTINCT m.conversation_id" + \
                    " FROM messages m " + \
                    " INNER JOIN participants p" + \
                    "         ON m.participant_id = p.participant_info_id" + \
                    "INNER JOIN participants_info pp"
                    "         ON pp._id = p.participant_info_id" + \
                    " WHERE m.conversation_id IS NOT NULL")

query = "SELECT m._id, m.date, m.body, m.conversation_id," + \
          "     p._id, p.conversation_id, p.active" + \
          " FROM messages m" + \
          " INNER JOIN participants p" + \
          "         ON m.participant_id = p._id" + \
          " WHERE m.conversation_id = ?"

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

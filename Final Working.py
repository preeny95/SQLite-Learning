import sqlite3
import pandas as pd

conn = sqlite3.connect('viber_messages2')

cur = conn.cursor()
#Adapted from Stackoverflow.com by Parfait
cur = cur.execute("""SELECT DISTINCT messages.conversation_id
                    FROM messages
                    INNER JOIN participants_info  ON messages.participant_id = participants_info._id
                    WHERE messages.conversation_id IS NOT NULL;""")

query = ("""SELECT messages.date, participants_info.number, participants_info.contact_name, messages.body AS Message_Sent, messages.conversation_id, messages.participant_id
            FROM messages
            INNER JOIN
            participants ON messages.participant_id = participants._id
            INNER JOIN
            participants_info ON participants.participant_info_id = participants_info._id
            WHERE messages.conversation_id = ?
            ORDER BY messages.date;""")

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

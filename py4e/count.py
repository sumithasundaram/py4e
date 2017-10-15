import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

name = input("Enter file:")
# fname ="/home/superadmin/PycharmProjects/py4e/mbox-short.txt.py"
fn = open(name)
words_list=list()
for line in fn:
    if not line.startswith("From:") : continue
    words = line.split()
    r = words[1].split("@")
    #print(r)
    w = r[1]
    print(w)
    words_list.append(w)
    print(words_list)
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
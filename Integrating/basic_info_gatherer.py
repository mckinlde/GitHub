import mysql.connector
import random

connection = mysql.connector.connect(host="localhost", port=3306, user="semdemo", passwd="demo", db="semdemo")
db = connection.cursor(prepared=True)

db.execute("""
        CREATE TABLE IF NOT EXISTS MY_TEST_TABLE_111222 (
            mid MEDIUMINT AUTO_INCREMENT PRIMARY KEY,
            txt VARCHAR(256) NOT NULL DEFAULT '',
            cat INT(5) UNSIGNED NULL,
            INDEX(cat)
        )""")

for i in range(100):
    db.execute("insert into MY_TEST_TABLE_111222(txt,cat) values(?,?)", ["string #" + str(i), random.randint(0, 10)])

db.execute("select * from MY_TEST_TABLE_111222 where cat = ?", [4])
for (mid, txt, cat) in db:
    print(mid, txt.decode("UTF-8"), cat)

connection.commit()  # required, as mysql generally doesn't autocommit

db.execute("DROP TABLE MY_TEST_TABLE_111222")  # note: table create/drop are generally auto-commit statements
connection.close()

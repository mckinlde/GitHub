# import mysql.connector
# import random
#
# connection = mysql.connector.connect(host="localhost", port=3306, user="semdemo", passwd="demo", db="semdemo")
# db = connection.cursor(prepared=True)
#
#
# db.execute("""
#         CREATE TABLE IF NOT EXISTS REPOSITORIES (
#             mid MEDIUMINT AUTO_INCREMENT PRIMARY KEY,
#             url VARCHAR(256) NOT NULL DEFAULT '',
#             repo_name VARCHAR(256) NOT NULL DEFAULT '',
#             username VARCHAR(256) NOT NULL DEFAULT '',
#             watchers INT(10) UNSIGNED NULL,
#             stars INT(10) UNSIGNED NULL,
#             forks INT(10) UNSIGNED NULL
#         )""")
#
#
# #db.execute("insert into BASIC_GITHUB(url, repo_name, username, watchers, stars, forks) values(?,?,?,?,?,?)",
# #           [repo.url, repo.name, repo.owner, repo.watchers, repo.stars, repo.forks])
#
#
# connection.commit()  # required, as mysql generally doesn't autocommit
#
# #db.execute("DROP TABLE MY_TEST_TABLE_111222")  # note: table create/drop are generally auto-commit statements
# connection.close()

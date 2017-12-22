import sqlite3

# Connect to Django SQL DB
path = "../db_old.sqlite3"
conn = sqlite3.connect(path)
cur = conn.cursor()


#change delay values to seconds
# cur.execute("SELECT ab_delay FROM delay_train")
# delay = cur.fetchall()
#
# for element in delay:
#     if element[0] is None:
#         delay_new = None
#     elif ":" in element[0]:
#         delay_new = int(element[0][2:4])*60 + int(element[0][5:7])
#     elif "." in element[0]:
#         delay_new = int(float(element[0]))
#         print("skipped")
#     elif type(element[0]) is int:
#         continue
#     else:
#         delay_new = None
#
#     print("Old:", element[0], "    New:", delay_new, "   Type:", type(delay_new))
#
#     cur.execute("UPDATE delay_train SET ab_delay= (?) WHERE ab_delay=(?)", ( delay_new, element[0] ) )
#     conn.commit()


#change uid to integers
# cur.execute("SELECT uid FROM delay_train")
# uid = cur.fetchall()
#
# for element in uid:
#     uid_new = element[0].replace("85:11:", "")
#     uid_new = uid_new.replace(":00", "")
#     uid_new = uid_new.replace("-", "")
#     uid_new = int(uid_new)
#
#     print("Old:", element[0], "    New:", uid_new)
#
#     cur.execute("UPDATE delay_train SET uid = (?) WHERE uid = (?)", ( uid_new, element[0] ) )
#     conn.commit()

#replace fällt aus through 0 and 1
cur.execute("SELECT faellt_aus_tf_old FROM delay_train")
fa = cur.fetchall()

for element in fa:
    if element[0] == "false":
        fa_new = 0
    elif element[0] == "true":
        fa_new = 1

    fa_new = int(fa_new)

    print("Old:", element[0], "    New:", fa_new)

    cur.execute("UPDATE delay_train SET faellt_aus_tf = (?) WHERE faellt_aus_tf_old = (?)", ( fa_new, element[0] ) )
    conn.commit()

cur.close()

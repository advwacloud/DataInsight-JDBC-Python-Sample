from impala.dbapi import connect

# `username` and `password` are your DataInsight account.
conn = connect(host="127.0.0.1", port=10090, user='xxxx@advantech.com.tw', password='password', auth_mechanism='PLAIN', timeout=30000)
cursor = conn.cursor()
cursor.execute('SHOW TABLES in main')
results = cursor.fetchall()
cursor.close()
conn.close()
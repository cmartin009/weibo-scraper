import sys
import pymysql

def connect():
    try:
        conn = pymysql.connect(host='127.0.0.1',  port=3306, user='root', passwd='!Catalan18', db='nlp', charset='utf8')
        #conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='m', charset='utf8')
        #  /var/lib/mysql/mysql.sock You can't run unix socket on windows so run port and host instead'
        cur = conn.cursor()
        cur.execute("USE nlp")
    except Exception as e:
        print(str(e))
        sys.exit('unable to connect to database')
    else:
        return conn, cur

def disconnect(conn, cur):
    cur.close()
    conn.close()

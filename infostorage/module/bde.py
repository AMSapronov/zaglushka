# coding: utf8
import psycopg2
import re
import json

class lsql:
    
    def load(self):
        
        with open('config.json', encoding="utf-8") as c:
            sqlc = json.load(c)
            
            #Чтение токена бота и ссылок на файлы:
            
        dbload = [''] * 4
        dbload[0] = sqlc['dbname']
        dbload[1] = sqlc['dbuser']
        dbload[2] = sqlc['dbpass']
        dbload[3] = sqlc['dbhost']
        
        
        return dbload
    
def exist(userid):
    
    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()
    
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
      
    userid = str(userid)
                
    cursor.execute('SELECT * FROM notes WHERE userid = %s LIMIT 1', [userid])
    records = cursor.fetchall()
    records = str(records)
                                
    cursor.close()
    conn.close()
    
    if records == '[]':
        answer = False
        
    else:
        answer = True
        
    return answer

def statusbit(userid, status):

    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()
        
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
    userid = str(userid)
    status = int(status) 
    print(userid)               
    cursor.execute('SELECT * FROM statusbit WHERE userid = %s', [userid])
    records = cursor.fetchall()
    print(userid, status, records)
    records = str(records)
                                             
    if records == '[]' and status != -1:
        insert = """INSERT INTO statusbit VALUES (%s, %s)"""
        iitem = (userid, status)
        cursor.execute(insert, iitem)
        conn.commit()
        
    elif status != -1:
        
        update = """UPDATE statusbit SET bit = %s WHERE userid = %s"""
        uitem = (status, userid)
        cursor.execute(update, uitem)
        conn.commit()
        
    else:
        cursor.execute('SELECT bit FROM statusbit WHERE userid = %s', [userid])
        records = cursor.fetchall()
        print(records)
        all = records[0] 
        print(all) 
        all = list(all)
        print(all)
        bit = all[0]
       
        return bit # Продолжить на движке
    
    cursor.close()
    conn.close()

def wnote(userid, text, notetime):
    
    notename = re.findall(r'\w+', text)[0]
    print(notename)
    text = text.replace(notename, '')
    
    if text.replace(' ', '') == '':
        text = notename 
    
    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()    
    
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
      
    userid = str(userid)
                
    insert = """INSERT INTO notes VALUES (%s, %s, %s, %s)"""
    iitem = (text, userid, notetime, notename)
    cursor.execute(insert, iitem)
    conn.commit()
        
    cursor.close()
    conn.close()
    
def rnote(userid, column):
    
    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()    
    
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
    userid = str(userid)                
    request = 'SELECT ' + column + ' FROM notes WHERE userid = %s'
    
    cursor.execute(request, [userid])
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records

def count(userid):
    
    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()    
    
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
    userid = str(userid)                
    cursor.execute('SELECT COUNT(*) FROM notes WHERE userid = %s', [userid])
    records = cursor.fetchall()   
    records = records[0]
    records = list(records)
    cursor.close()
    conn.close()
    print(records)
    return records  

def sqltopy(slist, btc, adslash):
    i = 0
    sbtcom = [''] * btc
    while i != btc:
        t = str(slist[i])
        t = t.replace('(', '')
        t = t.replace("'", '')
        t = t.replace(',', '')
        t = t.replace(')', '')
        sbtcom[i] = adslash + t
        i = i + 1    
    return sbtcom   

def note(notetime):
    
    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()    
    
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
    request = 'SELECT note FROM notes WHERE notetime = %s'
    
    cursor.execute(request, [notetime])
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records

def dell(notetime, userid):
    
    userid = str(userid)
    
    lo = lsql()
    dbdata = [''] * 4
    dbdata = lo.load()    
    
    conn = psycopg2.connect(dbname=dbdata[0], user=dbdata[1], password=dbdata[2], host=dbdata[3]) # ПЕРЕНЕСТИ НА ПЕРЕМЕННЫЕ!!!!!!!
    cursor = conn.cursor()
    request = 'DELETE FROM notes WHERE notetime = %s AND userid = %s'
    
    cursor.execute(request, [notetime, userid])
#    records = cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()

#    return records
        
# -*- coding: UTF-8 -*-

# program builds linkage of MD5 and Absolute File Path
# after running the program, all files in the input directory can be all loaded into database

import MySQLdb
import os
import hashlib

def getfilemd5(file_path):
    file = open(file_path)
    file_data = file.read(os.path.getsize(file_path))
    file_md5 = hashlib.md5()
    file_md5.update(file_data)
    file_digest = file_md5.hexdigest()
    return file_digest
    file.close()

def get_file_list(path, topdown):
    list_file_all = []
    walk = os.walk(path, topdown=topdown, onerror=None, followlinks=False)
    for root, dirs, files in walk:
        for file_name in files:
            #list_file.append(file_name)
                
            file_path = root + '/' + file_name
            #list_file_path.append(file_path)
                
            file_digest = getfilemd5(file_path)
            #list_file_digest.append(file_digest)
                
            list_file_all.append((file_name, file_path, file_digest))
    return list_file_all
    
path = raw_input('Input Path to write into Database:')

(list_file_all) = get_file_list(path, True)

#host = raw_input('Input MySQL Host:')
host = 'localhost'
#usr = raw_input('Input MySQL User:')
usr = 'root'
#pwd = raw_input('Input MySQL Password:')
pwd = 'dageada'
conn = MySQLdb.connect(host=host, user=usr,passwd=pwd, use_unicode=True, charset='utf8')

cursor = conn.cursor()

#Create Database
sql = 'CREATE DATABASE IF NOT EXISTS PhotoAdmin'
cursor.execute(sql) 

conn.select_db('PhotoAdmin')

#Create Table
sql = "CREATE TABLE IF NOT EXISTS MD5_FILE_PATH (ID int(10) not null PRIMARY KEY, MD5 char(128) not null, SEQ INT4 not null, File_Path char(255) not null, File_Exists char(3) not NULL)"
cursor.execute(sql)

sql = 'select * from MD5_FILE_PATH where file_path like %s'
check_path = path + '%'
total = cursor.execute(sql,check_path)
db_all = cursor.fetchall()
list_db_all = list(db_all)

for i in list_file_all:    
    sql = 'select * from MD5_FILE_PATH where (MD5=%s)'
    count = cursor.execute(sql,i[2])
    db = cursor.fetchall()
    list_db = list(db)
    
    for list_db_i in list_db:
        #print list_db_i
        try:
            list_db_all.remove(list_db_i)
        except Exception as already_removed:
            print 'Already Removed'

    
    file_logged = ''
    if count > 0:
        for db_i in db:
            if db_i[3] == i[1]:
                value = ['Yes', db_i[0]]
                cursor.execute('UPDATE MD5_FILE_PATH SET File_Exists=%s WHERE ID=%s', value)
                file_logged = 'X'
                break
        if file_logged <> 'X':
            sql = 'INSERT INTO MD5_FILE_PATH (ID,MD5,SEQ,File_Path,File_Exists) VALUES(%s,%s,%s,%s,%s)'
            total = total + 1
            count = count + 1
            value = [total, i[2], count, i[1], 'Yes']
            cursor.execute(sql,value)
    if count == 0:
        sql = 'INSERT INTO MD5_FILE_PATH (ID,MD5,SEQ,File_Path,File_Exists) VALUES(%s,%s,%s,%s,%s)'
        total = total + 1
        value = [total, i[2], 1, i[1], 'Yes']
        cursor.execute(sql,value)

for i in list_db_all:
    value = ['No', i[0]]
    cursor.execute('UPDATE MD5_FILE_PATH SET File_Exists=%s WHERE ID=%s', value)
            
conn.commit()
cursor.close()



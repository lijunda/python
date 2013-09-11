# -*- coding: UTF-8 -*-

import hashlib
import os
import time


def getfilemd5(file_path):
    file = open(file_path)
    file_data = file.read(os.path.getsize(file_path))
    file_md5 = hashlib.md5()
    file_md5.update(file_data)
    file_digest = file_md5.hexdigest()
    return file_digest
    file.close()

def get_file_list(path, topdown, test):
    list_file = []
    list_file_path = []
    list_file_digest = []
    list_file_all = []
    list_file_md5_unique = []
    list_file_md5_duplicated = []
    list_file_all_unique = []
    list_file_all_duplicated = []
    walk = os.walk(path, topdown=topdown, onerror=None, followlinks=False)
    for root, dirs, files in walk:
        for file_name in files:
            #print file_name
            list_file.append(file_name)
            
            file_path = root + '/' + file_name
            #print list_file_path
            list_file_path.append(file_path)
            
            file_digest = getfilemd5(file_path)
            #print file_digest
            list_file_digest.append(file_digest)
            
            list_file_all.append((file_name, file_path, file_digest))
            
            if file_digest in list_file_md5_unique:
                list_file_md5_duplicated.append(file_digest)
                list_file_all_duplicated.append((file_name, file_path, file_digest))
                if test != 'X':
                    os.remove(file_path)
            else:
                list_file_md5_unique.append(file_digest)
                list_file_all_unique.append((file_name, file_path, file_digest))
    return (list_file_all, list_file_all_unique, list_file_all_duplicated)
    
#path = '/home/legend/Desktop/test'
path = raw_input('Input Path to check duplicates:')

(list_file_all, list_file_all_unique, list_file_all_duplicated) = get_file_list(path, True, 'X')

no_files = len(list_file_all)
no_files_unique = len(list_file_all_unique)
no_files_duplicated = len(list_file_all_duplicated)

log_file_path = path + '/' + time.ctime() + '.txt'
print 'Log Path' + log_file_path
log_file = open(log_file_path, 'w')

line_data = 'Number of Files:' + str(no_files)
log_file.write(line_data)
log_file.write("\n")
line_data = 'Number of Files Unique:' + str(no_files_unique)
log_file.write(line_data)
log_file.write("\n")
line_data = 'Number of Files Duplicated:' + str(no_files_duplicated)
log_file.write(line_data)
log_file.write("\n")

log_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>>')
log_file.write("\n")
line_data = 'List of Files:'
log_file.write(line_data)
log_file.write("\n")

for i in list_file_all:
    line_data = i[1] + i[2]
    log_file.write(line_data)
    log_file.write("\n")

log_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>>')
log_file.write("\n")
line_data = 'List of Unique Files:'
log_file.write(line_data)
log_file.write("\n")

for i in list_file_all_unique:
    line_data = i[1] + i[2]
    log_file.write(line_data)
    log_file.write("\n")

log_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>>')
log_file.write("\n")
line_data = 'List of Duplicated Files:'
log_file.write(line_data)
log_file.write("\n")

for i in list_file_all_duplicated:
    line_data = i[1] + i[2]
    log_file.write(line_data)
    log_file.write("\n")
    
log_file.close()

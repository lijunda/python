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

def get_file_list(path, topdown):
    list_file = []
    list_file_path = []
    list_file_digest = []
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
    return (list_file, list_file_path, list_file_digest)
    
#path = '/home/legend/Desktop/test'
path = raw_input('Input Path to check duplicates:')
log_file_path = path + '/' + time.ctime() + '.txt'
print log_file_path


list_file = []
list_file_path = []
list_file_digest = []

(list_file, list_file_path, list_file_digest) = get_file_list(path, True)

no_files = len(list_file)
print 'Number of Files:' + str(no_files)

list_zip = zip(list_file_path, list_file_digest)

list_key_digest = sorted(set(list_file_digest))
no_key_digest = len(list_key_digest)
print 'Number of Unique MD5 Digests:' + str(no_key_digest)

log_file = open(log_file_path, 'w')

counter_digest = 0
for key_digest in list_key_digest:
    counter_digest = counter_digest + 1
    key = 'Key' + '-' + str(counter_digest)# + '-' + key_digest
    log_file.write(key)
    log_file.write("\n")
    
    print key
    counter_file = 0
    for x in list_zip:
        if x[1] == key_digest:
            counter_file = counter_file + 1
            file = 'File' + '-' + str(counter_file) + '-' + x[0]
            log_file.write(file)
            log_file.write("\n")
            
log_file.close()

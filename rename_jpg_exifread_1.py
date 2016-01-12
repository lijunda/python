# -*- coding: UTF-8 -*-
import exifread
import os
import sys
import csv
import traceback
import time
import datetime
import shutil

no_renamed = 0
no_to_rename = 0


def rename_dir_using_exif_time(path, test):
    global no_renamed, no_to_rename

    timestr = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

#Open Log File
    Log_Path = ''
    # Fail_File_Path = ''
    Log_Path = path + '/' + 'Log_' + timestr
    # Fail_File_Path = path + '/' + 'Fail_File'
    os.mkdir(Log_Path)

    logfile = Log_Path + '/' + timestr + ' ' + 'Rename Log.CSV'
    csvfile = open(logfile, 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(['Old File Full Name', 'Old File Name', 'New File Full Name', 'New File Name', 'dateTime', 'dateTimeOriginal', 'dateTimeDigitized', ''])

    dateTime=''
    dateTimeOriginal= ''
    dateTimeDigitized = ''
    timeValue = ''

#Go through all files & Rename
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) == True:
            if '.' in file:
                file_type = file.rsplit('.', 1)[1]
                if file_type == 'JPG' or file_type == 'jpg':
                    try:
                        no_to_rename = no_to_rename + 1
# Use Exifread
#Open JPG File
                        f = open(os.path.join(path, file), 'rb')

                        tags = exifread.process_file(f, details=False)

                        for tag in tags.keys():
                            if tag == 'EXIF DateTime':
                                dateTime = tags['EXIF DateTime']
                                # timeValue = dateTime
                            if tag == 'EXIF DateTimeDigitized':
                                dateTimeDigitized = tags['EXIF DateTimeDigitized']
                                # timeValue = dateTimeDigitized
                            if tag == 'EXIF DateTimeOriginal':
                                dateTimeOriginal = tags['EXIF DateTimeOriginal']
                                # timeValue = dateTimeOriginal
                        timeValue = dateTimeOriginal
                        if timeValue is not '':
                            #Convert to string format
                            timeValue = timeValue.values
                            #Convert to time format
                            timeValue = time.strptime(timeValue, '%Y:%m:%d %H:%M:%S')
                            #Convert to required time format
                            timeValue = time.strftime('%Y-%m-%d %H-%M-%S', timeValue)
                            #Use time as file name
                            timeValue = timeValue + '.JPG'
                            #Rename File with Time
                            f.close()
                            try:
                                os.rename(os.path.join(path, file), os.path.join(path, timeValue))
                                no_renamed = no_renamed + 1

                                #Generate Log File - Sucessful

                                writer.writerow([os.path.join(path, file), file, os.path.join(path, timeValue), timeValue, dateTime, dateTimeOriginal, dateTimeDigitized, 'Yes'])
                            except:
                                #Generate Log File - Failed

                                writer.writerow([os.path.join(path, file), file, os.path.join(path, timeValue), timeValue, dateTime, dateTimeOriginal, dateTimeDigitized, 'No'])

                                #Move Failed Files into Fail Folder
                                # shutil.move(os.path.join(path, file), os.path.join(Log_Path, file))

                                traceback.print_exc()
                        else:
                                                            #Generate Log File - Failed

                            writer.writerow([os.path.join(path, file), file, os.path.join(path, timeValue), timeValue, dateTime, dateTimeOriginal, dateTimeDigitized, 'No'])
                            f.close()
                            # try:
                                #Move Failed Files into Fail Folder
                                # shutil.move(os.path.join(path, file), Log_Path)
                            # except:
                            #     traceback.print_exc()
                    except:
                        traceback.print_exc()
                else:
                    writer.writerow([os.path.join(path, file), file, os.path.join(path, timeValue), timeValue, dateTime, dateTimeOriginal, dateTimeDigitized, 'No'])
                    # try:
                        #Move Failed Files into Fail Folder
                        # shutil.move(os.path.join(path, file), Log_Path)
                    # except:
                    #     traceback.print_exc()
    #Close Log File
    csvfile.close()

#3-tuple (dirpath, dirnames, filenames) returned from os.walk
def show_list(path, topdown):
    no_dir = 0
    no_file = 0
    walk = os.walk(path, topdown=topdown, onerror=None, followlinks=False)
    for root, dirs, files in walk:
        for dir_path in dirs:
            no_dir = no_dir + 1
        for file_path in files:
            no_file = no_file + 1
    return (no_dir, no_file)


path = input('Input Directory to Rename JPG files with Exif Information:')

# Display directory/file list
print('LOG: AFTER RENAME')
(no_dir, no_file) = show_list(path, True)

message = ''
message = 'no of directories nested in the root path: ' + str(no_dir)
print(message)
message = ''
message = 'no of files nested in the root path and all subsidiary directories: ' + str(no_file)
print(message)
message = ''
message = 'all directories and files nested in the root path: ' + str(os.listdir(path))
print(message)

# Rename all '.jpg' or 'JPG' files using Exif time
rename_dir_using_exif_time(path, '')

message = ''
message = 'Number of Files Needs Renamed ' + str(no_to_rename)
print(message)

message = ''
message = 'Number of Files Renamed ' + str(no_renamed)
print(message)


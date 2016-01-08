# -*- coding: UTF-8 -*-
import exifread
import os
import sys

no_renamed = 0


def rename_dir_using_exif_time(path, test):
    global no_renamed
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) == True:
            if '.' in file:
                file_type = file.rsplit('.', 1)[1]
                print
                file_type
                if file_type == 'JPG' or file_type == 'jpg':
                    try:
# Use Exifread
                        f = open(os.path.join(path, file), 'rb')
                        tags = exifread.process_file(f, details=False)
                        for tag in tags.keys():
                            if tag == 'EXIF DateTime':
                                dateTime = tags['EXIF DateTime']
                                print(dateTime)
                            if tag == 'EXIF DateTimeOriginal':
                                dateTimeOriginal = tags['EXIF DateTimeOriginal']
                                print(dateTimeOriginal)
                            if tag == 'EXIF DateTimeDigitized':
                                dateTimeDigitized = tags['EXIF DateTimeDigitized']
                                print(dateTimeDigitized)


# Use Pyexiv
#                         metadata = pyexiv2.ImageMetadata(os.path.join(path, file))
#                         metadata.read()
#                         # print 'exif_keys:'
#                         # print metadata.exif_keys
#                         # print 'iptc_keys:'
#                         # print metadata.iptc_keys
#                         # print 'xmp_keys:'
#                         # print metadata.xmp_keys
#                         mime_type = metadata.mime_type
#                         print
#                         mime_type
#                         if mime_type == 'image/jpeg':
                            value = ''
                            # try:
                            # tag = metadata['Exif.Photo.ExposureTime']
                            # ExposureTime = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                            # print '#S: Exif.Image.DateTime' + '=' + ExposureTime
                            # ExposureTime = ExposureTime + '.JPG'
                            # value = ExposureTime
                            # except Exception as not_set:
                            # print '#E: Exif.Photo.ExposureTime' + 'Not Set'
                            # try:
                            #     tag = metadata['Exif.Image.DateTime']
                            #     DateTime = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                            #     print
                            #     '#S: Exif.Image.DateTime' + '=' + DateTime
                            #     DateTime = DateTime + '.JPG'
                            #     value = DateTime
                            # except Exception as not_set:
                            #     print
                            #     '#E: Exif.Image.DateTime' + 'Not Set'
                            #
                            # try:
                            #     tag = metadata['Exif.Photo.DateTimeDigitized']
                            #     DateTimeDigitized = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                            #     print
                            #     '#S: Exif.Photo.DateTimeDigitized' + '=' + DateTimeDigitized
                            #     DateTimeDigitized = DateTimeDigitized + '.JPG'
                            #     value = DateTimeDigitized
                            # except Exception as not_set:
                            #     print
                            #     '#E: Exif.Photo.DateTimeDigitized' + 'Not Set'
                            #
                            # try:
                            #     tag = metadata['Exif.Photo.DateTimeOriginal']
                            #     DateTimeOriginal = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                            #     print
                            #     '#S: Exif.Photo.DateTimeOriginal' + '=' + DateTimeOriginal
                            #     value = DateTimeOriginal
                            # except Exception as not_set:
                            #     print
                            #     '#E: Exif.Photo.DateTimeOriginal' + 'Not Set'
                            #
                            # if test != 'X':
                            #     if value is not '':
                            #         value = value + '.JPG'
                            #         os.rename(os.path.join(path, file), os.path.join(path, value))
                            #     no_renamed = no_renamed + 1
                            #     # print counter_renamed
                            # else:
                            #     print
                            #     'I: No Date Set'
                    except Exception as bad_jpg:
                        print('#E: Bad JPG File')

                        # else:
                        # value = file + '.JPG'
                        # os.rename(os.path.join(path,file), os.path.join(path,value))
        # else:
            # print
            # '>>>' + os.path.join(path, file)
            # print
            # '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            # rename_dir_using_exif_time(os.path.join(path, file), test)


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


path = input('Input Directory:')
# path = '/home/legend/Desktop/test'

# Rename all '.jpg' or 'JPG' files using Exif time
rename_dir_using_exif_time(path, '')
#print
#'Number of Files Renamed' + str(no_renamed)


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


# -*- coding: UTF-8 -*-
import pyexiv2
import os
import sys

no_renamed = 0

def rename_dir_using_exif_time(path, test):
    global no_renamed
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)) == True:
            if '.' in file:
                file_type  = file.rsplit('.',1)[1]
                print file_type                    
                if file_type == 'JPG' or file_type == 'jpg':
                    print 'file:' + os.path.join(path,file)
                    print '--------------------------------------------------------------'
                    try:
                        metadata = pyexiv2.ImageMetadata(os.path.join(path,file))
                        metadata.read()
                        #print 'exif_keys:'
                        #print metadata.exif_keys
                        #print 'iptc_keys:'
                        #print metadata.iptc_keys
                        #print 'xmp_keys:'
                        #print metadata.xmp_keys
                        mime_type = metadata.mime_type
                        print mime_type
                        if mime_type == 'image/jpeg':
                            value = ''
                            #try:
                                #tag = metadata['Exif.Photo.ExposureTime']
                                #ExposureTime = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                                #print '#S: Exif.Image.DateTime' + '=' + ExposureTime
                                #ExposureTime = ExposureTime + '.JPG'
                                #value = ExposureTime
                            #except Exception as not_set:
                                #print '#E: Exif.Photo.ExposureTime' + 'Not Set'    
                            try:
                                tag = metadata['Exif.Image.DateTime']
                                DateTime = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                                print '#S: Exif.Image.DateTime' + '=' + DateTime
                                DateTime = DateTime + '.JPG'
                                value = DateTime
                            except Exception as not_set:
                                print '#E: Exif.Image.DateTime' + 'Not Set'

                            try:
                                tag = metadata['Exif.Photo.DateTimeDigitized']
                                DateTimeDigitized = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                                print '#S: Exif.Photo.DateTimeDigitized' + '=' + DateTimeDigitized
                                DateTimeDigitized = DateTimeDigitized + '.JPG'
                                value = DateTimeDigitized
                            except Exception as not_set:
                                print '#E: Exif.Photo.DateTimeDigitized' + 'Not Set'

                            try:
                                tag = metadata['Exif.Photo.DateTimeOriginal']
                                DateTimeOriginal = tag.value.strftime('%Y-%m-%d %H-%M-%S')
                                print '#S: Exif.Photo.DateTimeOriginal' + '=' + DateTimeOriginal
                                value = DateTimeOriginal
                            except Exception as not_set:
                                print '#E: Exif.Photo.DateTimeOriginal' + 'Not Set'

                            if test != 'X':
                                if value is not '':
                                    value = value + '.JPG'
                                    os.rename(os.path.join(path,file), os.path.join(path,value))
                                no_renamed = no_renamed + 1
                                #print counter_renamed
                            else:
                                print 'I: No Date Set'
                    except Exception as bad_jpg:
                        print '#E: Bad JPG File'
            #else:
                #value = file + '.JPG'
                #os.rename(os.path.join(path,file), os.path.join(path,value))
        else:
            print '>>>' + os.path.join(path,file)
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            rename_dir_using_exif_time(os.path.join(path,file), test)


def show_list(path, topdown):
    no_root = 0
    no_dir = 0
    no_file = 0
    walk = os.walk(path, topdown=topdown, onerror=None, followlinks=False)
    for root, dirs, files in walk:
	#print 'Root Dir:' + root
	print root	
	no_root = no_root + 1
	#print 'Dirs:'
	for dir_path in dirs:
	    print dir_path
	    no_dir = no_dir + 1
	#print 'Files:'
	for file_path in files:
	    print file_path
	    no_file = no_file + 1
    return (no_root, no_dir, no_file)

path = raw_input('Input Directory:')
#path = '/home/legend/Desktop/test'

# Rename all '.jpg' or 'JPG' files using Exif time
rename_dir_using_exif_time(path, '')
print 'Number of Files Renamed' + str(no_renamed )

## Display directory/file list
#(no_root, no_dir, no_file) = show_list(path, True)
#print no_root
#print no_dir
#print no_file


#print os.listdir('.')


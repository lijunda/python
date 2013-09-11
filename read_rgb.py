

import os
from PIL import Image

file_path = raw_input('Input JPG file for Read:')
path = os.path.dirname(file_path)
print path
file_name = os.path.split(file_path)[-1]
print file_name
log_path = path + '/' + file_name.split('.',1)[0] + '.txt'
print log_path

im = Image.open(file_path)

(width, height) = im.size
print width, height

# Fast
pix = im.load()
print pix[1, 1]


# Slow
#rgb_im = im.convert('RGB')
#(width, height) = rgb_im.size
#print width, height
#r, g, b = rgb_im.getpixel((1, 1))
#print r, g, b

log_file = open(log_path, 'w')
for y in range(0, height):
    for x in range(0, width):
        if pix[x, y] != (0, 0, 0):
            #print '1'
            log_file.write(' ')
        else:
            #print ' '
            log_file.write('0')
    #print "\n"
    log_file.write("\n")
#im.rotate(90).show()
log_file.close()

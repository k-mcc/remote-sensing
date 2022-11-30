# get_reflector_pixels.py
# AUTHOR:       Kate McCarthy (kem6ur@virginia.edu, kemccarthy6@gmail.com)
# CREATED:      November 2022
# DESCRIPTION:  Finds TIFF radargram of a given orbit and outputs a CSV file containing 
#               lat, lon, and two-way travel time of all red pixels.

import cv2
import numpy as np
import csv
import pandas

orbit_str = "6652101"
orbit_str = orbit_str.zfill(8)

coordinates = {}
#xvals = []

img = cv2.imread("./downloads/images/radargrams/s_" + orbit_str + ".tif")

red_pixels = np.argwhere(cv2.inRange(img, (0, 0, 250), (0, 0, 255)))

for py, px in red_pixels:
    #if not px in xvals: # ignores any duplicate observations (as written, it favors shallowest observation if there are duplicates).
        #coordinates.append([py,px])
    coordinates[px] = py

    #xvals.append(px)

print("found " + str(len(coordinates)) + " red pixels")

with open(('./outputs/s_' + orbit_str + '_output.csv'), mode='w') as output:

    # write header
    writer = csv.writer(output)
    header = ['X Pixel', 'Y Pixel (Pixel depth from top of image)', 'Lat', 'Lon', 'Delay (microsec)']
    writer.writerow(header)

    # grab lat & lon of frames from geom table corresponding to radargram
    with open('./downloads/geom/s_' + orbit_str + '_geom.csv') as geom:
        reader = csv.reader(geom, delimiter=',')
        radargram_column = 1
        for row in reader:
            radargram_column += 1
            if not coordinates.get(radargram_column) == None: # if this frame was highlighted
                lat = row[2]
                lon = row[3]
                delay = coordinates.get(radargram_column)*0.0375
                row_to_write = [radargram_column, coordinates.get(radargram_column), lat, lon, delay]
                #print("rdg col = ", radargram_column)
                #print("pixel depth = ", coordinates.get(radargram_column))
                writer.writerow(row_to_write)

# import numpy as np
# import matplotlib.pyplot as plt

# class Formatter(object):
#     def __init__(self, im):
#         self.im = im

# imagefile = plt.imread('s_05990101_tiff_copy.tif')
# fig, ax = plt.subplots()
# im = ax.imshow(imagefile)
# ax.format_coord = Formatter(im)
# plt.show()
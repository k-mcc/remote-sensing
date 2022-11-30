# download_files.py
# AUTHOR:		Kate McCarthy (kem6ur@virginia.edu, kemccarthy6@gmail.com)
# CREATED: 		November 2022
# DESCRIPTION:	Downloads SHARAD radargram, cluttergram, and geom table for a given orbit.

import requests
import cv2

orbit_str = "6652101"
orbit_str = orbit_str.zfill(8)
first_4_digits = str(orbit_str)[:4]

#######################################################
################# GET RADARGRAM FILE ##################
radargram_file_name = "./downloads/images/radargrams/s_" + orbit_str + ".tif"
radargram_URL = "https://pds-geosciences.wustl.edu/mro/mro-m-sharad-5-radargram-v2/mrosh_2101/browse/tiff/s_" + first_4_digits + "xx/s_" + orbit_str + "_tiff.tif"
response = requests.get(radargram_URL)
open(radargram_file_name, "wb").write(response.content)
#######################################################
######## Convert gray image to color format. ##########
gray = cv2.imread(radargram_file_name)
backtorgb = gray[:,:,::-1]
cv2.imwrite(radargram_file_name, backtorgb)
#######################################################

#######################################################
################ GET CLUTTERGRAM FILE #################
cluttergram_file_name = "./downloads/images/cluttergrams/s_" + orbit_str + ".tif"
cluttergram_URL = "https://pds-geosciences.wustl.edu/mro/urn-nasa-pds-mro_sharad_simulations/browse/s_" + first_4_digits + "xx/s_" + orbit_str + "/s_" + orbit_str + "_browse_combined.tif"
#cluttergram_URL = "https://pds-geosciences.wustl.edu/mro/urn-nasa-pds-mro_sharad_simulations/browse/s_0596xx/s_05969001/s_05969001_browse_combined.tif"
response = requests.get(cluttergram_URL)
open(cluttergram_file_name, "wb").write(response.content)
#######################################################

#######################################################
#################### GET GEOM FILE ####################
geom_file_name = "./downloads/geom/s_" + orbit_str + "_geom.csv"
geom_URL = "https://pds-geosciences.wustl.edu/mro/mro-m-sharad-5-radargram-v2/mrosh_2101/data/geom/s_" + first_4_digits + "xx/s_" + orbit_str + "_geom.tab"
response = requests.get(geom_URL)
open(geom_file_name, "wb").write(response.content)
#######################################################

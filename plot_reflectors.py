# plot_reflectors.py
# AUTHOR:       Kate McCarthy (kem6ur@virginia.edu, kemccarthy6@gmail.com)
# CREATED:      November 2022
# DESCRIPTION:  Plots points from all CSV files in ./outputs/ dir on an image.
#               Color corresponds to two-way travel time.

import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import glob
import os

plt.figure()

#filename = "h2976_0000_ir3.jpeg"
#lonmin, lonmax, latmin, latmax = (210.503, 212.464, 0.49597, 15.8603)  # for H2976_0000_IR3
#lonmin, lonmax, latmin, latmax = (209.32, 211.437, 1.45876, 15.8649)    # for H2965_0000_IR3
#lonmin, lonmax, latmin, latmax = (209.989, 210.831, 5.671, 9.676)    # for V14097010 (themis)
#lonmin, lonmax, latmin, latmax = (210.0625, 218.796875, 0.4999999999999558, 9.921874999999964)  # for jmars_background_1.png
lonmin, lonmax, latmin, latmax = (210.0625, 212, 0, 6.003906250000003)  # for jmars_background_2.png
image_extent = [lonmin, lonmax, latmin, latmax] # was tuple before
# ax = plt.gca()
# ax.imshow(plt.imread(filename), extent=image_extent)

img = plt.imread("./backgrounds/jmars_background_2.png")
fig, ax = plt.subplots()
ax.imshow(img, extent=image_extent)

#.plot(figsize=image_extent,ax=ax)

files = os.path.join("./outputs/", "*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.plot(x="Lon", y="Lat", kind="scatter", 
        c="Delay (microsec)", colormap="jet", ax=ax)
# (for more colormap options, see https://matplotlib.org/stable/tutorials/colors/colormaps.html)

# #Q: how to use same color scale for both????? maybe should combine into 1 csv file first, then use that here.
#df = pd.read_csv("./outputs/s_06236701_output.csv", delimiter=',', skiprows=0, low_memory=False)
#df.plot(x="Lon", y="Lat", kind="scatter", 
#        c="Delay (microsec)", colormap="YlOrRd", ax=ax)

# df = pd.read_csv("./outputs/s_03334301_output.csv", delimiter=',', skiprows=0, low_memory=False)
# df.plot(x="Lon", y="Lat", kind="scatter", 
#         c="Delay (microsec)", colormap="YlOrRd", ax=ax)

# zoom in
minx, miny, maxx, maxy = (210.0625, 0.4999999999999558, 212, 6) #df.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)

plt.show()

#gdf.plot(ax=image.plot(figsize=image_extent), marker='o', color='red', markersize=15);



from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    #llcrnrlon=-136.25, llcrnrlat=56.0,
    #urcrnrlon=-134.25, urcrnrlat=57.75)
    llcrnrlon=-136.0, llcrnrlat=56.75,
    urcrnrlon=-134.5, urcrnrlat=57.5)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()
 
lats = []
lons = []

filename="tracks.gpx"

import re
lat_pattern = '.*lat="(\d\d\.\d\d\d\d\d).*'
lon_pattern = '.*lon="(-\d\d\d\.\d\d\d\d\d).*'

with open(filename) as f:
    lines = f.readlines()
    print(len(lines))
    for line in lines:
        matchObj = re.match(lat_pattern, line)
        if matchObj:
            #print(matchObj.group(1))
            lat = float(matchObj.group(1))
            lats.append(lat)

        matchObj = re.match(lon_pattern, line)
        if matchObj:
            #print(matchObj.group(1))
            lon = float(matchObj.group(1))
            lons.append(lon)


x,y = map(lons, lats)
map.plot(x, y, 'bo', markersize=10)
 
plt.show()

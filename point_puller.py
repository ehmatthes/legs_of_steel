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
        


#print(lats)
#print(lons)
print(len(lats), len(lons))

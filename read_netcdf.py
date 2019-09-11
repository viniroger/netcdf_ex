# Read netCDF file
from netCDF4 import Dataset
#import numpy as np

# Loading dataset
fh = Dataset('data.nc')
#print(fh.dimensions.keys())
#print(fh.variables.keys())
#print(fh.variables['precip'])

# Getting values
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
var = fh.variables['precip'][:]
var_units = fh.variables['precip'].long_name
#print(var)

# Close file
fh.close()

# Plot map from netCDF data
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()
m = Basemap(width=2500000,height=2000000,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)

# Because our lon and lat variables are 1D,
# use meshgrid to create 2D arrays
# Not necessary if coordinates are already in 2D arrays.
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)

# Plot data from first time
cs = m.pcolor(xi,yi,np.squeeze(var[0]))

# Add grid lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add coastlines, states and country boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(var_units)

# Add title
plt.title('Map plot example')

# Show or save figure
#plt.show()
plt.savefig('map.png')

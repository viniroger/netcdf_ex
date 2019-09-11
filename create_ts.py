# Create RR time series

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

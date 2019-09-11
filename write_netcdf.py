import numpy as np
from netCDF4 import Dataset

# Creating sample data
n1 = 385
n2 = 538
#data_array = np.zeros((n1, n2))
data_array = np.random.randint(400, size=(n1, n2))

# Creating dataset
dataset = Dataset('dataset.nc', 'w', format='NETCDF4')

# Creating the dimensions to use
dataset.createDimension('x', n1)
dataset.createDimension('y', n2)

# Creating variable (name, format, dimensions)
var = dataset.createVariable('varname', 'f8', ('x', 'y'))

# Writing data
dataset['varname'][:] = data_array

# Close file
dataset.close()

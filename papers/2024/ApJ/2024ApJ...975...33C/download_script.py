# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the observations
time_range_iris = a.Time('2013-10-21', '2013-10-22')  # IRIS observation date
time_range_hmi = a.Time('2013-10-21', '2013-10-22')  # HMI observation date

# Define the instrument attributes
instrument_iris = a.Instrument('IRIS')
instrument_hmi = a.Instrument('HMI')

# Define the wavelength for IRIS Si IV 1403 Å
wavelength_iris = a.Wavelength(1403 * u.Angstrom, 1403 * u.Angstrom)

# Query for IRIS data
iris_query = Fido.search(time_range_iris, instrument_iris, wavelength_iris)
print("IRIS Query Results:")
print(iris_query)
# Note: One of the IRIS results has a negative size value, which may indicate a data issue.

# Query for HMI data
# Note: Wavelength is not applicable for HMI vector magnetic field data
hmi_query = Fido.search(time_range_hmi, instrument_hmi, a.Physobs('vector_magnetic_field'))
print("HMI Query Results:")
print(hmi_query)

# Note: If the dataset is large, consider checking for pagination in the results.
# Uncomment the following lines to fetch the data
# iris_download = Fido.fetch(iris_query)
# hmi_download = Fido.fetch(hmi_query)

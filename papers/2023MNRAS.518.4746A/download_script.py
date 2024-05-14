# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation periods for MDI and HMI as specified in the context
mdi_start_date = '1996-05-12'
mdi_end_date = '2010-06-06'
hmi_start_date = '2010-06-07'
hmi_end_date = '2021-12-27'

# Time range for MDI observations
mdi_time_range = a.Time(mdi_start_date, mdi_end_date)

# Time range for HMI observations
hmi_time_range = a.Time(hmi_start_date, hmi_end_date)

# MDI instrument details
mdi_instrument = a.Instrument("MDI")
mdi_wavelength = a.Wavelength(6768 * u.angstrom)
mdi_physobs = a.Physobs("LOS_magnetic_field")

# HMI instrument details
hmi_instrument = a.Instrument("HMI")
hmi_wavelength = a.Wavelength(6173.3 * u.angstrom)
hmi_physobs = a.Physobs("LOS_magnetic_field")

# Construct queries for MDI and HMI
mdi_query = Fido.search(mdi_time_range, mdi_instrument, mdi_wavelength, mdi_physobs)
hmi_query = Fido.search(hmi_time_range, hmi_instrument, hmi_wavelength, hmi_physobs)

# Display the query results for MDI and HMI
print("Query for MDI observations:")
print(mdi_query)
print("Query for HMI observations:")
print(hmi_query)

# Uncomment the lines below to download the data
# mdi_files = Fido.fetch(mdi_query)
# hmi_files = Fido.fetch(hmi_query)

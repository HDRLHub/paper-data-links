# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the time range for the queries
# Note: The time range might be too broad, consider using a smaller range if you encounter issues.
time_range = a.Time('2011-09-01', '2017-06-30')

# Example smaller time range to avoid potential issues with broad time ranges
# time_range = a.Time('2011-09-01', '2011-09-30')  # Using smaller example time range

# Query for AIA data
aia_wavelengths = [94*u.Angstrom, 131*u.Angstrom, 171*u.Angstrom, 193*u.Angstrom, 211*u.Angstrom, 304*u.Angstrom, 335*u.Angstrom, 1600*u.Angstrom, 1700*u.Angstrom]
aia_query = Fido.search(time_range, a.Instrument('AIA'), a.Wavelength(aia_wavelengths))
print("AIA Query Results:")
print(aia_query)
# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(aia_query)

# Query for HMI data
hmi_query = Fido.search(time_range, a.Instrument('HMI'), a.Physobs('LOS_magnetic_field'))
print("HMI Query Results:")
print(hmi_query)
# Uncomment the following line to fetch the data
# hmi_files = Fido.fetch(hmi_query)

# Query for GOES data
goes_query = Fido.search(time_range, a.Instrument('GOES'), a.Wavelength(1*u.Angstrom, 8*u.Angstrom))
print("GOES Query Results:")
print(goes_query)
# Uncomment the following line to fetch the data
# goes_files = Fido.fetch(goes_query)

# Query for LASCO data
lasco_query = Fido.search(time_range, a.Instrument('LASCO'), a.Wavelength(5294*u.Angstrom, 6576*u.Angstrom))
print("LASCO Query Results:")
print(lasco_query)
# Uncomment the following line to fetch the data
# lasco_files = Fido.fetch(lasco_query)

# Query for WAVES data
waves_query = Fido.search(time_range, a.Instrument('WAVES'), a.Wavelength(0.02*u.MHz, 13.825*u.MHz))
print("WAVES Query Results:")
print(waves_query)
# Uncomment the following line to fetch the data
# waves_files = Fido.fetch(waves_query)

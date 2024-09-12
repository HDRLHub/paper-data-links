# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Context: We are interested in data from the Helioseismic and Magnetic Imager (HMI) and the Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO).
# The data will be used to investigate the rapid increase of horizontal magnetic field (Bh) around the flaring polarity inversion line during major solar flares.

# Reasoning:
# 1. We need to query the HMI instrument for vector magnetic field data.
# 2. We need to query the AIA instrument for 1600 Å images to analyze flare ribbons.
# 3. The time range is not explicitly stated, but we will assume a general time range that includes major flares.

# Define the time range for the query
# Using a smaller example time range due to potential issues with broad time ranges
time_range = a.Time('2011-02-14', '2011-02-16')  # Example time range within the original range

# Define the instruments and their respective wavelengths
hmi_instrument = a.Instrument('HMI')
aia_instrument = a.Instrument('AIA')
aia_wavelength = a.Wavelength(1600 * u.Angstrom)

# Query for HMI vector magnetic field data
hmi_query = Fido.search(time_range, hmi_instrument, a.Physobs('vector_magnetic_field'))

# Query for AIA 1600 Å images
# Note: This query may return a large number of results, indicating potential pagination issues.
aia_query = Fido.search(time_range, aia_instrument, aia_wavelength)

# Print out the query results
print("HMI Query Results:")
print(hmi_query)
print("\nAIA Query Results:")
print(aia_query)

# Uncomment the following lines to fetch the data
# hmi_files = Fido.fetch(hmi_query)
# aia_files = Fido.fetch(aia_query)

# Note: The original time range was '2010-05-01' to '2023-01-01'. If needed, adjust the time range accordingly.

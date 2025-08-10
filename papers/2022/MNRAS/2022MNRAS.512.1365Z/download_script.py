# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the queries
# Using a smaller example time range due to potential issues with broad time ranges
time_range = a.Time('2010-01-01', '2010-01-31')  # Example time range within the original range

# Query for SOHO/MDI data
mdi_query = Fido.search(time_range, a.Instrument('MDI'))
print("SOHO/MDI Query Results:")
print(mdi_query)
# mdi_files = Fido.fetch(mdi_query)

# Query for SDO/HMI data
hmi_query = Fido.search(time_range, a.Instrument('HMI'))
print("SDO/HMI Query Results:")
print(hmi_query)
# hmi_files = Fido.fetch(hmi_query)

# Query for SOHO/EIT data
eit_query = Fido.search(time_range, a.Instrument('EIT'), a.Physobs('intensity'))
print("SOHO/EIT Query Results:")
print(eit_query)
# Note: Pagination might be an issue here, as the query returns 10,000 results
# eit_files = Fido.fetch(eit_query)

# Query for SDO/AIA data
aia_query = Fido.search(time_range, a.Instrument('AIA'), a.Physobs('intensity'))
print("SDO/AIA Query Results:")
print(aia_query)
# aia_files = Fido.fetch(aia_query)

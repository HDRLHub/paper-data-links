# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for the queries
# Using smaller example time range for SDO/HMI due to potential broad range issue
time_range_sdo_hmi = a.Time('2010-01-01', '2010-01-07')  # Example time range within the original range
time_range_soho_mdi = a.Time('1995-01-01', '2010-12-31')
time_range_goes = a.Time('1995-01-01', '2023-12-31')  # Continuous time range

# Define the instruments
instrument_sdo_hmi = a.Instrument('HMI')
instrument_soho_mdi = a.Instrument('MDI')
instrument_goes = a.Instrument('XRS')

# Query for SDO/HMI data
print("Querying SDO/HMI data...")
query_sdo_hmi = Fido.search(time_range_sdo_hmi, instrument_sdo_hmi)
print(query_sdo_hmi)
# Uncomment the following line to fetch the data
# Fido.fetch(query_sdo_hmi)

# Query for SOHO/MDI data
print("Querying SOHO/MDI data...")
query_soho_mdi = Fido.search(time_range_soho_mdi, instrument_soho_mdi)
print(query_soho_mdi)
# Uncomment the following line to fetch the data
# Fido.fetch(query_soho_mdi)

# Query for GOES data
print("Querying GOES data...")
query_goes = Fido.search(time_range_goes, instrument_goes)
print(query_goes)
# Uncomment the following line to fetch the data
# Fido.fetch(query_goes)

# Note: The queries for SOHO/MDI and GOES data return a large number of results.
# This may lead to pagination issues. Consider narrowing down the time range if needed.

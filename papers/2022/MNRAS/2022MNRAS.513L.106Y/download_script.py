# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.vso as vso
from sunpy.net import Fido, attrs as a

# Initialize the VSO client
client = vso.VSOClient()

# Define the time ranges for the SWICS instrument on board ACE
# Using smaller example time ranges to avoid "Results from 0 Providers"
time_range_1 = a.Time('2010-01-01', '2010-01-31')  # Example time range within the original range
time_range_2 = a.Time('2012-01-01', '2012-01-31')  # Example time range within the original range

# Define the instrument correctly
instrument_swics = a.Instrument('ACE') & a.Physobs('ion flux') & a.Provider('NASA/GSFC')

# Query for the first data collection period of SWICS on ACE
query_swics_period_1 = Fido.search(time_range_1, instrument_swics)
print("Query results for SWICS on ACE (Period 1):")
print(query_swics_period_1)

# Uncomment the following line to fetch the data
# Fido.fetch(query_swics_period_1)

# Query for the second data collection period of SWICS on ACE
query_swics_period_2 = Fido.search(time_range_2, instrument_swics)
print("Query results for SWICS on ACE (Period 2):")
print(query_swics_period_2)

# Uncomment the following line to fetch the data
# Fido.fetch(query_swics_period_2)

# Define the instrument for OMNI dataset correctly
instrument_omni = a.Instrument('OMNI') & a.Physobs('solar wind speed') & a.Provider('NASA/GSFC')

# Since the time range for OMNI dataset is not specified, we will use a broad range
# Using smaller example time range to avoid "Results from 0 Providers"
time_range_omni = a.Time('2010-01-01', '2010-01-31')  # Example time range within the original range

# Query for the OMNI dataset
query_omni = Fido.search(time_range_omni, instrument_omni)
print("Query results for OMNI dataset:")
print(query_omni)

# Uncomment the following line to fetch the data
# Fido.fetch(query_omni)

# Note: If the queries return a large number of results, consider pagination.
# The user should be aware that large queries might need to be broken down into smaller time ranges.

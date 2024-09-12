# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a

# Context: We want to download data from SOHO/MDI and SDO/HMI for the study of the Sun's magnetic field over two Hale cycles.

# Reasoning:
# 1. We need to query data from SOHO/MDI for the period prior to May 2010.
# 2. We need to query data from SDO/HMI for the period from May 2010 to the present.
# 3. We will use the time range and instrument as the primary attributes for our queries.
# 4. We will print out the query results and comment out the Fido.fetch commands.

# Define the time ranges for the queries
time_range_mdi = a.Time('1996-03-03', '2010-04-30')  # SOHO/MDI data collection period
time_range_hmi = a.Time('2010-05-01', '2023-10-01')  # SDO/HMI data collection period

# Define the instruments
instrument_mdi = a.Instrument('mdi')
instrument_hmi = a.Instrument('hmi')

# Query for SOHO/MDI data
query_mdi = Fido.search(time_range_mdi, instrument_mdi)
print("SOHO/MDI Query Results:")
print(query_mdi)
# Uncomment the following line to fetch the data
# mdi_files = Fido.fetch(query_mdi)

# Query for SDO/HMI data
query_hmi = Fido.search(time_range_hmi, instrument_hmi)
print("SDO/HMI Query Results:")
print(query_hmi)
# Uncomment the following line to fetch the data
# hmi_files = Fido.fetch(query_hmi)
```

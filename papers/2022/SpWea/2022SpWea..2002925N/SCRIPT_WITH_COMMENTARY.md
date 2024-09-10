# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Context: We want to download data from the LASCO instrument on board SOHO for CME observations.
# The time range specified is from May 1996 to the present.

# Reasoning:
# 1. We need to specify the time range for the query.
# 2. We need to specify the instrument as LASCO.
# 3. We will use the Fido module from SunPy to construct and execute the query.
# 4. We will print out the query results and comment out the data fetching part.

# Step 1: Define the time range for the query
time_range = a.Time('1996-05-01', '2023-10-01')  # Adjust the end date as needed

# Step 2: Define the instrument for the query
instrument = a.Instrument('LASCO')

# Step 3: Construct the query using Fido
query = Fido.search(time_range, instrument)

# Step 4: Print out the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
```

This script is designed to query the Virtual Solar Observatory (VSO) for data from the LASCO instrument on board the SOHO spacecraft, specifically for CME observations from May 1996 to the present. The script uses the SunPy library to construct and execute the query, and it prints out the query results. The data fetching command is commented out to prevent automatic downloading.

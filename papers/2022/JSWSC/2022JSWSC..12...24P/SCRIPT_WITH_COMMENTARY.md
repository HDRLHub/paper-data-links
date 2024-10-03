# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import sunpy.net
from sunpy.net import Fido, attrs as a

# Query for GOES/EPS data for SEP event cataloging
# Time Range: 1984 – 2013
# Physical Observable: Proton peak flux and total fluence
# Note: GOES/EPS is not explicitly listed in the provided VSO interface, but we will use GOES as the source.

# Define the time range for the query
time_range_goes_eps = a.Time('1984-01-01', '2013-12-31')

# Define the instrument
instrument_goes_eps = a.Instrument('goes')

# Perform the query
query_goes_eps = Fido.search(time_range_goes_eps, instrument_goes_eps)

# Print the query results
print("GOES/EPS Data for SEP Event Cataloging:")
print(query_goes_eps)

# Uncomment the following line to fetch the data
# files_goes_eps = Fido.fetch(query_goes_eps)

# Query for SOHO/LASCO data for CME identification and characterization
# Time Range: 1997 – 2013
# Physical Observable: CME plane-of-sky speeds and angular widths

# Define the time range for the query
time_range_soho_lasco = a.Time('1997-01-01', '2013-12-31')

# Define the instrument
instrument_soho_lasco = a.Instrument('lasco')

# Perform the query
query_soho_lasco = Fido.search(time_range_soho_lasco, instrument_soho_lasco)

# Print the query results
print("SOHO/LASCO Data for CME Identification and Characterization:")
print(query_soho_lasco)

# Uncomment the following line to fetch the data
# files_soho_lasco = Fido.fetch(query_soho_lasco)

# Query for GOES Solar X-ray (SXR) flux measurements for solar flare recording
# Time Range: 1984 – 2013
# Physical Observable: Solar flare magnitude and location

# Define the time range for the query
time_range_goes_sxr = a.Time('1984-01-01', '2013-12-31')

# Define the instrument
instrument_goes_sxr = a.Instrument('goes')

# Perform the query
query_goes_sxr = Fido.search(time_range_goes_sxr, instrument_goes_sxr)

# Print the query results
print("GOES Solar X-ray (SXR) Flux Measurements for Solar Flare Recording:")
print(query_goes_sxr)

# Uncomment the following line to fetch the data
# files_goes_sxr = Fido.fetch(query_goes_sxr)
```

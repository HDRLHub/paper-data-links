# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
from sunpy.net import Fido, attrs as a

# Define the time range for the query
time_range = a.Time('1996-01-01', '2014-12-31')

# Define the instrument and source
instrument = a.Instrument('LASCO')
source = a.Source('SOHO')

# Query for LASCO C2 and C3 data within the specified time range
query_result = Fido.search(time_range, source, instrument, a.Detector('C2') | a.Detector('C3'))

# Print the query results
print(query_result)

# Uncomment the following line to download the data
# files = Fido.fetch(query_result)
```

This script sets up a query for the LASCO instrument on the SOHO spacecraft, specifically targeting the C2 and C3 detectors, which are relevant for the study of CMEs. The time range is set from 1996 to 2014, as specified in the context. The script prints the query results, and the data download command is commented out, as per the instructions.

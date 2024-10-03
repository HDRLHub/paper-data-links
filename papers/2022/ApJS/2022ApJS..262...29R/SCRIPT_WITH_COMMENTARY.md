# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the query
time_range = a.Time('1986-01-01', '2017-12-31')

# Define the instrument and source
instrument = a.Instrument('sem')
source = a.Source('goes')

# Construct the query
query = Fido.search(time_range, source, instrument)

# Print out the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
```

This script sets up a query to search for data from the Space Environment Monitor (SEM) on board the GOES satellites for the specified time range. The `Fido.search` function is used to perform the query, and the results are printed out. The `Fido.fetch` command is commented out to avoid downloading the data directly.

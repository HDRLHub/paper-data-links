# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
# Context: Scientific Observation Instrumentation Form
# Instruments: SOHO/MDI

# Reasoning: Let's think step by step in order to produce the script. We need to query the VSO for data from the Michelson Doppler Imager (MDI) on board the SOHO spacecraft. The context specifies that we need photospheric magnetogram data from the pre-eruption phase of the CME on December 13, 2006. The exact time provided is 20:51:01 UT on December 12, 2006. We will use the SunPy library to construct and execute this query.

from sunpy.net import Fido
from sunpy.net import attrs as a

# Define the time range for the query
time_range = a.Time('2006-12-12T20:51:01', '2006-12-12T20:51:01')

# Define the instrument and source
instrument = a.Instrument('mdi')
source = a.Source('soho')

# Construct the query
query = Fido.search(time_range, instrument, source)

# Print out the query results
print(query)

# Uncomment the following line to fetch the data
# files = Fido.fetch(query)
```

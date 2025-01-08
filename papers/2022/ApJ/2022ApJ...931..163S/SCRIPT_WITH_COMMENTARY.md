# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
from sunpy.net import Fido, attrs as a

# Query for SHARP data from HMI on SDO
print("Querying SHARP data from HMI on SDO...")
sharp_query = Fido.search(
    a.Time('2010-05-01', '2020-12-01'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Source('SDO')
)
print(sharp_query)
# Uncomment the following line to fetch the data
# sharp_download = Fido.fetch(sharp_query)

# Query for SMARP data from MDI on SOHO
print("Querying SMARP data from MDI on SOHO...")
smarp_query = Fido.search(
    a.Time('1996-04-23', '2010-10-28'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field'),
    a.Source('SOHO')
)
print(smarp_query)
# Uncomment the following line to fetch the data
# smarp_download = Fido.fetch(smarp_query)
```

This script sets up two queries using the `Fido.search` function from SunPy, specifying the time range, instrument, physical observable, and source for each dataset. The results of the queries are printed, and the data fetching commands are commented out.

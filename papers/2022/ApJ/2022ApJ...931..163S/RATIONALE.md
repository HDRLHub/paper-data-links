_This commentary was initially drafted by an AI model. Please use with caution_

produce the script. We need to construct two separate queries for the data products mentioned in the context: SHARP from HMI on SDO and SMARP from MDI on SOHO. The queries will focus on the line-of-sight magnetic field data for the specified time ranges. We will use the `sunpy.net.Fido` module to perform these queries. The key parameters for each query are the time range and the instrument. We will ensure that the instruments and physical observables match those available in the VSO interface.

1. **Query for SHARP data from HMI on SDO:**
   - **Instrument**: HMI
   - **Physical Observable**: Line-of-sight magnetic field
   - **Time Range**: May 1, 2010 – December 1, 2020

2. **Query for SMARP data from MDI on SOHO:**
   - **Instrument**: MDI
   - **Physical Observable**: Line-of-sight magnetic field
   - **Time Range**: April 23, 1996 – October 28, 2010

Now, let's write the Python script using SunPy to perform these queries.

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

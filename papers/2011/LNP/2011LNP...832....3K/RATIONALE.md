_This commentary was initially drafted by an AI model. Please use with caution_

produce the script. We need to create a Python script using SunPy to query the Virtual Solar Observatory (VSO) for data related to the Michelson Doppler Imager (MDI) on the SOHO spacecraft and the Helioseismic and Magnetic Imager (HMI) on the Solar Dynamics Observatory (SDO). The context provides specific time ranges and physical observables for these instruments. We will focus on querying data for the line-of-sight (Doppler) velocity from MDI and solar oscillations and magnetic fields from HMI. The script will use the `Fido` interface from SunPy to construct and execute the queries, and it will print the results. We will not execute the `Fido.fetch` command but will include it as a comment for potential data downloading.

```python
from sunpy.net import Fido, attrs as a

# Query for Michelson Doppler Imager (MDI) on SOHO
# Time Range: 1997-06-19, 02:00 UT
# Physical Observable: Line-of-sight (Doppler) velocity
mdi_query = Fido.search(
    a.Time('1997-06-19 02:00', '1997-06-19 02:10'),  # 10-minute window for demonstration
    a.Instrument('MDI'),
    a.Physobs('LOS_velocity')
)

# Print the results of the MDI query
print("MDI Query Results:")
print(mdi_query)

# Uncomment the following line to fetch the data
# mdi_downloaded_files = Fido.fetch(mdi_query)

# Query for Helioseismic and Magnetic Imager (HMI) on SDO
# Time Range: Starting from 2010-02-11 (launch date)
# Physical Observable: Solar oscillations and magnetic fields
hmi_query = Fido.search(
    a.Time('2010-02-11', '2010-02-12'),  # 1-day window for demonstration
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')  # Example observable, can be adjusted
)

# Print the results of the HMI query
print("HMI Query Results:")
print(hmi_query)

# Uncomment the following line to fetch the data
# hmi_downloaded_files = Fido.fetch(hmi_query)
```

This script sets up two queries: one for the MDI instrument on SOHO for a specific date and time, and another for the HMI instrument on SDO starting from its launch date. The queries are constructed using the `Fido.search` method with appropriate attributes for time, instrument, and physical observable. The results of each query are printed, and the `Fido.fetch` commands are included as comments for potential data retrieval.

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

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

This script sets up two queries using the SunPy library to access data from the Virtual Solar Observatory (VSO). The first query targets the Michelson Doppler Imager (MDI) on the SOHO spacecraft for a specific date and time, focusing on the line-of-sight (Doppler) velocity. The second query targets the Helioseismic and Magnetic Imager (HMI) on the Solar Dynamics Observatory (SDO) starting from its launch date, focusing on solar oscillations and magnetic fields. The results of each query are printed, and the `Fido.fetch` commands are included as comments for potential data retrieval.

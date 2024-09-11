# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Define the time range for the query
time_range = a.Time('2009-01-01', '2019-12-31')

# Define the instruments
instrument_lasco = a.Instrument('LASCO')
instrument_secchi = a.Instrument('SECCHI')

# Define the detectors for SECCHI
detector_cor1 = a.Detector('COR1')
detector_cor2 = a.Detector('COR2')

# Query for LASCO data on SOHO
query_lasco = Fido.search(time_range, instrument_lasco, a.Source('SOHO'))
print("LASCO Query Results:")
print(query_lasco)

# Uncomment the following line to fetch the data
# lasco_files = Fido.fetch(query_lasco)

# Query for SECCHI COR1 data on STEREO-A
query_secchi_cor1_a = Fido.search(time_range, instrument_secchi, detector_cor1, a.Source('STEREO_A'))
print("SECCHI COR1 on STEREO-A Query Results:")
print(query_secchi_cor1_a)

# Uncomment the following line to fetch the data
# secchi_cor1_a_files = Fido.fetch(query_secchi_cor1_a)

# Query for SECCHI COR2 data on STEREO-A
query_secchi_cor2_a = Fido.search(time_range, instrument_secchi, detector_cor2, a.Source('STEREO_A'))
print("SECCHI COR2 on STEREO-A Query Results:")
print(query_secchi_cor2_a)

# Uncomment the following line to fetch the data
# secchi_cor2_a_files = Fido.fetch(query_secchi_cor2_a)

# Query for SECCHI COR1 data on STEREO-B
query_secchi_cor1_b = Fido.search(time_range, instrument_secchi, detector_cor1, a.Source('STEREO_B'))
print("SECCHI COR1 on STEREO-B Query Results:")
print(query_secchi_cor1_b)

# Uncomment the following line to fetch the data
# secchi_cor1_b_files = Fido.fetch(query_secchi_cor1_b)

# Query for SECCHI COR2 data on STEREO-B
query_secchi_cor2_b = Fido.search(time_range, instrument_secchi, detector_cor2, a.Source('STEREO_B'))
print("SECCHI COR2 on STEREO-B Query Results:")
print(query_secchi_cor2_b)

# Uncomment the following line to fetch the data
# secchi_cor2_b_files = Fido.fetch(query_secchi_cor2_b)
```

This script queries the VSO for data from the LASCO instrument on SOHO and the SECCHI instrument on STEREO-A and STEREO-B for the specified time range. The results of the queries are printed, and the `Fido.fetch` commands are commented out.

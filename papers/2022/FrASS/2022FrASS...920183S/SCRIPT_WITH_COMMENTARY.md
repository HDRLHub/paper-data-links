# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query for IRIS data on April 4, 2017
print("Querying IRIS data for April 4, 2017...")
iris_query = Fido.search(
    a.Time('2017-04-04', '2017-04-05'),
    a.Instrument('IRIS')
)
print(iris_query)
# Uncomment the following line to fetch the data
# iris_files = Fido.fetch(iris_query)

# Query for SDO/AIA data on April 4, 2017
print("Querying SDO/AIA data for April 4, 2017...")
aia_query = Fido.search(
    a.Time('2017-04-04', '2017-04-05'),
    a.Instrument('AIA')
)
print(aia_query)
# Uncomment the following line to fetch the data
# aia_files = Fido.fetch(aia_query)

# Query for SDO/HMI data on April 15-16, 2014
print("Querying SDO/HMI data for April 15-16, 2014...")
hmi_query = Fido.search(
    a.Time('2014-04-15', '2014-04-17'),
    a.Instrument('HMI')
)
print(hmi_query)
# Uncomment the following line to fetch the data
# hmi_files = Fido.fetch(hmi_query)

# Query for SOHO/EIT data post-1995 (example date range)
print("Querying SOHO/EIT data for January 1-2, 1996...")
eit_query = Fido.search(
    a.Time('1996-01-01', '1996-01-02'),
    a.Instrument('EIT')
)
print(eit_query)
# Uncomment the following line to fetch the data
# eit_files = Fido.fetch(eit_query)

# Query for SOHO/LASCO data post-1995 (example date range)
print("Querying SOHO/LASCO data for January 1-2, 1996...")
lasco_query = Fido.search(
    a.Time('1996-01-01', '1996-01-02'),
    a.Instrument('LASCO')
)
print(lasco_query)
# Uncomment the following line to fetch the data
# lasco_files = Fido.fetch(lasco_query)
```

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for each instrument
time_range_aia = a.Time('2012-12-07 21:10', '2012-12-07 21:50')
time_range_hmi = a.Time('2012-12-07 21:10', '2012-12-07 21:50')
time_range_euvi = a.Time('2012-12-07 21:05', '2012-12-07 23:05')
time_range_cor2 = a.Time('2012-12-07 22:24', '2012-12-07 23:39')
time_range_lasco_c2 = a.Time('2012-12-07 21:36', '2012-12-07 22:36')
time_range_goes = a.Time('2012-12-07 21:00', '2012-12-07 22:30')

# Define the queries for each instrument
query_aia = Fido.search(time_range_aia, a.Instrument('AIA'), a.Wavelength(131 * u.Angstrom))
query_aia += Fido.search(time_range_aia, a.Instrument('AIA'), a.Wavelength(171 * u.Angstrom))
query_aia += Fido.search(time_range_aia, a.Instrument('AIA'), a.Wavelength(193 * u.Angstrom))
query_aia += Fido.search(time_range_aia, a.Instrument('AIA'), a.Wavelength(211 * u.Angstrom))

query_hmi = Fido.search(time_range_hmi, a.Instrument('HMI'), a.Wavelength(6173 * u.Angstrom))

query_euvi = Fido.search(time_range_euvi, a.Instrument('EUVI'), a.Wavelength(195 * u.Angstrom))

query_cor2 = Fido.search(time_range_cor2, a.Instrument('COR2'))

query_lasco_c2 = Fido.search(time_range_lasco_c2, a.Instrument('LASCO'), a.Detector('C2'))

query_goes = Fido.search(time_range_goes, a.Instrument('GOES'), a.Wavelength(0.5 * u.Angstrom, 4 * u.Angstrom))
query_goes += Fido.search(time_range_goes, a.Instrument('GOES'), a.Wavelength(1 * u.Angstrom, 8 * u.Angstrom))

# Print out the query results
print("AIA Query Results:")
print(query_aia)

print("\nHMI Query Results:")
print(query_hmi)

print("\nEUVI Query Results:")
print(query_euvi)

print("\nCOR2 Query Results:")
print(query_cor2)

print("\nLASCO C2 Query Results:")
print(query_lasco_c2)

print("\nGOES Query Results:")
print(query_goes)

# Uncomment the following lines to fetch the data
# files_aia = Fido.fetch(query_aia)
# files_hmi = Fido.fetch(query_hmi)
# files_euvi = Fido.fetch(query_euvi)
# files_cor2 = Fido.fetch(query_cor2)
# files_lasco_c2 = Fido.fetch(query_lasco_c2)
# files_goes = Fido.fetch(query_goes)
```

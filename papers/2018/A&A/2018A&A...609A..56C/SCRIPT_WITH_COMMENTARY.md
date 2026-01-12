# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
#!/usr/bin/env python3
"""
SunPy VSO Query Script for SOHO/MDI Full-Disk Magnetograms
Context:
  - Instrument: Michelson Doppler Imager (MDI) on board SOHO
  - Physical Observable: Line-of-sight photospheric magnetic field (used for toroidal field derivation)
  - Time Range: 1996-01-30 to 2011-04-12 (full MDI operational period)
"""

from sunpy.net import Fido, attrs as a

# 1. Define the time range for the query.
#    According to the VSO interface, MDI LOS magnetic field data are available
#    from 1996-01-30 through 2011-04-12.
start_time = "1996-01-30"
end_time   = "2011-04-12"
time_range = a.Time(start_time, end_time)

# 2. Specify the data source and instrument.
#    We're querying the SOHO mission's MDI instrument.
source     = a.Source('SOHO')
instrument = a.Instrument('MDI')

# 3. Specify the physical observable.
#    We want the line-of-sight magnetic field data (used to derive the toroidal field).
physobs    = a.Physobs('LOS_magnetic_field')

# 4. Perform the search.
mdi_query = Fido.search(time_range, source, instrument, physobs)

# 5. Display the search results.
#    This will print a table of files available in the specified time range.
print(mdi_query)

# 6. (Optional) Fetch the data.
#    Uncomment the following line to download the files returned by the query.
# mdi_downloaded_files = Fido.fetch(mdi_query)
```

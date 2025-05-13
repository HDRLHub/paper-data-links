# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query for solar observations that
are referenced in the paper. The paper compares extreme-ultraviolet (EUV) jet
observations from the Atmospheric Imaging Assembly (AIA) onboard SDO with
coronagraph imaging from the LASCO C2 instrument onboard SOHO during the solar
eclipse on 2017 August 21.

According to the paper:
    - SDO/AIA data (Source: SDO, Instrument: AIA) were used to track EUV jets 
      using filters at 211 Å and 193 Å.
    - SOHO/LASCO C2 data (Source: SOHO, Instrument: LASCO, Detector: C2) were
      used to capture the white-light corona at high altitudes.
      
The query time interval chosen here covers the period from 16:00 UT to 19:00 UT 
on 2017 August 21, which spans the key jet events.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the observations
start_time = '2017-08-21T16:00:00'
end_time = '2017-08-21T19:00:00'

# -----------------------------------------------------------------------------
# Query 1: SDO/AIA EUV data at 211 Å
#
# The AIA instrument on board SDO provides high-cadence EUV images.
# In the study, the 211 Å filter was used to monitor the evolution of solar jets.
# -----------------------------------------------------------------------------
query_aia_211 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(211*u.AA)
)

print("SDO/AIA 211 Å Query Results:")
print(query_aia_211)

# -----------------------------------------------------------------------------
# Query 2: SDO/AIA EUV data at 193 Å
#
# The 193 Å filter is also utilized in the paper to judge the EUV brightness
# enhancements corresponding to jet events.
# -----------------------------------------------------------------------------
query_aia_193 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(193*u.AA)
)

print("\nSDO/AIA 193 Å Query Results:")
print(query_aia_193)

# -----------------------------------------------------------------------------
# Query 3: SOHO/LASCO C2 coronagraph data
#
# The LASCO C2 coronagraph on board SOHO captures the white-light corona 
# (via Thomson scattering) from about 2 R⊙ up to 6 R⊙. The available detector
# for this instrument is C2, and its data are used to track the propagation 
# of jets at larger altitudes.
# -----------------------------------------------------------------------------
query_lasco_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

print("\nSOHO/LASCO C2 Query Results:")
print(query_lasco_c2)

# -----------------------------------------------------------------------------
# The following Fido.fetch commands are commented out to prevent data download
# during testing. When ready to download the data, simply uncomment these lines.
# -----------------------------------------------------------------------------
# fetched_aia_211 = Fido.fetch(query_aia_211)
# fetched_aia_193 = Fido.fetch(query_aia_193)
# fetched_lasco_c2 = Fido.fetch(query_lasco_c2)

if __name__ == '__main__':
    print("\nQueries executed successfully. Review the printed query results for more details.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO)
using SunPy’s Fido interface for solar data relevant to the paper’s analysis.
We construct separate queries for:
  1. Pre-2010 observations with SOHO instruments (EIT and MDI) to cover the 1996–2005 interval.
  2. Post-2010 observations with SDO instruments (AIA and HMI) to capture the September 2017 events.

Note:
- For SOHO/EIT, we select the 195 Å channel.
- For SDO/AIA, although the paper uses 193 Å images, the available wavelengths for AIA in the VSO interface
  include a range (191.0 - 195.0 Å); we choose 193 Å which lies in the acceptable range.
- The only required query parameters here are the time range and the instrument.
- Fido.fetch commands remain commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a
from datetime import datetime

# ------------------------------
# Query 1: SOHO/EIT Data (1996–2005)
# ------------------------------
# Time range: 1996 January 1 to 2005 December 31 based on the paper (EIT observations during 1996–2005)
eit_time_start = "1996-01-01"
eit_time_end = "2005-12-31"
# Instrument: EIT on board SOHO, wavelength 195 Å
eit_query = Fido.search(
    a.Time(eit_time_start, eit_time_end),
    a.Source("SOHO"),
    a.Instrument("EIT"),
    a.Wavelength(195 * u.angstrom)
)

print("SOHO/EIT query results (1996-2005):")
print(eit_query)
# Uncomment the next line to download the files
#eit_files = Fido.fetch(eit_query)


# ------------------------------
# Query 2: SOHO/MDI Data (1996–2005)
# ------------------------------
# Time range: 1996 January 1 to 2005 December 31 for SOHO MDI magnetogram data.
mdi_time_start = "1996-01-01"
mdi_time_end = "2005-12-31"
# Instrument: MDI on board SOHO. We rely on default and time range as MDI measurements are available for multiple physobs.
mdi_query = Fido.search(
    a.Time(mdi_time_start, mdi_time_end),
    a.Source("SOHO"),
    a.Instrument("MDI")
)

print("\nSOHO/MDI query results (1996-2005):")
print(mdi_query)
# Uncomment the next line to download the files
#mdi_files = Fido.fetch(mdi_query)


# ------------------------------
# Query 3: SDO/AIA Data for September 2017 Event
# ------------------------------
# Time range: For example the flare SOL2017-09-04T20:33 event;
# we choose a short interval surrounding the flare peak.
aia_time_start = "2017-09-04T20:00:00"
aia_time_end = "2017-09-04T20:40:00"
# Instrument: AIA on board SDO; choose wavelength 193 Å (part of available 191.0-195.0 Å range)
aia_query = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.angstrom)
)

print("\nSDO/AIA query results for September 4, 2017 event:")
print(aia_query)
# Uncomment the next line to download the files
#aia_files = Fido.fetch(aia_query)


# ------------------------------
# Query 4: SDO/HMI Data for September 2017 Event
# ------------------------------
# Time range: same as for AIA to capture the magnetogram snapshot just before the eruption.
hmi_time_start = "2017-09-04T20:00:00"
hmi_time_end = "2017-09-04T20:40:00"
# Instrument: HMI on board SDO; HMI provides the line-of-sight magnetic field measurements.
hmi_query = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source("SDO"),
    a.Instrument("HMI")
)

print("\nSDO/HMI query results for September 4, 2017 event:")
print(hmi_query)
# Uncomment the next line to download the files
#hmi_files = Fido.fetch(hmi_query)


if __name__ == "__main__":
    print("\nQueries complete. Review the printed query results to verify data availability.")

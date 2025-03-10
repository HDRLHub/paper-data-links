# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to construct several data queries of instruments used in the paper.
In this study, two stealth CME events are considered:
  Event 1 (27 October 2009): Observations from SOHO/EIT (EUV imaging at 195 Å) and SOHO/MDI (photospheric magnetograms).
  Event 2 (03 March 2011): Observations from SDO/AIA (multi-wavelength EUV imaging), SOHO/LASCO (white‐light coronagraph with C2 detector),
                           and SDO/HMI (photospheric magnetograms).

Note:
  - Only the time ranges and instruments are specified here.
  - Some instruments mentioned in the context (e.g., STEREO/ EUVI and COR1, and Nancay Radioheliograph) are not available in the provided VSO interface.
  - Fido.fetch commands are provided but commented out. They can be enabled if needed.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# -----------------------------
# Event 1: Stealth Event 1 on 27 October 2009 (SOHO instruments)
# -----------------------------

# Query 1a: SOHO/EIT data at 195 Å (EUV imaging)
eit_time_start = "2009-10-27T00:00:00"
eit_time_end   = "2009-10-27T23:59:59"
# The wavelength is set to 195 Å based on the context
query_eit = Fido.search(
    a.Time(eit_time_start, eit_time_end),
    a.Source("SOHO"),
    a.Instrument("EIT"),
    a.Wavelength(195 * u.Angstrom)
)
print("Query Results for SOHO/EIT (195 Å) on 27 October 2009:")
print(query_eit)
# To download the data, you would use:
# files_eit = Fido.fetch(query_eit)

# Query 1b: SOHO/MDI magnetogram (photospheric magnetic field – using LOS_magnetic_field)
mdi_time_start = "2009-10-27T00:00:00"
mdi_time_end   = "2009-10-27T23:59:59"
query_mdi = Fido.search(
    a.Time(mdi_time_start, mdi_time_end),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Physobs("LOS_magnetic_field")
)
print("\nQuery Results for SOHO/MDI (LOS magnetic field) on 27 October 2009:")
print(query_mdi)
# To download the data, you would use:
# files_mdi = Fido.fetch(query_mdi)

# -----------------------------
# Event 2: Stealth Event 2 on 03 March 2011 (SDO and SOHO instruments)
# -----------------------------

# Query 2a: SDO/AIA EUV imaging data.
# Based on the context, AIA wavebands used include 94, 131, 171, 193, 211, and 304 Å.
# Here we choose 94 Å as an example.
aia_time_start = "2011-03-03T00:00:00"
aia_time_end   = "2011-03-03T23:59:59"
query_aia = Fido.search(
    a.Time(aia_time_start, aia_time_end),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(94 * u.Angstrom)
)
print("\nQuery Results for SDO/AIA (94 Å) on 03 March 2011:")
print(query_aia)
# To download the data, you would use:
# files_aia = Fido.fetch(query_aia)

# Query 2b: SDO/HMI magnetogram data (photospheric magnetic field observations)
hmi_time_start = "2011-03-03T00:00:00"
hmi_time_end   = "2011-03-03T23:59:59"
query_hmi = Fido.search(
    a.Time(hmi_time_start, hmi_time_end),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)
print("\nQuery Results for SDO/HMI (LOS magnetic field) on 03 March 2011:")
print(query_hmi)
# To download the data, you would use:
# files_hmi = Fido.fetch(query_hmi)

# Query 2c: SOHO/LASCO data using the C2 detector (white-light coronagraph; no specific wavelength required)
lasco_time_start = "2011-03-03T00:00:00"
lasco_time_end   = "2011-03-03T23:59:59"
query_lasco = Fido.search(
    a.Time(lasco_time_start, lasco_time_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nQuery Results for SOHO/LASCO C2 on 03 March 2011:")
print(query_lasco)
# To download the data, you would use:
# files_lasco = Fido.fetch(query_lasco)

if __name__ == '__main__':
    print("\nAll queries have been executed. Please review the results above.")

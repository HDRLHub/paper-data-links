# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy to query the Virtual Solar Observatory (VSO)
for specific solar data that are used in the context of constraining
CME properties via multiple observational instruments. The queries
include:
  1. SDO-AIA EUV images at ~193 Å (using the wavelength range 191-195 Å)
     recorded at 16:21 UT on 7 March 2011 (post-eruption arcade observation).
  2. SDO-HMI line-of-sight magnetograms recorded at 13:00 UT on 7 March 2011
     (for pre-eruption magnetic flux estimation in the active region).
  3. SOHO LASCO/C2 coronagraph white-light image at 14:54 UT on 7 March 2011
     (as part of the multi-viewpoint white-light observations of the CME).
     
Note: In this script, the actual Fido.fetch commands are commented out.
Only query results are printed.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# -----------------------------------------------------------------------------
# Query 1: SDO-AIA 193 Å EUV data for observing the post-eruption arcade.
# The available wavelengths for AIA include the range 191.0 - 195.0 Å,
# which covers the desired 193 Å channel.
# -----------------------------------------------------------------------------
print("Querying SDO-AIA EUV data (193 Å) for 7 Mar 2011 at 16:21 UT ...")
aia_query = Fido.search(
    a.Time("2011-03-07T16:21:00", "2011-03-07T16:21:00"),
    a.Instrument("AIA"),
    a.Wavelength(191*u.angstrom, 195*u.angstrom)
)
print(aia_query)

# Uncomment the following line to download the AIA data:
# files_aia = Fido.fetch(aia_query)

# -----------------------------------------------------------------------------
# Query 2: SDO-HMI line-of-sight magnetograms for pre-eruption magnetic field.
# This query targets the LOS magnetogram observation at 13:00 UT on 7 Mar 2011,
# which is used to estimate the unsigned (reconnected) magnetic flux.
# -----------------------------------------------------------------------------
print("\nQuerying SDO-HMI LOS magnetogram data for 7 Mar 2011 at 13:00 UT ...")
hmi_query = Fido.search(
    a.Time("2011-03-07T13:00:00", "2011-03-07T13:00:00"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)
print(hmi_query)

# Uncomment the following line to download the HMI data:
# files_hmi = Fido.fetch(hmi_query)

# -----------------------------------------------------------------------------
# Query 3: SOHO LASCO coronagraph C2 white-light data for CME imaging.
# The query is for a white-light image at 14:54 UT on 7 Mar 2011. We choose
# the LASCO C2 detector because it is available from 1995/12/08 to present.
# -----------------------------------------------------------------------------
print("\nQuerying SOHO LASCO/C2 coronagraph data for 7 Mar 2011 at 14:54 UT ...")
soho_query = Fido.search(
    a.Time("2011-03-07T14:54:00", "2011-03-07T14:54:00"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)
print(soho_query)

# Uncomment the following line to download the SOHO LASCO data:
# files_soho = Fido.fetch(soho_query)

if __name__ == "__main__":
    print("\nAll queries executed. Review the printed query results above.")

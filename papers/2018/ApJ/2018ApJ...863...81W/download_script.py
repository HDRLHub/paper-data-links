# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client to query observations for multiple instruments based on the context 
of a solar eruption event on November 4, 2015.

The queries include:
1. SDO/AIA EUV images in the 131 Å and 304 Å channels (observing the hot flux rope and filament evolution)
   during the pre-eruptive and early eruption phase between 13:20 UT and 13:33 UT.
2. SDO/HMI magnetogram observations – a snapshot at 13:22:57 UT and a flow map period from 07:00 UT to 12:00 UT 
   to capture the photospheric magnetic field evolution.
3. SOHO/LASCO C2 coronagraph observations near 14:48 UT to capture the early CME emergence.

Note: This script prints out the query results. The Fido.fetch commands are provided as comments.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------
# Query 1: SDO/AIA 131 Å images
# -----------------------------
# Set the pre-eruption observation time range
aia_start_time = "2015-11-04T13:20:00"
aia_end_time = "2015-11-04T13:33:00"
# Query for AIA images, filtering around 131 Å (using a narrow band around 131 Å)
print("Querying SDO/AIA 131 Å images from {} to {}...".format(aia_start_time, aia_end_time))
query_aia_131 = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Instrument("AIA"),
    a.Wavelength(130 * u.AA, 132 * u.AA)
)
print(query_aia_131)
# To fetch the data, uncomment the following line:
# files_aia_131 = Fido.fetch(query_aia_131)

# -----------------------------
# Query 2: SDO/AIA 304 Å images
# -----------------------------
# Query for AIA images filtering for 304 Å channel (used for imaging the filament)
print("Querying SDO/AIA 304 Å images from {} to {}...".format(aia_start_time, aia_end_time))
query_aia_304 = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Instrument("AIA"),
    a.Wavelength(303 * u.AA, 305 * u.AA)
)
print(query_aia_304)
# To fetch the data, uncomment the following line:
# files_aia_304 = Fido.fetch(query_aia_304)

# --------------------------------------
# Query 3: SDO/HMI magnetogram snapshot
# --------------------------------------
# Query for an HMI snapshot magnetogram at 13:22:57 UT to capture the magnetic configuration
hmi_snapshot_time = "2015-11-04T13:22:57"
print("Querying SDO/HMI magnetogram snapshot at {}...".format(hmi_snapshot_time))
query_hmi_snapshot = Fido.search(
    a.Time(hmi_snapshot_time, hmi_snapshot_time),
    a.Instrument("HMI")
)
print(query_hmi_snapshot)
# To fetch the data, uncomment the following line:
# files_hmi_snapshot = Fido.fetch(query_hmi_snapshot)

# --------------------------------------------------------
# Query 4: SDO/HMI magnetogram data for a flow map period
# --------------------------------------------------------
# Query for HMI data from 07:00 UT to 12:00 UT on November 4, 2015 to study converging flows and flux cancellation
hmi_flow_start = "2015-11-04T07:00:00"
hmi_flow_end   = "2015-11-04T12:00:00"
print("Querying SDO/HMI data for flow mapping from {} to {}...".format(hmi_flow_start, hmi_flow_end))
query_hmi_flow = Fido.search(
    a.Time(hmi_flow_start, hmi_flow_end),
    a.Instrument("HMI")
)
print(query_hmi_flow)
# To fetch the data, uncomment the following line:
# files_hmi_flow = Fido.fetch(query_hmi_flow)

# --------------------------------------------
# Query 5: SOHO/LASCO C2 coronagraph observations
# --------------------------------------------
# Query for LASCO C2 coronagraph data starting at 14:48 UT to capture the early phase of the CME
lasco_start = "2015-11-04T14:48:00"
lasco_end   = "2015-11-04T14:50:00"  # small time window around the reported time
print("Querying SOHO/LASCO C2 data from {} to {}...".format(lasco_start, lasco_end))
query_lasco = Fido.search(
    a.Time(lasco_start, lasco_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print(query_lasco)
# To fetch the data, uncomment the following line:
# files_lasco = Fido.fetch(query_lasco)

if __name__ == "__main__":
    print("All queries have been executed. Review the printed query objects for details.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data for a study on solar dynamic events
observed on 18 July 2014. The queries target three instruments: 
1. AIA (Atmospheric Imaging Assembly on SDO) for EUV imaging,
2. HMI (Helioseismic Magnetic Imager on SDO) for photospheric magnetic field observations,
3. LASCO C2 (on SOHO) for coronagraph observations of CMEs.

The queries are constructed based on the time stamps and wavelength filters as reported in the paper.
Note: The Fido.fetch commands are included as comments and are not executed.
"""

from sunpy.net import Fido, attrs as a
from astropy.time import Time

# -------------------------
# 1. Query for AIA observations (SDO/AIA)
# -------------------------
# a) Early interaction and reconnection signatures: 
#    - Time: 18 July 2014 at 05:12 UT (small time interval chosen)
#    - Wavelength: 171 Å (to capture bright loops as indicated in the study)
time_start_aia_early = "2014-07-18T05:12:00"
time_end_aia_early = "2014-07-18T05:20:00"  # 8-minute window around the event

# Constructing query for AIA early interaction data with wavelength 171 Å
query_aia_early = Fido.search(
    a.Time(time_start_aia_early, time_end_aia_early),
    a.Instrument("AIA"),
    a.Wavelength(171*u.AA, 171*u.AA)
)
print("AIA early interaction query results:")
print(query_aia_early)
# To fetch the data:
# files_aia_early = Fido.fetch(query_aia_early)

# b) Pre-eruption and post-eruption imaging:
#    - Pre-eruption AIA: around 07:04 UT on 18 July 2014 (wavelength 171 and 193 Å)
#    - Post-eruption AIA: around 08:59 UT on 18 July 2014 (wavelength 171 and 193 Å)

# Pre-eruption query for AIA (171 Å)
time_start_aia_pre = "2014-07-18T07:04:00"
time_end_aia_pre = "2014-07-18T07:10:00"  # short time window near the observation time
query_aia_pre_171 = Fido.search(
    a.Time(time_start_aia_pre, time_end_aia_pre),
    a.Instrument("AIA"),
    a.Wavelength(171*u.AA, 171*u.AA)
)
print("\nAIA pre-eruption (171 Å) query results:")
print(query_aia_pre_171)
# To fetch the data:
# files_aia_pre_171 = Fido.fetch(query_aia_pre_171)

# Pre-eruption query for AIA (193 Å)
query_aia_pre_193 = Fido.search(
    a.Time(time_start_aia_pre, time_end_aia_pre),
    a.Instrument("AIA"),
    a.Wavelength(193*u.AA, 193*u.AA)
)
print("\nAIA pre-eruption (193 Å) query results:")
print(query_aia_pre_193)
# To fetch the data:
# files_aia_pre_193 = Fido.fetch(query_aia_pre_193)

# Post-eruption query for AIA (171 Å)
time_start_aia_post = "2014-07-18T08:59:00"
time_end_aia_post = "2014-07-18T09:05:00"  # short window after eruption onset
query_aia_post_171 = Fido.search(
    a.Time(time_start_aia_post, time_end_aia_post),
    a.Instrument("AIA"),
    a.Wavelength(171*u.AA, 171*u.AA)
)
print("\nAIA post-eruption (171 Å) query results:")
print(query_aia_post_171)
# To fetch the data:
# files_aia_post_171 = Fido.fetch(query_aia_post_171)

# Post-eruption query for AIA (193 Å)
query_aia_post_193 = Fido.search(
    a.Time(time_start_aia_post, time_end_aia_post),
    a.Instrument("AIA"),
    a.Wavelength(193*u.AA, 193*u.AA)
)
print("\nAIA post-eruption (193 Å) query results:")
print(query_aia_post_193)
# To fetch the data:
# files_aia_post_193 = Fido.fetch(query_aia_post_193)


# -------------------------
# 2. Query for HMI observations (SDO/HMI)
# -------------------------
# HMI observations for capturing photospheric magnetic field evolution.
# Two times are highlighted in the paper:
#    - 03:30 UT on 18 July 2014 (initial magnetogram showing the filament)
#    - 05:55 UT on 18 July 2014 (rotated images for observer's view)
# Here we choose a small time window around each event for clarity.
# Note: HMI typically observes in the Fe I 6173 Å line.
from astropy import units as u

# Query for HMI observation at 03:30 UT
time_start_hmi_early = "2014-07-18T03:30:00"
time_end_hmi_early = "2014-07-18T03:35:00"
query_hmi_early = Fido.search(
    a.Time(time_start_hmi_early, time_end_hmi_early),
    a.Instrument("HMI")
)
print("\nHMI early observation query results:")
print(query_hmi_early)
# To fetch the data:
# files_hmi_early = Fido.fetch(query_hmi_early)

# Query for HMI observation at 05:55 UT
time_start_hmi_later = "2014-07-18T05:55:00"
time_end_hmi_later = "2014-07-18T06:00:00"
query_hmi_later = Fido.search(
    a.Time(time_start_hmi_later, time_end_hmi_later),
    a.Instrument("HMI")
)
print("\nHMI later observation query results:")
print(query_hmi_later)
# To fetch the data:
# files_hmi_later = Fido.fetch(query_hmi_later)


# -------------------------
# 3. Query for LASCO C2 observations (SOHO/LASCO)
# -------------------------
# LASCO C2 coronagraph observations are used to monitor the evolution of CMEs.
# Two CME observation times are highlighted:
#    - First CME: ≈09:35 UT on 18 July 2014
#    - Second CME: ≈11:50 UT on 18 July 2014
# The available time ranges for LASCO C2 are:
#   "1995/12/08 - present" so the dates are valid.

# Query for first CME observation using LASCO C2
time_start_lasco1 = "2014-07-18T09:35:00"
time_end_lasco1 = "2014-07-18T09:45:00"  # allow a short interval to capture the event
query_lasco1 = Fido.search(
    a.Time(time_start_lasco1, time_end_lasco1),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nLASCO C2 first CME query results:")
print(query_lasco1)
# To fetch the data:
# files_lasco1 = Fido.fetch(query_lasco1)

# Query for second CME observation using LASCO C2
time_start_lasco2 = "2014-07-18T11:50:00"
time_end_lasco2 = "2014-07-18T12:00:00"
query_lasco2 = Fido.search(
    a.Time(time_start_lasco2, time_end_lasco2),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nLASCO C2 second CME query results:")
print(query_lasco2)
# To fetch the data:
# files_lasco2 = Fido.fetch(query_lasco2)

# End of script.
if __name__ == "__main__":
    print("\nAll queries have been executed and their results printed above.")

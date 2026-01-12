# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to construct and print Sunpy VSO queries
for downloading solar observational data associated with a solar eruption.
It uses the Sun Dynamics Observatory (SDO)/AIA data to capture multi-wavelength EUV
observations during the eruptive event, the PROBA2/SWAP data at 171 Å for complementary
EUV imaging, and SOHO/LASCO C2 white-light coronagraph data to track the CME outer corona.
The time period is chosen based on the event description in the context (2014 June 15,
from flare onset and initial eruption around 11:20 UT up to the later phase at ~13:04 UT,
with an additional LASCO C2 observation near 13:12 UT).
Only the time range and instrument parameters are explicitly used in the query.
"""

# Import required modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------
# Define the observation time ranges
# ---------------------------
# For the AIA observations, we use the full eruption period from ~11:20 UT to ~13:04 UT
start_time_aia = "2014-06-15T11:20:00"
end_time_aia   = "2014-06-15T13:04:00"

# For SWAP, we assume a similar time range as the EUV signatures are concurrent with the AIA observations
start_time_swap = start_time_aia
end_time_swap   = end_time_aia

# For LASCO C2, we target a snapshot near 13:12 UT when the CME’s outer structure is evident
time_lasco = "2014-06-15T13:12:00"

# ---------------------------
# Query 1: SDO/AIA data (EUV intensity at multiple wavelengths)
# ---------------------------
# We query four different wavelength channels used in the analysis (131 Å, 94 Å, 171 Å, 304 Å).
# For each channel, we use a narrow wavelength window (±0.5 Å) to get the appropriate data.
query_aia_131 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Physobs("intensity"),
    a.Wavelength(130.5 * u.angstrom, 131.5 * u.angstrom)
)
query_aia_94 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Physobs("intensity"),
    a.Wavelength(93.5 * u.angstrom, 94.5 * u.angstrom)
)
query_aia_171 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Physobs("intensity"),
    a.Wavelength(170.5 * u.angstrom, 171.5 * u.angstrom)
)
query_aia_304 = Fido.search(
    a.Time(start_time_aia, end_time_aia),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Physobs("intensity"),
    a.Wavelength(303.5 * u.angstrom, 304.5 * u.angstrom)
)

# Print out the query results for AIA
print("SDO/AIA 131 Å query results:")
print(query_aia_131)
print("\nSDO/AIA 94 Å query results:")
print(query_aia_94)
print("\nSDO/AIA 171 Å query results:")
print(query_aia_171)
print("\nSDO/AIA 304 Å query results:")
print(query_aia_304)

# Uncomment the following lines to fetch the data (disabled by default)
# aia_131_files = Fido.fetch(query_aia_131)
# aia_94_files = Fido.fetch(query_aia_94)
# aia_171_files = Fido.fetch(query_aia_171)
# aia_304_files = Fido.fetch(query_aia_304)

# ---------------------------
# Query 2: PROBA2/SWAP data (EUV intensity at 171 Å)
# ---------------------------
# SWAP provides single-passband imaging near 171 Å.
query_swap = Fido.search(
    a.Time(start_time_swap, end_time_swap),
    a.Source("PROBA2"),
    a.Instrument("SWAP"),
    a.Physobs("intensity"),
    # The available wavelength range for SWAP is 171.0 - 174.0 Å,
    # so we select a narrow window near 171 Å.
    a.Wavelength(170.5 * u.angstrom, 171.5 * u.angstrom)
)

# Print out the query result for SWAP
print("\nPROBA2/SWAP 171 Å query results:")
print(query_swap)

# Uncomment the following line to fetch the SWAP data
# swap_files = Fido.fetch(query_swap)

# ---------------------------
# Query 3: SOHO/LASCO C2 data (White-Light Coronagraph Imaging)
# ---------------------------
# LASCO C2 observations capture the CME outer structure.
query_lasco = Fido.search(
    a.Time(time_lasco, time_lasco),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Physobs("intensity")
)

# Print out the query result for LASCO C2
print("\nSOHO/LASCO C2 query results:")
print(query_lasco)

# Uncomment the following line to fetch the LASCO C2 data
# lasco_files = Fido.fetch(query_lasco)

if __name__ == '__main__':
    print("\nSunpy VSO queries constructed successfully.")

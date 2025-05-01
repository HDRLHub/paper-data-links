# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client (Fido) to query data relevant to the analysis in the paper.
It queries observations from SDO/AIA capturing both a confined X2.2 flare and an eruptive X9.3 flare,
as well as complementary observations from SDO/HMI (magnetograms) and SOHO/LASCO (coronagraph data).
The time ranges and wavelengths are chosen based on the flare timings and passbands discussed in the paper.
Note: The Fido.fetch commands are commented out.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# ------------------------------
# Query 1: SDO/AIA data for the confined X2.2 flare
# Observing the hot channels and flare ribbons in 94 Å, 131 Å, and 1600 Å.
# Flare timing: SOL2017-09-06T08:57 UT
confined_start = "2017-09-06T08:55:00"  # a few minutes before the flare onset
confined_end   = "2017-09-06T09:05:00"  # a few minutes after the flare onset

# Query for 94 Å data (captures the hot channel manifestations)
query_aia_confined_94 = Fido.search(
    a.Time(confined_start, confined_end),
    a.Instrument("AIA"),
    a.Wavelength(94*u.AA)
)
print("SDO/AIA confined flare query for 94 Å results:")
print(query_aia_confined_94)

# Query for 131 Å data (additional hot channel indication)
query_aia_confined_131 = Fido.search(
    a.Time(confined_start, confined_end),
    a.Instrument("AIA"),
    a.Wavelength(131*u.AA)
)
print("SDO/AIA confined flare query for 131 Å results:")
print(query_aia_confined_131)

# Query for 1600 Å data (captures the flare ribbons)
query_aia_confined_1600 = Fido.search(
    a.Time(confined_start, confined_end),
    a.Instrument("AIA"),
    a.Wavelength(1600*u.AA)
)
print("SDO/AIA confined flare query for 1600 Å results:")
print(query_aia_confined_1600)

# Uncomment to download the data
# files_confined_94 = Fido.fetch(query_aia_confined_94)
# files_confined_131 = Fido.fetch(query_aia_confined_131)
# files_confined_1600 = Fido.fetch(query_aia_confined_1600)


# ------------------------------
# Query 2: SDO/AIA data for the eruptive X9.3 flare
# Observing the hot channel eruption, post-flare dimmings, and ribbon separation.
# Flare timing: SOL2017-09-06T11:53 UT
eruptive_start = "2017-09-06T11:50:00"  # slightly before the flare onset
eruptive_end   = "2017-09-06T12:00:00"  # slightly after the flare onset

# Query for 94 Å data (continuing to capture the hot channel dynamics)
query_aia_eruptive_94 = Fido.search(
    a.Time(eruptive_start, eruptive_end),
    a.Instrument("AIA"),
    a.Wavelength(94*u.AA)
)
print("SDO/AIA eruptive flare query for 94 Å results:")
print(query_aia_eruptive_94)

# Query for 211 Å data (shows clear post-flare dimmings)
query_aia_eruptive_211 = Fido.search(
    a.Time(eruptive_start, eruptive_end),
    a.Instrument("AIA"),
    a.Wavelength(211*u.AA)
)
print("SDO/AIA eruptive flare query for 211 Å results:")
print(query_aia_eruptive_211)

# Query for 304 Å data (provides additional context for coronal response)
query_aia_eruptive_304 = Fido.search(
    a.Time(eruptive_start, eruptive_end),
    a.Instrument("AIA"),
    a.Wavelength(304*u.AA)
)
print("SDO/AIA eruptive flare query for 304 Å results:")
print(query_aia_eruptive_304)

# Query for 1600 Å data (flare ribbons, similar as during the confined flare)
query_aia_eruptive_1600 = Fido.search(
    a.Time(eruptive_start, eruptive_end),
    a.Instrument("AIA"),
    a.Wavelength(1600*u.AA)
)
print("SDO/AIA eruptive flare query for 1600 Å results:")
print(query_aia_eruptive_1600)

# Uncomment to download the data
# files_eruptive_94 = Fido.fetch(query_aia_eruptive_94)
# files_eruptive_211 = Fido.fetch(query_aia_eruptive_211)
# files_eruptive_304 = Fido.fetch(query_aia_eruptive_304)
# files_eruptive_1600 = Fido.fetch(query_aia_eruptive_1600)


# ------------------------------
# Query 3: SDO/HMI Vector Magnetograms (SHARP) during the evolution period
# Provides the photospheric magnetic field measurements used in NLFFF extrapolations.
# Here we use a broader time range covering both events.
hmi_start = "2017-09-06T08:30:00"
hmi_end   = "2017-09-06T12:30:00"

query_hmi = Fido.search(
    a.Time(hmi_start, hmi_end),
    a.Instrument("HMI")
)
print("SDO/HMI query for magnetic field data results:")
print(query_hmi)

# Uncomment to download the HMI data
# files_hmi = Fido.fetch(query_hmi)


# ------------------------------
# Query 4: SOHO/LASCO coronagraph data for CME observations during the eruptive flare
# LASCO/C2 is used here to monitor the bright, halo CME.
# Using a time range that accounts for the CME observation related to SOL2017-09-06T11:53 UT.
lasco_start = "2017-09-06T11:45:00"
lasco_end   = "2017-09-06T12:30:00"

query_lasco = Fido.search(
    a.Time(lasco_start, lasco_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("SOHO/LASCO (C2) query for CME observations results:")
print(query_lasco)

# Uncomment to download the LASCO data
# files_lasco = Fido.fetch(query_lasco)


if __name__ == "__main__":
    print("Data queries have been executed. Inspect the printed query results for details.")

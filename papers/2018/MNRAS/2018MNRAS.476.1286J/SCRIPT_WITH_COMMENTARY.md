# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query solar data using SunPy's VSO client.
In this example we query for data from the Atmospheric Imaging Assembly (AIA)
and the Helioseismic and Magnetic Imager (HMI) onboard SDO that were used in a study
of a helical blowout jet on 2016 January 9. The queries focus solely on the required
values: time ranges and instrument names, as specified by the VSO interface.
Note that while the paper also used data from NSO-GONG and SOHO LASCO,
those instruments are not available in the provided VSO interface and therefore are omitted.
Each Fido.fetch command is commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the SDO source attribute common to both instruments
source_sdo = a.Source("SDO")

###############################################################################
# Query 1: AIA observation of the mini-filament and initial eruption at ~13:15 UT
# Time Range: Around 13:15 UT on 2016 January 9
# Wavelengths: 171 Å and 193 Å
###############################################################################
time_initial = a.Time("2016-01-09T13:14:00", "2016-01-09T13:16:00")
instrument_aia = a.Instrument("AIA")
wavelength_171 = a.Wavelength(171*u.AA, 171*u.AA)
wavelength_193 = a.Wavelength(193*u.AA, 193*u.AA)

print("Querying AIA data for the initial mini-filament eruption (channels 171 Å and 193 Å)...")

# Query for AIA 171 Å data
result_aia_171 = Fido.search(time_initial, source_sdo, instrument_aia, wavelength_171)
print("\nAIA 171 Å query result:")
print(result_aia_171)
# To download the data, uncomment the following line:
# files_aia_171 = Fido.fetch(result_aia_171)

# Query for AIA 193 Å data
result_aia_193 = Fido.search(time_initial, source_sdo, instrument_aia, wavelength_193)
print("\nAIA 193 Å query result:")
print(result_aia_193)
# To download the data, uncomment the following line:
# files_aia_193 = Fido.fetch(result_aia_193)

###############################################################################
# Query 2: AIA hot plasma brightening (jet formation phase) around 13:43 UT
# Time Range: 13:42 UT to 13:44 UT on 2016 January 9
# Wavelengths: 94 Å, 131 Å (for hot plasma) and 1600 Å (for ribbon structures)
###############################################################################
time_hot = a.Time("2016-01-09T13:42:00", "2016-01-09T13:44:00")
wavelength_94 = a.Wavelength(94*u.AA, 94*u.AA)
wavelength_131 = a.Wavelength(131*u.AA, 131*u.AA)
wavelength_1600 = a.Wavelength(1600*u.AA, 1600*u.AA)

print("\nQuerying AIA data for hot plasma brightening (channels 94 Å, 131 Å, and 1600 Å)...")

# Query for AIA 94 Å data
result_aia_94 = Fido.search(time_hot, source_sdo, instrument_aia, wavelength_94)
print("\nAIA 94 Å query result:")
print(result_aia_94)
# To download the data, uncomment the following line:
# files_aia_94 = Fido.fetch(result_aia_94)

# Query for AIA 131 Å data
result_aia_131 = Fido.search(time_hot, source_sdo, instrument_aia, wavelength_131)
print("\nAIA 131 Å query result:")
print(result_aia_131)
# To download the data, uncomment the following line:
# files_aia_131 = Fido.fetch(result_aia_131)

# Query for AIA 1600 Å data
result_aia_1600 = Fido.search(time_hot, source_sdo, instrument_aia, wavelength_1600)
print("\nAIA 1600 Å query result:")
print(result_aia_1600)
# To download the data, uncomment the following line:
# files_aia_1600 = Fido.fetch(result_aia_1600)

###############################################################################
# Query 3: AIA observation of the rotational motion of the jet (untwisting phase)
# Time Range: 13:52 UT to 14:07 UT on 2016 January 9
# Wavelengths: 304 Å (to capture the cool plasma structures) and 171 Å (to complement the view)
###############################################################################
time_rot = a.Time("2016-01-09T13:52:00", "2016-01-09T14:07:00")
wavelength_304 = a.Wavelength(304*u.AA, 304*u.AA)
# Reusing wavelength_171 defined earlier for the rotational phase query

print("\nQuerying AIA data for the rotational motion phase (channels 304 Å and 171 Å)...")

# Query for AIA 304 Å data
result_aia_304 = Fido.search(time_rot, source_sdo, instrument_aia, wavelength_304)
print("\nAIA 304 Å query result:")
print(result_aia_304)
# To download the data, uncomment the following line:
# files_aia_304 = Fido.fetch(result_aia_304)

# Query for AIA 171 Å data during the rotational phase
result_aia_171_rot = Fido.search(time_rot, source_sdo, instrument_aia, wavelength_171)
print("\nAIA 171 Å (rotational phase) query result:")
print(result_aia_171_rot)
# To download the data, uncomment the following line:
# files_aia_171_rot = Fido.fetch(result_aia_171_rot)

###############################################################################
# Query 4: HMI magnetogram for magnetic field mapping
# Time: A specific snapshot at 13:12 UT on 2016 January 6 (covering the period 2016 Jan 6-9)
###############################################################################
time_hmi = a.Time("2016-01-06T13:12:00", "2016-01-06T13:12:00")
instrument_hmi = a.Instrument("HMI")

print("\nQuerying HMI magnetogram data for magnetic field mapping...")
result_hmi = Fido.search(time_hmi, source_sdo, instrument_hmi)
print("\nHMI query result:")
print(result_hmi)
# To download the data, uncomment the following line:
# files_hmi = Fido.fetch(result_hmi)

print("\n--- All VSO queries have been executed. Inspect the printed query results for further analysis. ---")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to search for solar observations that match the criteria
depicted in the scientific paper. The paper focuses on the evolution of a hot-channel-like CME,
with observations from SDO/AIA for multi-wavelength imaging and SDO/HMI for magnetic field measurements,
as well as SOHO/LASCO (C2) for CME detection. 

In this script, we create three separate queries using SunPy:
1. SDO/AIA data in the 131 Å passband covering the precursor and formation phase of the hot channel,
   from 03:30 UT to 03:43 UT on 2014 March 20.
2. SDO/HMI vector magnetogram data at approximately 03:12 UT on 2014 March 20 to capture the pre‐flare magnetic configuration.
3. SOHO/LASCO C2 data for a snapshot CME observation at approximately 05:12 UT on 2014 March 20.

Note: The actual data download commands (Fido.fetch) are commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ----------------------- 1. Query for SDO/AIA Data -----------------------
# Define the time range for the precursor/formation phase (03:30 UT to 03:43 UT, March 20, 2014)
time_aia = a.Time("2014-03-20T03:30:00", "2014-03-20T03:43:00")
# Specify the instrument (AIA onboard SDO)
instrument_aia = a.Instrument("AIA")
# For this study, we are mainly interested in the 131 Å passband.
wavelength_aia = a.Wavelength(131 * u.Angstrom, 131 * u.Angstrom)

# Construct the search query for AIA data.
query_aia = Fido.search(time_aia, instrument_aia, wavelength_aia)

# Print the query result for AIA.
print("SDO/AIA Query Results:")
print(query_aia)

# Uncomment the following line to download the AIA data.
# aia_files = Fido.fetch(query_aia)

# ----------------------- 2. Query for SDO/HMI Vector Magnetogram -----------------------
# Define the time for the pre-eruptive magnetic configuration observation.
# Using a one-second interval around 03:12 UT on March 20, 2014.
time_hmi = a.Time("2014-03-20T03:12:00", "2014-03-20T03:12:01")
# Specify the instrument (HMI onboard SDO)
instrument_hmi = a.Instrument("HMI")
# Use the wavelength corresponding to 6173 Å for the photospheric magnetic field.
wavelength_hmi = a.Wavelength(6173 * u.Angstrom, 6173 * u.Angstrom)
# Specify the physical observable: vector magnetic field.
# (This constraint helps select the vector magnetogram data.)
physobs_hmi = a.Physobs("vector_magnetic_field")

# Construct the search query for HMI data.
query_hmi = Fido.search(time_hmi, instrument_hmi, wavelength_hmi, physobs_hmi)

# Print the query result for HMI.
print("\nSDO/HMI Query Results:")
print(query_hmi)

# Uncomment the following line to download the HMI data.
# hmi_files = Fido.fetch(query_hmi)

# ----------------------- 3. Query for SOHO/LASCO C2 Data -----------------------
# Define the time for the snapshot CME detection at around 05:12 UT on March 20, 2014.
time_lasco = a.Time("2014-03-20T05:12:00", "2014-03-20T05:12:01")
# Specify the instrument (LASCO onboard SOHO)
instrument_lasco = a.Instrument("LASCO")
# Specify the detector as C2 (as provided in the VSO interface data).
detector_lasco = a.Detector("C2")
# For LASCO, wavelength information is not specified (white-light observations).

# Construct the search query for LASCO/C2 data.
query_lasco = Fido.search(time_lasco, a.Source("SOHO"), instrument_lasco, detector_lasco)

# Print the query result for LASCO/C2.
print("\nSOHO/LASCO C2 Query Results:")
print(query_lasco)

# Uncomment the following line to download the LASCO/C2 data.
# lasco_files = Fido.fetch(query_lasco)

if __name__ == '__main__':
    # This block ensures that the script can be run as a standalone program.
    pass

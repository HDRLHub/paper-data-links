# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for:
 1) SDO/AIA high-temperature passband data (131 Å and 94 Å) for the AR 11520 event in July 2012.
 2) IRIS FUV and NUV spectroscopic data for pre-flare hot-channel diagnostics.
 
Note:
 - Instruments like Hinode/EIS, NVST, and NST are not served by the VSO interface provided.
 - Please adjust the IRIS time range below to match the exact observation period used in Cheng et al. (2015a).
"""

import sunpy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Initialize the VSO client via Fido
# (Fido is the unified interface for querying multiple data sources, including VSO.)
# No explicit client object is needed when using Fido.query.

# ------------------------------------------------------------------
# 1) Query SDO/AIA 131 Å and 94 Å data for AR 11520 in July 2012
# ------------------------------------------------------------------

# Define the time range for the event (AR 11520 eruption in July 2012)
time_start_aia = a.Time("2012-07-12T00:00:00", "2012-07-12T12:00:00")

# Define the instrument and wavelengths of interest
instrument_aia = a.Instrument("AIA")
wavelength_131 = a.Wavelength(131.0 * u.Angstrom)
wavelength_94  = a.Wavelength(94.0 * u.Angstrom)

# Build and execute the query for both 131 Å and 94 Å
query_aia_131 = Fido.search(time_start_aia, instrument_aia, wavelength_131, a.Physobs("intensity"))
query_aia_94  = Fido.search(time_start_aia, instrument_aia, wavelength_94,  a.Physobs("intensity"))

# Print the results
print("SDO/AIA 131 Å query results:")
print(query_aia_131)
print("\nSDO/AIA 94 Å query results:")
print(query_aia_94)

# To download the data, uncomment the following lines:
# files_aia_131 = Fido.fetch(query_aia_131)
# files_aia_94  = Fido.fetch(query_aia_94)


# ------------------------------------------------------------------
# 2) Query IRIS FUV and NUV spectroscopic data
#    (Si IV, C II, Mg II lines for pre-flare diagnostics)
# ------------------------------------------------------------------

# Define a placeholder time range covering ~5 hours in the pre-flare phase.
# Replace these with the exact start and end times from Cheng et al. (2015a).
time_start_iris = a.Time("2015-03-11T00:00:00", "2015-03-11T05:00:00")

# Define the IRIS instrument detectors for spectroscopic lines:
#   - FUV (covers Si IV, C II)
#   - NUV (covers Mg II)
detector_fuv = a.Detector("FUV")
detector_nuv = a.Detector("NUV")

# Build and execute the queries
query_iris_fuv = Fido.search(time_start_iris, a.Instrument("IRIS"), detector_fuv, a.Physobs("intensity"))
query_iris_nuv = Fido.search(time_start_iris, a.Instrument("IRIS"), detector_nuv, a.Physobs("intensity"))

# Print the results
print("\nIRIS FUV spectroscopic query results:")
print(query_iris_fuv)
print("\nIRIS NUV spectroscopic query results:")
print(query_iris_nuv)

# To download the data, uncomment the following lines:
# files_iris_fuv = Fido.fetch(query_iris_fuv)
# files_iris_nuv = Fido.fetch(query_iris_nuv)


# ------------------------------------------------------------------
# Summary:
# - We have queried for the high-temperature AIA channels (131 Å, 94 Å)
#   that reveal the sigmoidal hot channels (MFRs) in AR 11520.
# - We have set up IRIS spectroscopic queries (FUV/NUV) for lines 
#   diagnosing pre-flare reconnection (Si IV, C II, Mg II). 
# - Other instruments referenced (EIS, NVST, NST) are not available 
#   in the provided VSO interface and thus are not included here.
# ------------------------------------------------------------------

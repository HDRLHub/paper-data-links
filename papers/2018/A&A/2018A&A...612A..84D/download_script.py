# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------------------------------------------------------
# Query 1: UVCS/SOHO Daily Synoptic H I Lyα Line Observations
# Time range: 1997-06-01 to 1997-06-28 (full Carrington rotation during solar minimum)
# Instrument: UVCS on SOHO
# Detector: LVA (covers Lyα at 1216 Å)
# Physical observable: Intensity
# Wavelength: 1216 Å (H I Lyα)
# -----------------------------------------------------------------------------

# Define time constraint for UVCS
time_uvcs = a.Time("1997-06-01", "1997-06-28")

# Define instrument and other attributes
instrument_uvcs = a.Instrument("UVCS")
detector_uvcs = a.Detector("LVA")
physobs_uvcs = a.Physobs("intensity")
wavelength_uvcs = a.Wavelength(1216 * u.Angstrom)

# Perform the search
query_uvcs = Fido.search(
    time_uvcs,
    instrument_uvcs,
    detector_uvcs,
    physobs_uvcs,
    wavelength_uvcs
)

# Print out the results
print("UVCS Lyα query results:")
print(query_uvcs)

# To download the data, uncomment the following line:
# fetched_uvcs = Fido.fetch(query_uvcs)

# -----------------------------------------------------------------------------
# Query 2: LASCO C2/SOHO Daily Polarised Brightness Images
# Time range: 1997-06-01 to 1997-06-28 (matching UVCS coverage)
# Instrument: LASCO on SOHO
# Detector: C2
# Physical observable: Intensity (broadband visible-light pB)
# Note: No specific wavelength attribute is provided for LASCO C2 in VSO
# -----------------------------------------------------------------------------

# Define time constraint for LASCO C2
time_c2 = a.Time("1997-06-01", "1997-06-28")

# Define instrument and other attributes
instrument_c2 = a.Instrument("LASCO")
detector_c2 = a.Detector("C2")
physobs_c2 = a.Physobs("intensity")

# Perform the search
query_c2 = Fido.search(
    time_c2,
    instrument_c2,
    detector_c2,
    physobs_c2
)

# Print out the results
print("LASCO C2 pB query results:")
print(query_c2)

# To download the data, uncomment the following line:
# fetched_c2 = Fido.fetch(query_c2)

# -----------------------------------------------------------------------------
# Note on Mk3/MLSO Data:
# The Mk3 K-Coronameter at MLSO is not available through the VSO interface.
# Mk3 polarised brightness images must be retrieved via the MLSO data archive.
# -----------------------------------------------------------------------------

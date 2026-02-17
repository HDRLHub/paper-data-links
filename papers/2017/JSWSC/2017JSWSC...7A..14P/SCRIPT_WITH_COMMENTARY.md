# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
Query script for SOHO/ERNE proton flux data and SOHO/LASCO C2 white-light CME observations
Time range: 1996-05-01 to 2016-12-31
"""

from sunpy.net import Fido, attrs as a

# Define the common time range for the catalogue period
time_range = a.Time('1996-05-01', '2016-12-31')

# ---------------------------------------------------------------------
# Query 1: SOHO/ERNE proton flux data (particle_flux)
# ---------------------------------------------------------------------
source_erne     = a.Source('SOHO')           # Spacecraft source
instrument_erne = a.Instrument('ERNE')       # ERNE instrument on SOHO
physobs_erne    = a.Physobs('particle_flux') # Proton flux observable

# Build and execute the search for ERNE data
query_erne = Fido.search(
    time_range,
    source_erne,
    instrument_erne,
    physobs_erne
)
print("SOHO/ERNE Query Results:")
print(query_erne)

# To download the data, uncomment the following line:
# results_erne = Fido.fetch(query_erne)

# ---------------------------------------------------------------------
# Query 2: SOHO/LASCO C2 white-light images (intensity)
# ---------------------------------------------------------------------
source_lasco     = a.Source('SOHO')          # Spacecraft source
instrument_lasco = a.Instrument('LASCO')      # LASCO instrument on SOHO
detector_lasco   = a.Detector('C2')           # C2 coronagraph
physobs_lasco    = a.Physobs('intensity')     # White-light intensity

# Build and execute the search for LASCO C2 images
query_lasco = Fido.search(
    time_range,
    source_lasco,
    instrument_lasco,
    detector_lasco,
    physobs_lasco
)
print("\nSOHO/LASCO C2 Query Results:")
print(query_lasco)

# To download the data, uncomment the following line:
# results_lasco = Fido.fetch(query_lasco)

if __name__ == "__main__":
    # This script only prints the query objects. Data fetching is commented out.
    pass

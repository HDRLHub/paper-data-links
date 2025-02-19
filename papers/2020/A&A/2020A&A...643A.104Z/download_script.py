# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script for querying SOHO data using SunPy's VSO client.
This script retrieves the main data sets used in the paper:
1. Primary spectroscopic observations from SOHO/UVCS (using the OVI detector to cover the O vi doublet and H i Lyα).
2. White-light coronagraph context images from SOHO/LASCO-C2.
3. EUV context images from SOHO/EIT (specifically for the 195 Å channel).

The observations span early April 1996 (April 6 to April 7, 1996) as described in the paper.
The queries use the time range and instrument details provided in the scientific context.
"""

# Import required modules from SunPy and Astropy for unit handling
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time range based on the paper's campaign (6-7 April 1996)
time_range = a.Time("1996-04-06", "1996-04-07")

# -----------------------------------------------------------------
# Query 1: SOHO/UVCS (using the OVI detector)
# The UVCS instrument (with detector OVI) observed the coronal UV spectra,
# including the O vi doublet at 1031.9 Å and 1037.6 Å as well as H i Lyα at 1215.7 Å.
# The available VSO record for UVCS/OVI has a full time range from 1996/01/20 to present.
uvcs_query = Fido.search(
    time_range,
    a.Source("SOHO"),
    a.Instrument("UVCS"),
    a.Detector("OVI")
)

# Print the query result for UVCS
print("UVCS Query Results:")
print(uvcs_query)
print("\n")
# To fetch the UVCS data, uncomment the following line:
# downloaded_uvcs = Fido.fetch(uvcs_query)

# -----------------------------------------------------------------
# Query 2: SOHO/LASCO-C2 (White-light coronagraph context images)
# LASCO-C2 provides white-light images showing the coronal brightness and plume morphology.
# Here, we choose the C2 detector which best fits the study's context images.
lasco_query = Fido.search(
    time_range,
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

# Print the query result for LASCO-C2
print("LASCO-C2 Query Results:")
print(lasco_query)
print("\n")
# To fetch the LASCO data, uncomment the following line:
# downloaded_lasco = Fido.fetch(lasco_query)

# -----------------------------------------------------------------
# Query 3: SOHO/EIT (EUV images at 195 Å for context)
# EIT provides EUV images useful for correlating the plume structures seen in UVCS data.
# Although EIT offers several wavelengths, we focus on 195 Å images as highlighted in the paper.
eit_query = Fido.search(
    time_range,
    a.Source("SOHO"),
    a.Instrument("EIT"),
    a.Wavelength(195 * u.angstrom, 195 * u.angstrom)
)

# Print the query result for EIT
print("EIT Query Results:")
print(eit_query)
print("\n")
# To fetch the EIT data, uncomment the following line:
# downloaded_eit = Fido.fetch(eit_query)

if __name__ == "__main__":
    print("Queries executed. Review the printed query results for details.")

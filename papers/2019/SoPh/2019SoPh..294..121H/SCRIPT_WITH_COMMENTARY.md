# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script demonstrates how to query data from the Virtual Solar Observatory (VSO)
using SunPy for a study of a CME and its associated flare and coronal dimmings.
The queries are based on the instrumentation details provided in the scientific paper
context. In this example, we query:

1. SDO/AIA data in the 211 Å filter around the time of the flare on June 21, 2011.
2. SDO/HMI data (synoptic vector magnetograms) from Carrington rotation 2111 (June 05,
   2011 to July 03, 2011).

Note: Fido.fetch commands are provided as comments. They can be uncommented to download data.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ---------------------------- SDO/AIA Query --------------------------------
# The AIA instrument on SDO observes the solar corona in multiple wavelengths.
# For this study, we are interested in the evolution of the flare and coronal dimmings,
# particularly using the 211 Å filter. The observation time covers the period of the flare
# and its aftermath on June 21, 2011.
start_aia = '2011-06-21T01:00:00'
end_aia   = '2011-06-21T03:30:00'

# Build the query for SDO/AIA with a wavelength of 211 Å.
query_aia = Fido.search(
    a.Time(start_aia, end_aia),
    a.Instrument('AIA'),
    a.Wavelength(211 * u.angstrom)
)

# Print the query results for SDO/AIA.
print("SDO/AIA Query Results (211 Å filter):")
print(query_aia)

# To fetch the SDO/AIA data, uncomment the following line:
# aia_files = Fido.fetch(query_aia)

# ---------------------------- SDO/HMI Query --------------------------------
# The HMI instrument on SDO provides synoptic vector magnetogram data. For Carrington rotation
# 2111 we are interested in the magnetic field maps covering the period between June 05, 2011 and July 03, 2011.
start_hmi = '2011-06-05'
end_hmi   = '2011-07-03'

# Build the query for SDO/HMI data.
query_hmi = Fido.search(
    a.Time(start_hmi, end_hmi),
    a.Instrument('HMI')
)

# Print the query results for SDO/HMI.
print("\nSDO/HMI Query Results (Synoptic Vector Magnetograms):")
print(query_hmi)

# To fetch the SDO/HMI data, uncomment the following line:
# hmi_files = Fido.fetch(query_hmi)

if __name__ == '__main__':
    # The queries have been executed and printed.
    # Uncomment the fetch commands above if you wish to download the data.
    pass

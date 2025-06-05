# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface to query solar data that are relevant
to the scientific event described in the context. The two queries below target:

1. SOHO/LASCO: To obtain white-light coronagraph images around the time when a candidate CME
   was observed (around February 14, 2014 near 11:42 UT). We use the LASCO C2 detector because
   it is available over the required time range ("1995/12/08 - present").

2. SDO/AIA: To obtain extreme-ultraviolet (EUV) images that could potentially capture low-coronal
   signatures associated with the same event. The query selects a representative wavelength (304 Å)
   and uses the available time range starting from May 2010.
   
Note: The Fido.fetch() steps are provided but commented out.
"""

import sunpy.net.vso as vso
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Create a VSO client
client = vso.VSOClient()

# ---------------------------
# Query 1: SOHO/LASCO (C2 detector)
# ---------------------------
# According to the context, a weak CME candidate was observed by the SOHO/LASCO instrument around
# February 14, 2014 (approximately at 11:42 UT). We define a short time interval around that event.
time_start_lasco = "2014-02-14T11:30:00"
time_end_lasco   = "2014-02-14T12:00:00"

# Build the query for SOHO/LASCO instrument using the C2 detector.
# The VSO interface confirms that LASCO C2 from SOHO is available during the period.
lasco_query = Fido.search(
    a.Time(time_start_lasco, time_end_lasco),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

print("SOHO/LASCO Query Results:")
print(lasco_query)

# To download the data, uncomment the following line:
# lasco_files = Fido.fetch(lasco_query)


# ---------------------------
# Query 2: SDO/AIA
# ---------------------------
# The SDO/AIA instrument observes the Sun in multiple EUV wavelengths.
# Although the context indicates that no clear low-coronal signature was found,
# we still query AIA data around the time of the candidate CME event (using the same window) as a sample.
time_start_aia = "2014-02-14T11:30:00"
time_end_aia   = "2014-02-14T12:00:00"
# Select a representative wavelength (304 Å is one of the available wavelengths for AIA).
aia_query = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(304*u.angstrom)
)

print("\nSDO/AIA Query Results:")
print(aia_query)

# To download the data, uncomment the following line:
# aia_files = Fido.fetch(aia_query)

if __name__ == "__main__":
    # Display both query results (printing already done above)
    pass

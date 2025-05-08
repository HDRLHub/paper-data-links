# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's Fido client to query data from the Virtual Solar Observatory (VSO)
that are relevant to the study of twisting and swirling motions in a solar prominence:
    (1) SDO/AIA data covering the overall prominence evolution on 2012 November 25–26 
        (focusing on the 171 Å channel, which captures dark intertwined threads in the prominence).
    (2) SOHO LASCO/C2 data capturing the CME rotation during the prominence eruption on 2012 November 26.

Note: The Fido.fetch() commands are present but commented out. They can be uncommented
to actually download the data.
"""

# Import necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------------------------
# Query 1: SDO/AIA Data for Overall Prominence Evolution
# ---------------------------------------------
# Time Range: 2012-11-25 09:00:00 to 2012-11-26 22:00:00
# Instrument: AIA onboard SDO
# Wavelength: 171 Å (selected based on the context of tracing dark intertwined threads)
start_aia = '2012-11-25T09:00:00'
end_aia = '2012-11-26T22:00:00'

# Create the query for AIA 171 Å
query_aia = Fido.search(
    a.Time(start_aia, end_aia),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(171 * u.Angstrom)
)

# Print out the query result for SDO/AIA
print("SDO/AIA query result (171 Å) for prominence evolution:")
print(query_aia)

# To actually download the data, uncomment the line below:
# files_aia = Fido.fetch(query_aia)

# ---------------------------------------------
# Query 2: SOHO LASCO/C2 Data for CME Rotation Observation
# ---------------------------------------------
# Time Range: 2012-11-26 19:00:00 to 2012-11-26 20:24:00
# Instrument: LASCO with Detector C2 onboard SOHO
start_lasco = '2012-11-26T19:00:00'
end_lasco = '2012-11-26T20:24:00'

# Create the query for LASCO/C2
query_lasco = Fido.search(
    a.Time(start_lasco, end_lasco),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

# Print out the query result for LASCO/C2
print("\nSOHO LASCO/C2 query result for CME rotation observation:")
print(query_lasco)

# To fetch the LASCO/C2 data, uncomment the line below:
# files_lasco = Fido.fetch(query_lasco)

if __name__ == '__main__':
    print("\nQueries executed. Check the printed query results for details.")

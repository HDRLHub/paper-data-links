# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs two separate VSO queries using SunPy.
One query retrieves extreme-ultraviolet (EUV) data from the PROBA2/SWAP instrument,
and the other retrieves EUV data from SDO/AIA.
Both queries cover the interval during the 22 September 2011 solar event.
Note: Fido.fetch commands are commented out as per instructions.
"""

# Import necessary modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the common time range for the observations (approximate interval of the event)
start_time = '2011-09-22T10:30:00'
end_time = '2011-09-22T11:10:00'

# ------------------------------------------------------------------------------
# Query 1: PROBA2/SWAP EUV Data
#
# Instrument details from the VSO interface:
#    Source: PROBA2
#    Instrument: SWAP
#    Detector: SWAP
#
# The SWAP instrument on board PROBA2 provides EUV images at wavelengths
# around 174 Å. We use the available full time range from 2010/03/09 to present.
#
# Here we query SWAP data for the event time.
# ------------------------------------------------------------------------------
print("Querying PROBA2/SWAP data...")

swap_query = Fido.search(
    a.Time(start_time, end_time),
    a.Source('PROBA2'),
    a.Instrument('SWAP')
)

# Print the results of the PROBA2/SWAP query.
print("PROBA2/SWAP Query Results:")
print(swap_query)

# Uncomment the following line to download the PROBA2/SWAP data:
# swap_files = Fido.fetch(swap_query)
# ------------------------------------------------------------------------------
# Query 2: SDO/AIA EUV Data
#
# Instrument details from the VSO interface:
#    Source: SDO
#    Instrument: AIA
#
# Although AIA can observe at several wavelengths, the context mentions
# the use of the 211 Å passband for overlaying radio source contours on coronal images.
#
# Here we query AIA data in the 211 Å channel for the event time.
# ------------------------------------------------------------------------------
print("\nQuerying SDO/AIA data...")

aia_query = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(211 * u.Angstrom)
)

# Print the results of the SDO/AIA query.
print("SDO/AIA Query Results:")
print(aia_query)

# Uncomment the following line to download the SDO/AIA data:
# aia_files = Fido.fetch(aia_query)

if __name__ == '__main__':
    print("\nVSO queries constructed for PROBA2/SWAP and SDO/AIA in the specified time range.")

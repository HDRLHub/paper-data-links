# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO)
using SunPy for downloading IRIS and SDO/AIA data relevant to UV burst studies.

The queries are constructed based on the provided context:
1. An IRIS raster scan observation on 2013 September 24 during 11:44–12:04 UT,
   using the IRIS SJI (slit-jaw imager) channel, which covers the 1400 Å band.
2. A SDO/AIA full-disk imaging observation on 2013 October 22 between 21:45 and 21:55 UT,
   e.g. in the 171 Å channel for coronal context.

Note: The actual download command (Fido.fetch) is commented out.
"""

from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# ---------------------------
# Query 1: IRIS Raster Scan Data
# ---------------------------

# Define time range for the IRIS observation: 2013-09-24 11:44 to 2013-09-24 12:04 UT.
iris_time_start = '2013-09-24T11:44:00'
iris_time_end   = '2013-09-24T12:04:00'
iris_timerange  = a.Time(iris_time_start, iris_time_end)

# Define the instrument and detector.
# Based on the VSO interface, we select:
# - Instrument: "IRIS"
# - Detector: "SJI" which includes wavelength range around 1400 Å (1380.0 - 1420.0 Å)
iris_instrument = a.Instrument('IRIS')
iris_detector   = a.Detector('SJI')

# Construct the IRIS query.
iris_query = Fido.search(iris_timerange, iris_instrument, iris_detector)

# Print the IRIS query results.
print("IRIS Query Results:")
print(iris_query)

# To download IRIS data, uncomment the following line:
# iris_downloaded_files = Fido.fetch(iris_query)

# ---------------------------
# Query 2: SDO/AIA Imaging Data
# ---------------------------

# Define time range for the SDO/AIA observation: 2013-10-22 21:45 to 2013-10-22 21:55 UT.
aia_time_start = '2013-10-22T21:45:00'
aia_time_end   = '2013-10-22T21:55:00'
aia_timerange  = a.Time(aia_time_start, aia_time_end)

# Define the instrument.
# Based on the VSO interface, we select:
# - Instrument: "AIA" (from SDO) and physical observable "intensity"
aia_instrument = a.Instrument('AIA')

# Optionally, if a specific wavelength or channel is preferred (e.g., 171 Å for coronal context),
# one can add the Wavelength attribute. Here we keep it general.
# Example (if needed):
# aia_wavelength = a.Wavelength(171*u.angstrom, 171*u.angstrom)
# For simplicity, we proceed without adding explicit wavelength limits.

# Construct the AIA query.
aia_query = Fido.search(aia_timerange, aia_instrument)

# Print the AIA query results.
print("\nSDO/AIA Query Results:")
print(aia_query)

# To download AIA data, uncomment the following line:
# aia_downloaded_files = Fido.fetch(aia_query)

if __name__ == '__main__':
    # This main block simply confirms that the script has run.
    print("\nVSO queries constructed successfully. Uncomment the fetch commands to download data.")

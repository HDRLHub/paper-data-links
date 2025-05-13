# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries helioseismology data for two instruments:
  1. SOHO/MDI observations in the period 1996-04-30 to 2011-03-20.
  2. SDO/HMI observations in the period 2011-03-20 to 2017-06-04.

Both datasets are used in the study to analyze f-mode oscillation frequencies 
which are sensitive to solar subsurface structure and seismic radius variations.
For SOHO/MDI we choose the "LOS_velocity" observable and for SDO/HMI we choose 
the "LOS_velocity" observable from the available VSO records.

The script uses Sunpy’s VSO module for querying. Note that the Fido.fetch 
commands are commented out as per instructions.
"""

from sunpy.net import Fido, attrs as a

# ---------------------------
# Query 1: SOHO/MDI Observations
# ---------------------------
# Define the time range for MDI observations (April 30, 1996 – March 20, 2011)
mdi_time = a.Time("1996-04-30", "2011-03-20")
# Define the instrument parameters for SOHO/MDI:
# Source is SOHO, Instrument is MDI, Detector is "MDI"
# We use the physical observable "LOS_velocity", which has available wavelengths of 6768 Å.
mdi_source = a.Source("SOHO")
mdi_instrument = a.Instrument("MDI")
mdi_detector = a.Detector("MDI")
mdi_physobs = a.Physobs("LOS_velocity")
# Optionally, include wavelength constraint based on the vso interface
mdi_wavelength = a.Wave(6768.0, 6768.0, unit="Angstrom")

# Construct the SOHO/MDI query
mdi_query = Fido.search(
    mdi_time,
    mdi_source,
    mdi_instrument,
    mdi_detector,
    mdi_physobs,
    mdi_wavelength
)

print("SOHO/MDI Query Results:")
print(mdi_query)

# Uncomment the following line to fetch the MDI data:
# mdi_downloaded_files = Fido.fetch(mdi_query)

# ---------------------------
# Query 2: SDO/HMI Observations
# ---------------------------
# Define the time range for HMI observations (March 20, 2011 – June 4, 2017)
hmi_time = a.Time("2011-03-20", "2017-06-04")
# Define the instrument parameters for SDO/HMI:
# Source is SDO, Instrument is HMI.
# The query uses a physical observable list that includes "LOS_velocity" (as part of the available options)
# Note: The available wavelength range for HMI is 6173.0 - 6174.0 Å.
hmi_source = a.Source("SDO")
hmi_instrument = a.Instrument("HMI")
# As the Detector field is blank for HMI in the interface, we do not specify it.
hmi_physobs = a.Physobs("LOS_velocity")
hmi_wavelength = a.Wave(6173.0, 6174.0, unit="Angstrom")

# Construct the SDO/HMI query
hmi_query = Fido.search(
    hmi_time,
    hmi_source,
    hmi_instrument,
    hmi_physobs,
    hmi_wavelength
)

print("\nSDO/HMI Query Results:")
print(hmi_query)

# Uncomment the following line to fetch the HMI data:
# hmi_downloaded_files = Fido.fetch(hmi_query)

if __name__ == "__main__":
    print("\nCompleted VSO Queries for SOHO/MDI and SDO/HMI data.")

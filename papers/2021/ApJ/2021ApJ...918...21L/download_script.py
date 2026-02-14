# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script constructs SunPy VSO queries for several solar instruments based on the study context.
The queries focus on data from:
  • SDO/AIA – EUV intensity images at key wavelengths (e.g., 171, 193, and 211 Å) to identify coronal holes.
  • SDO/HMI – Photospheric magnetograms (e.g., LOS magnetic field at 6173 Å) for magnetic flux analysis.
  • SWAP/PROBA2 – EUV images at 174 Å for intercomparison of CH detection.
  • EIT/SOHO – EUV images at 195 Å to evaluate consistency with other instruments.
  • MDI/SOHO – Magnetograms used to build synoptic magnetic maps during Carrington Rotation CR2101.
The queries below use the minimum required parameters (time range and instrument) and reflect the 
data collection periods from the context:
  1. For Sept 19, 2010 – targeted CH observation.
  2. For Carrington Rotation CR2101 (2010-09-05 to 2010-10-03) – full-Sun mapping.
Note: The Fido.fetch() commands are provided as comments; uncomment them to download data.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define time ranges for the two study periods
time_sep19 = a.Time("2010-09-19T00:00:00", "2010-09-19T23:59:59")
time_cr2101 = a.Time("2010-09-05", "2010-10-03")

# ----------------------------
# Query SDO/AIA Data
# ----------------------------
# Query 1: SDO/AIA for coronal hole detection on September 19, 2010.
print("Querying SDO/AIA data for September 19, 2010 (EUV intensity data for CH detection)...")
aia_sep19 = Fido.search(time_sep19, 
                        a.Source('SDO'), 
                        a.Instrument('AIA'), 
                        a.Physobs('intensity'))
print(aia_sep19)
# Uncomment the following line to fetch the data:
# downloaded_aia_sep19 = Fido.fetch(aia_sep19)

# Query 2: SDO/AIA for Carrington Rotation CR2101 (2010-09-05 to 2010-10-03).
print("\nQuerying SDO/AIA data for Carrington Rotation CR2101 (2010-09-05 to 2010-10-03)...")
aia_cr2101 = Fido.search(time_cr2101, 
                         a.Source('SDO'), 
                         a.Instrument('AIA'), 
                         a.Physobs('intensity'))
print(aia_cr2101)
# Uncomment the following line to fetch the data:
# downloaded_aia_cr2101 = Fido.fetch(aia_cr2101)

# ----------------------------
# Query SDO/HMI Data
# ----------------------------
# Query 3: SDO/HMI magnetograms for September 19, 2010.
print("\nQuerying SDO/HMI data for September 19, 2010 (magnetogram observations)...")
hmi_sep19 = Fido.search(time_sep19, 
                        a.Source('SDO'), 
                        a.Instrument('HMI'))
print(hmi_sep19)
# Uncomment the following line to fetch the data:
# downloaded_hmi_sep19 = Fido.fetch(hmi_sep19)

# Query 4: SDO/HMI for Carrington Rotation CR2101.
print("\nQuerying SDO/HMI data for Carrington Rotation CR2101 (2010-09-05 to 2010-10-03)...")
hmi_cr2101 = Fido.search(time_cr2101, 
                         a.Source('SDO'), 
                         a.Instrument('HMI'))
print(hmi_cr2101)
# Uncomment the following line to fetch the data:
# downloaded_hmi_cr2101 = Fido.fetch(hmi_cr2101)

# ----------------------------
# Query SWAP/PROBA2 Data
# ----------------------------
# Query 5: SWAP/PROBA2 for September 19, 2010.
# SWAP provides EUV filtergrams at 174 Å, used to intercompare CH area estimates.
print("\nQuerying SWAP/PROBA2 data for September 19, 2010 (EUV data at 174 Å)...")
swap_sep19 = Fido.search(time_sep19, 
                         a.Source('PROBA2'), 
                         a.Instrument('SWAP'), 
                         a.Physobs('intensity'),
                         a.Wavelength(174 * u.angstrom, 174 * u.angstrom))
print(swap_sep19)
# Uncomment the following line to fetch the data:
# downloaded_swap_sep19 = Fido.fetch(swap_sep19)

# ----------------------------
# Query EIT/SOHO Data
# ----------------------------
# Query 6: EIT/SOHO for September 19, 2010.
# EIT is used for supplementary EUV imaging at 195 Å.
print("\nQuerying EIT/SOHO data for September 19, 2010 (EUV data at 195 Å)...")
eit_sep19 = Fido.search(time_sep19, 
                        a.Source('SOHO'), 
                        a.Instrument('EIT'), 
                        a.Physobs('intensity'),
                        a.Wavelength(195 * u.angstrom, 195 * u.angstrom))
print(eit_sep19)
# Uncomment the following line to fetch the data:
# downloaded_eit_sep19 = Fido.fetch(eit_sep19)

# ----------------------------
# Query MDI/SOHO Data
# ----------------------------
# Query 7: MDI/SOHO for Carrington Rotation CR2101.
# MDI magnetograms help compute the photospheric magnetic maps needed for open magnetic flux calculations.
print("\nQuerying MDI/SOHO data for Carrington Rotation CR2101 (2010-09-05 to 2010-10-03)...")
mdi_cr2101 = Fido.search(time_cr2101, 
                         a.Source('SOHO'), 
                         a.Instrument('MDI'), 
                         a.Physobs('LOS_magnetic_field'))
print(mdi_cr2101)
# Uncomment the following line to fetch the data:
# downloaded_mdi_cr2101 = Fido.fetch(mdi_cr2101)

print("\nAll queries completed successfully.")

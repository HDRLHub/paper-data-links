# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses sunpy.net.vso (Virtual Solar Observatory) to query several instruments
that are employed in the study of coronal mass ejections (CMEs) and their associated
solar source active regions, as described in the scientific paper. The instruments queried
include white‐light coronagraphs (SECCHI/COR2 on STEREO A & B and LASCO on SOHO),
extreme ultraviolet imagers (SDO/AIA, SECCHI/EUVI on STEREO A & B), and vector magnetograms (SDO/HMI).

The time range is chosen to cover the solar cycle 24 observations, starting from the launch
of the SDO mission in May 2010 through the period where both STEREO and SOHO data are available,
i.e. approximately 2010–2014.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs as a

# Define the time range: Solar Cycle 24 observations (from May 2010 to December 2014)
start_time = "2010-05-01"
end_time   = "2014-12-31"

# ------------------------------
# Query 1: STEREO_A - SECCHI Coronagraph (COR2)
# White-light images to track CME flux-rope morphology.
query_stereoA_cor2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("Query Results for STEREO_A SECCHI COR2:")
print(query_stereoA_cor2)

# Uncomment the line below to fetch the data
# files_stereoA_cor2 = Fido.fetch(query_stereoA_cor2)

# ------------------------------
# Query 2: STEREO_B - SECCHI Coronagraph (COR2)
query_stereoB_cor2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nQuery Results for STEREO_B SECCHI COR2:")
print(query_stereoB_cor2)

# Uncomment the line below to fetch the data
# files_stereoB_cor2 = Fido.fetch(query_stereoB_cor2)

# ------------------------------
# Query 3: SOHO - LASCO C2 Coronagraph
# LASCO C2 images are used for additional white-light CME characterization.
query_soho_lasco_c2 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nQuery Results for SOHO LASCO C2:")
print(query_soho_lasco_c2)

# Uncomment the line below to fetch the data
# files_soho_lasco_c2 = Fido.fetch(query_soho_lasco_c2)

# ------------------------------
# Query 4: SOHO - LASCO C3 Coronagraph
query_soho_lasco_c3 = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nQuery Results for SOHO LASCO C3:")
print(query_soho_lasco_c3)

# Uncomment the line below to fetch the data
# files_soho_lasco_c3 = Fido.fetch(query_soho_lasco_c3)

# ------------------------------
# Query 5: SDO - Atmospheric Imaging Assembly (AIA)
# Although the paper mentions 193 Å imaging for identifying post-eruption arcades,
# we narrow the wavelength range to cover this filter (within the available wavelengths).
query_sdo_aia = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SDO"),
    a.Instrument("AIA"),
    # Using a wavelength range that includes 193 Å (given available range 191-195 Å)
    a.Wavelength(191, 195)
)
print("\nQuery Results for SDO AIA (193 Å):")
print(query_sdo_aia)

# Uncomment the line below to fetch the data
# files_sdo_aia = Fido.fetch(query_sdo_aia)

# ------------------------------
# Query 6: SDO - Helioseismic Magnetic Imager (HMI) for vector magnetograms
# Select observations for vector magnetic field measurements.
query_sdo_hmi = Fido.search(
    a.Time(start_time, end_time),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field")
)
print("\nQuery Results for SDO HMI (vector magnetic field):")
print(query_sdo_hmi)

# Uncomment the line below to fetch the data
# files_sdo_hmi = Fido.fetch(query_sdo_hmi)

# ------------------------------
# Query 7: STEREO_A - SECCHI Extreme Ultraviolet Imager (EUVI)
# EUVI images at around 195 Å help pinpoint the CME source regions.
query_stereoA_euvi = Fido.search(
    a.Time(start_time, end_time),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    # Define wavelength range around 195 Å (EUV observations)
    a.Wavelength(190, 200)
)
print("\nQuery Results for STEREO_A SECCHI EUVI (≈195 Å):")
print(query_stereoA_euvi)

# Uncomment the line below to fetch the data
# files_stereoA_euvi = Fido.fetch(query_stereoA_euvi)

# ------------------------------
# Query 8: STEREO_B - SECCHI Extreme Ultraviolet Imager (EUVI)
query_stereoB_euvi = Fido.search(
    a.Time(start_time, end_time),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(190, 200)
)
print("\nQuery Results for STEREO_B SECCHI EUVI (≈195 Å):")
print(query_stereoB_euvi)

# Uncomment the line below to fetch the data
# files_stereoB_euvi = Fido.fetch(query_stereoB_euvi)

if __name__ == "__main__":
    print("\nVSO Query script executed successfully.")

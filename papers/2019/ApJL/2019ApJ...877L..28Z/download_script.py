# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Python script to query solar data from the Virtual Solar Observatory (VSO) using SunPy.
This script builds queries corresponding to the observational instruments discussed in the paper:
SDO/AIA for EUV imaging at 304 Å and 193 Å, SDO/HMI for photospheric magnetic field data,
STEREO-A and STEREO-B SECCHI/EUVI for EUV imaging at 304 Å and 195 Å, SOHO LASCO-C2 for
white-light coronagraph observations, and STEREO-A/B SECCHI COR1 coronagraph data.
The observation period is set for the full event period: from 2010 July to 2013 February.
Note: The Fido.fetch commands are provided as commented-out lines.
"""

# Import necessary modules
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the observation time range for the paper's event period: 2010 July to 2013 February.
time_start = "2010-07-01"
time_end   = "2013-02-28"

# ---------------------------
# 1. Query SDO/AIA EUV Images
# ---------------------------
# SDO/AIA 304 Å channel: We use a narrow wavelength range around 304 Å (e.g., 303-305 Å) to capture the filament.
query_aia_304 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(303 * u.AA, 305 * u.AA)
)
print("SDO/AIA 304 Å query result:")
print(query_aia_304)

# SDO/AIA 193 Å channel: Use the wavelength range from 191 Å to 195 Å (which covers the 193 Å passband).
query_aia_193 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(191 * u.AA, 195 * u.AA)
)
print("\nSDO/AIA 193 Å query result:")
print(query_aia_193)

# ---------------------------
# 2. Query SDO/HMI Magnetic Field Data
# ---------------------------
# SDO/HMI delivers photospheric magnetic field data; no wavelength filter is needed.
query_hmi = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SDO"),
    a.Instrument("HMI")
)
print("\nSDO/HMI query result:")
print(query_hmi)

# ---------------------------
# 3. Query STEREO SECCHI/EUVI EUV Images
# ---------------------------
# STEREO-A SECCHI/EUVI 304 Å channel: Use the same narrow wavelength range around 304 Å.
query_stereo_a_euvi_304 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(303 * u.AA, 305 * u.AA)
)
print("\nSTEREO-A SECCHI/EUVI 304 Å query result:")
print(query_stereo_a_euvi_304)

# STEREO-A SECCHI/EUVI 195 Å channel: Use a narrow range (e.g., 194-196 Å) to capture the 195 Å passband.
query_stereo_a_euvi_195 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(194 * u.AA, 196 * u.AA)
)
print("\nSTEREO-A SECCHI/EUVI 195 Å query result:")
print(query_stereo_a_euvi_195)

# STEREO-B SECCHI/EUVI 304 Å channel.
query_stereo_b_euvi_304 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(303 * u.AA, 305 * u.AA)
)
print("\nSTEREO-B SECCHI/EUVI 304 Å query result:")
print(query_stereo_b_euvi_304)

# STEREO-B SECCHI/EUVI 195 Å channel.
query_stereo_b_euvi_195 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI"),
    a.Wavelength(194 * u.AA, 196 * u.AA)
)
print("\nSTEREO-B SECCHI/EUVI 195 Å query result:")
print(query_stereo_b_euvi_195)

# ---------------------------
# 4. Query White-light Coronagraph Data for CME Detection
# ---------------------------
# SOHO LASCO-C2: Used to check for the presence of CMEs; no wavelength filter is required.
query_lasco_c2 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSOHO LASCO-C2 query result:")
print(query_lasco_c2)

# STEREO-A SECCHI COR1: White-light coronagraph observations.
query_stereo_a_cor1 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("\nSTEREO-A SECCHI COR1 query result:")
print(query_stereo_a_cor1)

# STEREO-B SECCHI COR1: White-light coronagraph observations.
query_stereo_b_cor1 = Fido.search(
    a.Time(time_start, time_end),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("\nSTEREO-B SECCHI COR1 query result:")
print(query_stereo_b_cor1)

# ---------------------------
# 5. Fetch Data (Optional)
# ---------------------------
# To download the data corresponding to the queries, uncomment the following Fido.fetch commands.
# Note: Uncomment one at a time as needed.

# data_aia_304 = Fido.fetch(query_aia_304)
# data_aia_193 = Fido.fetch(query_aia_193)
# data_hmi = Fido.fetch(query_hmi)
# data_stereo_a_euvi_304 = Fido.fetch(query_stereo_a_euvi_304)
# data_stereo_a_euvi_195 = Fido.fetch(query_stereo_a_euvi_195)
# data_stereo_b_euvi_304 = Fido.fetch(query_stereo_b_euvi_304)
# data_stereo_b_euvi_195 = Fido.fetch(query_stereo_b_euvi_195)
# data_lasco_c2 = Fido.fetch(query_lasco_c2)
# data_stereo_a_cor1 = Fido.fetch(query_stereo_a_cor1)
# data_stereo_b_cor1 = Fido.fetch(query_stereo_b_cor1)

print("\nAll queries have been executed. Please review the printed query results for data selection.")

if __name__ == "__main__":
    pass

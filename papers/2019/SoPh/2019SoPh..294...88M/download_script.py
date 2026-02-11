# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script builds two Sunpy VSO queries using the SunPy Fido interface.
One query retrieves SOHO/EIT data that captures the Solar Cycle 22/23 termination event
(at around 195 Å) between 1 August 1997 and 31 December 1999.
The other query retrieves SDO/AIA data capturing the Solar Cycle 23/24 termination event
(at approximately 193 Å) between 1 January 2010 and 31 December 2012.
Note: The Fido.fetch commands are commented out to avoid automatic download.
"""

# Import necessary modules from SunPy and astropy
from sunpy.net import Fido, attrs as a
from astropy import units as u

# -----------------------------
# Query 1: SOHO/EIT Data Query
# -----------------------------
# Define time range for the Solar Cycle 22/23 termination event
eit_start_time = "1997-08-01"
eit_end_time   = "1999-12-31"

# Define the wavelength range for SOHO/EIT (targeting the ~195 Å channel)
# Using a small interval around 195 Å (194-196 Å)
eit_wave_min = 194 * u.AA
eit_wave_max = 196 * u.AA

# Build the query for SOHO/EIT from the VSO
eit_query = Fido.search(
    a.Time(eit_start_time, eit_end_time),
    a.Source("SOHO"),
    a.Instrument("EIT"),
    a.Detector("EIT"),
    a.Wavelength(eit_wave_min, eit_wave_max)
)

# Print the query result for SOHO/EIT data
print("SOHO/EIT Query Results:")
print(eit_query)

# Uncomment the following line to fetch the SOHO/EIT data:
# eit_files = Fido.fetch(eit_query)

# -----------------------------
# Query 2: SDO/AIA Data Query
# -----------------------------
# Define time range for the Solar Cycle 23/24 termination event
aia_start_time = "2010-01-01"
aia_end_time   = "2012-12-31"

# Define the wavelength range for SDO/AIA data targeting the ~193 Å channel.
# In the available AIA wavelengths, "191 - 195 Å" covers 193 Å.
aia_wave_min = 192 * u.AA
aia_wave_max = 194 * u.AA

# Build the query for SDO/AIA from the VSO
aia_query = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(aia_wave_min, aia_wave_max)
)

# Print the query result for SDO/AIA data
print("\nSDO/AIA Query Results:")
print(aia_query)

# Uncomment the following line to fetch the SDO/AIA data:
# aia_files = Fido.fetch(aia_query)

if __name__ == '__main__':
    print("\nQueries constructed successfully. Review the printed query results.")

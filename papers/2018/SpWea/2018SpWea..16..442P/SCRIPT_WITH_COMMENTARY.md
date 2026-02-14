# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs two separate VSO queries using SunPy:
1. Query for an SDO/HMI line‐of‐sight (LOS) magnetogram around mid-June 2012.
   (Based on the context: a HMI magnetogram obtained ~2 days before the SOL2012-06-14 eruption.)
2. Query for an SDO/AIA image in the 131 Å channel on SOL2012-06-14,
   when the forward-S sigmoid is observed as described in the context.
   
Note: The script prints out the query results. The actual Fido.fetch commands are commented out.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------
# 1. Query SDO/HMI LOS Magnetogram
# ---------------------------
# Define the time range: Around 2 days before SOL2012-06-14 eruption (i.e., mid-June 2012).
# Using a one-hour window on 2012-06-12, assuming the magnetogram is acquired during this period.
hmi_start_time = "2012-06-12T10:00:00"
hmi_end_time   = "2012-06-12T11:00:00"
# Define query attributes:
# We select the SDO source and HMI instrument.
# For the observable we use the 'LOS_magnetic_field' (line-of-sight magnetic field) as available in the VSO interface.
hmi_query = Fido.search(
    a.Time(hmi_start_time, hmi_end_time),
    a.Instrument("HMI"),
    a.Source("SDO"),
    a.Physobs("LOS_magnetic_field"),
    a.Wavelength(6173*u.Angstrom)  # HMI uses the 6173 Å spectral line.
)

print("SDO/HMI Query Result:")
print(hmi_query)
# Uncomment the following line to download HMI data:
# downloaded_hmi = Fido.fetch(hmi_query)

# ---------------------------
# 2. Query SDO/AIA 131 Å Image
# ---------------------------
# Define the time range: Around the SOL2012-06-14 eruption at ~13 UT (using a two-hour window).
aia_start_time = "2012-06-14T12:00:00"
aia_end_time   = "2012-06-14T14:00:00"
# Set query attributes:
# We select the SDO source and AIA instrument.
# We further specify the wavelength filter to extract data corresponding to 131 Å.
aia_query = Fido.search(
    a.Time(aia_start_time, aia_end_time),
    a.Instrument("AIA"),
    a.Source("SDO"),
    a.Wavelength(131*u.Angstrom)
)

print("\nSDO/AIA Query Result:")
print(aia_query)
# Uncomment the following line to download AIA data:
# downloaded_aia = Fido.fetch(aia_query)

if __name__ == "__main__":
    print("\nQueries have been executed. Review the printed query results for details.")

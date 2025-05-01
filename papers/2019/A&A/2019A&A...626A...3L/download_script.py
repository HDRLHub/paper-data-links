# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO interface to construct separate queries
for SOHO/MDI and SDO/HMI data as described in the context.
The queries use the time ranges for each instrument and are aimed at retrieving
Dopplergrams (LOS_velocity) data suitable for helioseismic analysis.
Note: The Fido.fetch commands are provided but commented out.
"""

from sunpy.net import Fido, attrs
import astropy.units as u

# -------------------------------
# Query for SOHO/MDI observations
# -------------------------------
# These observations cover the period from May 1996 to April 2010.
mdi_start_time = '1996-05-01T12:00:00'
mdi_end_time   = '2010-04-30T00:00:00'
# The Fido query below requests data from the SOHO source, with instrument MDI,
# Detector set to 'MDI', and physical observable 'LOS_velocity'
mdi_query = Fido.search(
    attrs.Time(mdi_start_time, mdi_end_time),
    attrs.Source("SOHO"),
    attrs.Instrument("MDI"),
    attrs.Detector("MDI"),
    attrs.Physobs("LOS_velocity")
)

# Print the query result for SOHO/MDI data
print("SOHO/MDI Query Results:")
print(mdi_query)

# Uncomment the following line to fetch the SOHO/MDI data:
# downloaded_mdi_files = Fido.fetch(mdi_query)


# -------------------------------
# Query for SDO/HMI observations
# -------------------------------
# These observations cover the period from May 2010 to April 2017.
hmi_start_time = '2010-05-01T12:00:00'
hmi_end_time   = '2017-04-30T00:00:00'
# The HMI instrument typically observes in the Fe I 6173 Å spectral line.
# The query below specifies the wavelength range 6173.0 - 6174.0 Å and requests
# the Doppler (LOS_velocity) observable from SDO/HMI.
hmi_query = Fido.search(
    attrs.Time(hmi_start_time, hmi_end_time),
    attrs.Source("SDO"),
    attrs.Instrument("HMI"),
    attrs.Wavelength(6173.0 * u.AA, 6174.0 * u.AA),
    attrs.Physobs("LOS_velocity")
)

# Print the query result for SDO/HMI data
print("\nSDO/HMI Query Results:")
print(hmi_query)

# Uncomment the following line to fetch the SDO/HMI data:
# downloaded_hmi_files = Fido.fetch(hmi_query)


if __name__ == '__main__':
    # This main block ensures the script runs as a standalone module.
    # The queries have already been executed and printed above.
    pass

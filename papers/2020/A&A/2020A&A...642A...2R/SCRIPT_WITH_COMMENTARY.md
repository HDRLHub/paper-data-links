# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query the Virtual Solar Observatory (VSO)
using sunpy for Solar Orbiter remote‐sensing data. Although the context
mentions several Solar Orbiter instruments (PHI, Metis, Solar Orbiter HI, SPICE, STIX, etc.),
the PHI instrument (Polarimetric and Helioseismic Imager) is not available in the provided VSO interface.
Instead, we use the available EUI instrument (Extreme Ultraviolet Imager) on board Solar Orbiter.
Specifically, we query for EUI data with the FSI detector, which captures high-resolution EUV images.
The time range chosen here corresponds to a typical 10‐day remote sensing window.
"""

# Import required modules
import sunpy.net.vso as vso
import astropy.units as u
from sunpy.time import TimeRange

# Define the time range (example 10-day remote‐sensing window)
start_time = "2021-06-01"
end_time = "2021-06-10"
time_range = TimeRange(start_time, end_time)

# Initialize the VSO client
client = vso.VSOClient()

# Construct the query for Solar Orbiter's EUI instrument with the FSI detector.
# Note: The available EUI FSI data in the VSO interface has a wavelength range of 171.0 - 185.0 Å.
# We specify the time range and instrument details as provided.
query_response = client.search(
    a.Time=time_range,
    a.Source="SO",           # "SO" corresponds to Solar Orbiter data in the interface
    a.Instrument="EUI",      # Query for the EUI instrument
    a.Detector="FSI",        # Select the FSI detector for full-disk intensity imaging
    a.Physobs="intensity"    # The physical observable, in this case intensity images
    # Wavelength filtering can be added if needed, for example:
    # a.Wavelength=(171 * u.Angstrom, 185 * u.Angstrom)
)

# Print the query response details.
# This will list all the available data files that match the above criteria.
print("Query Results for Solar Orbiter EUI (FSI) from {} to {}:".format(start_time, end_time))
print(query_response)

# Uncomment the following line to download the data files.
# Note: This command fetches the data; it is commented out as per instruction.
# files = client.fetch(query_response)

if __name__ == "__main__":
    pass

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Query Script for SOHO/MDI Daily Full-Disk Magnetograms

This script searches the Virtual Solar Observatory (VSO) for daily,
5-minute averaged, full-disk Michelson Doppler Imager (MDI) magnetograms
(LOS magnetic field) over the period 1996-04-21 to 2010-12-30.
"""

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# -----------------------------------------------------------------------------
# 1) Define the time range for the query
# -----------------------------------------------------------------------------
start_time = '1996-04-21'  # Start date for daily magnetograms
end_time   = '2010-12-30'  # End date for daily magnetograms

# -----------------------------------------------------------------------------
# 2) Specify the VSO search attributes
# -----------------------------------------------------------------------------
# Source satellite and instrument
source     = a.Source('SOHO')
instrument = a.Instrument('MDI')

# Physical observable: line-of-sight magnetic field
physobs    = a.Physobs('LOS_magnetic_field')

# Wavelength settings: Ni I 6768 Å photospheric line (MDI standard wavelength)
wavelength = a.Wavelength(6768.0 * u.Angstrom)

# -----------------------------------------------------------------------------
# 3) Build and execute the search query
# -----------------------------------------------------------------------------
query = Fido.search(
    a.Time(start_time, end_time),
    source,
    instrument,
    physobs,
    wavelength
)

# -----------------------------------------------------------------------------
# 4) Inspect the query results
# -----------------------------------------------------------------------------
print("VSO Query Results for SOHO/MDI LOS Magnetic Field Magnetograms:")
print(query)

# -----------------------------------------------------------------------------
# 5) (Optional) Fetch the files corresponding to the query
# -----------------------------------------------------------------------------
# The download step is commented out. Uncomment the following line
# to perform the actual data download.
#
# files = Fido.fetch(query)

# End of script

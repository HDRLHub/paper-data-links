# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy's VSO client to query solar data for supporting observations.
We query two SOHO instruments used for context:
  1. SOHO/EIT for EUV intensity images at 195 Å.
  2. SOHO/MDI for photospheric line-of-sight magnetic field measurements.
Additionally, a query for TRACE is included to serve as historical reference imaging.
All queries are set for 30 October 2005, corresponding to the CoMP observation date
discussed in the paper context.
Note: Fido.fetch commands are provided as commented-out lines.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the observation time range based on the context (CoMP observation dated 30 October 2005)
start_time = '2005-10-30T00:00:00'
end_time = '2005-10-30T23:59:59'

# -------------------------------
# Query for SOHO/EIT Data:
# -------------------------------
# EIT provides EUV context images, notably in the 195 Å passband.
eit_search = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(195 * u.Angstrom)
)
print("SOHO/EIT Query Results:")
print(eit_search)

# -------------------------------
# Query for SOHO/MDI Data:
# -------------------------------
# MDI supplies line-of-sight magnetograms to infer the photospheric magnetic field.
mdi_search = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field')
)
print("\nSOHO/MDI Query Results:")
print(mdi_search)

# -------------------------------
# Optional: Query for TRACE Data:
# -------------------------------
# TRACE is included as a historical reference instrument for coronal loop imaging.
trace_search = Fido.search(
    a.Time(start_time, end_time),
    a.Source('TRACE'),
    a.Instrument('TRACE')
)
print("\nTRACE Query Results:")
print(trace_search)

# -------------------------------
# To download the data, uncomment the following fetch commands:
# -------------------------------
# eit_files = Fido.fetch(eit_search)
# mdi_files = Fido.fetch(mdi_search)
# trace_files = Fido.fetch(trace_search)

if __name__ == "__main__":
    pass

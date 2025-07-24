# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to query data from the Virtual Solar Observatory (VSO)
using SunPy for two Swift instruments described in the scientific context:
1. Swift Burst Alert Telescope (BAT)
2. Swift X‐Ray Telescope (XRT)

The only required query parameters are the time range and the instrument.
For Swift/XRT, the data collection period is given explicitly as December 2004 to May 2012.
For Swift/BAT, although no explicit dates are provided, we use the same time range to
compare the prompt gamma‐ray lightcurve observations with the X‐ray afterglow.

NOTE: The Fido.fetch commands are commented out to avoid automatic data downloads.
"""

import datetime
from sunpy.net import Fido, attrs as a

# Define the time range for the queries
# For Swift/XRT, the observation period is December 2004 – May 2012.
# We use the same time range for Swift/BAT for consistency.
start_time = '2004-12-01T00:00:00'
end_time = '2012-05-31T23:59:59'

# Query 1: Swift Burst Alert Telescope (BAT)
# BAT provides prompt gamma‐ray lightcurves in the energy range 15–150 keV.
bat_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('BAT'),           # Instrument from Swift used for gamma-ray prompt emission.
    # Additional constraints like energy range are noted in the context but not required for query.
)

print("Query results for Swift/BAT:")
print(bat_query)

# Uncomment the following line to fetch the BAT data:
# bat_files = Fido.fetch(bat_query)


# Query 2: Swift X‐Ray Telescope (XRT)
# XRT provides early X‐ray afterglow lightcurves.
xrt_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('XRT'),           # Instrument from Swift for X-ray observations.
    # Note: XRT typically covers soft X-ray wavelengths (e.g., 0.3–10 keV), but only time range and instrument are required.
)

print("\nQuery results for Swift/XRT:")
print(xrt_query)

# Uncomment the following line to fetch the XRT data:
# xrt_files = Fido.fetch(xrt_query)


if __name__ == '__main__':
    # The script prints the query results. Fetch commands are provided as commented lines.
    pass

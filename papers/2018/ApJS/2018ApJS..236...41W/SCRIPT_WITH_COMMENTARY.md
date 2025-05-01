# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries Wind spacecraft data available on the Virtual Solar Observatory (VSO)
using SunPy's Fido interface. The queries target four instruments onboard Wind:
    1. Wind/SWE Faraday Cups (measuring proton/alpha ion properties)
    2. Wind/3DP Electron Electrostatic Analyzers (EESA Low and EESA High for electron distributions)
    3. Wind/MFI Dual Triaxial Fluxgate Magnetometers (measuring the magnetic field vector)
    4. Wind/WAVES/TNR Instrument (observing the plasma upper hybrid line to derive electron density)

All queries are performed over the time range:
    January 1, 1995 00:00:33.565 UTC to January 1, 2005 00:00:33.565 UTC

Note:
    The Fido.fetch commands are provided as commented lines. Removing the comment markers
    will then execute the download.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the common time range for the queries
start_time = '1995-01-01T00:00:33.565'
end_time   = '2005-01-01T00:00:33.565'

# Query 1: Wind/SWE Faraday Cups
# These data provide ion moment measurements (proton and alpha-particle densities and temperatures)
query_swe = Fido.search(
    a.Time(start_time, end_time),
    a.Source('wind'),
    a.Instrument('swe')
)
print("Query Results for Wind/SWE Faraday Cups:")
print(query_swe)
# To download the SWE data, uncomment the following line:
# files_swe = Fido.fetch(query_swe)

# Query 2: Wind/3DP Electron Electrostatic Analyzers
# These data provide electron velocity distributions for density and temperature estimation.
query_3dp = Fido.search(
    a.Time(start_time, end_time),
    a.Source('wind'),
    a.Instrument('3dp')
)
print("\nQuery Results for Wind/3DP Electron Electrostatic Analyzers (EESA Low/High):")
print(query_3dp)
# To download the 3DP data, uncomment the following line:
# files_3dp = Fido.fetch(query_3dp)

# Query 3: Wind/MFI Dual Triaxial Fluxgate Magnetometers
# These data provide the magnetic field vectors necessary for plasma categorization.
query_mfi = Fido.search(
    a.Time(start_time, end_time),
    a.Source('wind'),
    a.Instrument('mfi')
)
print("\nQuery Results for Wind/MFI Fluxgate Magnetometers:")
print(query_mfi)
# To download the MFI data, uncomment the following line:
# files_mfi = Fido.fetch(query_mfi)

# Query 4: Wind/WAVES/TNR Instrument
# These data capture the upper hybrid (plasma) line, yielding an independent measurement of electron density.
query_waves = Fido.search(
    a.Time(start_time, end_time),
    a.Source('wind'),
    a.Instrument('waves')
)
print("\nQuery Results for Wind/WAVES/TNR Instrument:")
print(query_waves)
# To download the WAVES/TNR data, uncomment the following line:
# files_waves = Fido.fetch(query_waves)

if __name__ == '__main__':
    # This portion of the script ensures it runs as a standalone program.
    print("\nCompleted querying VSO for Wind spacecraft instruments over the specified time range.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs queries using SunPy's VSO client (Fido) to download data relevant to the events described in the paper.
We focus on SDO/AIA data during three key time periods on 2014 December 20:
1. X1.8-class flare imaging between 00:11 UT and 00:28 UT.
2. Hot loop expansion visible in the 131 Å channel between 00:37 UT and 00:49 UT.
3. Cold loop contraction (and coronal dimming) observed in the 171 Å channel between 00:51 UT and 01:00 UT.

Note: The Fido.fetch() commands are commented out to avoid actual downloading.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

def main():
    # Query 1: SDO/AIA flare imaging data for the X1.8-class flare.
    flare_start = "2014-12-20T00:11:00"
    flare_end = "2014-12-20T00:28:00"
    print("Querying SDO/AIA flare imaging data (2014-12-20 00:11 UT to 00:28 UT)...")
    query_flare = Fido.search(
        a.Time(flare_start, flare_end),
        a.Source('SDO'),
        a.Instrument('AIA'),
        a.Physobs('intensity')
    )
    print(query_flare)
    # Uncomment the following line to fetch the flare imaging data:
    # flare_files = Fido.fetch(query_flare)
    
    # Query 2: SDO/AIA hot loop imaging in the 131 Å channel.
    loop_start = "2014-12-20T00:37:00"
    loop_end = "2014-12-20T00:49:00"
    print("\nQuerying SDO/AIA hot loop imaging data in 131 Å (2014-12-20 00:37 UT to 00:49 UT)...")
    query_hot_loop = Fido.search(
        a.Time(loop_start, loop_end),
        a.Source('SDO'),
        a.Instrument('AIA'),
        a.Wavelength(131 * u.Angstrom)
    )
    print(query_hot_loop)
    # Uncomment the following line to fetch the hot loop imaging data:
    # hot_loop_files = Fido.fetch(query_hot_loop)
    
    # Query 3: SDO/AIA cold loop contraction imaging in the 171 Å channel.
    cold_loop_start = "2014-12-20T00:51:00"
    cold_loop_end = "2014-12-20T01:00:00"
    print("\nQuerying SDO/AIA cold loop contraction data in 171 Å (2014-12-20 00:51 UT to 01:00 UT)...")
    query_cold_loop = Fido.search(
        a.Time(cold_loop_start, cold_loop_end),
        a.Source('SDO'),
        a.Instrument('AIA'),
        a.Wavelength(171 * u.Angstrom)
    )
    print(query_cold_loop)
    # Uncomment the following line to fetch the cold loop contraction data:
    # cold_loop_files = Fido.fetch(query_cold_loop)

if __name__ == '__main__':
    main()

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar radio data related to a decameter type IV burst event recorded on 7 November 2013.
The event was observed by several instruments. In this script we demonstrate queries for the following instruments and time ranges:

1. URAN-2:
   - Query the dynamic spectrum around the type IV burst registration period.
   - Time Range: 10:22 UT – 10:44 UT on 7 November 2013.
   - Frequency: Using the sub-band where the burst is best seen (22–33 MHz).

2. NDA (Nancay Decameter Array):
   - Query for the type IV burst registration.
     - Time Range: 10:22 UT – 10:44 UT on 7 November 2013.
     - Frequency: 30–60 MHz.
   - Query for the weak type II burst observation.
     - Time Range: 10:16 UT – 10:17 UT on 7 November 2013.
     - Frequency: 44–64 MHz.

3. STEREO A:
   - Query for the type IV burst observation (and associated bursts).
   - Time Range: 10:40 UT – 11:50 UT on 7 November 2013.

4. STEREO B:
   - Query for the type IV burst (mainly observed at lower frequencies).
   - Time Range: 10:50 UT – 11:30 UT on 7 November 2013.
   - Frequency: 11–16 MHz.
   
Note:
- The Fido.fetch commands are provided but commented out so that no downloading is initiated by accident.
- Ensure that your local SunPy installation and network access are properly configured for VSO queries.
"""

import astropy.units as u
from sunpy.net import Fido, attrs

def main():
    # ------------------------- URAN-2 Query -------------------------
    # Dynamic spectrum of the type IV burst observed by URAN-2.
    time_range_uran = ("2013-11-07T10:22:00", "2013-11-07T10:44:00")
    query_uran = Fido.search(
        attrs.Time(time_range_uran[0], time_range_uran[1]),
        attrs.Instrument("URAN-2"),
        attrs.Wave(22*u.MHz, 33*u.MHz)
    )
    print("URAN-2 Query Results (10:22 - 10:44 UT, 22–33 MHz):")
    print(query_uran)
    # Uncomment the line below to fetch the URAN-2 data:
    # files_uran = Fido.fetch(query_uran)
    
    # ------------------------- NDA Query -------------------------
    # (a) Type IV burst registration by NDA.
    time_range_nda_iv = ("2013-11-07T10:22:00", "2013-11-07T10:44:00")
    query_nda_iv = Fido.search(
        attrs.Time(time_range_nda_iv[0], time_range_nda_iv[1]),
        attrs.Instrument("NDA"),
        attrs.Wave(30*u.MHz, 60*u.MHz)
    )
    print("\nNDA (Type IV) Query Results (10:22 - 10:44 UT, 30–60 MHz):")
    print(query_nda_iv)
    # Uncomment the line below to fetch the NDA type IV data:
    # files_nda_iv = Fido.fetch(query_nda_iv)
    
    # (b) Weak Type II burst observation by NDA.
    time_range_nda_ii = ("2013-11-07T10:16:00", "2013-11-07T10:17:00")
    query_nda_ii = Fido.search(
        attrs.Time(time_range_nda_ii[0], time_range_nda_ii[1]),
        attrs.Instrument("NDA"),
        attrs.Wave(44*u.MHz, 64*u.MHz)
    )
    print("\nNDA (Type II) Query Results (10:16 - 10:17 UT, 44–64 MHz):")
    print(query_nda_ii)
    # Uncomment the line below to fetch the NDA type II data:
    # files_nda_ii = Fido.fetch(query_nda_ii)
    
    # ------------------------- STEREO A Query -------------------------
    # Type IV burst (and associated burst signatures) observed by STEREO A.
    time_range_stereoA = ("2013-11-07T10:40:00", "2013-11-07T11:50:00")
    query_stereoA = Fido.search(
        attrs.Time(time_range_stereoA[0], time_range_stereoA[1]),
        attrs.Instrument("STEREO A")
        # Frequency range is not explicitly defined for STEREO A in this context.
    )
    print("\nSTEREO A Query Results (10:40 - 11:50 UT):")
    print(query_stereoA)
    # Uncomment the line below to fetch the STEREO A data:
    # files_stereoA = Fido.fetch(query_stereoA)
    
    # ------------------------- STEREO B Query -------------------------
    # Type IV burst mainly in the lower frequency range observed by STEREO B.
    time_range_stereoB = ("2013-11-07T10:50:00", "2013-11-07T11:30:00")
    query_stereoB = Fido.search(
        attrs.Time(time_range_stereoB[0], time_range_stereoB[1]),
        attrs.Instrument("STEREO B"),
        attrs.Wave(11*u.MHz, 16*u.MHz)
    )
    print("\nSTEREO B Query Results (10:50 - 11:30 UT, 11–16 MHz):")
    print(query_stereoB)
    # Uncomment the line below to fetch the STEREO B data:
    # files_stereoB = Fido.fetch(query_stereoB)

if __name__ == "__main__":
    main()

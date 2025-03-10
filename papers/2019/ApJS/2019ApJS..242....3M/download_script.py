# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query coronagraph observations
that were used in the scientific paper described in the context.
It performs three separate queries:
1. LASCO C2 synthetic observations for method testing (2007/03/15–2007/03/30)
2. LASCO C2 real observations (half-Carrington period centered on 2009/03/20,
   approximated here as 2009/03/13–2009/03/27)
3. STEREO_A SECCHI COR2 (representing COR2 A) real observations for the same period
   (2009/03/13–2009/03/27)

Note: We print the query results. Fido.fetch commands are commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# --------------------------------------------------------------------------------
# Query 1: LASCO C2 Synthetic Observations (Method Testing)
# --------------------------------------------------------------------------------
# These synthetic observations are used for testing the inversion method.
# Time Range: 2007/03/15 to 2007/03/30 
# Instrument: LASCO C2 onboard SOHO
query_lasco_synthetic = Fido.search(
    a.Time("2007-03-15", "2007-03-30"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

print("=== LASCO C2 Synthetic Observations (2007/03/15 - 2007/03/30) ===")
print(query_lasco_synthetic)
print("\n")

# Uncomment the following line to fetch data for the synthetic test period.
# data_lasco_synthetic = Fido.fetch(query_lasco_synthetic)

# --------------------------------------------------------------------------------
# Query 2: LASCO C2 Real Observations (Half-Carrington Period Centered on 2009/03/20)
# --------------------------------------------------------------------------------
# The real observations are used to reconstruct the coronal electron density.
# Time Range: Approximate two-week period (chosen as 2009/03/13 to 2009/03/27)
# Instrument: LASCO C2 onboard SOHO
query_lasco_real = Fido.search(
    a.Time("2009-03-13", "2009-03-27"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)

print("=== LASCO C2 Real Observations (2009/03/13 - 2009/03/27) ===")
print(query_lasco_real)
print("\n")

# Uncomment the following line to fetch data for the real observation period.
# data_lasco_real = Fido.fetch(query_lasco_real)


# --------------------------------------------------------------------------------
# Query 3: STEREO_A SECCHI COR2 Observations (Representing COR2 A)
# --------------------------------------------------------------------------------
# These observations complement the LASCO C2 data and allow a comparative analysis.
# Time Range: Approximate two-week period (chosen as 2009/03/13 to 2009/03/27)
# Instrument: SECCHI with Detector COR2 onboard STEREO_A
query_stereo_cor2 = Fido.search(
    a.Time("2009-03-13", "2009-03-27"),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)

print("=== STEREO_A SECCHI COR2 Observations (2009/03/13 - 2009/03/27) ===")
print(query_stereo_cor2)
print("\n")

# Uncomment the following line to fetch data for the STEREO_A observations.
# data_stereo_cor2 = Fido.fetch(query_stereo_cor2)

if __name__ == '__main__':
    print("SunPy VSO queries constructed. Review the printed query results for details.")

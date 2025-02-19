# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar observations relevant to the paper.
In particular, we query:
  1. RHESSI data for microflare events on 2003-09-26 (hard X-ray observations).
  2. TRACE data for the same day at 1600 Å (UV observations used for determining flare loop geometry).
  3. SDO/AIA data from a post-2010 M/X-class flare (e.g., EUV 171 Å channel for DEM analysis).
  4. SOHO/VIRGO data for bolometric TSI observations (used in ensemble analyses of bolometric energy).
  
Note: The only required query parameters are the time ranges and the instrument names.
Fido.fetch commands are provided but commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------------------------------------------------------
# Query 1: RHESSI microflare event observations on 2003-09-26
# -----------------------------------------------------------------------------
# Define the time range for the 2003-09-26 microflare observations.
rhessi_start = "2003-09-26T00:00:00"
rhessi_end   = "2003-09-26T23:59:59"

print("Querying RHESSI data for microflare events on 2003-09-26...")
rhessi_query = Fido.search(a.Time(rhessi_start, rhessi_end),
                           a.Instrument("RHESSI"))
print(rhessi_query)

# To fetch levels of RHESSI files, uncomment the following line:
# rhessi_files = Fido.fetch(rhessi_query)

# -----------------------------------------------------------------------------
# Query 2: TRACE UV observations at 1600 Å on 2003-09-26
# -----------------------------------------------------------------------------
# TRACE was used to identify footpoint brightenings in the UV.
trace_start = "2003-09-26T00:00:00"
trace_end   = "2003-09-26T23:59:59"

# We query for TRACE data using a narrow wavelength filter of 1600 Å.
print("\nQuerying TRACE data for UV footpoint observations at 1600 Å on 2003-09-26...")
trace_query = Fido.search(a.Time(trace_start, trace_end),
                          a.Instrument("TRACE"),
                          a.Wavelength(1600*u.AA, 1600*u.AA))
print(trace_query)

# To fetch TRACE files, uncomment the following line:
# trace_files = Fido.fetch(trace_query)

# -----------------------------------------------------------------------------
# Query 3: SDO/AIA EUV observations for a M/X-class flare (DEM reconstructions)
# -----------------------------------------------------------------------------
# AIA observations post-2010 are used to constrain thermal plasma parameters.
aia_start = "2015-06-15T00:00:00"
aia_end   = "2015-06-15T23:59:59"

# We choose the 171 Å channel as a representative coronal EUV wavelength.
print("\nQuerying SDO/AIA data for EUV observations (171 Å) on 2015-06-15...")
aia_query = Fido.search(a.Time(aia_start, aia_end),
                        a.Instrument("AIA"),
                        a.Wavelength(171*u.AA, 171*u.AA))
print(aia_query)

# To fetch AIA files, uncomment the following line:
# aia_files = Fido.fetch(aia_query)

# -----------------------------------------------------------------------------
# Query 4: SOHO/VIRGO bolometric TSI observations for ensemble flare analysis
# -----------------------------------------------------------------------------
# VIRGO TSI measurements provide bolometric energy outputs for flares.
virgo_start = "2011-06-15T00:00:00"
virgo_end   = "2011-06-15T23:59:59"

print("\nQuerying SOHO/VIRGO TSI data on 2011-06-15 for bolometric energy analysis...")
virgo_query = Fido.search(a.Time(virgo_start, virgo_end),
                          a.Instrument("VIRGO"))
print(virgo_query)

# To fetch VIRGO data, uncomment the following line:
# virgo_files = Fido.fetch(virgo_query)

if __name__ == '__main__':
    print("\nAll queries have been executed. Review the printed query results above.")

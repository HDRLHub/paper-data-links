# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script to query the Virtual Solar Observatory (VSO) for the SOHO and TRACE
observations used in Event 2 (2002-08-19) of the 3He-rich SEP source study.
This script searches for:
  - SOHO/CDS NIS spectra (raster 10:29:15–10:56:31 UT)
  - SOHO/EIT 195 Å images (10:24:31–10:36:10 UT)
  - TRACE 195 Å images (10:34:55–10:50:00 UT)
  - SOHO/MDI magnetograms (01:36:00–11:25:00 UT)
Queries are printed; fetch commands are provided but commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# 1. SOHO CDS NIS slit spectrometer raster 
cds_start = '2002-08-19T10:29:15'
cds_end   = '2002-08-19T10:56:31'
cds_query = Fido.search(
    a.Time(cds_start, cds_end),
    a.Source('SOHO'),
    a.Instrument('CDS')
)
print("CDS Query Results:")
print(cds_query)
# To download:
# files_cds = Fido.fetch(cds_query)

# 2. SOHO EIT 195 Å context imaging
eit_start = '2002-08-19T10:24:31'
eit_end   = '2002-08-19T10:36:10'
eit_query = Fido.search(
    a.Time(eit_start, eit_end),
    a.Source('SOHO'),
    a.Instrument('EIT'),
    a.Wavelength(195 * u.Angstrom)
)
print("\nEIT Query Results:")
print(eit_query)
# To download:
# files_eit = Fido.fetch(eit_query)

# 3. TRACE 195 Å high-resolution imaging
trace_start = '2002-08-19T10:34:55'
trace_end   = '2002-08-19T10:50:00'
trace_query = Fido.search(
    a.Time(trace_start, trace_end),
    a.Instrument('TRACE'),
    a.Wavelength(195 * u.Angstrom)
)
print("\nTRACE Query Results:")
print(trace_query)
# To download:
# files_trace = Fido.fetch(trace_query)

# 4. SOHO MDI photospheric magnetograms
mdi_start = '2002-08-19T01:36:00'
mdi_end   = '2002-08-19T11:25:00'
mdi_query = Fido.search(
    a.Time(mdi_start, mdi_end),
    a.Source('SOHO'),
    a.Instrument('MDI')
)
print("\nMDI Query Results:")
print(mdi_query)
# To download:
# files_mdi = Fido.fetch(mdi_query)

print("\nAll queries submitted. Uncomment the fetch lines to download the data.")

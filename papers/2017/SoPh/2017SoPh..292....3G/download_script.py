# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query 1: TRACE 1600 Å ultraviolet images during the flare event on 2001-12-26
# Time interval corresponds to 04:23 – 05:22 UT as used in the paper (668 images total)
time_start_trace = "2001-12-26T04:23:00"
time_end_trace   = "2001-12-26T05:22:00"
instrument_trace = "TRACE"
wavelength_uv    = 1600 * u.Angstrom

# Perform the search for TRACE 1600 Å data
trace_query = Fido.search(
    a.Time(time_start_trace, time_end_trace),
    a.Instrument(instrument_trace),
    a.Wavelength(wavelength_uv)
)

# Print the TRACE query results
print("TRACE 1600 Å data search results:")
print(trace_query)

# Uncomment the following line to download the TRACE data
# fetched_trace = Fido.fetch(trace_query)


# Query 2: SOHO/MDI line-of-sight magnetogram near flare peak for magnetic configuration
# The paper references a magnetogram at 04:51 UT on 2001-12-26 for coalignment and inversion-line mapping
time_start_mdi = "2001-12-26T04:50:00"
time_end_mdi   = "2001-12-26T04:52:00"
instrument_mdi = "MDI"
physobs_mdi    = "LOS_magnetic_field"

# Perform the search for MDI LOS magnetic field data
mdi_query = Fido.search(
    a.Time(time_start_mdi, time_end_mdi),
    a.Instrument(instrument_mdi),
    a.Physobs(physobs_mdi)
)

# Print the MDI query results
print("\nSOHO/MDI LOS magnetic field data search results:")
print(mdi_query)

# Uncomment the following line to download the MDI data
# fetched_mdi = Fido.fetch(mdi_query)

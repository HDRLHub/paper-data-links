# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ------------------------------------------------------------------------------
# Query 1: SOHO/MDI Line‐of‐Sight Magnetograms
# Time Range: 1998-04-29 to 2005-05-13 (inclusive of all 16 studied CME events)
# Physical Observable: LOS magnetic field
# ------------------------------------------------------------------------------

mdi_start = "1998-04-29T00:00:00"
mdi_end   = "2005-05-13T23:59:59"

mdi_search = Fido.search(
    a.Time(mdi_start, mdi_end),
    a.Instrument("MDI"),
    a.Physobs("LOS_magnetic_field")
)

# Print the results of the MDI search
print("MDI Search Results:")
print(mdi_search)

# To download the MDI data, uncomment the following line:
# Fido.fetch(mdi_search)

# ------------------------------------------------------------------------------
# Queries 2–8: TRACE 1600 Å UV Flare‐Ribbon Observations
# Seven TRACE events labeled "T" in Table 1:
#   1) 2000-07-25 01:39:01
#   2) 2001-04-10 04:48:02
#   3) 2001-04-26 09:36:03
#   4) 2003-10-28 09:35:03
#   5) 2003-10-29 19:11:03
#   6) 2003-11-18 06:23:03
#   7) 2004-11-07 14:23:03
# Instrument: TRACE, Wavelength: 1600 Å, Physobs: intensity
# ------------------------------------------------------------------------------

# Event 1: 2000-07-25 01:39:01 UTC
trace1_time = ("2000-07-25T01:39:01", "2000-07-25T01:39:01")
trace1_search = Fido.search(
    a.Time(*trace1_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 1 (2000-07-25T01:39:01) Search Results:")
print(trace1_search)
# Fido.fetch(trace1_search)

# Event 2: 2001-04-10 04:48:02 UTC
trace2_time = ("2001-04-10T04:48:02", "2001-04-10T04:48:02")
trace2_search = Fido.search(
    a.Time(*trace2_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 2 (2001-04-10T04:48:02) Search Results:")
print(trace2_search)
# Fido.fetch(trace2_search)

# Event 3: 2001-04-26 09:36:03 UTC
trace3_time = ("2001-04-26T09:36:03", "2001-04-26T09:36:03")
trace3_search = Fido.search(
    a.Time(*trace3_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 3 (2001-04-26T09:36:03) Search Results:")
print(trace3_search)
# Fido.fetch(trace3_search)

# Event 4: 2003-10-28 09:35:03 UTC
trace4_time = ("2003-10-28T09:35:03", "2003-10-28T09:35:03")
trace4_search = Fido.search(
    a.Time(*trace4_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 4 (2003-10-28T09:35:03) Search Results:")
print(trace4_search)
# Fido.fetch(trace4_search)

# Event 5: 2003-10-29 19:11:03 UTC
trace5_time = ("2003-10-29T19:11:03", "2003-10-29T19:11:03")
trace5_search = Fido.search(
    a.Time(*trace5_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 5 (2003-10-29T19:11:03) Search Results:")
print(trace5_search)
# Fido.fetch(trace5_search)

# Event 6: 2003-11-18 06:23:03 UTC
trace6_time = ("2003-11-18T06:23:03", "2003-11-18T06:23:03")
trace6_search = Fido.search(
    a.Time(*trace6_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 6 (2003-11-18T06:23:03) Search Results:")
print(trace6_search)
# Fido.fetch(trace6_search)

# Event 7: 2004-11-07 14:23:03 UTC
trace7_time = ("2004-11-07T14:23:03", "2004-11-07T14:23:03")
trace7_search = Fido.search(
    a.Time(*trace7_time),
    a.Instrument("TRACE"),
    a.Physobs("intensity"),
    a.Wavelength(1600 * u.Angstrom)
)
print("\nTRACE Event 7 (2004-11-07T14:23:03) Search Results:")
print(trace7_search)
# Fido.fetch(trace7_search)

print("\nAll queries executed. Uncomment the Fido.fetch lines to download data.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Script to query solar data for two partial filament eruption events
using Sunpy's Fido interface to the Virtual Solar Observatory (VSO).
This script searches for AIA, HMI, RHESSI, and LASCO/C2 data
for the 2014-12-24 and 2015-11-04 events.
"""

from sunpy.net import Fido
import sunpy.net.attrs as a
import astropy.units as u

# ------------------------------------------------------------------------------
# Event 1: Confined Partial Eruption (SOL2014-12-24T02:30)
# ------------------------------------------------------------------------------

# 1) AIA EUV/UV imagery (2014-12-24 02:20 – 03:30 UT)
#    Wavelengths: 171, 211, 304, 131, 193, 1600 Å

# AIA 171 Å
query_aia1_171 = Fido.search(
    a.Time("2014-12-24T02:20:00", "2014-12-24T03:30:00"),
    a.Instrument("AIA"),
    a.Wavelength(171 * u.angstrom)
)
print(query_aia1_171)
# files_aia1_171 = Fido.fetch(query_aia1_171)

# AIA 211 Å
query_aia1_211 = Fido.search(
    a.Time("2014-12-24T02:20:00", "2014-12-24T03:30:00"),
    a.Instrument("AIA"),
    a.Wavelength(211 * u.angstrom)
)
print(query_aia1_211)
# files_aia1_211 = Fido.fetch(query_aia1_211)

# AIA 304 Å
query_aia1_304 = Fido.search(
    a.Time("2014-12-24T02:20:00", "2014-12-24T03:30:00"),
    a.Instrument("AIA"),
    a.Wavelength(304 * u.angstrom)
)
print(query_aia1_304)
# files_aia1_304 = Fido.fetch(query_aia1_304)

# AIA 131 Å
query_aia1_131 = Fido.search(
    a.Time("2014-12-24T02:20:00", "2014-12-24T03:30:00"),
    a.Instrument("AIA"),
    a.Wavelength(131 * u.angstrom)
)
print(query_aia1_131)
# files_aia1_131 = Fido.fetch(query_aia1_131)

# AIA 193 Å
query_aia1_193 = Fido.search(
    a.Time("2014-12-24T02:20:00", "2014-12-24T03:30:00"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.angstrom)
)
print(query_aia1_193)
# files_aia1_193 = Fido.fetch(query_aia1_193)

# AIA 1600 Å
query_aia1_1600 = Fido.search(
    a.Time("2014-12-24T02:20:00", "2014-12-24T03:30:00"),
    a.Instrument("AIA"),
    a.Wavelength(1600 * u.angstrom)
)
print(query_aia1_1600)
# files_aia1_1600 = Fido.fetch(query_aia1_1600)


# 2) HMI Line-of-Sight Magnetic Field (2014-12-24 00:00 – 04:00 UT)
query_hmi1 = Fido.search(
    a.Time("2014-12-24T00:00:00", "2014-12-24T04:00:00"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)
print(query_hmi1)
# files_hmi1 = Fido.fetch(query_hmi1)


# 3) RHESSI Hard X-ray Flux (2014-12-24 02:30 – 03:30 UT)
#    Energy bands: 6–12 keV and 12–25 keV

# RHESSI 6–12 keV
query_rhessi1_6_12 = Fido.search(
    a.Time("2014-12-24T02:30:00", "2014-12-24T03:30:00"),
    a.Instrument("RHESSI"),
    a.Wavelength(6 * u.keV, 12 * u.keV)
)
print(query_rhessi1_6_12)
# files_rhessi1_6_12 = Fido.fetch(query_rhessi1_6_12)

# RHESSI 12–25 keV
query_rhessi1_12_25 = Fido.search(
    a.Time("2014-12-24T02:30:00", "2014-12-24T03:30:00"),
    a.Instrument("RHESSI"),
    a.Wavelength(12 * u.keV, 25 * u.keV)
)
print(query_rhessi1_12_25)
# files_rhessi1_12_25 = Fido.fetch(query_rhessi1_12_25)


# 4) LASCO/C2 White-light Coronagraph (2014-12-24 02:30 – 05:00 UT)
query_lasco1 = Fido.search(
    a.Time("2014-12-24T02:30:00", "2014-12-24T05:00:00"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print(query_lasco1)
# files_lasco1 = Fido.fetch(query_lasco1)


# ------------------------------------------------------------------------------
# Event 2: Successful Partial Eruption (SOL2015-11-04T13:31)
# ------------------------------------------------------------------------------

# 1) AIA EUV/UV imagery (2015-11-04 13:10 – 14:15 UT)
#    Wavelengths: 131, 171, 304, 1600, 211, 193 Å

# AIA 131 Å
query_aia2_131 = Fido.search(
    a.Time("2015-11-04T13:10:00", "2015-11-04T14:15:00"),
    a.Instrument("AIA"),
    a.Wavelength(131 * u.angstrom)
)
print(query_aia2_131)
# files_aia2_131 = Fido.fetch(query_aia2_131)

# AIA 171 Å
query_aia2_171 = Fido.search(
    a.Time("2015-11-04T13:10:00", "2015-11-04T14:15:00"),
    a.Instrument("AIA"),
    a.Wavelength(171 * u.angstrom)
)
print(query_aia2_171)
# files_aia2_171 = Fido.fetch(query_aia2_171)

# AIA 304 Å
query_aia2_304 = Fido.search(
    a.Time("2015-11-04T13:10:00", "2015-11-04T14:15:00"),
    a.Instrument("AIA"),
    a.Wavelength(304 * u.angstrom)
)
print(query_aia2_304)
# files_aia2_304 = Fido.fetch(query_aia2_304)

# AIA 1600 Å
query_aia2_1600 = Fido.search(
    a.Time("2015-11-04T13:10:00", "2015-11-04T14:15:00"),
    a.Instrument("AIA"),
    a.Wavelength(1600 * u.angstrom)
)
print(query_aia2_1600)
# files_aia2_1600 = Fido.fetch(query_aia2_1600)

# AIA 211 Å
query_aia2_211 = Fido.search(
    a.Time("2015-11-04T13:10:00", "2015-11-04T14:15:00"),
    a.Instrument("AIA"),
    a.Wavelength(211 * u.angstrom)
)
print(query_aia2_211)
# files_aia2_211 = Fido.fetch(query_aia2_211)

# AIA 193 Å
query_aia2_193 = Fido.search(
    a.Time("2015-11-04T13:10:00", "2015-11-04T14:15:00"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.angstrom)
)
print(query_aia2_193)
# files_aia2_193 = Fido.fetch(query_aia2_193)


# 2) HMI Vector Magnetic Field (2015-11-04 13:00 – 15:00 UT)
query_hmi2 = Fido.search(
    a.Time("2015-11-04T13:00:00", "2015-11-04T15:00:00"),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field")
)
print(query_hmi2)
# files_hmi2 = Fido.fetch(query_hmi2)


# 3) RHESSI Hard X-ray Flux (2015-11-04 13:31 – 14:13 UT)
#    Energy bands: 6–12 keV, 12–25 keV, 25–50 keV

# RHESSI 6–12 keV
query_rhessi2_6_12 = Fido.search(
    a.Time("2015-11-04T13:31:00", "2015-11-04T14:13:00"),
    a.Instrument("RHESSI"),
    a.Wavelength(6 * u.keV, 12 * u.keV)
)
print(query_rhessi2_6_12)
# files_rhessi2_6_12 = Fido.fetch(query_rhessi2_6_12)

# RHESSI 12–25 keV
query_rhessi2_12_25 = Fido.search(
    a.Time("2015-11-04T13:31:00", "2015-11-04T14:13:00"),
    a.Instrument("RHESSI"),
    a.Wavelength(12 * u.keV, 25 * u.keV)
)
print(query_rhessi2_12_25)
# files_rhessi2_12_25 = Fido.fetch(query_rhessi2_12_25)

# RHESSI 25–50 keV
query_rhessi2_25_50 = Fido.search(
    a.Time("2015-11-04T13:31:00", "2015-11-04T14:13:00"),
    a.Instrument("RHESSI"),
    a.Wavelength(25 * u.keV, 50 * u.keV)
)
print(query_rhessi2_25_50)
# files_rhessi2_25_50 = Fido.fetch(query_rhessi2_25_50)


# 4) LASCO/C2 White-light Coronagraph (2015-11-04 13:31 – 16:00 UT)
query_lasco2 = Fido.search(
    a.Time("2015-11-04T13:31:00", "2015-11-04T16:00:00"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print(query_lasco2)
# files_lasco2 = Fido.fetch(query_lasco2)

# End of script

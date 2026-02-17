# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define time ranges for observations
time_range_imaging = a.Time("2011-03-16T17:30:00", "2011-03-16T23:30:00")
time_range_cme_c2 = a.Time("2011-03-16T19:00:00", "2011-03-16T23:36:00")

# ------------------------------------------------------------------
# 1. SDO/AIA multiwavelength imaging (1600, 171, 193, 211, 304 Å)
# ------------------------------------------------------------------

# AIA 1600 Å
query_aia_1600 = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(1600 * u.angstrom)
)
print("AIA 1600 Å Query Results:")
print(query_aia_1600)
# Fido.fetch(query_aia_1600)

# AIA 171 Å
query_aia_171 = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(171 * u.angstrom)
)
print("AIA 171 Å Query Results:")
print(query_aia_171)
# Fido.fetch(query_aia_171)

# AIA 193 Å
query_aia_193 = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.angstrom)
)
print("AIA 193 Å Query Results:")
print(query_aia_193)
# Fido.fetch(query_aia_193)

# AIA 211 Å
query_aia_211 = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(211 * u.angstrom)
)
print("AIA 211 Å Query Results:")
print(query_aia_211)
# Fido.fetch(query_aia_211)

# AIA 304 Å
query_aia_304 = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(304 * u.angstrom)
)
print("AIA 304 Å Query Results:")
print(query_aia_304)
# Fido.fetch(query_aia_304)

# ------------------------------------------------------------------
# 2. SDO/HMI line-of-sight magnetograms (6173 Å)
# ------------------------------------------------------------------

query_hmi_los = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field"),
    a.Wavelength(6173 * u.angstrom)
)
print("HMI LOS Magnetogram Query Results:")
print(query_hmi_los)
# Fido.fetch(query_hmi_los)

# ------------------------------------------------------------------
# 3. SDO/EVE EUV irradiance (1–70 Å)
# ------------------------------------------------------------------

query_eve = Fido.search(
    time_range_imaging,
    a.Source("SDO"),
    a.Instrument("EVE"),
    a.Physobs("irradiance"),
    a.Wavelength(1 * u.angstrom, 70 * u.angstrom)
)
print("EVE 1–70 Å Irradiance Query Results:")
print(query_eve)
# Fido.fetch(query_eve)

# ------------------------------------------------------------------
# 4. SOHO/LASCO C2 white-light CME observations
# ------------------------------------------------------------------

query_lasco_c2 = Fido.search(
    time_range_cme_c2,
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("LASCO C2 CME Query Results:")
print(query_lasco_c2)
# Fido.fetch(query_lasco_c2)

# ------------------------------------------------------------------
# 5. RHESSI hard X-ray imaging (6–12 keV and 12–25 keV)
# ------------------------------------------------------------------

# RHESSI 6–12 keV
query_rhessi_6_12 = Fido.search(
    time_range_imaging,
    a.Source("RHESSI"),
    a.Instrument("RHESSI"),
    a.Wavelength(6 * u.keV, 12 * u.keV)
)
print("RHESSI 6–12 keV Query Results:")
print(query_rhessi_6_12)
# Fido.fetch(query_rhessi_6_12)

# RHESSI 12–25 keV
query_rhessi_12_25 = Fido.search(
    time_range_imaging,
    a.Source("RHESSI"),
    a.Instrument("RHESSI"),
    a.Wavelength(12 * u.keV, 25 * u.keV)
)
print("RHESSI 12–25 keV Query Results:")
print(query_rhessi_12_25)
# Fido.fetch(query_rhessi_12_25)

print("All queries completed. Review results above before fetching data.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# 1. KSO Hα filtergrams for flare ribbon evolution
time_start_halpha = "2011-10-01 09:18"
time_end_halpha = "2011-10-01 11:00"
query_halpha = Fido.search(
    a.Time(time_start_halpha, time_end_halpha),
    a.Source("KSO"),
    a.Instrument("HA2")
)
print("KSO HA2 Hα query results:")
print(query_halpha)
# files_halpha = Fido.fetch(query_halpha)

# 2. SDO/HMI LOS magnetogram at flare onset (720s data series)
time_hmi_los = "2011-10-01 09:18"
query_hmi_los = Fido.search(
    a.Time(time_hmi_los, time_hmi_los),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)
print("\nSDO/HMI LOS magnetogram query results:")
print(query_hmi_los)
# files_hmi_los = Fido.fetch(query_hmi_los)

# 3. SDO/HMI vector magnetogram for pre-flare NLFF modeling (720s data series)
time_hmi_vec = "2011-10-01 07:59"
query_hmi_vec = Fido.search(
    a.Time(time_hmi_vec, time_hmi_vec),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field")
)
print("\nSDO/HMI vector magnetogram query results:")
print(query_hmi_vec)
# files_hmi_vec = Fido.fetch(query_hmi_vec)

# 4. SDO/AIA coronal dimming evolution in multiple EUV wavelengths
time_start_aia = "2011-10-01 09:14"
time_end_aia   = "2011-10-01 21:14"

# AIA 171 Å
query_aia_171 = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Wavelength(171 * u.Angstrom),
    a.Physobs("intensity")
)
print("\nSDO/AIA 171 Å intensity query results:")
print(query_aia_171)
# files_aia_171 = Fido.fetch(query_aia_171)

# AIA 193 Å
query_aia_193 = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Wavelength(193 * u.Angstrom),
    a.Physobs("intensity")
)
print("\nSDO/AIA 193 Å intensity query results:")
print(query_aia_193)
# files_aia_193 = Fido.fetch(query_aia_193)

# AIA 211 Å
query_aia_211 = Fido.search(
    a.Time(time_start_aia, time_end_aia),
    a.Instrument("AIA"),
    a.Wavelength(211 * u.Angstrom),
    a.Physobs("intensity")
)
print("\nSDO/AIA 211 Å intensity query results:")
print(query_aia_211)
# files_aia_211 = Fido.fetch(query_aia_211)

# 5. STEREO SECCHI EUVI, COR1, COR2 for CME early evolution (STEREO-A and B)
time_start_cme = "2011-10-01 09:18"
time_end_cme   = "2011-10-01 14:00"

# STEREO-A EUVI
query_st_a_euvi = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI")
)
print("\nSTEREO-A SECCHI EUVI query results:")
print(query_st_a_euvi)
# files_st_a_euvi = Fido.fetch(query_st_a_euvi)

# STEREO-A COR1
query_st_a_cor1 = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("\nSTEREO-A SECCHI COR1 query results:")
print(query_st_a_cor1)
# files_st_a_cor1 = Fido.fetch(query_st_a_cor1)

# STEREO-A COR2
query_st_a_cor2 = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nSTEREO-A SECCHI COR2 query results:")
print(query_st_a_cor2)
# files_st_a_cor2 = Fido.fetch(query_st_a_cor2)

# STEREO-B EUVI
query_st_b_euvi = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("EUVI")
)
print("\nSTEREO-B SECCHI EUVI query results:")
print(query_st_b_euvi)
# files_st_b_euvi = Fido.fetch(query_st_b_euvi)

# STEREO-B COR1
query_st_b_cor1 = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("\nSTEREO-B SECCHI COR1 query results:")
print(query_st_b_cor1)
# files_st_b_cor1 = Fido.fetch(query_st_b_cor1)

# STEREO-B COR2
query_st_b_cor2 = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nSTEREO-B SECCHI COR2 query results:")
print(query_st_b_cor2)
# files_st_b_cor2 = Fido.fetch(query_st_b_cor2)

# 6. SOHO/LASCO coronagraphic data for 3D CME modeling (C2 and C3)
query_lasco_c2 = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSOHO LASCO C2 query results:")
print(query_lasco_c2)
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

query_lasco_c3 = Fido.search(
    a.Time(time_start_cme, time_end_cme),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nSOHO LASCO C3 query results:")
print(query_lasco_c3)
# files_lasco_c3 = Fido.fetch(query_lasco_c3)

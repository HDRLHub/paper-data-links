# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net Fido
from sunpy.net import attrs as a
import astropy.units as u

# Query 1: SDO/AIA pre-eruption data (211 Å and 304 Å)
time_start1 = "2015-11-04T02:30:00"
time_end1   = "2015-11-04T03:23:00"
query_aia_pre = Fido.search(
    a.Time(time_start1, time_end1),
    a.Instrument("AIA"),
    a.Wavelength(211 * u.angstrom, 211 * u.angstrom),
    a.Wavelength(304 * u.angstrom, 304 * u.angstrom)
)
print("AIA pre-eruption search results:")
print(query_aia_pre)

# Query 2: SDO/AIA impulsive and CME main phase data (94 Å, 193 Å, 211 Å, 304 Å)
time_start2 = "2015-11-04T03:20:00"
time_end2   = "2015-11-04T03:33:30"
query_aia_impulsive = Fido.search(
    a.Time(time_start2, time_end2),
    a.Instrument("AIA"),
    a.Wavelength(94 * u.angstrom, 94 * u.angstrom),
    a.Wavelength(193 * u.angstrom, 193 * u.angstrom),
    a.Wavelength(211 * u.angstrom, 211 * u.angstrom),
    a.Wavelength(304 * u.angstrom, 304 * u.angstrom)
)
print("\nAIA impulsive/CME main-phase search results:")
print(query_aia_impulsive)

# Query 3: SDO/AIA DEM diagnostics epoch (94, 131, 171, 193, 211, 335 Å)
time_start3 = "2015-11-04T03:25:00"
time_end3   = "2015-11-04T03:27:00"
query_aia_dem = Fido.search(
    a.Time(time_start3, time_end3),
    a.Instrument("AIA"),
    a.Wavelength(94  * u.angstrom, 94  * u.angstrom),
    a.Wavelength(131 * u.angstrom, 131 * u.angstrom),
    a.Wavelength(171 * u.angstrom, 171 * u.angstrom),
    a.Wavelength(193 * u.angstrom, 193 * u.angstrom),
    a.Wavelength(211 * u.angstrom, 211 * u.angstrom),
    a.Wavelength(335 * u.angstrom, 335 * u.angstrom)
)
print("\nAIA DEM diagnostics search results:")
print(query_aia_dem)

# Query 4: SDO/HMI vector magnetic field before and during eruption
# Pre-eruption at 02:34:12 UT
time_hmi1 = "2015-11-04T02:34:12"
query_hmi_pre = Fido.search(
    a.Time(time_hmi1, time_hmi1),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field")
)
print("\nHMI vector magnetogram at 02:34:12 UT:")
print(query_hmi_pre)

# During eruption at 03:22:12 UT
time_hmi2 = "2015-11-04T03:22:12"
query_hmi_during = Fido.search(
    a.Time(time_hmi2, time_hmi2),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field")
)
print("\nHMI vector magnetogram at 03:22:12 UT:")
print(query_hmi_during)

# Query 5: RHESSI hard X-ray light curves and imaging
time_rhessi = "2015-11-04T03:15:02", "2015-11-04T03:40:00"
query_rhessi = Fido.search(
    a.Time(*time_rhessi),
    a.Instrument("RHESSI"),
    a.Wavelength(3 * u.keV, 800 * u.keV)
)
print("\nRHESSI HXR search results (3–800 keV):")
print(query_rhessi)

# Query 6: SDO/EVE ESP irradiance (0.1–7 nm equivalent)
time_eve = "2015-11-04T03:15:00", "2015-11-04T03:40:00"
query_eve = Fido.search(
    a.Time(*time_eve),
    a.Instrument("EVE"),
    a.Physobs("irradiance")
)
print("\nEVE ESP irradiance search results (0.1–7 nm):")
print(query_eve)

# Query 7: SOHO/LASCO C2 white-light coronagraph (CME propagation after 03:48 UT)
time_lasco = "2015-11-04T03:48:00", "2015-11-04T05:00:00"
query_lasco = Fido.search(
    a.Time(*time_lasco),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nLASCO C2 search results (white-light CME):")
print(query_lasco)

# Uncomment the following lines to fetch data once queries are verified
# files_aia_pre       = Fido.fetch(query_aia_pre)
# files_aia_impulsive = Fido.fetch(query_aia_impulsive)
# files_aia_dem       = Fido.fetch(query_aia_dem)
# files_hmi_pre       = Fido.fetch(query_hmi_pre)
# files_hmi_during    = Fido.fetch(query_hmi_during)
# files_rhessi        = Fido.fetch(query_rhessi)
# files_eve           = Fido.fetch(query_eve)
# files_lasco         = Fido.fetch(query_lasco)

print("\nScript completed. Verify search results before fetching data.")

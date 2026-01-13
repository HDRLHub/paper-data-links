# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a
import astropy.units as u

# -------------------------------------------------------------------
# 1. AIA Multiwavelength Imaging: Morphological Evolution and Eruption Onset
# Time Range: 2015-05-09 00:00 – 2015-05-09 01:14 UT
# Wavelengths: 304, 193, 131, 1600, 211 Å
# -------------------------------------------------------------------
time_aia1 = a.Time('2015-05-09 00:00:00', '2015-05-09 01:14:00')
wavelengths_aia1 = [304 * u.Angstrom,
                    193 * u.Angstrom,
                    131 * u.Angstrom,
                    1600 * u.Angstrom,
                    211 * u.Angstrom]

query_aia1 = Fido.search(
    time_aia1,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(wavelengths_aia1)
)
print("AIA Morphology Query Results:")
print(query_aia1)
# files_aia1 = Fido.fetch(query_aia1)

# -------------------------------------------------------------------
# 2. AIA Plasma Flow and Kinematic Analysis
# Time Range: 2015-05-09 00:55 – 2015-05-09 01:03 UT
# Wavelength: 304 Å (one-minute cadence for DAVE)
# -------------------------------------------------------------------
time_aia2 = a.Time('2015-05-09 00:55:00', '2015-05-09 01:03:00')
wavelength_aia2 = 304 * u.Angstrom

query_aia2 = Fido.search(
    time_aia2,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(wavelength_aia2)
)
print("\nAIA Plasma Flow Query Results:")
print(query_aia2)
# files_aia2 = Fido.fetch(query_aia2)

# -------------------------------------------------------------------
# 3. AIA Thermal Diagnostics via DEM
# Time Range: 2015-05-09 00:50 – 2015-05-09 01:30 UT
# Wavelengths: 94, 131, 171, 193, 211, 335 Å
# -------------------------------------------------------------------
time_aia3 = a.Time('2015-05-09 00:50:00', '2015-05-09 01:30:00')
wavelengths_aia3 = [94 * u.Angstrom,
                    131 * u.Angstrom,
                    171 * u.Angstrom,
                    193 * u.Angstrom,
                    211 * u.Angstrom,
                    335 * u.Angstrom]

query_aia3 = Fido.search(
    time_aia3,
    a.Source('SDO'),
    a.Instrument('AIA'),
    a.Wavelength(wavelengths_aia3)
)
print("\nAIA DEM Query Results:")
print(query_aia3)
# files_aia3 = Fido.fetch(query_aia3)

# -------------------------------------------------------------------
# 4. HMI Photospheric Magnetic Field: LOS and Vector Magnetograms
# Time Range: 2015-05-09 00:00 – 2015-05-09 01:30 UT
# Data Types: LOS magnetic field, vector magnetic field
# -------------------------------------------------------------------
time_hmi = a.Time('2015-05-09 00:00:00', '2015-05-09 01:30:00')

# 4a. Line-of-sight magnetograms
query_hmi_los = Fido.search(
    time_hmi,
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field')
)
print("\nHMI LOS Magnetogram Query Results:")
print(query_hmi_los)
# files_hmi_los = Fido.fetch(query_hmi_los)

# 4b. Vector magnetic field
query_hmi_vector = Fido.search(
    time_hmi,
    a.Source('SDO'),
    a.Instrument('HMI'),
    a.Physobs('vector_magnetic_field')
)
print("\nHMI Vector Magnetogram Query Results:")
print(query_hmi_vector)
# files_hmi_vector = Fido.fetch(query_hmi_vector)

# -------------------------------------------------------------------
# 5. SOHO LASCO White-light Coronagraphy: CME Kinematics
# Time Range: 2015-05-09 01:36 – 2015-05-09 02:30 UT
# Detectors: C2 and C3
# -------------------------------------------------------------------
time_lasco = a.Time('2015-05-09 01:36:00', '2015-05-09 02:30:00')

# 5a. LASCO/C2
query_lasco_c2 = Fido.search(
    time_lasco,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Physobs('intensity')
)
print("\nLASCO C2 Query Results:")
print(query_lasco_c2)
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# 5b. LASCO/C3
query_lasco_c3 = Fido.search(
    time_lasco,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C3'),
    a.Physobs('intensity')
)
print("\nLASCO C3 Query Results:")
print(query_lasco_c3)
# files_lasco_c3 = Fido.fetch(query_lasco_c3)

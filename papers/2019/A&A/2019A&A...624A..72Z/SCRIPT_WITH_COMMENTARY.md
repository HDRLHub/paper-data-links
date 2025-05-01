# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Python script to query solar data from the Virtual Solar Observatory (VSO)
using SunPy’s Fido interface.

This script queries data for the eruptive prominence event on May 28, 2014.
Data from IRIS (both slit‐jaw imaging and Mg II spectral observations),
SDO/AIA 304 Å imaging, and SOHO/LASCO C2 white-light coronagraph are retrieved.

Note: The actual fetching of data (with Fido.fetch) is commented out.
"""

# Import necessary modules from SunPy and Astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ------------------------------
# 1. IRIS Data Query: Slit-Jaw Imaging (SJI)
#    - Instrument: IRIS with Detector 'SJI'
#    - Time Range: 2014-05-28T11:24:00 to 2014-05-28T16:01:00
#    - Wavelength: Two channels are used in SJI. 
#         -> One channel covers ~1400 Å (using the available range 1380-1420 Å)
#         -> The other channel covers ~2796 Å (using the available range 2794-2798 Å)
# We perform two separate queries for clarity.
# ------------------------------

# Define the time range for IRIS SJI observations
time_iris_sji = a.Time("2014-05-28T11:24:00", "2014-05-28T16:01:00")

# Query for IRIS SJI 1400 Å channel using the wavelength range 1380-1420 Å
iris_sji_1400 = Fido.search(time_iris_sji,
                            a.Instrument("IRIS"),
                            a.Detector("SJI"),
                            a.Wavelength(1380*u.AA, 1420*u.AA))
print("IRIS SJI 1400 Å Query Results:")
print(iris_sji_1400)

# Uncomment the following line to fetch the IRIS SJI 1400 Å data
# files_iris_sji_1400 = Fido.fetch(iris_sji_1400)

# Query for IRIS SJI 2796 Å channel using the wavelength range 2794-2798 Å
iris_sji_2796 = Fido.search(time_iris_sji,
                            a.Instrument("IRIS"),
                            a.Detector("SJI"),
                            a.Wavelength(2794*u.AA, 2798*u.AA))
print("\nIRIS SJI 2796 Å Query Results:")
print(iris_sji_2796)

# Uncomment the following line to fetch the IRIS SJI 2796 Å data
# files_iris_sji_2796 = Fido.fetch(iris_sji_2796)

# ------------------------------
# 2. IRIS Data Query: Mg II Spectral Observations
#    - Instrument: IRIS with Detector 'NUV'
#    - Time Range: 2014-05-28T11:24:00 to 2014-05-28T16:01:00
#    - Wavelength: Mg II h & k lines are contained in the near-UV (range 2785-2835 Å)
# ------------------------------

# Define the time range is the same as for SJI observations.
time_iris_spec = a.Time("2014-05-28T11:24:00", "2014-05-28T16:01:00")

iris_mgii_spec = Fido.search(time_iris_spec,
                             a.Instrument("IRIS"),
                             a.Detector("NUV"),
                             a.Wavelength(2785*u.AA, 2835*u.AA))
print("\nIRIS Mg II Spectrum (NUV) Query Results:")
print(iris_mgii_spec)

# Uncomment the following line to fetch the IRIS Mg II spectral data
# files_iris_mgii_spec = Fido.fetch(iris_mgii_spec)

# ------------------------------
# 3. SDO/AIA Data Query: 304 Å Imaging
#    - Instrument: AIA on board SDO
#    - Time Range: 2014-05-28T11:00:00 to 2014-05-28T21:00:00
#    - Wavelength: 304 Å channel
# ------------------------------

# Define the time range for AIA 304 Å observations
time_aia = a.Time("2014-05-28T11:00:00", "2014-05-28T21:00:00")

aia_304 = Fido.search(time_aia,
                      a.Source("SDO"),
                      a.Instrument("AIA"),
                      a.Wavelength(304*u.AA, 304*u.AA))
print("\nSDO/AIA 304 Å Query Results:")
print(aia_304)

# Uncomment the following line to fetch the AIA 304 Å data
# files_aia_304 = Fido.fetch(aia_304)

# ------------------------------
# 4. SOHO/LASCO Data Query: White-Light Coronagraph (C2)
#    - Instrument: LASCO (SOHO) with Detector 'C2'
#    - Time Range: 2014-05-28T21:00:00 to 2014-05-28T22:50:00
#    - Wavelength: White-light observations (no specific wavelength required)
# ------------------------------

# Define the time range for LASCO C2 white-light observations
time_lasco = a.Time("2014-05-28T21:00:00", "2014-05-28T22:50:00")

lasco_c2 = Fido.search(time_lasco,
                       a.Source("SOHO"),
                       a.Instrument("LASCO"),
                       a.Detector("C2"))
print("\nSOHO/LASCO C2 White-Light Query Results:")
print(lasco_c2)

# Uncomment the following line to fetch the LASCO C2 data
# files_lasco_c2 = Fido.fetch(lasco_c2)

# End of Script
if __name__ == "__main__":
    print("\nQuerying completed. Data can be fetched by uncommenting the Fido.fetch lines.")

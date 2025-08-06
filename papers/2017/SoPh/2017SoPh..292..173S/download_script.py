# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the primary time ranges based on the study context
# CME and EIT data: 11 January 1996 to 31 March 2013
time_cme = a.Time('1996-01-11', '2013-03-31')

# AIA data (SDO launch to study end): 11 February 2010 to 31 March 2013
time_aia = a.Time('2010-02-11', '2013-03-31')

# -------------------------------------------------------------------
# 1. Query SOHO/EIT 195 Å data for flare–CME association confirmation
# -------------------------------------------------------------------
query_eit_195 = Fido.search(
    time_cme,
    a.Instrument('EIT'),
    a.Detector('EIT'),
    a.Wavelength(195.0 * u.angstrom)
)
print("EIT 195 Å query results:")
print(query_eit_195)

# To download the data, uncomment the line below:
# files_eit_195 = Fido.fetch(query_eit_195)

# -------------------------------------------------------------------
# 2. Query SDO/AIA 193 Å data for flare–CME association confirmation
# -------------------------------------------------------------------
query_aia_193 = Fido.search(
    time_aia,
    a.Instrument('AIA'),
    a.Wavelength(193.0 * u.angstrom)
)
print("AIA 193 Å query results:")
print(query_aia_193)

# To download the data, uncomment the line below:
# files_aia_193 = Fido.fetch(query_aia_193)

# -------------------------------------------------------------------
# 3. Query SOHO/LASCO C2 coronagraph data for CME parameterization
# -------------------------------------------------------------------
query_lasco_c2 = Fido.search(
    time_cme,
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("LASCO C2 query results:")
print(query_lasco_c2)

# To download the data, uncomment the line below:
# files_lasco_c2 = Fido.fetch(query_lasco_c2)

# -------------------------------------------------------------------
# 4. Query SOHO/LASCO C3 coronagraph data for CME parameterization
# -------------------------------------------------------------------
query_lasco_c3 = Fido.search(
    time_cme,
    a.Instrument('LASCO'),
    a.Detector('C3')
)
print("LASCO C3 query results:")
print(query_lasco_c3)

# To download the data, uncomment the line below:
# files_lasco_c3 = Fido.fetch(query_lasco_c3)

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import datetime
from astropy import units as u
from sunpy.net import Fido, attrs as a

# Define the time range for the 2017 June 1 event
t_start = datetime.datetime(2017, 6, 1, 1, 30, 0)
t_end   = datetime.datetime(2017, 6, 1, 2, 38, 0)

# -------------------------------------------------------------------
# Query 1: SDO/AIA 171 Å data for the filament eruption and EUV waves
# -------------------------------------------------------------------
query_aia_171 = Fido.search(
    a.Time(t_start, t_end),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(171 * u.angstrom)
)
print("AIA 171 Å Query Results:")
print(query_aia_171)

# To download the data, uncomment the next line
# Fido.fetch(query_aia_171)

# --------------------------------------------------------------------
# Query 2: SDO/AIA 193 Å data for EUV wave fronts and base-ratio images
# --------------------------------------------------------------------
query_aia_193 = Fido.search(
    a.Time(t_start, t_end),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(193 * u.angstrom)
)
print("AIA 193 Å Query Results:")
print(query_aia_193)

# To download the data, uncomment the next line
# Fido.fetch(query_aia_193)

# --------------------------------------------------------------------
# Query 3: SDO/AIA 211 Å data for heating diagnostics during the eruption
# --------------------------------------------------------------------
query_aia_211 = Fido.search(
    a.Time(t_start, t_end),
    a.Instrument('AIA'),
    a.Source('SDO'),
    a.Wavelength(211 * u.angstrom)
)
print("AIA 211 Å Query Results:")
print(query_aia_211)

# To download the data, uncomment the next line
# Fido.fetch(query_aia_211)

# ------------------------------------------------------------------------
# Query 4: SOHO/LASCO C2 white-light coronagraph data for CME and streamer
# ------------------------------------------------------------------------
query_lasco_c2 = Fido.search(
    a.Time(t_start, t_end),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Source('SOHO')
)
print("LASCO C2 Query Results:")
print(query_lasco_c2)

# To download the data, uncomment the next line
# Fido.fetch(query_lasco_c2)

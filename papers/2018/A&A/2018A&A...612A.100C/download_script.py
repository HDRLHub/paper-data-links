# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time

# --------------------------------------------------------------------------------
# Query 1: SDO/AIA 193 Å imagery around the EUV wave event on 2012-03-09
# Time range: 2012-03-09T03:41:00 – 2012-03-09T04:00:00 UT
# Wavelength: 193 Å (Fe XII channel for coronal EUV wave fronts)
# --------------------------------------------------------------------------------
tstart_aia = parse_time("2012-03-09T03:41:00")
tend_aia   = parse_time("2012-03-09T04:00:00")

query_aia = Fido.search(
    a.Time(tstart_aia, tend_aia),
    a.Instrument('AIA'),
    a.Wavelength(193 * u.Angstrom)
)

print("AIA 193 Å search results:")
print(query_aia)

# To download the data, uncomment the following line:
# fetched_aia = Fido.fetch(query_aia)

# --------------------------------------------------------------------------------
# Query 2: SDO/HMI line-of-sight magnetograms around the event for magnetic field extrapolation
# Time range: 2012-03-09T03:40:00 – 2012-03-09T04:00:00 UT
# Observable: LOS_magnetic_field at 6173 Å
# --------------------------------------------------------------------------------
tstart_hmi = parse_time("2012-03-09T03:40:00")
tend_hmi   = parse_time("2012-03-09T04:00:00")

query_hmi = Fido.search(
    a.Time(tstart_hmi, tend_hmi),
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Wavelength(6173 * u.Angstrom)
)

print("\nHMI LOS magnetogram search results:")
print(query_hmi)

# To download the data, uncomment the following line:
# fetched_hmi = Fido.fetch(query_hmi)

# --------------------------------------------------------------------------------
# Query 3: SOHO/LASCO-C2 white-light coronagraph images for CME observation
# Time range: 2012-03-09T03:41:00 – 2012-03-09T04:26:09 UT
# Detector: C2
# --------------------------------------------------------------------------------
tstart_lasco = parse_time("2012-03-09T03:41:00")
tend_lasco   = parse_time("2012-03-09T04:26:09")

query_lasco_c2 = Fido.search(
    a.Time(tstart_lasco, tend_lasco),
    a.Instrument('LASCO'),
    a.Detector('C2')
)

print("\nLASCO C2 search results:")
print(query_lasco_c2)

# To download the data, uncomment the following line:
# fetched_lasco_c2 = Fido.fetch(query_lasco_c2)

# --------------------------------------------------------------------------------
# Query 4: SOHO/LASCO-C3 white-light coronagraph images for extended CME evolution
# Time range: 2012-03-09T03:41:00 – 2012-03-09T04:26:09 UT
# Detector: C3
# --------------------------------------------------------------------------------
query_lasco_c3 = Fido.search(
    a.Time(tstart_lasco, tend_lasco),
    a.Instrument('LASCO'),
    a.Detector('C3')
)

print("\nLASCO C3 search results:")
print(query_lasco_c3)

# To download the data, uncomment the following line:
# fetched_lasco_c3 = Fido.fetch(query_lasco_c3)

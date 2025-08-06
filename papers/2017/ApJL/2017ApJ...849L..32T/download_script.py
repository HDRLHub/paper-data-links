# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.vso as vso
from sunpy.net.vso import attrs as a

# Initialize the VSO client
client = vso.VSOClient()

# ----------------------------------------------------------------------
# 1. Query PAMELA monthly-resolved proton data (July 2006 – January 2010)
# ----------------------------------------------------------------------
time_range_pamela = a.Time('2006-07-01', '2010-01-31')
instrument_pamela = a.Instrument('PAMELA')

print("=== PAMELA Proton Flux Query ===")
print(f"Time range : {time_range_pamela}")
print(f"Instrument : {instrument_pamela}")
results_pamela = client.query(time_range_pamela, instrument_pamela)
print(results_pamela)
# To download the data, uncomment the following line:
# client.fetch(results_pamela)

# ----------------------------------------------------------------------
# 2. Query EPHIN/SOHO yearly-resolved proton data (2000 – 2016)
# ----------------------------------------------------------------------
time_range_ephin = a.Time('2000-01-01', '2016-12-31')
source_ephin = a.Source('SOHO')
instrument_ephin = a.Instrument('EPHIN')

print("\n=== EPHIN/SOHO Proton Flux Query ===")
print(f"Time range : {time_range_ephin}")
print(f"Source     : {source_ephin}")
print(f"Instrument : {instrument_ephin}")
results_ephin = client.query(time_range_ephin, source_ephin, instrument_ephin)
print(results_ephin)
# To download the data, uncomment the following line:
# client.fetch(results_ephin)

# ----------------------------------------------------------------------
# 3. Query BESS Polar-I proton data (13 December 2004 – 21 December 2004)
# ----------------------------------------------------------------------
time_range_bess1 = a.Time('2004-12-13', '2004-12-21')
instrument_bess = a.Instrument('BESS')

print("\n=== BESS Polar-I Proton Flux Query ===")
print(f"Time range : {time_range_bess1}")
print(f"Instrument : {instrument_bess}")
results_bess1 = client.query(time_range_bess1, instrument_bess)
print(results_bess1)
# To download the data, uncomment the following line:
# client.fetch(results_bess1)

# ----------------------------------------------------------------------
# 4. Query BESS Polar-II proton data (23 December 2007 – 16 January 2008)
# ----------------------------------------------------------------------
time_range_bess2 = a.Time('2007-12-23', '2008-01-16')

print("\n=== BESS Polar-II Proton Flux Query ===")
print(f"Time range : {time_range_bess2}")
print(f"Instrument : {instrument_bess}")
results_bess2 = client.query(time_range_bess2, instrument_bess)
print(results_bess2)
# To download the data, uncomment the following line:
# client.fetch(results_bess2)

print("\nNote: If any of these instruments are not available in the VSO database, the query results will be empty.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.dataretriever.sources.vso as vso_sources
from sunpy.net import Fido, attrs as a

# NOTE: The provided VSO interface did not list any available instruments.
# We attempt queries for the instruments used in the context (GOES, SOHO, ACE),
# but these may not be available in the actual VSO registry.

# 1. Query GOES proton flux data for >10 MeV (SPEs) from 1996-01-01 to 2011-12-31.
time_goes = a.Time('1996-01-01', '2011-12-31')
instrument_goes = a.Instrument('GOES')
# Physobs is not strictly required for VSO search, but we include it for clarity.
physobs_protons = a.Physobs('proton flux')

query_goes = Fido.search(time_goes, instrument_goes, physobs_protons)
print("GOES SPE proton flux query results:")
print(query_goes)
# To download the data, uncomment the following line:
# files_goes = Fido.fetch(query_goes)

# 2. Query SOHO in-situ solar wind speed measurements for the same interval.
# Context specifies ±2 hours around each event maximum; here we default to the full range.
time_soho = a.Time('1996-01-01', '2011-12-31')
instrument_soho = a.Instrument('SOHO')
physobs_speed = a.Physobs('bulk speed')

query_soho = Fido.search(time_soho, instrument_soho, physobs_speed)
print("\nSOHO solar wind speed query results:")
print(query_soho)
# To download the data, uncomment the following line:
# files_soho = Fido.fetch(query_soho)

# 3. Query ACE in-situ solar wind speed measurements for the same interval.
time_ace = a.Time('1996-01-01', '2011-12-31')
instrument_ace = a.Instrument('ACE')

query_ace = Fido.search(time_ace, instrument_ace, physobs_speed)
print("\nACE solar wind speed query results:")
print(query_ace)
# To download the data, uncomment the following line:
# files_ace = Fido.fetch(query_ace)

print("\nNote: If these queries return empty results, the instruments may not be registered "
      "in the provided VSO interface. Please verify instrument availability in VSO.")

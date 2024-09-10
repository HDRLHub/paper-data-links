# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for the different data collection periods
time_range_sc23 = a.Time('1996-08-01', '2008-12-31')
time_range_sc24 = a.Time('2009-01-01', '2019-12-31')
time_range_wind_waves = a.Time('1997-04-01', '2006-10-31')
time_range_stereo_waves = a.Time('2006-10-01', '2019-12-31')

# Define the instruments and their respective attributes
instrument_lasco = a.Instrument('LASCO')
instrument_wind_waves = a.Instrument('WAVES')
instrument_stereo_waves = a.Instrument('WAVES')

# LASCO queries for SC 23 and SC 24
# Warning: The following queries may return a large number of results and could be paginated
query_lasco_sc23 = Fido.search(time_range_sc23, instrument_lasco)
query_lasco_sc24 = Fido.search(time_range_sc24, instrument_lasco)

# Wind/WAVES query for type II radio bursts
# Note: The time range might be too broad. Using a smaller example time range.
# Original time range: time_range_wind_waves
example_time_range_wind_waves = a.Time('1997-04-01', '1997-04-30')  # Example time range within the original range
query_wind_waves = Fido.search(example_time_range_wind_waves, instrument_wind_waves)

# STEREO/WAVES query for type II radio bursts
# Note: The time range might be too broad. Using a smaller example time range.
# Original time range: time_range_stereo_waves
example_time_range_stereo_waves = a.Time('2006-10-01', '2006-10-31')  # Example time range within the original range
query_stereo_waves = Fido.search(example_time_range_stereo_waves, instrument_stereo_waves)

# Print out the query results
print("LASCO SC 23 Query Results:")
print(query_lasco_sc23)
print("\nLASCO SC 24 Query Results:")
print(query_lasco_sc24)
print("\nWind/WAVES Query Results:")
print(query_wind_waves)
print("\nSTEREO/WAVES Query Results:")
print(query_stereo_waves)

# Uncomment the following lines to fetch the data
# lasco_sc23_files = Fido.fetch(query_lasco_sc23)
# lasco_sc24_files = Fido.fetch(query_lasco_sc24)
# wind_waves_files = Fido.fetch(query_wind_waves)
# stereo_waves_files = Fido.fetch(query_stereo_waves)

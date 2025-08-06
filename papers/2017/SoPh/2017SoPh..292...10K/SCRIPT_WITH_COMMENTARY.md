# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.dataretriever.sources.soho as soho
from sunpy.net import Fido, attrs as a
from astropy.time import Time, TimeDelta

# =============================================================================
# 1. Full‐Mission SOHO/EPHIN Data Search (1995‐12‐01 to 2015‐10‐01)
# =============================================================================

# Define the full‐mission time range for EPHIN data
time_full_start = '1995-12-01 00:00'
time_full_end   = '2015-10-01 23:59'

# Instrument and source attributes for the SOHO/EPHIN instrument
instrument = a.vso.Instrument('EPHIN')
source     = a.vso.Source('SOHO')

# Assemble the time attribute
time_range_full = a.Time(time_full_start, time_full_end)

# Perform the query
search_full = Fido.search(time_range_full, instrument, source)

# Print out the search results for inspection
print("Full‐Mission SOHO/EPHIN Search Results:")
print(search_full)

# To download the data, uncomment the following line
# results_full = Fido.fetch(search_full)

# =============================================================================
# 2. Example SEP Event Spectral Analysis Interval
#    (2‐hour window starting 30 min after event onset)
# =============================================================================

# Replace the following placeholder with an actual event onset time
event_onset = 'YYYY-MM-DDThh:mm:ss'

# Convert onset time into an Astropy Time object
onset_time = Time(event_onset)

# Calculate start time: 30 minutes after onset
start_time_event = onset_time + TimeDelta(30 * 60, format='sec')

# Calculate end time: 2 hours (120 minutes) after that
end_time_event = start_time_event + TimeDelta(120 * 60, format='sec')

# Assemble the event‐specific time attribute
time_range_event = a.Time(start_time_event.iso, end_time_event.iso)

# Perform the query for this specific SEP event interval
search_event = Fido.search(time_range_event, instrument, source)

# Print out the event‐specific search results
print("\nSEP Event‐Specific SOHO/EPHIN Search Results:")
print(search_event)

# To download the event‐specific data, uncomment the following line
# results_event = Fido.fetch(search_event)

# =============================================================================
# End of script
# =============================================================================

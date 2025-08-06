# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido
import sunpy.net.attrs as a

# Query RHESSI hard X-ray data for the two events identified in the context.
# Instrument "RHESSI" is available in the provided VSO interface.

# Event 1: RHESSI peak at 2004-02-28 03:24 UT
time_event1 = a.Time('2004-02-28 03:24', '2004-02-28 03:24')
instrument = a.Instrument('RHESSI')

# Search for RHESSI data at the time of the first event
query1 = Fido.search(time_event1, instrument)
print("RHESSI Query Results for Event 1 (2004-02-28 03:24 UT):")
print(query1)

# To download the data for Event 1, uncomment the following line:
# files_event1 = Fido.fetch(query1)

# Event 2: RHESSI peak at 2004-03-16 08:56 UT
time_event2 = a.Time('2004-03-16 08:56', '2004-03-16 08:56')

# Search for RHESSI data at the time of the second event
query2 = Fido.search(time_event2, instrument)
print("RHESSI Query Results for Event 2 (2004-03-16 08:56 UT):")
print(query2)

# To download the data for Event 2, uncomment the following line:
# files_event2 = Fido.fetch(query2)

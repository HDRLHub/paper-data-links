# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a

# Define the GONG instrument attribute for all queries
gong_instrument = a.Instrument('GONG')

# -----------------------------------------------------------------------------
# 1. Query GONG data for the solar minimum preceding Cycle 23 ("Min23")
#    Time Range: 7 May 1995 – 11 August 1997 (inclusive)
# -----------------------------------------------------------------------------
time_min23 = a.Time('1995-05-07', '1997-08-11')

# Perform the search for Min23
results_min23 = Fido.search(
    time_min23,
    gong_instrument
)

# Print out the search results for inspection
print("Min23 Query Results:")
print(results_min23)

# To download the data, uncomment the following line:
# Fido.fetch(results_min23)

# -----------------------------------------------------------------------------
# 2. Query GONG data for the solar maximum of Cycle 23 ("Max23")
#    Time Range: 29 January 2000 – 5 May 2002 (inclusive)
# -----------------------------------------------------------------------------
time_max23 = a.Time('2000-01-29', '2002-05-05')

# Perform the search for Max23
results_max23 = Fido.search(
    time_max23,
    gong_instrument
)

# Print out the search results for inspection
print("\nMax23 Query Results:")
print(results_max23)

# To download the data, uncomment the following line:
# Fido.fetch(results_max23)

# -----------------------------------------------------------------------------
# 3. Query GONG data for the solar minimum following Cycle 23 ("Min24")
#    Time Range: 21 June 2007 – 25 November 2009 (inclusive)
# -----------------------------------------------------------------------------
time_min24 = a.Time('2007-06-21', '2009-11-25')

# Perform the search for Min24
results_min24 = Fido.search(
    time_min24,
    gong_instrument
)

# Print out the search results for inspection
print("\nMin24 Query Results:")
print(results_min24)

# To download the data, uncomment the following line:
# Fido.fetch(results_min24)

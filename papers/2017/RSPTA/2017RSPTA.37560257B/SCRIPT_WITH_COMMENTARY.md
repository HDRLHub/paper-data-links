# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido
from sunpy.net import attrs as a

# -------------------------------------------------------------------
# Data Collection Period 1: SOHO/LASCO C2 and C3 from 1996-01-01 to 2016-05-31
# -------------------------------------------------------------------

# Define the time range for the main mission phase
time_period1 = a.Time('1996-01-01', '2016-05-31')

# Define the instruments for C2 and C3 coronagraphs
instrument_c2 = a.Instrument('LASCO C2')
instrument_c3 = a.Instrument('LASCO C3')

# Query for LASCO C2 images in the main mission phase
print("Searching for SOHO/LASCO C2 data (1996-01-01 to 2016-05-31)...")
result_c2_p1 = Fido.search(time_period1, instrument_c2)
print(result_c2_p1)
# To download, uncomment the following line:
# downloaded_c2_p1 = Fido.fetch(result_c2_p1)

# Query for LASCO C3 images in the main mission phase
print("Searching for SOHO/LASCO C3 data (1996-01-01 to 2016-05-31)...")
result_c3_p1 = Fido.search(time_period1, instrument_c3)
print(result_c3_p1)
# To download, uncomment the following line:
# downloaded_c3_p1 = Fido.fetch(result_c3_p1)


# -------------------------------------------------------------------
# Data Collection Period 2: High–Cadence Phase from 2010-08-03 to 2016-05-31
# -------------------------------------------------------------------

# Define the time range for the high–cadence extended mission phase
time_period2 = a.Time('2010-08-03', '2016-05-31')

# Query for LASCO C2 images in the high–cadence phase
print("Searching for SOHO/LASCO C2 data (2010-08-03 to 2016-05-31)...")
result_c2_p2 = Fido.search(time_period2, instrument_c2)
print(result_c2_p2)
# To download, uncomment the following line:
# downloaded_c2_p2 = Fido.fetch(result_c2_p2)

# Query for LASCO C3 images in the high–cadence phase
print("Searching for SOHO/LASCO C3 data (2010-08-03 to 2016-05-31)...")
result_c3_p2 = Fido.search(time_period2, instrument_c3)
print(result_c3_p2)
# To download, uncomment the following line:
# downloaded_c3_p2 = Fido.fetch(result_c3_p2)

print("All searches complete.")

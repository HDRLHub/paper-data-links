# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a

# Context: We want to query data from the following instruments:
# 1. Low Energy Matrix Telescope (LEMT) on board Wind spacecraft
# 2. Low Energy Telescope (LET) on board STEREO spacecraft (both ahead (A) and behind (B))
# 3. Large Angle and Spectrometric Coronagraph (LASCO) on board SOHO

# Define the time range for the queries
time_range = a.Time('2006-10-01', '2023-10-01')

# Query for Low Energy Matrix Telescope (LEMT) on board Wind spacecraft
# Note: Wind spacecraft is not listed in the provided VSO interface, so we will skip this query.

# Query for Low Energy Telescope (LET) on board STEREO spacecraft (both ahead (A) and behind (B))
query_stereo_a_let = Fido.search(
    time_range, a.Instrument('LET'), a.Source('STEREO_A')
)
query_stereo_b_let = Fido.search(
    time_range, a.Instrument('LET'), a.Source('STEREO_B')
)

# Query for Large Angle and Spectrometric Coronagraph (LASCO) on board SOHO
query_soho_lasco = Fido.search(
    time_range, a.Instrument('LASCO'), a.Source('SOHO')
)

# Print out the query results
print("Query results for STEREO_A LET:")
print(query_stereo_a_let)
print("\nQuery results for STEREO_B LET:")
print(query_stereo_b_let)
print("\nQuery results for SOHO LASCO:")
print(query_soho_lasco)

# Note: The results are paginated. The output shows only a portion of the total results.
# Uncomment the following lines to fetch the data
# Fido.fetch(query_stereo_a_let)
# Fido.fetch(query_stereo_b_let)
# Fido.fetch(query_soho_lasco)

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Context: We are interested in data from the SWAN instrument on board SOHO
# for the study of backscattered solar Lyman-α emission and solar wind mass flux.

# Reasoning:
# 1. We need to query the VSO for data from the SWAN instrument on SOHO.
# 2. The time ranges of interest are 1996-2018 and 1996-2001.
# 3. The wavelength of interest is 121.567 nm (Lyman-α).
# 4. The physical observables are backscattered solar Lyman-α intensity and solar wind mass flux.

# Define the time ranges for the two data collection periods
time_range_1 = a.Time('1996-01-01', '2018-12-31')
time_range_2 = a.Time('1996-01-01', '2001-12-31')

# Define the instrument and wavelength
instrument = a.Instrument('swan')
wavelength = a.Wavelength(121.567 * u.nm)

# Query for the first data collection period (1996-2018)
# Note: The results may be paginated due to the large time range
query_1 = Fido.search(time_range_1, instrument, wavelength)
print("Query results for 1996-2018:")
print(query_1)

# Uncomment the following line to fetch the data
# files_1 = Fido.fetch(query_1)

# Query for the second data collection period (1996-2001)
# Note: The results may be paginated due to the large time range
query_2 = Fido.search(time_range_2, instrument, wavelength)
print("Query results for 1996-2001:")
print(query_2)

# Uncomment the following line to fetch the data
# files_2 = Fido.fetch(query_2)

# Example of a smaller time range to avoid pagination issues
# Note: This is just an example; adjust the dates as needed within the true time range
example_time_range = a.Time('1996-01-01', '1996-01-31')
query_example = Fido.search(example_time_range, instrument, wavelength)
print("Query results for example smaller time range (1996-01-01 to 1996-01-31):")
print(query_example)

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the time ranges and instruments based on the context provided
# Time ranges are in the format 'YYYY/MM/DD HH:MM:SS'

# Data Collection Period 1: Early eruption of the hot channel
time_range_1 = a.Time('2022-01-20 05:00:00', '2022-01-20 05:51:30')
instrument_1 = a.Instrument('AIA')

# Data Collection Period 2: Formation and propagation of the EUV wave
time_range_2 = a.Time('2022-01-20 05:49:54', '2022-01-20 05:57:52')
wavelength_2 = a.Wavelength(193 * u.Angstrom)
instrument_2 = a.Instrument('AIA')

# Data Collection Period 3: Flare observation by ESP on EVE
time_range_3 = a.Time('2022-01-20 00:00:00', '2022-01-20 23:59:59')  # Assuming full day for simplicity
wavelength_3 = a.Wavelength(1 * u.Angstrom, 70 * u.Angstrom)
instrument_3 = a.Instrument('EVE')

# Data Collection Period 4: Flare observation by HMI
time_range_4 = a.Time('2022-01-20 00:00:00', '2022-01-20 23:59:59')  # Assuming full day for simplicity
instrument_4 = a.Instrument('HMI')

# Data Collection Period 5: CME observation by LASCO
time_range_5 = a.Time('2022-01-20 06:12:08', '2022-01-20 06:12:08')
instrument_5 = a.Instrument('LASCO')

# Data Collection Period 6: CME observation by COR2 on STEREO
time_range_6 = a.Time('2022-01-20 06:23:30', '2022-01-20 06:53:30')
instrument_6 = a.Instrument('SECCHI')
detector_6 = a.Detector('COR2')

# Construct the queries
# Construct the queries for each AIA wavelength separately
query_1_wavelength_131 = Fido.search(time_range_1, instrument_1, a.Wavelength(131 * u.Angstrom))
query_1_wavelength_94 = Fido.search(time_range_1, instrument_1, a.Wavelength(94 * u.Angstrom))
query_2 = Fido.search(time_range_2, instrument_2, wavelength_2)
query_3 = Fido.search(time_range_3, instrument_3, wavelength_3)
query_4 = Fido.search(time_range_4, instrument_4)
query_5 = Fido.search(time_range_5, instrument_5)
query_6 = Fido.search(time_range_6, instrument_6, detector_6)

# Print out the query results
# Print out the results for each query in wavelengths_1
print("Query 1 Results: Early eruption of the hot channel (131 Angstrom)")
print(query_1_wavelength_131)
# Uncomment the following line to fetch the data
# files_1_wavelength_131 = Fido.fetch(query_1_wavelength_131)

print("\nQuery 1 Results: Early eruption of the hot channel (94 Angstrom)")
print(query_1_wavelength_94)
# Uncomment the following line to fetch the data
# files_1_wavelength_94 = Fido.fetch(query_1_wavelength_94)

print("\nQuery 2 Results: Formation and propagation of the EUV wave")
print(query_2)
# Uncomment the following line to fetch the data
# files_2 = Fido.fetch(query_2)

print("\nQuery 3 Results: Flare observation by ESP on EVE")
print(query_3)
# Uncomment the following line to fetch the data
# files_3 = Fido.fetch(query_3)

print("\nQuery 4 Results: Flare observation by HMI")
print(query_4)
# Uncomment the following line to fetch the data
# files_4 = Fido.fetch(query_4)

print("\nQuery 5 Results: CME observation by LASCO")
print(query_5)
# Uncomment the following line to fetch the data
# files_5 = Fido.fetch(query_5)

print("\nQuery 6 Results: CME observation by COR2 on STEREO")
print(query_6)
# Uncomment the following line to fetch the data
# files_6 = Fido.fetch(query_6)

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange

# Context: We want to download data from three instruments: WISPR on PSP, LASCO/C3 on SOHO, and COR2 on STEREO-A
# for the time range January 17, 2021 – January 18, 2021.

# Define the time range for the query
time_range = TimeRange('2021-01-17', '2021-01-18')

# Define the instruments and their respective sources
instruments = [
    {'source': 'PSP', 'instrument': 'WISPR'},
    {'source': 'SOHO', 'instrument': 'LASCO', 'detector': 'C3'},
    {'source': 'STEREO_A', 'instrument': 'SECCHI', 'detector': 'COR2'}
]

# Query for WISPR data from PSP
print("Querying WISPR data from PSP...")
query_wispr = Fido.search(a.Time(time_range.start, time_range.end), a.Instrument('WISPR'), a.Source('PSP'))
print(query_wispr)
# Uncomment the following line to fetch the data
# files_wispr = Fido.fetch(query_wispr)

# Query for LASCO/C3 data from SOHO
print("Querying LASCO/C3 data from SOHO...")
query_lasco = Fido.search(a.Time(time_range.start, time_range.end), a.Instrument('LASCO'), a.Detector('C3'), a.Source('SOHO'))
print(query_lasco)
# Uncomment the following line to fetch the data
# files_lasco = Fido.fetch(query_lasco)

# Query for COR2 data from STEREO-A
print("Querying COR2 data from STEREO-A...")
query_cor2 = Fido.search(a.Time(time_range.start, time_range.end), a.Instrument('SECCHI'), a.Detector('COR2'), a.Source('STEREO_A'))
print(query_cor2)
# Uncomment the following line to fetch the data
# files_cor2 = Fido.fetch(query_cor2)

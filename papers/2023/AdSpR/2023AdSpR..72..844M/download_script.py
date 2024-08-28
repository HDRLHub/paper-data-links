from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation periods for the type II and type III radio bursts
type_ii_start_time = '2021-10-09T06:30:00'
type_ii_end_time = '2021-10-09T07:00:00'
type_iii_start_time = '2021-08-27T10:45:00'
type_iii_end_time = '2021-08-27T11:00:00'

# Define the time range for the solar flare and CME observations
flare_start_time = '2021-10-09T06:19:00'
flare_end_time = '2021-10-09T06:53:00'
cme_start_time = '2021-10-09T07:00:00'
cme_end_time = '2021-10-09T08:00:00'

# Construct the time attributes for the queries
type_ii_time_range = a.Time(type_ii_start_time, type_ii_end_time)
type_iii_time_range = a.Time(type_iii_start_time, type_iii_end_time)
flare_time_range = a.Time(flare_start_time, flare_end_time)
cme_time_range = a.Time(cme_start_time, cme_end_time)

# Define the instruments
aia_instrument = a.Instrument('AIA')
lasco_instrument = a.Instrument('LASCO')
stereo_instrument = a.Instrument('SECCHI')
stereo_detector = a.Detector("COR2")
stereo_source = a.Source("STEREO_A")

# Define the explicitly mentioned wavelengths
aia_wavelength = a.Wavelength(211 * u.angstrom)

# Construct the queries
flare_query = Fido.search(flare_time_range, aia_instrument, aia_wavelength)
cme_query_lasco = Fido.search(cme_time_range, lasco_instrument)
cme_query_stereo = Fido.search(cme_time_range, stereo_instrument, stereo_detector, stereo_source)

# Display the query results
print("Query for Solar Flare observations (AIA):")
print(flare_query)
print("Query for CME observations (LASCO):")
print(cme_query_lasco)
print("Query for CME observations (SECCHI-COR2A):")
print(cme_query_stereo)

# Uncomment the lines below to download the data
# flare_files = Fido.fetch(flare_query)
# cme_files_lasco = Fido.fetch(cme_query_lasco)
# cme_files_stereo = Fido.fetch(cme_query_stereo)

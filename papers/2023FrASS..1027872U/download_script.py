# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# LASCO on SOHO: Observations of the solar corona
lasco_time_range_2001 = a.Time('2001-01-07T00:00:00', '2001-01-07T23:59:59')
lasco_time_range_2022 = a.Time('2022-08-29T00:00:00', '2022-08-29T23:59:59')
lasco_instrument = a.Instrument("LASCO")
lasco_detector_c2 = a.Detector("C2")  # Assuming C2 is the relevant detector for the context

# SECCHI on STEREO: Observations of CMEs and coronal dynamics
secchi_time_range_2010 = a.Time('2010-08-01T00:00:00', '2010-08-01T23:59:59')
secchi_instrument = a.Instrument("SECCHI")
secchi_detector_hi1 = a.Detector("COR1")

# Constructing the queries
lasco_query_2001 = Fido.search(lasco_time_range_2001, lasco_instrument, lasco_detector_c2)
lasco_query_2022 = Fido.search(lasco_time_range_2022, lasco_instrument, lasco_detector_c2)
secchi_query_2010 = Fido.search(secchi_time_range_2010, secchi_instrument, secchi_detector_hi1)

# Display the query results
print("Query for LASCO C2 Detector Data on 2001-01-07:")
print(lasco_query_2001)
print("Query for LASCO C2 Detector Data on 2022-08-29:")
print(lasco_query_2022)
print("Query for SECCHI COR1 Detector Data on 2010-08-01:")
print(secchi_query_2010)

# Uncomment the lines below to download the data
# lasco_files_2001 = Fido.fetch(lasco_query_2001)
# lasco_files_2022 = Fido.fetch(lasco_query_2022)
# secchi_files_2010 = Fido.fetch(secchi_query_2010)

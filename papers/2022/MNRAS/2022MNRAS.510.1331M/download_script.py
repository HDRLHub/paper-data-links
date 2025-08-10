# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.vso as vso
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Initialize the VSO client
client = vso.VSOClient()

# Explicit Fido searches for each query

# Query 3: vsm from 2003-01-01 to 2012-12-31
time_range_3 = a.Time("2003-01-01", "2012-12-31")
instrument_3 = a.Instrument("vsm")
physobs_3 = a.Physobs("LOS_magnetic_field")
wavelength_3 = a.Wavelength(6302.0 * u.Angstrom)

search_result_3 = Fido.search(time_range_3, instrument_3, physobs_3, wavelength_3)
print("Query for instrument vsm from 2003-01-01 to 2012-12-31")
print(search_result_3)

# Query 4: MDI from 1996-01-01 to 2010-12-31
time_range_4 = a.Time("1996-01-01", "2010-12-31")
instrument_4 = a.Instrument("MDI")
physobs_4 = a.Physobs("LOS_magnetic_field")
wavelength_4 = a.Wavelength(6768.0 * u.Angstrom)

search_result_4 = Fido.search(time_range_4, instrument_4, physobs_4, wavelength_4)
print("Query for instrument MDI from 1996-01-01 to 2010-12-31")
print(search_result_4)


# Query 5: HMI from 2010-01-01 to 2021-12-31
time_range_5 = a.Time("2010-01-01", "2021-12-31")
instrument_5 = a.Instrument("HMI")
physobs_5 = a.Physobs("LOS_magnetic_field")
wavelength_5 = a.Wavelength(6173.0 * u.Angstrom)

search_result_5 = Fido.search(time_range_5, instrument_5, physobs_5, wavelength_5)
print("Query for instrument HMI from 2010-01-01 to 2021-12-31")
print(search_result_5)

# Commented out fetch calls
# Uncomment the following lines to fetch the data

# files_3 = Fido.fetch(search_result_3)
# print("Fetched files for vsm from 2003-01-01 to 2012-12-31")

# files_4 = Fido.fetch(search_result_4)
# print("Fetched files for MDI from 1996-01-01 to 2010-12-31")

# files_5 = Fido.fetch(search_result_5)
# print("Fetched files for HMI from 2010-01-01 to 2021-12-31")



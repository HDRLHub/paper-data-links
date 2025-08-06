# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Query 1: SOHO/MDI full‐disk line‐of‐sight magnetograms for solar cycle analysis
# Time Range: December 1995 – April 2011
time_mdi = a.Time('1995-12-01', '2011-04-12')
source_mdi = a.Source('SOHO')
instrument_mdi = a.Instrument('MDI')
physobs_mdi = a.Physobs('LOS_magnetic_field')
wavelength_mdi = a.Wavelength(6768 * u.Angstrom)

print("Searching for SOHO/MDI LOS magnetograms from 1995-12-01 to 2011-04-12")
results_mdi = Fido.search(time_mdi, source_mdi, instrument_mdi, physobs_mdi, wavelength_mdi)
print(results_mdi)
# To download the data, uncomment the following line:
# files_mdi = Fido.fetch(results_mdi)

# Query 2: SDO/HMI full‐disk vector magnetogram survey of active regions
# Time Range: February 2011 – July 2014
time_hmi = a.Time('2011-02-01', '2014-07-31')
source_hmi = a.Source('SDO')
instrument_hmi = a.Instrument('HMI')
physobs_hmi = a.Physobs('vector_magnetic_field')
wavelength_hmi = a.Wavelength(6173 * u.Angstrom)

print("Searching for SDO/HMI vector magnetograms from 2011-02-01 to 2014-07-31")
results_hmi = Fido.search(time_hmi, source_hmi, instrument_hmi, physobs_hmi, wavelength_hmi)
print(results_hmi)
# To download the data, uncomment the following line:
# files_hmi = Fido.fetch(results_hmi)

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a

# This script queries SOHO/CELIAS HSTOF particle_flux (ENA) data
# for two quiet-solar-wind intervals:
#   - Interval A: 1996-01-01 to 1997-12-31
#   - Interval B: 2008-01-01 to 2010-12-31

# Define time ranges for the two epochs
time_interval_A = a.Time('1996-01-01', '1997-12-31')
time_interval_B = a.Time('2008-01-01', '2010-12-31')

# Define common query attributes for SOHO/CELIAS HSTOF particle_flux
source_attr     = a.Source('SOHO')
instrument_attr = a.Instrument('CELIAS')
detector_attr   = a.Detector('HSTOF')
physobs_attr    = a.Physobs('particle_flux')

# Perform Query 1: 1996-1997 quiet period
query1 = Fido.search(
    time_interval_A,
    source_attr,
    instrument_attr,
    detector_attr,
    physobs_attr
)

print('=== Query 1: SOHO/CELIAS HSTOF ENA data (1996-1997) ===')
print(query1)

# To download the data, uncomment the line below:
# files1 = Fido.fetch(query1)

# Perform Query 2: 2008-2010 quiet period
query2 = Fido.search(
    time_interval_B,
    source_attr,
    instrument_attr,
    detector_attr,
    physobs_attr
)

print('=== Query 2: SOHO/CELIAS HSTOF ENA data (2008-2010) ===')
print(query2)

# To download the data, uncomment the line below:
# files2 = Fido.fetch(query2)

# End of script

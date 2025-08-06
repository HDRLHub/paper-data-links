# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.Fido as Fido
from sunpy.net import attrs as a

#------------------------------------------------------------------------------
# 1. Query RHESSI X-ray flare data (12 February 2002 – 23 February 2016)
#------------------------------------------------------------------------------
# Define the time range for the full study period
time_rhessi = a.Time("2002-02-12 00:00", "2016-02-23 23:59")

# Build the search attributes for RHESSI
source_rhessi = a.Source('RHESSI')
instrument_rhessi = a.Instrument('RHESSI')

# Perform the search
rhessi_query = Fido.search(time_rhessi,
                           source_rhessi,
                           instrument_rhessi)

# Display the results table for RHESSI flares
print("RHESSI flare query results:")
print(rhessi_query)

# Uncomment the following line to download the RHESSI data
# Fido.fetch(rhessi_query)



#------------------------------------------------------------------------------
# 2. Query SOHO/MDI LOS magnetic field magnetograms
#    (12 February 2002 – 12 April 2011)
#------------------------------------------------------------------------------
time_mdi = a.Time("2002-02-12 00:00", "2011-04-12 23:59")
source_mdi = a.Source('SOHO')
instrument_mdi = a.Instrument('MDI')
physobs_mdi = a.Physobs('LOS_magnetic_field')

mdi_query = Fido.search(time_mdi,
                        source_mdi,
                        instrument_mdi,
                        physobs_mdi)

print("\nSOHO/MDI LOS magnetic field query results:")
print(mdi_query)

# Uncomment the following line to download the MDI magnetogram data
# Fido.fetch(mdi_query)



#------------------------------------------------------------------------------
# 3. Query SDO/HMI LOS magnetic field magnetograms
#    (29 March 2010 – 23 February 2016)
#------------------------------------------------------------------------------
time_hmi = a.Time("2010-03-29 00:00", "2016-02-23 23:59")
source_hmi = a.Source('SDO')
instrument_hmi = a.Instrument('HMI')
physobs_hmi = a.Physobs('LOS_magnetic_field')

hmi_query = Fido.search(time_hmi,
                        source_hmi,
                        instrument_hmi,
                        physobs_hmi)

print("\nSDO/HMI LOS magnetic field query results:")
print(hmi_query)

# Uncomment the following line to download the HMI magnetogram data
# Fido.fetch(hmi_query)

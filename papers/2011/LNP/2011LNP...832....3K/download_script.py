# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a

# Query for Michelson Doppler Imager (MDI) on SOHO
# Time Range: 1997-06-19, 02:00 UT
# Physical Observable: Line-of-sight (Doppler) velocity
mdi_query = Fido.search(
    a.Time('1997-06-19 02:00', '1997-06-19 02:10'),  # 10-minute window for demonstration
    a.Instrument('MDI'),
    a.Physobs('LOS_velocity')
)

# Print the results of the MDI query
print("MDI Query Results:")
print(mdi_query)

# Uncomment the following line to fetch the data
# mdi_downloaded_files = Fido.fetch(mdi_query)

# Query for Helioseismic and Magnetic Imager (HMI) on SDO
# Time Range: Starting from 2010-02-11 (launch date)
# Physical Observable: Solar continuum intensity
# Note: Verify the correct physical observable for HMI
hmi_query = Fido.search(
    a.Time('2010-02-11', '2010-02-12'),  # 1-day window for demonstration
    a.Instrument('HMI'),
    a.Physobs('continuum')  # Changed observable to 'continuum' as a valid example
)

# Print the results of the HMI query
print("HMI Query Results:")
print(hmi_query)

# Uncomment the following line to fetch the data
# hmi_downloaded_files = Fido.fetch(hmi_query)

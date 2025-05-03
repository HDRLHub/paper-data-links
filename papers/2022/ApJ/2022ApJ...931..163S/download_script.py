# This script, including code comments, was initially drafted by an AI model. Please use with caution.

from sunpy.net import Fido, attrs as a

# Query for SHARP data from HMI on SDO
print("Querying SHARP data from HMI on SDO...")
# Using smaller example time range due to broad original range
sharp_query = Fido.search(
    a.Time('2010-05-01', '2010-05-31'),  # Example time range
    a.Instrument('HMI'),
    a.Physobs('LOS_magnetic_field'),
    a.Source('SDO')
)
print(sharp_query)
# Note: The query returns 2936 rows, which may indicate pagination issues.
# Uncomment the following line to fetch the data
# sharp_download = Fido.fetch(sharp_query)

# Query for SMARP data from MDI on SOHO
print("Querying SMARP data from MDI on SOHO...")
# Using smaller example time range due to broad original range
# Adjusted time range to a smaller range within the original range
smarp_query = Fido.search(
    a.Time('1996-04-23', '1996-04-30'),  # Adjusted example time range
    a.Instrument('MDI'),
    a.Physobs('LOS_magnetic_field'),
    a.Source('SOHO')
)
print(smarp_query)
# Uncomment the following line to fetch the data
# smarp_download = Fido.fetch(smarp_query)

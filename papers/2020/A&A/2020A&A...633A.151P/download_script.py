# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to build Sunpy VSO queries using Fido to obtain full-disc
LOS magnetograms from the Michelson Doppler Imager (MDI) on board SOHO.
The observational data are used in studies of emerging active regions (ARs) such as AR 9574, AR 10268, AR 9748, and AR 9906.
Each query uses the time range relevant to the respective AR emergence episode as described in the context.
The queries target the physical observable "LOS_magnetic_field" as this represents the photospheric magnetic field measurements.
"""

from sunpy.net import Fido, attrs as a

# ---------------------- AR 9574 Query ----------------------
# Data Collection Period 1 for AR 9574:
# Time Range: 10 August 2001 – 13 August 2001
query_ar9574 = Fido.search(
    a.Time('2001-08-10', '2001-08-13'),
    a.Instrument('MDI'),
    a.Source('SOHO'),
    a.Physobs('LOS_magnetic_field')
)
print("Query results for AR 9574 (10 August 2001 – 13 August 2001):")
print(query_ar9574)
# To fetch the data, uncomment the following line:
# files_ar9574 = Fido.fetch(query_ar9574)


# ---------------------- AR 10268 Query ----------------------
# Data Collection Period 2 for AR 10268:
# Time Range: Approximately 21 January 2003 – 26 January 2003 (5-day evolution)
query_ar10268 = Fido.search(
    a.Time('2003-01-21', '2003-01-26'),
    a.Instrument('MDI'),
    a.Source('SOHO'),
    a.Physobs('LOS_magnetic_field')
)
print("\nQuery results for AR 10268 (21 January 2003 – 26 January 2003):")
print(query_ar10268)
# To fetch the data, uncomment the following line:
# files_ar10268 = Fido.fetch(query_ar10268)


# ---------------------- AR 9748 Query ----------------------
# Data Collection Period 3 for AR 9748:
# Time Range: 21 December 2001 – 24 December 2001
query_ar9748 = Fido.search(
    a.Time('2001-12-21', '2001-12-24'),
    a.Instrument('MDI'),
    a.Source('SOHO'),
    a.Physobs('LOS_magnetic_field')
)
print("\nQuery results for AR 9748 (21 December 2001 – 24 December 2001):")
print(query_ar9748)
# To fetch the data, uncomment the following line:
# files_ar9748 = Fido.fetch(query_ar9748)


# ---------------------- AR 9906 Query ----------------------
# Data Collection Period 4 for AR 9906:
# Time Range: 12 April 2002 – 17 April 2002
query_ar9906 = Fido.search(
    a.Time('2002-04-12', '2002-04-17'),
    a.Instrument('MDI'),
    a.Source('SOHO'),
    a.Physobs('LOS_magnetic_field')
)
print("\nQuery results for AR 9906 (12 April 2002 – 17 April 2002):")
print(query_ar9906)
# To fetch the data, uncomment the following line:
# files_ar9906 = Fido.fetch(query_ar9906)


# End of script.
if __name__ == '__main__':
    print("\nSunpy VSO queries for MDI LOS magnetograms have been executed.")

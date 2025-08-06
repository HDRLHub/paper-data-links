# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.vso as vso
from sunpy.net import Fido
from sunpy.time import TimeRange

# Initialize VSO client
client = Fido

# 1) UVCS OVI channel observation on 1996-05-27
tr1 = TimeRange('1996-05-27 00:00', '1996-05-27 23:59')
search1 = client.search(tr1,
                        vso.Instrument('UVCS'),
                        vso.Detector('OVI'))
print("Search results for UVCS OVI on 1996-05-27:")
print(search1)
# To download the data, uncomment the following line:
# client.fetch(search1, path='UVCS_OVI_19960527/{file}')

# 2) UVCS OVI channel observation on 1996-06-01
tr2 = TimeRange('1996-06-01 00:00', '1996-06-01 23:59')
search2 = client.search(tr2,
                        vso.Instrument('UVCS'),
                        vso.Detector('OVI'))
print("\nSearch results for UVCS OVI on 1996-06-01:")
print(search2)
# client.fetch(search2, path='UVCS_OVI_19960601/{file}')

# 3) UVCS OVI channel observation on 1996-07-22
tr3 = TimeRange('1996-07-22 00:00', '1996-07-22 23:59')
search3 = client.search(tr3,
                        vso.Instrument('UVCS'),
                        vso.Detector('OVI'))
print("\nSearch results for UVCS OVI on 1996-07-22:")
print(search3)
# client.fetch(search3, path='UVCS_OVI_19960722/{file}')

# 4) UVCS OVI channel observation on 1996-08-19
tr4 = TimeRange('1996-08-19 00:00', '1996-08-19 23:59')
search4 = client.search(tr4,
                        vso.Instrument('UVCS'),
                        vso.Detector('OVI'))
print("\nSearch results for UVCS OVI on 1996-08-19:")
print(search4)
# client.fetch(search4, path='UVCS_OVI_19960819/{file}')

# 5) UVCS OVI channel observation on 1996-08-21
tr5 = TimeRange('1996-08-21 00:00', '1996-08-21 23:59')
search5 = client.search(tr5,
                        vso.Instrument('UVCS'),
                        vso.Detector('OVI'))
print("\nSearch results for UVCS OVI on 1996-08-21:")
print(search5)
# client.fetch(search5, path='UVCS_OVI_19960821/{file}')

# Note: Hinode/EIS is not available in the provided VSO interface, 
# so EIS data must be obtained through the Hinode/EIS data archive.

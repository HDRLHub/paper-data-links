# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# LASCO-C2 on SOHO
print("Querying LASCO-C2 data on SOHO for 07 January 2001")
lasco_c2_query = Fido.search(
    a.Time('2001-01-07', '2001-01-08'),
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print(lasco_c2_query)
# lasco_c2_files = Fido.fetch(lasco_c2_query)
# Note: The query returned 129 rows, indicating potential pagination.

# COR-2A on STEREO
print("Querying COR-2A data on STEREO for 01 August 2010")
cor2a_query = Fido.search(
    a.Time('2010-08-01', '2010-08-02'),
    a.Instrument('SECCHI'),
    a.Detector('COR2'),
    a.Source('STEREO_A')
)
print(cor2a_query)
# cor2a_files = Fido.fetch(cor2a_query)
# Note: The query returned 168 rows, indicating potential pagination.

# COR-1A on STEREO for 01 August 2010
print("Querying COR-1A data on STEREO for 01 August 2010")
cor1a_query_2010 = Fido.search(
    a.Time('2010-08-01', '2010-08-02'),
    a.Instrument('SECCHI'),
    a.Detector('COR1'),
    a.Source('STEREO_A')
)
print(cor1a_query_2010)
# cor1a_files_2010 = Fido.fetch(cor1a_query_2010)
# Note: The query returned 1025 rows, indicating potential pagination.

# COR-1A on STEREO for 03 April 2014
print("Querying COR-1A data on STEREO for 03 April 2014")
cor1a_query_2014 = Fido.search(
    a.Time('2014-04-03', '2014-04-04'),
    a.Instrument('SECCHI'),
    a.Detector('COR1'),
    a.Source('STEREO_A')
)
print(cor1a_query_2014)
# cor1a_files_2014 = Fido.fetch(cor1a_query_2014)
# Note: The query returned 351 rows, indicating potential pagination.

# KCor at MLSO
print("Querying KCor data at MLSO for 02 July 2015")
kcor_query = Fido.search(
    a.Time('2015-07-02', '2015-07-03'),
    a.Instrument('K-Cor'),
    a.Source('MLSO')
)
print(kcor_query)
# kcor_files = Fido.fetch(kcor_query)
# Note: The query returned 0 results. This might be due to data not being available for the specified date.

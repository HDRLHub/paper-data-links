# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for the data collection periods
time_range_1 = a.Time('1996-01-01', '2014-06-30')
time_range_2 = a.Time('2014-07-01', '2022-02-07')

# LASCO-C2 on board SOHO
# Query for general observations of the solar corona (1996 – 2014.5)
# Warning: This query returns 10,000 rows, indicating pagination
query_lasco_c2_period_1 = Fido.search(
    time_range_1,
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("LASCO-C2 Period 1 Query Results:")
print(query_lasco_c2_period_1)

# Query for analysis of the solar minima and ascending phases (2014.5 – 2022.2)
# Warning: This query returns 10,000 rows, indicating pagination
query_lasco_c2_period_2 = Fido.search(
    time_range_2,
    a.Instrument('LASCO'),
    a.Detector('C2')
)
print("LASCO-C2 Period 2 Query Results:")
print(query_lasco_c2_period_2)

# WISPR on board Parker Solar Probe
# Query for imaging the solar corona and inner heliosphere
# Note: Using a smaller example time range due to potential issues with broad time ranges
query_wispr = Fido.search(
    a.Time('2021-01-01', '2021-01-31'),  # Example time range within the true range
    a.Instrument('WISPR')
)
print("WISPR Query Results:")
print(query_wispr)

# Metis on board Solar Orbiter
# Query for observing the solar corona in visible and ultraviolet light
# Note: Using a smaller example time range due to potential issues with broad time ranges
query_metis = Fido.search(
    a.Time('2021-01-01', '2021-01-15'),  # Adjusted smaller example time range
    a.Instrument('Metis')
)
print("Metis Query Results:")
print(query_metis)

# SoloHI on board Solar Orbiter
# Query for imaging the solar wind and CMEs
query_solohi = Fido.search(
    a.Time('2021-12-27', '2022-02-07'),  # Available time range for SoloHI
    a.Instrument('SoloHI')
)
print("SoloHI Query Results:")
print(query_solohi)

# Uncomment the following lines to fetch the data
# lasco_c2_data_period_1 = Fido.fetch(query_lasco_c2_period_1)
# lasco_c2_data_period_2 = Fido.fetch(query_lasco_c2_period_2)
# wispr_data = Fido.fetch(query_wispr)
# metis_data = Fido.fetch(query_metis)
# solohi_data = Fido.fetch(query_solohi)

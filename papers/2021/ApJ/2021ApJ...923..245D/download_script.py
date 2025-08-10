# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy’s VSO client (Fido) to construct queries for three data sources mentioned in the context:
 - Parker Solar Probe (PSP)
 - Wind Spacecraft
 - ARTEMIS Mission

Since the paper does not specify an explicit data collection period for these missions,
we use a representative time range ("2020-01-01" to "2020-01-02") for demonstration.
Note that actual queries should use the correct time ranges when they become available.
The queries are printed out and the commands to fetch the data are provided as commented code.
"""

from sunpy.net import Fido, attrs as a

# Define a representative time interval for the queries.
start_time = '2020-01-01'
end_time = '2020-01-02'

# -----------------------------------------------------------------------------
# Query for Parker Solar Probe (PSP)
# -----------------------------------------------------------------------------
# The PSP data are used for in-situ measurements of whistler waves in the solar wind.
psp_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('PSP')  # Querying data for Parker Solar Probe
)
print("Parker Solar Probe (PSP) Query Results:")
print(psp_query)
# To fetch the data, uncomment the following line:
# psp_downloaded_files = Fido.fetch(psp_query)

# -----------------------------------------------------------------------------
# Query for Wind Spacecraft
# -----------------------------------------------------------------------------
# The Wind spacecraft data illustrate scaling of the electron heat flux with local plasma βₑ.
wind_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('Wind')  # Querying data for Wind Spacecraft
)
print("\nWind Spacecraft Query Results:")
print(wind_query)
# To fetch the data, uncomment the following line:
# wind_downloaded_files = Fido.fetch(wind_query)

# -----------------------------------------------------------------------------
# Query for ARTEMIS Mission
# -----------------------------------------------------------------------------
# The ARTEMIS observations are used to correlate whistler wave amplitudes with electron heat flux behavior.
artemis_query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('ARTEMIS')  # Querying data for ARTEMIS Mission
)
print("\nARTEMIS Mission Query Results:")
print(artemis_query)
# To fetch the data, uncomment the following line:
# artemis_downloaded_files = Fido.fetch(artemis_query)

if __name__ == "__main__":
    print("\nSunPy VSO query script completed. Review the above query outputs.")

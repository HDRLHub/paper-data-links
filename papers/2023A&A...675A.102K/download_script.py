# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

# Import necessary libraries from SunPy
from sunpy.net import Fido, attrs as a
import datetime

# Define the time ranges for the observations
time_range_cycle_23 = (datetime.datetime(1996, 1, 1), datetime.datetime(2008, 12, 31))  # Example time range
time_range_cycle_24 = (datetime.datetime(2009, 1, 1), datetime.datetime(2019, 12, 31))  # Example time range

# WARNING: The time ranges defined above may be too broad for the VSO to return results.
# Consider using a smaller example time range for testing, such as:
# time_range_example = (datetime.datetime(2009, 1, 1), datetime.datetime(2009, 1, 7))

# LASCO for coronal mass ejections (CMEs)
lasco_query_cycle_23 = Fido.search(
    a.Time(time_range_cycle_23[0], time_range_cycle_23[1]),
    a.Instrument('LASCO'),
)
lasco_query_cycle_24 = Fido.search(
    a.Time(time_range_cycle_24[0], time_range_cycle_24[1]),
    a.Instrument('LASCO'),
)

# SECCHI for coronal mass ejections (CMEs)
# SECCHI should be queried with its detectors, not as an instrument
secchi_query_cycle_24 = Fido.search(
    a.Time(time_range_cycle_24[0], time_range_cycle_24[1]),
    a.Detector('COR1'),  # Correcting to use COR1 as a detector
)

print("\nLASCO Query Results for Cycle 23:")
print(lasco_query_cycle_23)  # Results may be empty if the time range is too broad
# Uncomment the following line to fetch the data
# Fido.fetch(lasco_query_cycle_23)

print("\nLASCO Query Results for Cycle 24:")
print(lasco_query_cycle_24)  # Results may be empty if the time range is too broad
# Uncomment the following line to fetch the data
# Fido.fetch(lasco_query_cycle_24)

print("\nSECCHI Query Results for Cycle 24:")
print(secchi_query_cycle_24)  # Results may be empty if the time range is too broad
# Uncomment the following line to fetch the data
# Fido.fetch(secchi_query_cycle_24)

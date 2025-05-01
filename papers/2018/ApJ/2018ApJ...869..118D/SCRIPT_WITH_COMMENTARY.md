# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query data from the Solar Dynamics Observatory/Atmospheric Imaging Assembly (SDO/AIA)
for a study of a filament eruption and current sheet (CS) formation as detailed in the provided context.

Two separate queries are defined:
1. Query for Filament Eruption Observations with the AIA 304 Å channel,
   covering approximately the period during the early activation and rising phase of the filament.
2. Query for Current Sheet (CS) Observations with the AIA 94 Å channel,
   covering the interval when the bright current sheet structures and plasmoids are observed.

Note:
- We only use the required attributes: time range and instrument (plus wavelength filter to specify the channel).
- The Fido.fetch commands are provided as commented code to prevent automatic data download.
- Additional comments in the code describe each query step.
"""

# Import required modules from sunpy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# ---------------------------
# 1. Query: Filament Eruption Observations using AIA 304 Å
# ---------------------------
# Data Collection Period: Around 15:50 UT – 16:10 UT on 2014-07-08
# The AIA 304 Å channel is used to trace the filament eruption.
time_start_erupt = '2014-07-08T15:50:00'
time_end_erupt = '2014-07-08T16:10:00'
query_erupt = Fido.search(
    a.Time(time_start_erupt, time_end_erupt),
    a.Instrument('AIA'),
    a.Wavelength(304*u.AA)
)

# Print the query results for the filament eruption observation
print("Query Results for Filament Eruption (AIA 304 Å):")
print(query_erupt)

# The following line would download the data, but is commented out to avoid execution.
# downloaded_files_erupt = Fido.fetch(query_erupt)

# ---------------------------
# 2. Query: Current Sheet (CS) and Plasmoid Observations using AIA 94 Å
# ---------------------------
# Data Collection Period: Around 16:12 UT – 16:22 UT on 2014-07-08
# The AIA 94 Å channel is particularly useful for observing the high-temperature current sheet features.
time_start_cs = '2014-07-08T16:12:00'
time_end_cs = '2014-07-08T16:22:00'
query_cs = Fido.search(
    a.Time(time_start_cs, time_end_cs),
    a.Instrument('AIA'),
    a.Wavelength(94*u.AA)
)

# Print the query results for the current sheet observation
print("\nQuery Results for Current Sheet (AIA 94 Å):")
print(query_cs)

# The following line would download the data, but is commented out to avoid execution.
# downloaded_files_cs = Fido.fetch(query_cs)

# End of script

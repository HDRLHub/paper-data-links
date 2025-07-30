# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO module to query LASCO coronagraph data from the SOHO satellite.
The context describes the observation of a CME eruption on 20 August 2018 at approximately 21:24 UT.
Since the only required query parameters are the time range and the instrument, we choose:
  • Time: A short window around 21:24 UT on 20 August 2018 (from 21:24 to 21:29 UT)
  • Instrument: LASCO (with source "SOHO" as specified in the VSO interface)
Note: Although the VSO interface lists several detectors (C1, C2, C3), only C2 and C3 offer data past 2000.
Here, we do not specify the detector because our context only requires the general instrument and time.
The Fido.fetch command is included as a commented-out option for actual data download.
"""

from sunpy.net import Fido, attrs as a

# Define the time range for the LASCO observation (CME eruption event on 20 August 2018)
start_time = "2018-08-20T21:24:00"
end_time   = "2018-08-20T21:29:00"

# Define the instrument and source based on the VSO interface and context
instrument = "LASCO"   # LASCO coronagraph instrument on SOHO
source = "SOHO"

# Build the query with the required parameters: time range, instrument, and source.
query = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument(instrument),
    a.Source(source)
)

# Print the query results (i.e., what files and data are available)
print("VSO Query Results:")
print(query)

# If you wish to download the data, uncomment the following lines.
# downloaded_files = Fido.fetch(query)
# print("Downloaded files:")
# print(downloaded_files)

if __name__ == '__main__':
    # The script queries the VSO and prints the available data for inspection.
    pass

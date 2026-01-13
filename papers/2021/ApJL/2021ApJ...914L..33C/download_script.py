# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query data from the STEREO-A spacecraft
for the whistler-mode wave observations during a CME event on March 24–25, 2017.
The query is based on the context details provided in the paper.
Only the time range and instrument (STEREO-A) are used, as specified.
Note: The Fido.fetch command is provided as a commented-out line.
"""

# Import necessary modules from sunpy
from sunpy.net import Fido, attrs
from sunpy.time import TimeRange

def main():
    # Define the observation time range for the STEREO-A CME event
    # Start: March 24, 2017; End: March 25, 2017
    time_start = "2017-03-24"
    time_end = "2017-03-25"
    tr = TimeRange(time_start, time_end)

    # Define instrument: STEREO-A whistler wave observations.
    # Here we use the instrument attribute as "STEREO_A".
    # Note: Depending on the VSO interface, the instrument naming might differ.
    instrument = "STEREO-A"
    
    # Construct the query using the time range and instrument.
    # We keep the query explicit and avoid any nested operations.
    query_result = Fido.search(attrs.Time(tr.start.isoformat(), tr.end.isoformat()),
                               attrs.Instrument(instrument))
    
    # Print out the query result
    print("Query Results for STEREO-A whistler-mode wave data (March 24-25, 2017):")
    print(query_result)

    # To download the data, uncomment the following line:
    # downloaded_files = Fido.fetch(query_result)
    # print("Downloaded files:", downloaded_files)

if __name__ == "__main__":
    main()

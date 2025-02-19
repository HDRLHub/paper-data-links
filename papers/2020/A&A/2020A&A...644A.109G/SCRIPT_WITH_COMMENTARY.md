# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SOHO/SUMER Lyman‑α observations.
The query is built to fetch observations corresponding to the quiet‑Sun Lyman‑α raster scan
recorded on June 24, 2008 at the solar disk centre (Disk Centre Observation from the paper).

Instrument details:
    Source: SOHO
    Instrument: SUMER
    Wavelength Range: 500.0 - 1610.0 Å (VSO interface) with our target Lyman‑α line at 1215.67 Å
    Observation Time: June 24, 2008, 18:11:32 – 18:32:44 UT

Note: The Fido.fetch() command is provided as a comment, so that the query result can be printed
and inspected without downloading data.
"""

import astropy.units as u
from sunpy.net import vso
from sunpy.net import attrs as a

def main():
    # Create a client for the VSO service.
    client = vso.VSOClient()

    # Define the observation time range based on the Disk Centre Observation period.
    time_start = "2008-06-24T18:11:32"
    time_end   = "2008-06-24T18:32:44"

    # Define the wavelength for the Lyman-α line (central wavelength 1215.67 Å).
    # Although SUMER instrument available wavelengths are 500-1610 Å, we target the Lyman-α line.
    target_wavelength = 1215.67 * u.AA

    # Build the query with time range, instrument, source, and wavelength.
    # Note: a.Source("SOHO") and a.Instrument("SUMER") are used to restrict the query to the desired data.
    # The wavelength constraint is given exactly at 1215.67 Å.
    query_result = client.search(
        a.Time(time_start, time_end),
        a.Source("SOHO"),
        a.Instrument("SUMER"),
        a.Wavelength(target_wavelength, target_wavelength)
    )

    # Print the query result to show the available data.
    print("Query Result for SOHO/SUMER Lyman-α observation:")
    print(query_result)

    # To download the data, uncomment the following line:
    # downloaded_files = client.fetch(query_result)
    # print("Downloaded Files:", downloaded_files)

if __name__ == "__main__":
    main()

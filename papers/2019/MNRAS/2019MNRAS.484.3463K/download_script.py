# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query solar data based on the paper's instrumentation details.
The script includes three separate queries corresponding to:
  1. SOHO data for the discovery of sungrazing comets (from 1995 to 2008).
  2. WISE/NEOWISE data associated with recent comet discoveries (using a derived time range from 2015 to 2017).
  3. Pan-STARRS data for the comet designated "C/2017 Y2 PANSTARRS" (using the year 2017).

NOTE: The Fido.fetch commands are commented out as per the directive.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

def main():
    # --------------------------- SOHO Query ---------------------------
    # Query parameters:
    #   Time range: 1995-01-01 to 2008-12-31 (discovery period for sungrazing comets).
    #   Instrument: SOHO
    time_soho = a.Time("1995-01-01T00:00:00", "2008-12-31T23:59:59")
    instr_soho = a.Instrument('soho')
    query_soho = Fido.search(time_soho, instr_soho)
    print("SOHO Query Results:\n", query_soho)
    # To fetch the SOHO data, uncomment the following line:
    # soho_downloaded_files = Fido.fetch(query_soho)

    # --------------------------- WISE/NEOWISE Query ---------------------------
    # Query parameters:
    #   Time range: 2015-01-01 to 2017-12-31
    #     (chosen based on the publication years cited for recent WISE/NEOWISE discoveries)
    #   Instrument: WISE/NEOWISE (assuming the VSO interface uses 'wise' to represent these observations)
    time_wise = a.Time("2015-01-01T00:00:00", "2017-12-31T23:59:59")
    instr_wise = a.Instrument('wise')
    query_wise = Fido.search(time_wise, instr_wise)
    print("WISE/NEOWISE Query Results:\n", query_wise)
    # To fetch the WISE/NEOWISE data, uncomment the following line:
    # wise_downloaded_files = Fido.fetch(query_wise)

    # --------------------------- Pan-STARRS Query ---------------------------
    # Query parameters:
    #   Time range: 2017-01-01 to 2017-12-31 (to cover the discovery of C/2017 Y2 PANSTARRS)
    #   Instrument: Pan-STARRS
    time_panstarrs = a.Time("2017-01-01T00:00:00", "2017-12-31T23:59:59")
    instr_panstarrs = a.Instrument('panstarrs')
    query_panstarrs = Fido.search(time_panstarrs, instr_panstarrs)
    print("Pan-STARRS Query Results:\n", query_panstarrs)
    # To fetch the Pan-STARRS data, uncomment the following line:
    # panstarrs_downloaded_files = Fido.fetch(query_panstarrs)

if __name__ == "__main__":
    main()

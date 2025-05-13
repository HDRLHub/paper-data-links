# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query data that are relevant to the analysis
of magnetic clouds (MCs) and their associated solar sources.

The queries below are based on the available instruments in the VSO interface:
  • SDO/AIA (from SDO): Provides high-cadence EUV full-disk solar images (e.g. 304 Å channel)
    with complete data coverage from 2010 onward.
  • SOHO/LASCO (from SOHO): Provides coronagraph images. In this example we query the C2 detector,
    which has data available from 1995/12/08 to the present.

The time intervals in these queries are chosen to reflect the periods used in the study:
  - For SDO/AIA, we select a period after 2010 (e.g. 2011-01-01 to 2011-01-02).
  - For SOHO LASCO, we choose a sample day within the study period (e.g. 1997-07-14 to 1997-07-15).
  
Note: Fido.fetch commands are commented out to prevent automatic data downloads.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

def main():
    # -----------------------
    # Query for SDO/AIA Data
    # -----------------------
    # Defining the time range for the SDO/AIA query.
    # SDO/AIA data starts from 2010 May 12, so we use a sample date shortly after (2011-01-01 to 2011-01-02).
    sdo_time_start = "2011-01-01"
    sdo_time_end = "2011-01-02"
    
    # Query attributes:
    #  • time: from sdo_time_start to sdo_time_end
    #  • source: 'SDO'
    #  • instrument: 'AIA'
    #  • wavelength: using one of the available EUV channels (304 Å is commonly used)
    sdo_query = Fido.search(
        a.Time(sdo_time_start, sdo_time_end),
        a.Source("SDO"),
        a.Instrument("AIA"),
        a.Wavelength(304 * u.Angstrom)
    )
    
    # Print out the query results for SDO/AIA.
    print("SDO/AIA Query Results:")
    print(sdo_query)
    
    # To fetch the SDO/AIA data, uncomment the following line:
    # sdo_files = Fido.fetch(sdo_query)
    
    
    # ---------------------------
    # Query for SOHO LASCO Data
    # ---------------------------
    # Selecting a sample period within the full available time range for LASCO C2 data.
    # LASCO C2 data are available from 1995-12-08 to present. Here we choose a day within the study period.
    soho_time_start = "1997-07-14"
    soho_time_end = "1997-07-15"
    
    # Query attributes:
    #  • time: from soho_time_start to soho_time_end
    #  • source: 'SOHO'
    #  • instrument: 'LASCO'
    #  • detector: 'C2' (this detector has near-continuous data from its available range)
    soho_query = Fido.search(
        a.Time(soho_time_start, soho_time_end),
        a.Source("SOHO"),
        a.Instrument("LASCO"),
        a.Detector("C2")
    )
    
    # Print out the query results for SOHO LASCO.
    print("\nSOHO LASCO C2 Query Results:")
    print(soho_query)
    
    # To fetch the SOHO LASCO data, uncomment the following line:
    # soho_files = Fido.fetch(soho_query)

if __name__ == '__main__':
    main()

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script performs two queries using sunpy's VSO to retrieve solar imaging data
that were used in the paper studying solar wind transients and their coronal origin.

Query 1: SDO/AIA data in the 171 Å channel for Event Two.
  - Instrument: SDO/AIA (source "SDO", instrument "AIA")
  - Time Range: 2011-06-07 05:10:00 to 2011-06-08 19:10:00
    (chosen to reflect the Event Two imaging period; note that SDO/AIA has full time
     coverage from 2010/05/12 to present.)
  - Although AIA offers multiple wavelengths, based on the paper the 171 Å channel is used.

Query 2: SOHO/EIT data in the 284 Å channel for Event One.
  - Instrument: SOHO/EIT (source "SOHO", instrument "EIT")
  - Time Range: 2007-04-08 20:30:00 to 2007-04-09 11:30:00
    (this time interval covers Event One as referenced in the in situ observations.
     SOHO/EIT is available from 1996/01/01 to present.)
  
The queries below print out the query results, and the Fido.fetch lines are commented out.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

def main():
    # Query 1: SDO/AIA 171 Å imaging for Event Two
    # Define the time interval according to Event Two.
    start_time_aia = "2011-06-07T05:10:00"
    end_time_aia   = "2011-06-08T19:10:00"
    # Build the query using the instrument and wavelength.
    # Note: a.Wavelength expects a Quantity; here we set 171 Å.
    aia_query = Fido.search(
        a.Time(start_time_aia, end_time_aia),
        a.Instrument("AIA"),
        a.Source("SDO"),
        a.Wavelength(171 * u.Angstrom, 171 * u.Angstrom)
    )
    print("SDO/AIA query results:")
    print(aia_query)
    
    # Uncomment the following line to fetch SDO/AIA data when ready:
    # aia_files = Fido.fetch(aia_query)

    # Query 2: SOHO/EIT 284 Å imaging for Event One
    # Define the time interval according to Event One.
    start_time_eit = "2007-04-08T20:30:00"
    end_time_eit   = "2007-04-09T11:30:00"
    # Build the query using the instrument and wavelength.
    # Note: a.Wavelength expects a Quantity; here we set 284 Å.
    eit_query = Fido.search(
        a.Time(start_time_eit, end_time_eit),
        a.Instrument("EIT"),
        a.Source("SOHO"),
        a.Wavelength(284 * u.Angstrom, 284 * u.Angstrom)
    )
    print("\nSOHO/EIT query results:")
    print(eit_query)
    
    # Uncomment the following line to fetch SOHO/EIT data when ready:
    # eit_files = Fido.fetch(eit_query)

if __name__ == "__main__":
    main()

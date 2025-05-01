# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query for SDO/AIA data from two time periods on August 4, 2011.
The queries are based on the scientific context of filament eruption observations. We use:
  1. AIA observations for filament imaging and EUV absorption diagnostics from 03:45 UT to 05:15 UT.
     These queries consider the following wavelength channels: 171 Å, 193 Å, 211 Å, and 304 Å.
  2. AIA high-cadence plasma parcel tracking from 04:10 UT to 05:00 UT.
     The same four wavelength channels are used.
Note: Although the SDO/AIA instrument normally offers additional wavelengths (e.g., 335 Å), the context
specifically excludes 335 Å for the absorption diagnostics because of its low signal‐to‐noise.
The script prints out the results of the queries. The actual data download commands (Fido.fetch) are commented out.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

def query_aia_filament_imaging():
    # Define the time range corresponding to the filament imaging and absorption diagnostic period.
    time_start = '2011-08-04T03:45:00'
    time_end   = '2011-08-04T05:15:00'
    
    # Define the wavelength channels used (in Angstroms)
    # 171, 193, 211, and 304 Å channels are used.
    # Each wavelength search is specified exactly (start=end) to target each channel.
    wave_171 = a.Wavelength(171*u.angstrom, 171*u.angstrom)
    wave_193 = a.Wavelength(193*u.angstrom, 193*u.angstrom)
    wave_211 = a.Wavelength(211*u.angstrom, 211*u.angstrom)
    wave_304 = a.Wavelength(304*u.angstrom, 304*u.angstrom)
    
    # Combine the wavelength attributes with OR (|)
    wavelength_attr = wave_171 | wave_193 | wave_211 | wave_304
    
    # Build the query using the time range, instrument and physical observable (intensity)
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument('AIA'),
        a.Physobs('intensity'),
        wavelength_attr
    )
    
    print("Query result for AIA filament imaging and absorption diagnostics (03:45 - 05:15 UT, 2011-08-04):")
    print(query_result)
    
    # Uncomment the following line to fetch the data (disabled for script demonstration)
    # files = Fido.fetch(query_result)
    
    return query_result

def query_aia_plasma_tracking():
    # Define the time range corresponding to the high-cadence tracking of plasma parcels.
    time_start = '2011-08-04T04:10:00'
    time_end   = '2011-08-04T05:00:00'
    
    # Use the same four wavelength channels as above
    wave_171 = a.Wavelength(171*u.angstrom, 171*u.angstrom)
    wave_193 = a.Wavelength(193*u.angstrom, 193*u.angstrom)
    wave_211 = a.Wavelength(211*u.angstrom, 211*u.angstrom)
    wave_304 = a.Wavelength(304*u.angstrom, 304*u.angstrom)
    
    wavelength_attr = wave_171 | wave_193 | wave_211 | wave_304
    
    # Build the query with the given time range, instrument, and observable.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Instrument('AIA'),
        a.Physobs('intensity'),
        wavelength_attr
    )
    
    print("\nQuery result for AIA high-cadence plasma parcel tracking (04:10 - 05:00 UT, 2011-08-04):")
    print(query_result)
    
    # Uncomment the following line to fetch the data (disabled for script demonstration)
    # files = Fido.fetch(query_result)
    
    return query_result

if __name__ == "__main__":
    # Perform the two queries sequentially.
    res_imaging = query_aia_filament_imaging()
    res_tracking = query_aia_plasma_tracking()
    
    # Optionally, further processing of the query results could be done here.
    # For example, inspecting the results or preparing them for analysis.
    
    print("\nQueries completed. See the printed search results above.")

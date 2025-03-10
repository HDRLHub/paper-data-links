# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses Sunpy’s VSO interface to query for and list available data from SDO/AIA,
which is one of the key instruments used in the study. The queries are set for three wavelength bands:
• EUV 171 Å (to capture the fine structure of the filament in the corona)
• EUV 304 Å (highlighting the cooler transition region emissions)
• UV 1600 Å (to show the flare ribbons and chromospheric response)
The time range for each query is set from 07:00 UT to 22:00 UT on 2010 October 18,
which corresponds to the observation period described in the scientific context.
Note: The Fido.fetch() calls are provided as commented-out lines.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

def main():
    # Define the observation time window based on the paper context.
    time_range = a.Time("2010-10-18 07:00:00", "2010-10-18 22:00:00")
    
    # ----------------------------------------------------------------------------
    # Query 1: SDO/AIA 171 Å Images (EUV)
    # ----------------------------------------------------------------------------
    # The AIA 171 channel images the corona and is ideal for seeing the filament's fine structure.
    # The wavelength range is set approximately from 170 Å to 180 Å to cover a band around 171 Å.
    query_aia_171 = Fido.search(time_range,
                                a.Instrument("AIA"),
                                a.Wavelength(170 * u.AA, 180 * u.AA))
    print("Query results for SDO/AIA 171 Å images:")
    print(query_aia_171)
    
    # Uncomment the line below to download the 171 Å data.
    # downloaded_files_171 = Fido.fetch(query_aia_171)
    
    # ----------------------------------------------------------------------------
    # Query 2: SDO/AIA 304 Å Images (EUV)
    # ----------------------------------------------------------------------------
    # The AIA 304 channel captures cooler plasma in the transition region,
    # which helps in visualizing the filament material.
    # We set the wavelength range roughly from 300 Å to 310 Å.
    query_aia_304 = Fido.search(time_range,
                                a.Instrument("AIA"),
                                a.Wavelength(300 * u.AA, 310 * u.AA))
    print("\nQuery results for SDO/AIA 304 Å images:")
    print(query_aia_304)
    
    # Uncomment the line below to download the 304 Å data.
    # downloaded_files_304 = Fido.fetch(query_aia_304)
    
    # ----------------------------------------------------------------------------
    # Query 3: SDO/AIA 1600 Å Images (UV)
    # ----------------------------------------------------------------------------
    # The AIA 1600 channel images the upper photosphere and lower chromosphere,
    # revealing flare ribbons and chromospheric responses associated with the filament.
    # Here the wavelength range is set from about 1590 Å to 1610 Å.
    query_aia_1600 = Fido.search(time_range,
                                 a.Instrument("AIA"),
                                 a.Wavelength(1590 * u.AA, 1610 * u.AA))
    print("\nQuery results for SDO/AIA 1600 Å images:")
    print(query_aia_1600)
    
    # Uncomment the line below to download the 1600 Å data.
    # downloaded_files_1600 = Fido.fetch(query_aia_1600)

if __name__ == "__main__":
    main()

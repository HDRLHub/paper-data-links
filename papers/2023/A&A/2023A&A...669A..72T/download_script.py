# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for each instrument
time_ranges = {
    "GOES_XRS": ("2021-11-01 23:35", "2021-11-02 04:00"),
    "Solar_Orbiter_STIX": ("2021-11-01 23:35", "2021-11-02 04:00"),
    "SDO_AIA": ("2021-11-01 23:05", "2021-11-02 01:05"),
    "STEREO_A_EUVI": ("2021-11-01 23:05", "2021-11-02 01:05"),
    "SOHO_LASCO": ("2021-11-02 02:00", "2021-11-02 04:23"),
    "STEREO_A_SECCHI": ("2021-11-02 01:31", "2021-11-02 04:23"),
    "Solar_Orbiter_MAG": ("2021-11-03 14:30", "2021-11-04 07:00"),
    "Solar_Orbiter_SWA": ("2021-11-03 14:30", "2021-11-04 07:00"),
    "ACE_Wind": ("2021-11-03 21:30", "2021-11-04 13:00")
}

# Define the instruments and their attributes
instruments = {
    "GOES_XRS": a.Instrument("XRS"),
    "Solar_Orbiter_STIX": a.Instrument("STIX"),
    "SDO_AIA": a.Instrument("AIA"),
    "STEREO_A_EUVI": a.Instrument("EUVI"),
    "SOHO_LASCO": a.Instrument("LASCO"),
    "STEREO_A_SECCHI": a.Instrument("SECCHI"),
    "Solar_Orbiter_MAG": a.Instrument("MAG"),
    "Solar_Orbiter_SWA": a.Instrument("SWA"),
    "ACE_Wind": a.Instrument("WIND")  # Assuming Wind instrument for ACE and Wind
}

# Define the wavelengths for each instrument where applicable
wavelengths = {
    "SDO_AIA": [1600 * u.Angstrom, 304 * u.Angstrom, 94 * u.Angstrom, 211 * u.Angstrom],
    "Solar_Orbiter_STIX": [4 * u.keV, 150 * u.keV]
}

# Query for each instrument
for instrument, time_range in time_ranges.items():
    start_time, end_time = time_range
    query = a.Time(start_time, end_time) & instruments[instrument]
    
    # Add wavelength attribute if applicable
    if instrument in wavelengths:
        for wavelength in wavelengths[instrument]:
            query = query & a.Wavelength(wavelength)
    
    # Perform the search
    result = Fido.search(query)
    
    # Print the results
    print(f"Results for {instrument}:")
    print(result)
    
    # Uncomment the following line to fetch the data
    # files = Fido.fetch(result)
    
    # Warning about potential pagination issues
    # Note: If the result set is too large, consider refining the time range or other search parameters.

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.vso as vso
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Initialize the VSO client
client = vso.VSOClient()

# Define the time ranges and instruments based on the context
queries = [
    {
        "time_range": ("1975-01-01", "2003-12-31"),
        "instrument": "512-channel magnetograph",
        "wavelength": 8688.0,
        "physobs": "LOS_magnetic_field"
    },
    {
        "time_range": ("1976-01-01", "1986-12-31"),
        "instrument": "512-channel magnetograph",
        "wavelength": 10830.0,
        "physobs": "intensity"
    },
    {
        "time_range": ("2003-01-01", "2012-12-31"),
        "instrument": "vsm",
        "wavelength": 6302.0,
        "physobs": "LOS_magnetic_field"
    },
    {
        "time_range": ("1996-01-01", "2010-12-31"),
        "instrument": "MDI",
        "wavelength": 6768.0,
        "physobs": "LOS_magnetic_field"
    },
    {
        "time_range": ("2010-01-01", "2021-12-31"),
        "instrument": "HMI",
        "wavelength": 6173.0,
        "physobs": "LOS_magnetic_field"
    },
    {
        "time_range": ("1976-01-01", "present"),
        "instrument": "WSO",
        "physobs": "LOS_magnetic_field"
    }
]

# Perform the queries and print the results
for query in queries:
    time_range = a.Time(query["time_range"][0], query["time_range"][1])
    instrument = a.Instrument(query["instrument"])
    physobs = a.Physobs(query["physobs"])
    
    if "wavelength" in query:
        wavelength = a.Wavelength(query["wavelength"] * u.Angstrom)
        search_result = Fido.search(time_range, instrument, physobs, wavelength)
    else:
        search_result = Fido.search(time_range, instrument, physobs)
    
    print(f"Query for instrument {query['instrument']} from {query['time_range'][0]} to {query['time_range'][1]}")
    print(search_result)
    # Uncomment the following line to fetch the data
    # files = Fido.fetch(search_result)

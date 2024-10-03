# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange
from astropy import units as u

# Context: We need to query data from the AIA instrument on board the SDO and the LASCO instrument on board the SOHO.
# The time ranges and wavelengths are specified for specific events.

# Define the time ranges for the specific events
time_ranges = [
    TimeRange("2017-04-02", "2017-04-03"),
    TimeRange("2017-09-08", "2017-09-09"),
    TimeRange("2021-04-19", "2021-04-21")
]

# Define the wavelengths for AIA
aia_wavelengths = [171 * u.Angstrom, 131 * u.Angstrom, 304 * u.Angstrom]

# Define the instruments
instruments = {
    "AIA": {
        "source": "SDO",
        "wavelengths": aia_wavelengths
    },
    "LASCO": {
        "source": "SOHO",
        "wavelengths": None  # LASCO wavelengths are not specified
    }
}

# Query for AIA data
for time_range in time_ranges:
    for wavelength in instruments["AIA"]["wavelengths"]:
        aia_query = Fido.search(
            a.Time(time_range.start, time_range.end),
            a.Instrument("AIA"),
            a.Wavelength(wavelength)
        )
        print(f"AIA Query Results for {time_range.start} to {time_range.end} at {wavelength}:")
        print(aia_query)
        # Uncomment the following line to fetch the data
        # Fido.fetch(aia_query)

# Query for LASCO data
for time_range in time_ranges:
    lasco_query = Fido.search(
        a.Time(time_range.start, time_range.end),
        a.Instrument("LASCO")
    )
    print(f"LASCO Query Results for {time_range.start} to {time_range.end}:")
    print(lasco_query)
    # Uncomment the following line to fetch the data
    # Fido.fetch(lasco_query)

# Note: Be aware of potential pagination issues when querying large datasets.
# If the query returns a large number of results, consider handling pagination.

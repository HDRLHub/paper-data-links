# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

# Define the time ranges and instruments for the queries
# Using smaller example time ranges to avoid potential issues with broad time ranges
time_ranges = [
    ("1996-05-01", "1996-05-31"),  # Example smaller time range within the original range
    ("1998-01-01", "1998-01-31")   # Example smaller time range within the original range
]

# Define the instruments and their respective wavelengths
instruments = [
    ("LASCO", "C2", 540 * u.nm, 640 * u.nm),
    ("LASCO", "C3", 540 * u.nm, 640 * u.nm)
]

# Perform the queries
for start_time, end_time in time_ranges:
    for instrument, detector, wave_min, wave_max in instruments:
        query = Fido.search(
            a.Time(start_time, end_time),
            a.Instrument(instrument),
            a.Detector(detector),
            a.Wavelength(wave_min, wave_max)
        )
        print(f"Query results for {instrument} {detector} from {start_time} to {end_time}:")
        print(query)
        # Uncomment the following line to fetch the data
        # files = Fido.fetch(query)

# Warning about potential pagination issues
# If the query returns a large number of results, consider breaking down the time range further

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import astropy.units as u
from astropy.time import Time
from sunpy.net import Fido, attrs as a

# Define the time range for SOHO/MDI data as used in the study
start_time = "1999-02-19"
end_time   = "2010-10-02"

# Create a Time attribute for the search
time_range = a.Time(start_time, end_time)

# Specify the VSO source and instrument
source     = a.Source("SOHO")
instrument = a.Instrument("MDI")

# Specify the wavelength for MDI data (6768 Å)
wavelength = a.Wavelength(6768.0 * u.Angstrom)

# 1) Search for continuum intensity images from MDI (used as continuum)
physobs_intensity = a.Physobs("intensity")
intensity_query = Fido.search(
    time_range,
    source,
    instrument,
    physobs_intensity,
    wavelength
)
print("Continuum intensity query results:")
print(intensity_query)

# To download the intensity data, uncomment the following line:
# Fido.fetch(intensity_query)

# 2) Search for line‐of‐sight magnetograms from MDI
physobs_mag = a.Physobs("LOS_magnetic_field")
mag_query = Fido.search(
    time_range,
    source,
    instrument,
    physobs_mag,
    wavelength
)
print("Line-of-sight magnetic field query results:")
print(mag_query)

# To download the magnetic field data, uncomment the following line:
# Fido.fetch(mag_query)

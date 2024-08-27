# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period for the 2005 May 15 event
event_date = '2005-05-15'
start_time = event_date + 'T00:00:00'
end_time = event_date + 'T23:59:59'
time_range = a.Time(start_time, end_time)

# EPAM instrument on ACE for particle fluxes
epam_instrument = a.Instrument("EPAM")
epam_query = Fido.search(time_range, epam_instrument, a.Physobs("particle_flux"), a.Level("L2"))

# MAG instrument on ACE for magnetic field components
mag_instrument = a.Instrument("MAG")
mag_query = Fido.search(time_range, mag_instrument, a.Physobs("magnetic_field"), a.Level("L2"))

# SWEPAM instrument on ACE for solar wind conditions
swepam_instrument = a.Instrument("SWEPAM")
swepam_query = Fido.search(time_range, swepam_instrument, a.Physobs("solar_wind"), a.Level("L2"))

# SST instrument on Wind for energetic particle anisotropy
sst_instrument = a.Instrument("SST")
sst_query = Fido.search(time_range, sst_instrument, a.Physobs("particle_flux"), a.Level("L2"))

# Print the query results
print("Query for EPAM particle fluxes:")
print(epam_query)
print("Query for MAG magnetic field components:")
print(mag_query)
print("Query for SWEPAM solar wind conditions:")
print(swepam_query)
print("Query for SST energetic particle anisotropy:")
print(sst_query)

# Uncomment the lines below to download the data
# epam_files = Fido.fetch(epam_query)
# mag_files = Fido.fetch(mag_query)
# swepam_files = Fido.fetch(swepam_query)
# sst_files = Fido.fetch(sst_query)

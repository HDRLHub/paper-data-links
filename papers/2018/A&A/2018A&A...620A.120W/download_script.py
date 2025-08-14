# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net.attrs as a
from sunpy.net import Fido

# Query 1: PMOD Total Solar Irradiance Composite via SOHO/VIRGO
# Time range: November 1978 – December 2015
tsi_start = "1978-11-01"
tsi_end = "2015-12-31"

# Define the time and instrument attributes
tsi_time_attr = a.Time(tsi_start, tsi_end)
tsi_instr_attr = a.Instrument('VIRGO')

# Perform the search for VIRGO TSI data
print("Searching for SOHO/VIRGO TSI data between {} and {}...".format(tsi_start, tsi_end))
search_tsi = Fido.search(tsi_time_attr, tsi_instr_attr)
print(search_tsi)

# Uncomment to download the files when ready
# fetched_tsi = Fido.fetch(search_tsi)


# Query 2: UARS/SUSIM Solar UV Spectral Irradiance
# Time range: October 1991 – August 2002
susim_start = "1991-10-01"
susim_end = "2002-08-31"

# Define the time and instrument attributes
susim_time_attr = a.Time(susim_start, susim_end)
susim_instr_attr = a.Instrument('SUSIM')

# Perform the search for UARS/SUSIM UV data
print("Searching for UARS/SUSIM data between {} and {}...".format(susim_start, susim_end))
search_susim = Fido.search(susim_time_attr, susim_instr_attr)
print(search_susim)

# Uncomment to download the files when ready
# fetched_susim = Fido.fetch(search_susim)


# Query 3: SORCE/SOLSTICE UV Spectral Irradiance
# Time range: May 2003 – December 2015
solstice_start = "2003-05-01"
solstice_end = "2015-12-31"

# Define the time and instrument attributes
solstice_time_attr = a.Time(solstice_start, solstice_end)
solstice_instr_attr = a.Instrument('SOLSTICE')

# Perform the search for SORCE/SOLSTICE UV data
print("Searching for SORCE/SOLSTICE data between {} and {}...".format(solstice_start, solstice_end))
search_solstice = Fido.search(solstice_time_attr, solstice_instr_attr)
print(search_solstice)

# Uncomment to download the files when ready
# fetched_solstice = Fido.fetch(search_solstice)

print("All searches completed.")

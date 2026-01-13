# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Query SoHO/VIRGO SPM green channel data for a 12-year solar reference power spectrum.
This corresponds to the green channel (∼500 nm) used to derive νmax,⊙ in the study.
"""
import astropy.units as u
from sunpy.net import Fido, attrs as a

# 1. Define the time range for the 12-year VIRGO green channel dataset.
#    Since the VIRGO SPM green channel has been operating since late 1995,
#    we select an approximate 12-year interval.
start_time = '1996-04-16'
end_time   = '2008-04-16'

time_attr = a.Time(start_time, end_time)

# 2. Specify the VSO source, instrument, and detector.
#    We want data from SoHO's VIRGO instrument, specifically the SPM green channel.
source_attr     = a.Source('SOHO')
instrument_attr = a.Instrument('VIRGO')
detector_attr   = a.Detector('SPM')

# 3. Specify the wavelength for the green channel: 5000 Å.
wavelength_attr = a.Wavelength(5000.0 * u.Angstrom)

# 4. Perform the search using Fido.
print(f"Searching for {instrument_attr.value} {detector_attr.value} data "
      f"from {start_time} to {end_time} at {wavelength_attr.value}.")

results = Fido.search(source_attr,
                      instrument_attr,
                      detector_attr,
                      wavelength_attr,
                      time_attr)

# 5. Display the search results.
print(results)

# 6. To download the data, uncomment the following line:
# downloaded_files = Fido.fetch(results)

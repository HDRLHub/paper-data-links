# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries SDO/AIA and SDO/HMI data for the two CME source events
using SunPy's Fido client. Other instruments (Hinode/XRT, GONG, Wind MFI/SWE)
are not available in the provided VSO interface and hence are not queried here.
"""
import astropy.units as u
from sunpy.net import Fido, attrs as a

# -----------------------------------------------------------
# Event 1: 2 June 2011 CME source (SDO/AIA and SDO/HMI)
# Time range covers pre- and post-eruption imaging: 2011-05-31 to 2011-06-03
# -----------------------------------------------------------

# Define common time attribute for Event 1
time_event1 = a.Time("2011-05-31 00:00", "2011-06-03 23:59")

# Query AIA 171 Å
instrument_aia = a.Instrument("AIA")
wvl_171 = a.Wavelength(171.0 * u.Angstrom)
results_evt1_aia_171 = Fido.search(time_event1, instrument_aia, wvl_171)
print("Event 1 - AIA 171 Å:")
print(results_evt1_aia_171)
# Fido.fetch(results_evt1_aia_171)

# Query AIA 131 Å
wvl_131 = a.Wavelength(131.0 * u.Angstrom)
results_evt1_aia_131 = Fido.search(time_event1, instrument_aia, wvl_131)
print("\nEvent 1 - AIA 131 Å:")
print(results_evt1_aia_131)
# Fido.fetch(results_evt1_aia_131)

# Query AIA 1600 Å
wvl_1600 = a.Wavelength(1600.0 * u.Angstrom)
results_evt1_aia_1600 = Fido.search(time_event1, instrument_aia, wvl_1600)
print("\nEvent 1 - AIA 1600 Å:")
print(results_evt1_aia_1600)
# Fido.fetch(results_evt1_aia_1600)

# Query HMI LOS magnetograms (6173 Å) for PIL and polarity analysis
instrument_hmi = a.Instrument("HMI")
wvl_6173 = a.Wavelength(6173.0 * u.Angstrom)
results_evt1_hmi = Fido.search(time_event1, instrument_hmi, wvl_6173)
print("\nEvent 1 - HMI 6173 Å LOS Magnetograms:")
print(results_evt1_hmi)
# Fido.fetch(results_evt1_hmi)

# -----------------------------------------------------------
# Event 2: 14 June 2012 CME source (SDO/AIA and SDO/HMI)
# Time range covers build-up and eruption: 2012-06-12 to 2012-06-15
# -----------------------------------------------------------

# Define common time attribute for Event 2
time_event2 = a.Time("2012-06-12 00:00", "2012-06-15 23:59")

# Query AIA 131 Å
results_evt2_aia_131 = Fido.search(time_event2, instrument_aia, wvl_131)
print("\nEvent 2 - AIA 131 Å:")
print(results_evt2_aia_131)
# Fido.fetch(results_evt2_aia_131)

# Query HMI LOS magnetograms (6173 Å) for PIL and tongue analysis
results_evt2_hmi = Fido.search(time_event2, instrument_hmi, wvl_6173)
print("\nEvent 2 - HMI 6173 Å LOS Magnetograms:")
print(results_evt2_hmi)
# Fido.fetch(results_evt2_hmi)

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
Sunpy VSO Queries for the 2012-05-17 SEP GLE 71 event.
Instruments queried (available in the provided VSO interface):
  - SOHO / ERNE (HED detector)
  - STEREO-A / IMPACT (HET detector)
  - STEREO-B / IMPACT (HET detector)
Time range covers the main phase of the event: 2012-05-17 01:25 UT through 2012-05-19 UT.
"""
from sunpy.net import Fido, attrs as a

# Define the time range for the SEP event main phase
t_start = '2012-05-17 01:25'
t_end =   '2012-05-19 00:00'
time_range = a.Time(t_start, t_end)

# -------------------------------------------------------------------
# 1) Query SOHO / ERNE HED proton flux (matching GOES energy channels: ~14.6–140 MeV)
# -------------------------------------------------------------------
soho_source = a.Source('SOHO')
soho_instrument = a.Instrument('ERNE')
soho_detector = a.Detector('HED')
soho_physobs = a.Physobs('particle_flux')

soho_query = Fido.search(time_range,
                         soho_source,
                         soho_instrument,
                         soho_detector,
                         soho_physobs)

print("SOHO ERNE HED query results:")
print(soho_query)
# To download the data, uncomment the following line:
# soho_files = Fido.fetch(soho_query)

# -------------------------------------------------------------------
# 2) Query STEREO-A / IMPACT HET proton flux (13–100 MeV channels)
# -------------------------------------------------------------------
stereo_a_source     = a.Source('STEREO_A')
stereo_a_instrument = a.Instrument('IMPACT')
stereo_a_detector   = a.Detector('HET')
stereo_a_physobs    = a.Physobs('particle_flux')

stereo_a_query = Fido.search(time_range,
                             stereo_a_source,
                             stereo_a_instrument,
                             stereo_a_detector,
                             stereo_a_physobs)

print("\nSTEREO-A IMPACT HET query results:")
print(stereo_a_query)
# To download the data, uncomment the following line:
# stereo_a_files = Fido.fetch(stereo_a_query)

# -------------------------------------------------------------------
# 3) Query STEREO-B / IMPACT HET proton flux (13–100 MeV channels)
# -------------------------------------------------------------------
stereo_b_source     = a.Source('STEREO_B')
stereo_b_instrument = a.Instrument('IMPACT')
stereo_b_detector   = a.Detector('HET')
stereo_b_physobs    = a.Physobs('particle_flux')

stereo_b_query = Fido.search(time_range,
                             stereo_b_source,
                             stereo_b_instrument,
                             stereo_b_detector,
                             stereo_b_physobs)

print("\nSTEREO-B IMPACT HET query results:")
print(stereo_b_query)
# To download the data, uncomment the following line:
# stereo_b_files = Fido.fetch(stereo_b_query)

# Note: GOES 13 SEM, MSL/RAD, and MESSENGER NS are not available in the provided VSO interface.
# -----------------------------------------------------------------------------
# End of script
# -----------------------------------------------------------------------------

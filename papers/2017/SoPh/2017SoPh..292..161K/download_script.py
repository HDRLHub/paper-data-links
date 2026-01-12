# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
Script to query SOHO/LASCO-C2 and STEREO-A/COR1 coronagraph data from the Virtual Solar Observatory
for the 23 July 2016 CME event. This script searches for pre‐CME background and CME evolution images
used for polarized brightness (pB) and white‐light analysis.
"""
import sunpy.net
from sunpy.net import Fido, attrs as a

# =============================================================================
# Define time ranges for queries
# =============================================================================

# SOHO/LASCO-C2:
#   - Pre‐CME background at 02:54 UT on 2016-07-23
time_lasco_bg = a.Time('2016-07-23T02:54:00', '2016-07-23T02:54:00')
#   - CME evolution in the C2 field of view between 05:24 – 06:12 UT on 2016-07-23
time_lasco_cme = a.Time('2016-07-23T05:24:00', '2016-07-23T06:12:00')

# STEREO-A/SECCHI-COR1:
#   - Pre‐CME background at 05:00 UT on 2016-07-23
time_cor1_bg = a.Time('2016-07-23T05:00:00', '2016-07-23T05:00:00')
#   - CME and shock evolution between 05:25 – 05:35 UT on 2016-07-23
time_cor1_cme = a.Time('2016-07-23T05:25:00', '2016-07-23T05:35:00')

# =============================================================================
# Perform VSO searches
# =============================================================================

# Query 1: SOHO/LASCO-C2 pre‐CME background image
results_lasco_bg = Fido.search(
    time_lasco_bg,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Physobs('intensity')
)
print('SOHO/LASCO-C2 background search results:')
print(results_lasco_bg)

# Query 2: SOHO/LASCO-C2 CME evolution images
results_lasco_cme = Fido.search(
    time_lasco_cme,
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C2'),
    a.Physobs('intensity')
)
print('\nSOHO/LASCO-C2 CME evolution search results:')
print(results_lasco_cme)

# Query 3: STEREO-A/SECCHI-COR1 pre‐CME background image
results_cor1_bg = Fido.search(
    time_cor1_bg,
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('COR1'),
    a.Physobs('intensity')
)
print('\nSTEREO-A/COR1 background search results:')
print(results_cor1_bg)

# Query 4: STEREO-A/SECCHI-COR1 CME and shock evolution images
results_cor1_cme = Fido.search(
    time_cor1_cme,
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('COR1'),
    a.Physobs('intensity')
)
print('\nSTEREO-A/COR1 CME evolution search results:')
print(results_cor1_cme)

# =============================================================================
# To download the data, uncomment the following lines:
# =============================================================================

# Fido.fetch(results_lasco_bg)
# Fido.fetch(results_lasco_cme)
# Fido.fetch(results_cor1_bg)
# Fido.fetch(results_cor1_cme)

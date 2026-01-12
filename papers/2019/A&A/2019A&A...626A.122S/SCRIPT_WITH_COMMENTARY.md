# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to construct queries for several instruments
and time ranges as described in the context. The queries below are built for the
two events discussed in the context (Event 1 and Event 2). Only instruments available
in the provided VSO interface are used.

Event 1:
  • SOHO/LASCO: Query LASCO C2 images between 16:48 and 17:24 UT on 12 July 2012.
  • STEREO/SECCHI: Query COR2 images from both STEREO_A and STEREO_B between
    16:54 and 18:24 UT on 12 July 2012.
  • SDO/AIA: Query AIA 94 Å images (sigmoid) taken at ~15:00 UT on 12 July 2012,
    and AIA 193 Å images (post-eruption arcade) from 18:00 UT on 12 July 2012 to
    00:00 UT on 13 July 2012.
  • SDO/HMI: Query a magnetogram around 15:00 UT on 12 July 2012.

Event 2:
  • SOHO/LASCO: Query LASCO C2 images for CME1 (13 June 2012, 15:45 UT – 17:54 UT)
    and for CME2 (14 June 2012, 15:24 UT – 15:54 UT). Also query LASCO C3 images
    for CME2 in the same time interval.
  • SDO/AIA: Query AIA 193 Å images for two post-eruption arcades (PEAs): one at
    ~16:00 UT on 13 June 2012 (PEA1) and one at ~19:00 UT on 14 June 2012 (PEA2).
  • SDO/HMI: Query corresponding HMI magnetograms for these intervals.

Note: The MESSENGER MAG, Venus Express, and Wind in-situ measurements are not available 
via the VSO interface and are therefore not included.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

# ----------------------- Event 1 Queries -----------------------
# SOHO/LASCO C2 query for Event 1 (12 July 2012, 16:48–17:24 UT)
event1_lasco_c2 = Fido.search(
    a.Time("2012-07-12T16:48:00", "2012-07-12T17:24:00"),
    a.Instrument("LASCO"),
    a.Detector("C2"),
    a.Source("SOHO")
)
print("Event 1 - SOHO LASCO C2 query:")
print(event1_lasco_c2)
# To fetch the data, uncomment the line below:
# files_event1_lasco_c2 = Fido.fetch(event1_lasco_c2)

# STEREO/SECCHI COR2 query for Event 1 from STEREO_A (12 July 2012, 16:54–18:24 UT)
event1_stereo_a_cor2 = Fido.search(
    a.Time("2012-07-12T16:54:00", "2012-07-12T18:24:00"),
    a.Instrument("SECCHI"),
    a.Detector("COR2"),
    a.Source("STEREO_A")
)
print("\nEvent 1 - STEREO_A SECCHI COR2 query:")
print(event1_stereo_a_cor2)
# To fetch the data, uncomment the line below:
# files_event1_stereo_a_cor2 = Fido.fetch(event1_stereo_a_cor2)

# STEREO/SECCHI COR2 query for Event 1 from STEREO_B (12 July 2012, 16:54–18:24 UT)
event1_stereo_b_cor2 = Fido.search(
    a.Time("2012-07-12T16:54:00", "2012-07-12T18:24:00"),
    a.Instrument("SECCHI"),
    a.Detector("COR2"),
    a.Source("STEREO_B")
)
print("\nEvent 1 - STEREO_B SECCHI COR2 query:")
print(event1_stereo_b_cor2)
# To fetch the data, uncomment the line below:
# files_event1_stereo_b_cor2 = Fido.fetch(event1_stereo_b_cor2)

# SDO/AIA 94 Å query for Event 1 (sigmoid observation at ~15:00 UT on 12 July 2012)
event1_aia_94 = Fido.search(
    a.Time("2012-07-12T15:00:00", "2012-07-12T15:10:00"),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(94*u.Angstrom)
)
print("\nEvent 1 - SDO AIA 94 Å query:")
print(event1_aia_94)
# To fetch the data, uncomment the line below:
# files_event1_aia_94 = Fido.fetch(event1_aia_94)

# SDO/AIA 193 Å query for Event 1 (PEA observation from 18:00 UT on 12 July 2012 to 00:00 UT on 13 July 2012)
event1_aia_193 = Fido.search(
    a.Time("2012-07-12T18:00:00", "2012-07-13T00:00:00"),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(193*u.Angstrom)
)
print("\nEvent 1 - SDO AIA 193 Å query:")
print(event1_aia_193)
# To fetch the data, uncomment the line below:
# files_event1_aia_193 = Fido.fetch(event1_aia_193)

# SDO/HMI query for Event 1 (magnetogram at ~15:00 UT on 12 July 2012)
event1_hmi = Fido.search(
    a.Time("2012-07-12T15:00:00", "2012-07-12T15:02:00"),
    a.Source("SDO"),
    a.Instrument("HMI")
)
print("\nEvent 1 - SDO HMI query:")
print(event1_hmi)
# To fetch the data, uncomment the line below:
# files_event1_hmi = Fido.fetch(event1_hmi)

# ----------------------- Event 2 Queries -----------------------
# SOHO/LASCO C2 query for Event 2, CME1 (13 June 2012, 15:45–17:54 UT)
event2_lasco_c2_cme1 = Fido.search(
    a.Time("2012-06-13T15:45:00", "2012-06-13T17:54:00"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nEvent 2 - SOHO LASCO C2 query for CME1:")
print(event2_lasco_c2_cme1)
# To fetch the data, uncomment the line below:
# files_event2_lasco_c2_cme1 = Fido.fetch(event2_lasco_c2_cme1)

# SOHO/LASCO C2 query for Event 2, CME2 (14 June 2012, 15:24–15:54 UT)
event2_lasco_c2_cme2 = Fido.search(
    a.Time("2012-06-14T15:24:00", "2012-06-14T15:54:00"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nEvent 2 - SOHO LASCO C2 query for CME2:")
print(event2_lasco_c2_cme2)
# To fetch the data, uncomment the line below:
# files_event2_lasco_c2_cme2 = Fido.fetch(event2_lasco_c2_cme2)

# SOHO/LASCO C3 query for Event 2, CME2 (14 June 2012, 15:24–15:54 UT)
event2_lasco_c3_cme2 = Fido.search(
    a.Time("2012-06-14T15:24:00", "2012-06-14T15:54:00"),
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nEvent 2 - SOHO LASCO C3 query for CME2:")
print(event2_lasco_c3_cme2)
# To fetch the data, uncomment the line below:
# files_event2_lasco_c3_cme2 = Fido.fetch(event2_lasco_c3_cme2)

# SDO/AIA 193 Å query for Event 2, PEA1 (13 June 2012, ~16:00 UT)
event2_aia_193_pea1 = Fido.search(
    a.Time("2012-06-13T16:00:00", "2012-06-13T16:10:00"),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(193*u.Angstrom)
)
print("\nEvent 2 - SDO AIA 193 Å query for PEA1:")
print(event2_aia_193_pea1)
# To fetch the data, uncomment the line below:
# files_event2_aia_193_pea1 = Fido.fetch(event2_aia_193_pea1)

# SDO/HMI query for Event 2, corresponding to PEA1 (13 June 2012, ~16:00 UT)
event2_hmi_pea1 = Fido.search(
    a.Time("2012-06-13T16:00:00", "2012-06-13T16:02:00"),
    a.Source("SDO"),
    a.Instrument("HMI")
)
print("\nEvent 2 - SDO HMI query for PEA1:")
print(event2_hmi_pea1)
# To fetch the data, uncomment the line below:
# files_event2_hmi_pea1 = Fido.fetch(event2_hmi_pea1)

# SDO/AIA 193 Å query for Event 2, PEA2 (14 June 2012, ~19:00 UT)
event2_aia_193_pea2 = Fido.search(
    a.Time("2012-06-14T19:00:00", "2012-06-14T19:10:00"),
    a.Source("SDO"),
    a.Instrument("AIA"),
    a.Wavelength(193*u.Angstrom)
)
print("\nEvent 2 - SDO AIA 193 Å query for PEA2:")
print(event2_aia_193_pea2)
# To fetch the data, uncomment the line below:
# files_event2_aia_193_pea2 = Fido.fetch(event2_aia_193_pea2)

# SDO/HMI query for Event 2, corresponding to PEA2 (14 June 2012, ~19:00 UT)
event2_hmi_pea2 = Fido.search(
    a.Time("2012-06-14T19:00:00", "2012-06-14T19:02:00"),
    a.Source("SDO"),
    a.Instrument("HMI")
)
print("\nEvent 2 - SDO HMI query for PEA2:")
print(event2_hmi_pea2)
# To fetch the data, uncomment the line below:
# files_event2_hmi_pea2 = Fido.fetch(event2_hmi_pea2)

if __name__ == '__main__':
    print("\nAll queries have been executed. Review the printed results for details.")

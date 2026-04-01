# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python
"""
This script uses SunPy's VSO interface (via Fido) to query data for several spacecraft
events as described in the paper. Each query uses the minimal required parameters:
a time range and an instrument name. Note that some of these instruments (e.g., MESSENGER,
Venus Express, Helios, IMP8, STEREO-A/B, Pioneer 11, Voyager 1/2) may not be available
in the VSO interface. In such cases the query result will indicate no matching data.

Important: The Fido.fetch commands are commented out to ensure that no data are actually
downloaded when running this script.

The time ranges below have been converted from Day-Of-Year (DOY) format to standard dates.
"""

import astropy.units as u
from sunpy.net import Fido, attrs as a

# ----- MESSENGER -----
# Event 6: 2009, DOY 069–071 (2009-03-10 to 2009-03-12)
messenger_start = '2009-03-10'
messenger_end   = '2009-03-12'
# Note: Instrument name is taken as 'MESSENGER'
q_messenger_event6 = Fido.search(a.Time(messenger_start, messenger_end), 
                                 a.Instrument("MESSENGER"))
print("MESSENGER Event 6 query result:")
print(q_messenger_event6)
# To fetch data (if available), uncomment the following line:
# data_messenger = Fido.fetch(q_messenger_event6)

# ----- Venus Express (VEX) -----
# Event 7: 2009, DOY 191–193 (2009-07-10 to 2009-07-12)
vex_start = '2009-07-10'
vex_end   = '2009-07-12'
# Instrument name assumed to be 'Venus_Express'
q_vex_event7 = Fido.search(a.Time(vex_start, vex_end),
                           a.Instrument("Venus_Express"))
print("\nVenus Express Event 7 query result:")
print(q_vex_event7)
# To fetch data (if available), uncomment the following line:
# data_vex = Fido.fetch(q_vex_event7)

# ----- Helios 1 (H1) -----
# Event 2: 1975, DOY 321 (1975-11-17 to 1975-11-17)
h1_start = '1975-11-17'
h1_end   = '1975-11-17'
q_h1_event2 = Fido.search(a.Time(h1_start, h1_end),
                          a.Instrument("Helios1"))
print("\nHelios 1 Event 2 query result:")
print(q_h1_event2)
# To fetch data (if available), uncomment the following line:
# data_h1 = Fido.fetch(q_h1_event2)

# ----- Helios 2 (H2) -----
# Event 3: 1977, DOY 328–333 (1977-11-24 to 1977-11-29)
h2_start = '1977-11-24'
h2_end   = '1977-11-29'
q_h2_event3 = Fido.search(a.Time(h2_start, h2_end),
                          a.Instrument("Helios2"))
print("\nHelios 2 Event 3 query result:")
print(q_h2_event3)
# To fetch data (if available), uncomment the following line:
# data_h2 = Fido.fetch(q_h2_event3)

# ----- Interplanetary Monitoring Platform-8 (IMP8) -----
# Event 1: 1974, DOY 285–299 (1974-10-12 to 1974-10-26)
imp8_start = '1974-10-12'
imp8_end   = '1974-10-26'
q_imp8_event1 = Fido.search(a.Time(imp8_start, imp8_end),
                            a.Instrument("IMP8"))
print("\nIMP8 Event 1 query result:")
print(q_imp8_event1)
# To fetch data (if available), uncomment the following line:
# data_imp8 = Fido.fetch(q_imp8_event1)

# ----- Wind -----
# Event 11: 2013, DOY 192–195 (2013-07-11 to 2013-07-14)
wind_start = '2013-07-11'
wind_end   = '2013-07-14'
q_wind_event11 = Fido.search(a.Time(wind_start, wind_end),
                             a.Instrument("Wind"))
print("\nWind Event 11 query result:")
print(q_wind_event11)
# To fetch data (if available), uncomment the following line:
# data_wind = Fido.fetch(q_wind_event11)

# ----- STEREO-A (STA) -----
# Event 10: 2013, DOY 008–010 (2013-01-08 to 2013-01-10)
sta_start = '2013-01-08'
sta_end   = '2013-01-10'
q_sta_event10 = Fido.search(a.Time(sta_start, sta_end),
                            a.Instrument("STEREO-A"))
print("\nSTEREO-A Event 10 query result:")
print(q_sta_event10)
# To fetch data (if available), uncomment the following line:
# data_sta = Fido.fetch(q_sta_event10)

# ----- STEREO-B (STB) -----
# Event 8: 2010, DOY 309–313 (2010-11-05 to 2010-11-09)
stb_start = '2010-11-05'
stb_end   = '2010-11-09'
q_stb_event8 = Fido.search(a.Time(stb_start, stb_end),
                           a.Instrument("STEREO-B"))
print("\nSTEREO-B Event 8 query result:")
print(q_stb_event8)
# To fetch data (if available), uncomment the following line:
# data_stb = Fido.fetch(q_stb_event8)

# ----- Pioneer 11 (P11) -----
# Event 1 (same time range as IMP8 for event 1): 1974, DOY 285–299 (1974-10-12 to 1974-10-26)
p11_start = '1974-10-12'
p11_end   = '1974-10-26'
q_p11_event1 = Fido.search(a.Time(p11_start, p11_end),
                           a.Instrument("Pioneer11"))
print("\nPioneer 11 Event 1 query result:")
print(q_p11_event1)
# To fetch data (if available), uncomment the following line:
# data_p11 = Fido.fetch(q_p11_event1)

# ----- Voyager 1 (V1) -----
# Event 4: 1978, DOY 004–008 (1978-01-04 to 1978-01-08)
v1_start = '1978-01-04'
v1_end   = '1978-01-08'
q_v1_event4 = Fido.search(a.Time(v1_start, v1_end),
                          a.Instrument("Voyager1"))
print("\nVoyager 1 Event 4 query result:")
print(q_v1_event4)
# To fetch data (if available), uncomment the following line:
# data_v1 = Fido.fetch(q_v1_event4)

# ----- Voyager 2 (V2) -----
# Event 5: 1978, DOY 060–069 (1978-03-01 to 1978-03-10)
v2_start = '1978-03-01'
v2_end   = '1978-03-10'
q_v2_event5 = Fido.search(a.Time(v2_start, v2_end),
                          a.Instrument("Voyager2"))
print("\nVoyager 2 Event 5 query result:")
print(q_v2_event5)
# To fetch data (if available), uncomment the following line:
# data_v2 = Fido.fetch(q_v2_event5)

print("\nAll queries executed. Note: Fido.fetch commands are commented out as instructed.")

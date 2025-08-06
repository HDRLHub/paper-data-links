# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido, attrs as a

# ------------------------------------------------------------------
# Query 1: LASCO/C2 white-light images for CME waiting time studies
# Time range: 1999-01-01 to 2001-12-31
# Instrument: SOHO LASCO, Detector: C2, PhysObs: intensity
# ------------------------------------------------------------------
time1 = a.Time('1999-01-01', '2001-12-31')
source1 = a.Source('SOHO')
instrument1 = a.Instrument('LASCO')
detector1 = a.Detector('C2')
physobs1 = a.Physobs('intensity')

query1 = Fido.search(time1, source1, instrument1, detector1, physobs1)
print("Query 1 Results:")
print(query1)
# To download the data, uncomment the following line:
# files1 = Fido.fetch(query1)

# ------------------------------------------------------------------
# Query 2: LASCO/C3 white-light images for the CME-CME interaction event
# Date: 2000-06-10 (SOL-2000-06-10)
# Instrument: SOHO LASCO, Detector: C3, PhysObs: intensity
# ------------------------------------------------------------------
time2 = a.Time('2000-06-10T00:00:00', '2000-06-10T23:59:59')
detector2 = a.Detector('C3')

query2 = Fido.search(time2, source1, instrument1, detector2, physobs1)
print("\nQuery 2 Results:")
print(query2)
# To download the data, uncomment the following line:
# files2 = Fido.fetch(query2)

# ------------------------------------------------------------------
# Query 3: STEREO-A HI1 white-light base-difference images for 25 May 2010 event
# Time range: 2010-05-25 00:00 to 2010-05-25 23:59
# Instrument: STEREO_A SECCHI, Detector: HI1, PhysObs: intensity
# ------------------------------------------------------------------
time3 = a.Time('2010-05-25T00:00:00', '2010-05-25T23:59:59')
source3 = a.Source('STEREO_A')
instrument3 = a.Instrument('SECCHI')
detector3 = a.Detector('HI1')

query3 = Fido.search(time3, source3, instrument3, detector3, physobs1)
print("\nQuery 3 Results:")
print(query3)
# To download the data, uncomment the following line:
# files3 = Fido.fetch(query3)

# ------------------------------------------------------------------
# Query 4: STEREO-A HI1 white-light running-difference images for 15 February 2011 event
# Time range: 2011-02-15 00:00 to 2011-02-15 23:59
# Instrument: STEREO_A SECCHI, Detector: HI1, PhysObs: intensity
# ------------------------------------------------------------------
time4 = a.Time('2011-02-15T00:00:00', '2011-02-15T23:59:59')

query4 = Fido.search(time4, source3, instrument3, detector3, physobs1)
print("\nQuery 4 Results:")
print(query4)
# To download the data, uncomment the following line:
# files4 = Fido.fetch(query4)

# ------------------------------------------------------------------
# Query 5: STEREO-A HI1 white-light base-difference images for 10 November 2012 event
# Time range: 2012-11-10 00:00 to 2012-11-10 23:59
# Instrument: STEREO_A SECCHI, Detector: HI1, PhysObs: intensity
# ------------------------------------------------------------------
time5 = a.Time('2012-11-10T00:00:00', '2012-11-10T23:59:59')

query5 = Fido.search(time5, source3, instrument3, detector3, physobs1)
print("\nQuery 5 Results:")
print(query5)
# To download the data, uncomment the following line:
# files5 = Fido.fetch(query5)

# Note: In situ instruments (ACE, Wind, DSCOVR) and particle detectors (GOES, LANL) 
# are not available via the provided VSO interface and therefore are not queried here.

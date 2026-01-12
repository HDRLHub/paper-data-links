# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3

import astropy.units as u
from sunpy.net import Fido, attrs as a

# Query AIA EUV data for six coronal dimming events based on the specified time ranges
# and six EUV channels: 94, 131, 171, 193, 211, 335 Å.

# Event 1: 01 August 2010 (07:00 – 19:00 UT)
time1 = a.Time('2010-08-01T07:00', '2010-08-01T19:00')
wavelengths = a.Wavelength([94, 131, 171, 193, 211, 335] * u.Angstrom)
query1 = Fido.search(time1, a.Instrument('AIA'), wavelengths)
print("Event 1 search results:")
print(query1)
# To download the files for Event 1, uncomment the line below:
# files_event1 = Fido.fetch(query1)

# Event 2: 21 June 2011 (01:00 – 13:00 UT)
time2 = a.Time('2011-06-21T01:00', '2011-06-21T13:00')
query2 = Fido.search(time2, a.Instrument('AIA'), wavelengths)
print("\nEvent 2 search results:")
print(query2)
# files_event2 = Fido.fetch(query2)

# Event 3: 06 September 2011 (21:30 – 09:30 UT next day)
time3 = a.Time('2011-09-06T21:30', '2011-09-07T09:30')
query3 = Fido.search(time3, a.Instrument('AIA'), wavelengths)
print("\nEvent 3 search results:")
print(query3)
# files_event3 = Fido.fetch(query3)

# Event 4: 19 January 2012 (13:30 – 01:30 UT next day)
time4 = a.Time('2012-01-19T13:30', '2012-01-20T01:30')
query4 = Fido.search(time4, a.Instrument('AIA'), wavelengths)
print("\nEvent 4 search results:")
print(query4)
# files_event4 = Fido.fetch(query4)

# Event 5: 09 March 2012 (03:00 – 15:00 UT)
time5 = a.Time('2012-03-09T03:00', '2012-03-09T15:00')
query5 = Fido.search(time5, a.Instrument('AIA'), wavelengths)
print("\nEvent 5 search results:")
print(query5)
# files_event5 = Fido.fetch(query5)

# Event 6: 14 March 2012 (15:00 – 03:00 UT next day)
time6 = a.Time('2012-03-14T15:00', '2012-03-15T03:00')
query6 = Fido.search(time6, a.Instrument('AIA'), wavelengths)
print("\nEvent 6 search results:")
print(query6)
# files_event6 = Fido.fetch(query6)

# End of script

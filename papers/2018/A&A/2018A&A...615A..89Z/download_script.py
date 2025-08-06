# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3

import sunpy.net
from sunpy.net import Fido, attrs as a
from astropy import units as u

# LOFAR data are not provided via the VSO interface
print("LOFAR data are not available through VSO. Skipping LOFAR query.")

# --------------------------------------------------------------------
# 1) Query SDO/HMI line-of-sight magnetograms for 2013-10-26
# --------------------------------------------------------------------
start_hmi = "2013-10-26T00:00:00"
end_hmi   = "2013-10-26T23:59:59"

time_hmi     = a.Time(start_hmi, end_hmi)
source_sdo   = a.Source("SDO")
instrument_hmi  = a.Instrument("HMI")
physobs_hmi  = a.Physobs("LOS_magnetic_field")

print("\nSearching for SDO/HMI LOS magnetic‐field data from", start_hmi, "to", end_hmi)
query_hmi = Fido.search(time_hmi, source_sdo, instrument_hmi, physobs_hmi)
print(query_hmi)

# To download the data, uncomment the following line:
# files_hmi = Fido.fetch(query_hmi)

# --------------------------------------------------------------------
# 2) Query SOHO/LASCO C2 coronagraph images for 2013-10-26 07:00–10:00 UT
# --------------------------------------------------------------------
start_lasco = "2013-10-26T07:00:00"
end_lasco   = "2013-10-26T10:00:00"

time_lasco      = a.Time(start_lasco, end_lasco)
source_soho     = a.Source("SOHO")
instrument_lasco  = a.Instrument("LASCO")
detector_c2     = a.Detector("C2")

print("\nSearching for SOHO/LASCO C2 images from", start_lasco, "to", end_lasco)
query_lasco = Fido.search(time_lasco, source_soho, instrument_lasco, detector_c2)
print(query_lasco)

# To download the data, uncomment the following line:
# files_lasco = Fido.fetch(query_lasco)

# --------------------------------------------------------------------
# 3) Query STEREO-A/SECCHI COR2 coronagraph images for 2013-10-26 07:00–10:00 UT
# --------------------------------------------------------------------
time_cor2       = a.Time(start_lasco, end_lasco)
source_stereo   = a.Source("STEREO_A")
instrument_secchi = a.Instrument("SECCHI")
detector_cor2   = a.Detector("COR2")

print("\nSearching for STEREO-A/SECCHI COR2 images from", start_lasco, "to", end_lasco)
query_cor2 = Fido.search(time_cor2, source_stereo, instrument_secchi, detector_cor2)
print(query_cor2)

# To download the data, uncomment the following line:
# files_cor2 = Fido.fetch(query_cor2)

if __name__ == "__main__":
    # The script only performs searches and prints results.
    pass

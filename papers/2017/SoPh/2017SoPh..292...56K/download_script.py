# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
import sunpy.net
from sunpy.net import Fido, attrs as a

# Define the observation window for the CME event on 2012-08-02
start_time = "2012-08-02 00:00"
end_time   = "2012-08-02 23:59"

# ---------------------------------------------------------------------
# 1. Query white-light images from SOHO/LASCO C3 for 2012-08-02
# ---------------------------------------------------------------------
print("Querying SOHO/LASCO C3 data for 2012-08-02...")
search_lasco = Fido.search(
    a.Time(start_time, end_time),
    a.Source('SOHO'),
    a.Instrument('LASCO'),
    a.Detector('C3')
)
print(search_lasco)  # Display the search results
# To download the files, uncomment the following line:
# files_lasco = Fido.fetch(search_lasco)

# ---------------------------------------------------------------------
# 2. Query white-light images from STEREO-A/SECCHI COR2 for 2012-08-02
# ---------------------------------------------------------------------
print("\nQuerying STEREO-A/SECCHI COR2 data for 2012-08-02...")
search_cor2a = Fido.search(
    a.Time(start_time, end_time),
    a.Source('STEREO_A'),
    a.Instrument('SECCHI'),
    a.Detector('COR2')
)
print(search_cor2a)  # Display the search results
# To download the files, uncomment the following line:
# files_cor2a = Fido.fetch(search_cor2a)

# ---------------------------------------------------------------------
# 3. Query white-light images from STEREO-B/SECCHI COR2 for 2012-08-02
# ---------------------------------------------------------------------
print("\nQuerying STEREO-B/SECCHI COR2 data for 2012-08-02...")
search_cor2b = Fido.search(
    a.Time(start_time, end_time),
    a.Source('STEREO_B'),
    a.Instrument('SECCHI'),
    a.Detector('COR2')
)
print(search_cor2b)  # Display the search results
# To download the files, uncomment the following line:
# files_cor2b = Fido.fetch(search_cor2b)

# End of script

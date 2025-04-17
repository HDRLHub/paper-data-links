# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface via Fido to query multiwavelength solar observations 
relevant to the study of the 1 May 2013 solar flare and associated CME. The queries are set up 
for different instruments and time ranges based on the context of the paper:
  1. RHESSI (for both thermal and non‐thermal X‑ray emission)
  2. SDO/AIA (for EUV imaging during the flare)
  3. STEREO-A SECCHI/EUVI (for filament eruption and post‐flare loops)
  4. STEREO-B SECCHI/EUVI (for flare magnitude estimation)
  5. SOHO LASCO (for coronagraph observations of the CME)

Note:
- Only the required values (time range and instrument) are provided.
- Fido.fetch commands are commented out to avoid performing data downloads.
- Each query is executed separately and the query results are printed.
"""

# Import required modules from sunpy.net
from sunpy.net import Fido, attrs as a

def main():
    # -------------------------------------------
    # 1. RHESSI: Thermal X-ray Emission (4–8 keV)
    # Thermal source was observed for ~5.5 minutes starting near 02:32 UT on 1 May 2013.
    thermal_start = "2013-05-01T02:32:00"
    thermal_end   = "2013-05-01T02:37:30"  # approx 5.5 minutes duration
    thermal_query = Fido.search(
        a.Time(thermal_start, thermal_end),
        a.Instrument("RHESSI")
    )
    print("RHESSI Thermal X-ray Query Result:")
    print(thermal_query)
    # Uncomment the next line to fetch the data:
    # downloaded_files = Fido.fetch(thermal_query)

    # -------------------------------------------
    # 2. RHESSI: Non-thermal X-ray Emission (13–30 keV)
    # Non-thermal burst integration from 02:32:03 UT to 02:33:21 UT on 1 May 2013.
    nonthermal_start = "2013-05-01T02:32:03"
    nonthermal_end   = "2013-05-01T02:33:21"
    nonthermal_query = Fido.search(
        a.Time(nonthermal_start, nonthermal_end),
        a.Instrument("RHESSI")
    )
    print("\nRHESSI Non-thermal X-ray Query Result:")
    print(nonthermal_query)
    # Uncomment the next line to fetch the data:
    # downloaded_files = Fido.fetch(nonthermal_query)

    # -------------------------------------------
    # 3. SDO/AIA: EUV Imaging During the Flare
    # EUV observations cover from the flare onset (~02:30 UT) to post-flare phases (~03:15 UT).
    aia_start = "2013-05-01T02:30:00"
    aia_end   = "2013-05-01T03:15:00"
    aia_query = Fido.search(
        a.Time(aia_start, aia_end),
        a.Source("SDO"),
        a.Instrument("AIA")
    )
    print("\nSDO/AIA EUV Query Result:")
    print(aia_query)
    # Uncomment the next line to fetch the data:
    # downloaded_files = Fido.fetch(aia_query)

    # -------------------------------------------
    # 4. STEREO-A SECCHI/EUVI: Filament Eruption & Post-flare Loops
    # STEREO-A provided an occulted view with observations starting near 02:30 UT.
    stereo_a_start = "2013-05-01T02:30:00"
    stereo_a_end   = "2013-05-01T03:15:00"
    stereo_a_query = Fido.search(
        a.Time(stereo_a_start, stereo_a_end),
        a.Source("STEREO_A"),
        a.Instrument("SECCHI"),
        a.Detector("EUVI")
    )
    print("\nSTEREO-A SECCHI/EUVI Query Result:")
    print(stereo_a_query)
    # Uncomment the next line to fetch the data:
    # downloaded_files = Fido.fetch(stereo_a_query)

    # -------------------------------------------
    # 5. STEREO-B SECCHI/EUVI: Flare Magnitude Estimation
    # A key saturated image at ~02:30:57 UT is used for flare class estimation.
    stereo_b_start = "2013-05-01T02:30:00"
    stereo_b_end   = "2013-05-01T02:31:00"
    stereo_b_query = Fido.search(
        a.Time(stereo_b_start, stereo_b_end),
        a.Source("STEREO_B"),
        a.Instrument("SECCHI"),
        a.Detector("EUVI")
    )
    print("\nSTEREO-B SECCHI/EUVI Query Result:")
    print(stereo_b_query)
    # Uncomment the next line to fetch the data:
    # downloaded_files = Fido.fetch(stereo_b_query)

    # -------------------------------------------
    # 6. SOHO LASCO: Coronagraph Imaging of the CME
    # LASCO/C2 data is used since its available time range covers the event.
    lasco_start = "2013-05-01T02:30:00"
    lasco_end   = "2013-05-01T03:00:00"
    lasco_query = Fido.search(
        a.Time(lasco_start, lasco_end),
        a.Source("SOHO"),
        a.Instrument("LASCO"),
        a.Detector("C2")
    )
    print("\nSOHO LASCO/C2 Query Result:")
    print(lasco_query)
    # Uncomment the next line to fetch the data:
    # downloaded_files = Fido.fetch(lasco_query)

if __name__ == "__main__":
    main()

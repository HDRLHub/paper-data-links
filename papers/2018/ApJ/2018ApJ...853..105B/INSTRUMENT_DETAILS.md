_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper investigates the magnetic field characteristics of solar active regions (ARs) that produce large solar flares (GOES class M5.0 and above) during 2011–2015, aiming to discriminate between confined and eruptive flares. The study uses direct data from the Solar Dynamics Observatory (SDO), specifically from the Helioseismic and Magnetic Imager (HMI) for vector magnetic field measurements and the Atmospheric Imaging Assembly (AIA) for high-resolution EUV/UV imaging. The analysis spans 44 flares with documented observation dates and employs potential field modeling for coronal magnetic field extrapolation. CME associations are determined via LASCO and STEREO-B CME catalogs and coronagraph images, while flare position and structure are derived using a combination of AIA and HMI data, focusing on precise time frames centered around each event.

## Instrumentation Details

### Helioseismic and Magnetic Imager (HMI) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
  - Used for direct measurements of the vector magnetic field on the solar photosphere, including the total field, inclination, and azimuth, on the entire solar disk. The data serve as the basis for 3D potential magnetic field modeling and to analyze the magnetic configuration of ARs before and during the analyzed flares.
- **Supporting Quote**: "The magnetic field configuration in and above the flare ARs was investigated based on full-disk vector magnetic field observations from the Solar Dynamics Observatory (SDO; Pesnell et al. 2012) Helioseismic and Magnetic Imager (HMI; Schou et al. 2012). We used hmi.B 720s data (Hoeksema et al. 2014) which provides the total field, inclination and azimuth on the entire solar disk."

#### Data Collection Period 1: Pre-flare and Flare Timing Analysis
- **Time Range**: January 2011 – December 2015, for each event last available HMI magnetic field data prior to flare onset (see Table 1 event list for individual event dates, e.g., "25 October 2014" for event no. 15)
  - **Supporting Quote**: "We searched the GOES flare catalog for flare events exceeding a peak soft X-ray (SXR) flux of 5 × 10−4 W m−2 (i.e., flares of GOES class M5.0 and larger), that occurred between January 2011 and December 2015."  
  - **Supporting Quote**: "Here, we used Bz of the last available magnetic field data prior to the flare onset as input."
- **Wavelength(s)**: 6173 Å (Fe I line, native for HMI vector imaging)
  - **Supporting Quote**: [Explicit line wavelength not re-quoted, but standard for HMI and implied through SDO/HMI dataset context.]
- **Physical Observable**: Photospheric vector magnetic field components (total field, inclination, azimuth, disambiguated and deprojected to derive local horizontal and vertical components)
  - **Supporting Quote**: "We used hmi.B 720s data (Hoeksema et al. 2014) which provides the total field, inclination and azimuth on the entire solar disk."
  - **Supporting Quote**: "After disambiguation of the provided azimuth, we applied a de-projection (following Gary & Hagyard 1990) to the image-plane transverse and line-of-sight (LOS) magnetic field (Bxt ,Byt ,BLOS) in order to obtain the local horizontal and vertical magnetic field components (Bxh,Byh,Bz)."
- **Additional Comments**: The HMI data were binned and aligned with AIA data for coronal extrapolation and flare analysis.
  - **Supporting Quote**: "For magnetic field modeling, we binned the data to a plate scale of 1.′′01 per pixel, with the binning of the data being nearly magnetic flux preserving."

---

### Atmospheric Imaging Assembly (AIA) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
  - Used for high-resolution imaging of flare ribbons and EUV/UV emission in flare-impacted regions to identify flare locations and structures, co-aligned with HMI magnetic maps.
- **Supporting Quote**: "We used high-resolution full-disk imagery from the SDO Atmospheric Imaging Assembly (AIA; Lemen et al. 2012), with a spatial resolution of 1.′′5. 1600 Å images were used to study the structure of the flare-associated ribbons."

#### Data Collection Period 1: Flare Ribbon and PIL Identification
- **Time Range**: January 2011 – December 2015, imaging centered around the peak times of all 44 analyzed flares (e.g. for event no. 15: "25 October 2014 17:08" UT)
  - **Supporting Quote**: "We analyzed 44 flares of GOES class M5.0 and larger that occurred during 2011–2015."
  - **Supporting Quote**: "We used flare ribbons observed around the flare peak time in AIA 1600 Å images (red filled contours in Fig. 1a and 1c), in combination with the Bz = 0 G contour in the pre-flare HMI map (yellow curve in Fig. 1a and 1c), to localize the flare-relevant part along the extended PIL within the AR (orange/yellow curve in Fig. 1a/c)."
- **Wavelength(s)**: 1600 Å, also UV/EUV AIA filtergrams as needed for flare evolution study
  - **Supporting Quote**: "1600 Å images were used to study the structure of the flare-associated ribbons. In order to identify the flare-relevant PILs, we inspected filtergram sequences during the flares at UV and EUV wavelengths, in combination with the HMI Bz magnetic field maps."
- **Physical Observable**: UV flare ribbons, EUV/UV emission associated with flare sites, spatial and temporal correlation with magnetic field features
  - **Supporting Quote**: "1600 Å images were used to study the structure of the flare-associated ribbons."
  - **Supporting Quote**: "In order to identify the flare-relevant PILs, we inspected filtergram sequences during the flares at UV and EUV wavelengths, in combination with the HMI Bz magnetic field maps."
- **Additional Comments**: AIA and HMI data co-registered and co-aligned for accurate spatial analysis.
  - **Supporting Quote**: "HMI and AIA data was co-registered and co-aligned using standard IDL routines."

---

### Large Angle and Spectrometric Coronagraph (LASCO) on board SOHO
- **General Comments**:
  - Used to visually confirm CME associations with specific flares and determine timing of CME events in relation to flare onset using C2 images.
- **Supporting Quote**: "To classify events as confined or eruptive, we consulted the LASCO CME catalog (Gopalswamy et al. 2009) and additionally the CACTus (Robbrecht & Berghmans 2004) and CORIMP CME lists. We regarded a flare and a CME to be associated, if the back-extrapolated height-time profile of the CME (as deduced from LASCO-C2 images) agreed with the flare onset time of the GOES flare catalog."

#### Data Collection Period 1: CME Association with Analyzed Flares
- **Time Range**: January 2011 – December 2015, CME onset and tracking per individual flare events as listed in Table 1 (e.g., "20120510T04:18" for event no. 29)
  - **Supporting Quote**: "To classify events as confined or eruptive, we consulted the LASCO CME catalog ... We regarded a flare and a CME to be associated, if the back-extrapolated height-time profile of the CME (as deduced from LASCO-C2 images) agreed with the flare onset time of the GOES flare catalog."
- **Wavelength(s)**: White-light coronagraph imaging; specific wavelength not directly stated but LASCO standard is broadband visible light
  - **Supporting Quote**: [LASCO wavelength not explicitly quoted, but "LASCO-C2 images" referenced as data source.]
- **Physical Observable**: Coronal mass ejections (CME) height-time profiles, CME-flare temporal association
  - **Supporting Quote**: "the back-extrapolated height-time profile of the CME (as deduced from LASCO-C2 images) agreed with the flare onset time of the GOES flare catalog."
- **Additional Comments**: Supplemented with CACTus and CORIMP automated CME catalogs for verification.
  - **Supporting Quote**: "we consulted the LASCO CME catalog (Gopalswamy et al. 2009) and additionally the CACTus (Robbrecht & Berghmans 2004) and CORIMP CME lists."

---

### Sun Earth Connection Coronal and Heliospheric Investigation (SECCHI) COR1 on board STEREO-B
- **General Comments**:
  - Used for visual inspection of CME occurrence during a data gap in LASCO coverage for at least one specific event.
- **Supporting Quote**: "Only one event (SOL20120510T04:18M5.7) occurred during a short period of non-coverage in the LASCO CME catalog. In order to be able to classify the flare as confined or eruptive, we visually inspected STEREO-B COR1 observations, in which the flare was observed above the north-west limb."

#### Data Collection Period 1: CME Verification for SOL20120510T04:18M5.7
- **Time Range**: May 10, 2012, focused on flare time "SOL20120510T04:18"
  - **Supporting Quote**: "Only one event (SOL20120510T04:18M5.7) occurred during a short period of non-coverage in the LASCO CME catalog. In order to be able to classify the flare as confined or eruptive, we visually inspected STEREO-B COR1 observations, in which the flare was observed above the north-west limb."
- **Wavelength(s)**: White-light coronagraphy in the field of view of COR1; specific wavelength not given, standard for COR1 is 650–670 nm
  - **Supporting Quote**: [Wavelength not quoted; usage of "STEREO-B COR1 observations" as data source.]
- **Physical Observable**: CME detection or non-detection above the limb
  - **Supporting Quote**: "we visually inspected STEREO-B COR1 observations, in which the flare was observed above the north-west limb. The absence of a flare-associated CME, together with the missing of a flare-associated EUV wave, allowed us to classify this event as to be confined."
- **Additional Comments**: Used only for events lacking LASCO coverage; direct visual assessment.
  - **Supporting Quote**: "In order to be able to classify the flare as confined or eruptive, we visually inspected STEREO-B COR1 observations..."

---

**[End of instrument analysis]**

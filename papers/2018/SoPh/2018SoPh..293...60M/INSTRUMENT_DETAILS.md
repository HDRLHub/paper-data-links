_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper presents an investigation into the solar drivers of coronal mass ejections (CMEs) by linking observations from multiple instruments. The study combines remote‐sensing observations of CMEs from space‐based telescopes with photospheric magnetic field measurements from magnetograms. In doing so, it uses data collected over extended time periods—from the early days of STEREO to the modern era of SDO—to associate heliospheric CME observations with lower coronal signatures (e.g., flares) and active region (AR) magnetic characteristics. In particular, the paper describes how the HELCATS project catalogued nearly 2,000 HI-observed CMEs (from mid‑2007 until early‑2017) and how associated events observed by coronagraphs (COR2), along with flare data from GOES and RHESSI, and magnetic field data from SOHO/MDI and SDO/HMI were integrated. In addition, the FLARECAST project’s SHARP-based active region properties (from September 2012 to April 2016) are used to study the evolution of AR properties in the day leading up to CMEs.

## Instrumentation Details

### 1. STEREO Heliospheric Imager (HI) on board STEREO A/B
- **General Comments**:
   - The HI instrument is a key component of the HELCATS project and is used to automatically detect and catalogue CMEs as they propagate through the inner heliosphere.
   - It provided the primary dataset (the HICAT catalogue) for the study with over 2,000 HI-observed CME events.
- **Supporting Quote**: 
   - “...the algorithm has been run with version 4 of the HICAT catalogue, which contains 2,020 HI-observed CMEs, the first of which launched on 15 April 2007 and the last on 26 February 2017.” 
   - (See p. 4)

#### Data Collection Period 1: CME Detection via HI Observations
- **Time Range**: 15 April 2007 – 26 February 2017
   - **Supporting Quote**: “...the first of which launched on 15 April 2007 and the last on 26 February 2017.”
- **Wavelength(s)**: The paper does not explicitly list the operating wavelengths; HI observations are typically in white light.
   - **Supporting Quote**: (General reference to heliospheric imaging in the context of white-light observations.)
- **Physical Observable**: CME brightness and kinematic properties (speed and angular width).
   - **Supporting Quote**: “...catalogue of CME events observed by the STEREO Heliospheric Imagers (HI; Eyles et al., 2009).”

- **Additional Comments**: The HI instrument provides a wide-angle view of the inner heliosphere, essential for tracking the evolution of CMEs after their launch.

---

### 2. STEREO COR2 Coronagraph on board STEREO A/B
- **General Comments**:
   - The COR2 instrument is used in conjunction with the HI observations. It observes CMEs at lower heliocentric distances, enabling the algorithm to back-propagate HI-observed events to the Sun.
   - A COR2-observed CME is selected based on its similarity in angular width and position to the HI-observed CME.
- **Supporting Quote**:
   - “First the algorithm identifies a time window during which a STEREO/HI-observed CME might have been observed by the STEREO/COR2 coronagraph.” (p. 3)
   - “In total there are 1,591 COR2 events…” (p. 8)

#### Data Collection Period 1: COR2 CME Association
- **Time Range**: Implicitly associated with the HI event period (mid-2007 to early-2017); one example event is associated with COR2 observation starting at 2012-03-05 02:54 UT.
   - **Supporting Quote**: “...the automated algorithm identified a COR2 CME ... starting at 2012-03-05 02:54 UT...” (p. 8)
- **Wavelength(s)**: Observations are conducted in white light, typical for coronagraph imaging.
   - **Supporting Quote**: (Inferred from standard COR2 operations; not explicitly stated.)
- **Physical Observable**: CME brightness and angular width as observed close to the Sun.
   - **Supporting Quote**: “...properties of the COR2 CME such as the mean speed, position angle, and width...” (p. 8)
- **Additional Comments**: The COR2 instrument provides the link between the wide-field heliospheric imagery and the initiation region of the CME.

---

### 3. SOHO LASCO Coronagraph on board SOHO
- **General Comments**:
   - LASCO is referenced in the context of historical CME catalogues and manual identification methods.
   - It forms part of the background against which automated CME detection (through HELCATS) is compared.
- **Supporting Quote**: 
   - “The NASA CDAW Data Center catalogue (Gopalswamy et al., 2009) contains manually identified CMEs since 1996 from the Large Angle and Spectrometric Coronagraph (LASCO) onboard the Solar and Heliospheric Observatory (SOHO; Brueckner et al., 1995).”
- **Data Collection Period 1**: 
   - **Time Range**: Since 1996.
   - **Supporting Quote**: “...CMEs since 1996 from the Large Angle and Spectrometric Coronagraph (LASCO)...”
- **Wavelength(s)**: White light observations.
   - **Supporting Quote**: (Inferred from standard LASCO operation.)
- **Physical Observable**: CME brightness and morphology.
   - **Supporting Quote**: (Context provided via historical catalogue comparisons.)

---

### 4. SOHO/MDI (Michelson Doppler Imager) on board SOHO
- **General Comments**:
   - MDI is employed by the SMART algorithm for obtaining line-of-sight magnetograms of active regions when SDO/HMI data are not available.
   - It helps determine the magnetic field properties and boundaries of ARs.
- **Supporting Quote**:
   - “SMART is run on regions using SOHO’s Michelson Doppler Imager (MDI; Scherrer et al., 1995) and Solar Dynamics Observatory Helioseismic and Magnetic Imager (SDO/HMI; Scherrer et al., 2012) line-of-sight magnetograms, depending on the date of the observations (HMI data being available from mid 2010).”
- **Data Collection Period 1**:
   - **Time Range**: Before mid 2010 (when SDO/HMI was not yet available).
   - **Supporting Quote**: “...depending on the date of the observations (HMI data being available from mid 2010).”
- **Wavelength(s)**: Magnetogram observations in the Ni I 6768 Å line (typical for MDI), although not explicitly stated.
- **Physical Observable**: Photospheric line-of-sight magnetic field information.
   - **Supporting Quote**: “...magnetic field properties are calculated…” (p. 5)
- **Additional Comments**: MDI provided a foundational dataset for AR magnetic properties prior to the existence of SDO/HMI.

---

### 5. SDO/HMI (Helioseismic and Magnetic Imager) on board SDO
- **General Comments**:
   - SDO/HMI is used for the modern measurement of solar magnetic fields. Its data contribute both to the SMART algorithm (for AR detection) and to the FLARECAST property database through SHARP data products.
- **Supporting Quote**:
   - “SMART is run on regions using ... Solar Dynamics Observatory Helioseismic and Magnetic Imager (SDO/HMI; Scherrer et al., 2012)...”
   - “...the FLARECAST property database spans from the beginning of the SHARP data availability (September 2012) to April 2016.” (p. 14)
- **Data Collection Period 1**:
   - **Time Range**: HMI observations for magnetograms available from mid 2010; SHARP magnetic vector data used in FLARECAST span from September 2012 to April 2016.
   - **Supporting Quote**: “HMI data being available from mid 2010” and “...the FLARECAST property database spans from the beginning of the SHARP data availability (September 2012) to April 2016.”
- **Wavelength(s)**: Observations are made in Fe I 6173 Å spectral line.
   - **Supporting Quote**: (Standard for HMI; not explicitly stated in the provided text.)
- **Physical Observable**: Vector and line-of-sight magnetograms that yield information on photospheric magnetic fields and derived AR properties (e.g., total unsigned flux, vertical current, helicity).
   - **Supporting Quote**: “...properties of ARs... including total unsigned flux, vertical current, and current helicity.” (p. 10, Table 3 context)
- **Additional Comments**: HMI data underpins both the automatic region detection (via SMART) and the subsequent active region analysis (in the FLARECAST database), and is critical for studying the evolution of AR magnetic properties.

---

### 6. NOAA GOES (Geostationary Operational Environmental Satellite)
- **General Comments**:
   - GOES provides soft X-ray measurements used in identifying and classifying solar flare events.
   - The automated algorithm uses the GOES flare list (with events B-class and above) to associate flares with CMEs.
- **Supporting Quote**:
   - “...the algorithm associates any identified ﬂare events with corresponding NOAA-numbered ARs. The ﬂare peak location is used to search for nearby ARs...” and further, “...associated with a GOES X1.1 ﬂare starting at 2012-03-05 02:30 UT...” (p. 8)
- **Data Collection Period 1**: 
   - **Time Range**: Not explicitly defined; however, in the study, a specific event is referenced on 5 March 2012.
   - **Supporting Quote**: “...GOES X1.1 ﬂare starting at 2012-03-05 02:30 UT.”
- **Wavelength(s)**: Soft X-rays (typical GOES wavelength bands, e.g., 1–8 Å and 0.5–4 Å).
   - **Supporting Quote**: (Inferred from standard GOES operations.)
- **Physical Observable**: Solar soft X-ray flux used to determine flare intensity.
   - **Supporting Quote**: “...flare magnitude, location, and start, peak, and end times are listed...” (p. 8)
- **Additional Comments**: GOES flare data play a critical role in the flare-CME association process in the automated algorithm.

---

### 7. RHESSI (Reuven Ramaty High Energy Solar Spectroscopic Imager)
- **General Comments**:
   - RHESSI is used as an alternative source of flare information in cases where the NOAA/SWPC flare list does not provide adequate data or lacks event localization.
   - It ensures that flares, particularly those without assigned locations, are still considered by the automated algorithm.
- **Supporting Quote**:
   - “It will also check the NASA Reuven Ramaty High Energy Solar Spectroscopic Imager (RHESSI) ﬂare list if no events are found in the NOAA ﬂare list, and for those events without any given location.” (p. 3)
- **Data Collection Period 1**:
   - **Time Range**: Not explicitly stated; RHESSI was operational during many of the same years as the study’s period. (No specific dates provided in the text.)
- **Wavelength(s)**: Observes hard X-rays and gamma-rays associated with flare energization.
   - **Supporting Quote**: (Standard RHESSI operation; details are not provided explicitly in the text.)
- **Physical Observable**: High-energy emission from flares (hard X-ray signatures).
   - **Supporting Quote**: (Implied by the reference to RHESSI as a flare detection resource.)
- **Additional Comments**: RHESSI data complement the GOES flare list and help to increase the completeness of the flare event associations in the study.

---

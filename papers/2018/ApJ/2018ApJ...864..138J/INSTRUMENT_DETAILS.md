_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This study statistically examines solar eruptions by analyzing the conditions of torus and kink instabilities in magnetic flux ropes (MFRs) using multi-instrument solar observations. It uses data from NOAA GOES soft X-ray flare reports, vector magnetograms from HMI, UV images from AIA, and coronal mass ejection (CME) information from the LASCO CME catalog to derive key parameters such as the decay index (n) of the strapping field and the twist number (Tw) of the MFR. The analyzed events span a seven‐year period (January 2011 to December 2017), and the paper compares these observationally derived parameters with those obtained in laboratory experiments.

### 1. NOAA GOES Soft X-ray Instrumentation
- **General Comments**:
   - This instrument provided the soft X-ray (SXR) flare reports that were used to select major solar flares for the study. The flare selection criterion required events to be stronger than approximately GOES class M5 (with a relaxed criterion to M4 for confined flares) and located within 45° of disk center.
- **Supporting Quote**: 
   - "We examined NOAA GOES soft X-ray (SXR) ﬂare reports to search for major ﬂares (stronger than GOES class M5 in general) that occurred within 45◦of the disk center over a seven-year period from January 2011 to December 2017."
   
#### Data Collection Period: Solar Flare Selection
- **Time Range**: January 2011 – December 2017
   - **Supporting Quote**: 
      - "…major ﬂares that occurred within 45◦of the disk center over a seven-year period from January 2011 to December 2017."
- **Wavelength(s)**: Soft X-ray (exact wavelengths not specified but generally sensitive to thermal plasma emission in the soft X-ray band)
   - **Supporting Quote**: 
      - "NOAA GOES soft X-ray (SXR) ﬂare reports…"
- **Physical Observable**: X-ray flux used for flare classification (e.g., M-class and X-class events)
   - **Supporting Quote**: 
      - "…major ﬂares (stronger than GOES class M5 in general)..."

- **Additional Comments**: The GOES SXR data were essential for determining the timing and classification of the solar flares that were further examined using magnetogram and UV imaging data.

---

### 2. Helioseismic and Magnetic Imager (HMI) on board SDO
- **General Comments**:
   - HMI provided the vector magnetograms that serve as the boundary conditions for coronal magnetic field extrapolations. These magnetograms, re-binned to 1″ pixel intervals and pre-processed under force-free conditions, offer detailed measurements of the photospheric magnetic field.
- **Supporting Quote**:
   - "For each event, we used the last available vector magnetograms (hmi.sharp_cea_720s) of the AR prior to the ﬂare, obtained by the the Helioseismic and Magnetic Imager (HMI; Schou et al. 2012) on board the Solar Dynamics Observatory (SDO)…"
   
#### Data Collection Period: Pre-Flare Magnetogram Acquisition
- **Time Range**: Variable for each event; for example, for the SOL2015-06-22T18:23 event the HMI Bz map was taken at 17:36 UT, and for the SOL2015-03-12T14:08 event the magnetogram was taken at 13:48 UT.
   - **Supporting Quote**:
      - "(a) AIA 1600 (18:23 UT) / HMI Bz (17:36 UT)" and
      - "(a) AIA 1600 (14:08 UT) / HMI Bz (13:48 UT)"
- **Wavelength(s)**: Although not explicitly provided in the text, HMI typically observes in the visible spectrum (around the Fe I 6173 Å absorption line).
   - **Supporting Quote**: 
      - "…HMI Bz map…" (implying photospheric magnetic field observations)
- **Physical Observable**: Photospheric vector magnetic field (specifically the Bz component used in mapping the flaring polarity inversion line)
   - **Supporting Quote**:
      - "…obtained by the Helioseismic and Magnetic Imager (HMI…)" 

- **Additional Comments**: The HMI data were re-mapped using a cylindrical equal area (CEA) projection and were crucial for both the non-linear force-free field (NLFF) extrapolations and the identification of the flaring polarity inversion line.

---

### 3. Atmospheric Imaging Assembly (AIA) on board SDO
- **General Comments**:
   - AIA contributed UV images that capture the flare emission at 1600 Å, which are combined with HMI magnetograms to outline the flaring region through the FPIL (flaring polarity inversion line) mask.
- **Supporting Quote**:
   - "The HMI Bz map together with the UV 1600 ˚A image taken near the ﬂare peak time by the Atmospheric Imaging Assembly (AIA; Lemen et al. 2012) on board SDO was used in this step."
   
#### Data Collection Period: Flare Peak Imaging
- **Time Range**: Taken near the flare peak time; specific examples include:
   - For the ejective M6.5 flare (SOL2015-06-22T18:23), the AIA image was captured at 18:23 UT.
   - For the confined M4.2 flare (SOL2015-03-12T14:08), the AIA image was captured at 14:08 UT.
   - **Supporting Quote**:
      - "(a) AIA 1600 (18:23 UT) / HMI Bz (17:36 UT)" and
      - "(a) AIA 1600 (14:08 UT) / HMI Bz (13:48 UT)"
- **Wavelength(s)**: 1600 Å (ultraviolet)
   - **Supporting Quote**:
      - "…UV 1600 ˚A image…"
- **Physical Observable**: UV emission that maps the regions of flare energy release and helps identify the FPIL.
   - **Supporting Quote**:
      - "…superimposed with the yellow contours of the ﬂaring polarity inversion line (FPIL) mask."

- **Additional Comments**: The near-simultaneous use of AIA and HMI data enables a comprehensive view of both the magnetic configuration and the flare’s radiative signatures.

---

### 4. LASCO on board SOHO
- **General Comments**:
   - LASCO (Large Angle and Spectrometric Coronagraph) data from the LASCO CME catalog were utilized to determine the association of the selected flares with CMEs. Only halo or partial-halo CMEs were considered compatible with the MFR topology.
- **Supporting Quote**:
   - "For each ﬂare, its CME association was determined by reference to the LASCO CME catalog (Gopalswamy et al. 2009)." Additionally, table notes refer to "LASCO C2" indicating that observations from specific coronagraph channels were also considered.
   
#### Data Collection Period: CME Association Determination
- **Time Range**: Corresponds to the period during which the selected flares occurred, i.e., January 2011 – December 2017. Specific CME onset times were extrapolated backward to correlate with the associated flare onset.
   - **Supporting Quote**:
      - "…the CME onset time at R⊙ extrapolated backward from the CME height-time profile reasonably agrees with the ﬂare onset time…"
- **Wavelength(s)**: White-light coronagraph observations (broadband visible light)
   - **Supporting Quote**: Not explicitly mentioned, but LASCO operates as a white-light coronagraph.
- **Physical Observable**: CME properties such as the kinetic energy of the CME and spatial association with the flare region.
   - **Supporting Quote**:
      - "…we also refer to the LASCO CME catalog for the CME kinetic energy…"
- **Additional Comments**: Data gaps (e.g., in LASCO C2) are occasionally noted, and only events with appropriate halo or partial-halo CMEs were retained to ensure compatibility with the MFR topology.

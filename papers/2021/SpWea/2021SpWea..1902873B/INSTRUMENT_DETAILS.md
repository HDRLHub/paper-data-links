_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper evaluates the viability of using the ELEvoHI model for predicting coronal mass ejection (CME) arrival times and speeds using two types of STEREO-HI data: higher‐quality “science” data and lower‐quality real‐time “beacon” data. The study focuses on 10 CME events observed by the STEREO-A spacecraft between 2010 and 2020. The paper details the data preparation from various instruments within the SECCHI suite onboard STEREO, and discusses how differences in spatial and temporal resolutions (and hence data quality) affect the predictions. CME observations from white-light imagers and coronagraphs are used to generate time–elongation profiles while corresponding in situ measurements from Wind at L1 are used to benchmark the predictions.

## Instrumentation Details

### 1. STEREO-HI1 on board STEREO-A (SECCHI Suite)
- **General Comments**:
   - HI1 is one of the two heliospheric imagers that form part of the SECCHI suite. It captures white-light images used to track the CME front. Its design allows it to observe events with both high‐quality science data and lower‐quality beacon data.
- **Supporting Quote**: 
   - “HI1 has a FOV extending from roughly 4◦ to 24◦ elongation when measured from the Sun center, giving it a FOV of 20 x 20 ◦.”
- 
#### Data Collection Period: CME Observations from 2010 – 2020
- **Time Range**: 2010 – 2020  
   - **Supporting Quote**: 
      - “...to predict the arrival time and speed of 10 CME events that were observed by HI on the STEREO-A spacecraft between 2010 and 2020.”
- **Wavelength(s)**: White-light imaging (visible light)
   - **Supporting Quote**:
      - “...the SECCHI suite of instruments, which consists of two white-light imagers with overlapping FOV…”
- **Physical Observable**: 
   - The instrument observes the “time-elongation” evolution of CME fronts, which appear as bright streaks in time–elongation (J-) maps.
   - **Supporting Quote**:
      - “...producing the final J-Map in which the leading edge of the CME is clearly visible as a bright streak.”
- **Additional Comments**:
   - HI1 operates in two data modes, providing high-resolution science data (with a cadence of 40 minutes) and beacon data (with a cadence of 120 minutes) that are available in near-real time via data downlink and compression techniques.

### 2. STEREO-HI2 on board STEREO-A (SECCHI Suite)
- **General Comments**:
   - HI2 is the second white-light heliospheric imager in the SECCHI suite. It extends the field of view to larger elongations, allowing the tracking of CME evolution further from the Sun.
- **Supporting Quote**: 
   - “HI2 has a FOV extending from 18.8◦ to 88.8◦ elongation, amounting to a FOV of 70 x 70 ◦.”
- 
#### Data Collection Period: CME Observations from 2010 – 2020
- **Time Range**: 2010 – 2020  
   - **Supporting Quote**: 
      - “...analyze 10 CMEs observed by the STEREO-A spacecraft between 2010 and 2020.”
- **Wavelength(s)**: White-light imaging (visible light)
   - **Supporting Quote**:
      - “...consists of two white-light imagers…”
- **Physical Observable**:
   - HI2 captures the extended evolution of CME fronts by measuring elongation angles under similar physical observables as HI1.
   - **Supporting Quote**:
      - “...the elongation gives the angle between the observer, Sun-centre and another object.”
- **Additional Comments**:
   - As with HI1, HI2 data are available as both science and beacon data types. Beacon data are transferred in real time but at a lower spatial and temporal resolution.

### 3. STEREO-COR1 on board STEREO (SECCHI Suite)
- **General Comments**:
   - COR1 is a white-light coronagraph that images the solar corona by blocking direct sunlight. It is part of the SECCHI suite and complements the HI instruments by tracking CME initiation in the lower corona.
- **Supporting Quote**:
   - “...SECCHI suite of instruments, which consists of two white-light imagers… as well as two white-light coronagraphs, COR1 and COR2…”
- 
#### Data Collection Period: Operational since the STEREO mission (from launch in 2006) through the observations reported in this study
- **Time Range**: Operational throughout the STEREO mission; CME events in this study (2010 – 2020) lie within its operational period.
   - **Supporting Quote**: (Implied in the instrument description within SECCHI suite.)
- **Wavelength(s)**: White-light imaging (visible light)
- **Physical Observable**:
   - Observes features in the solar corona which may be related to the initiation of CMEs.
- **Additional Comments**:
   - Although not the primary focus for CME prediction in this study, COR1 images contribute to the broader set of observations in the SECCHI suite.

### 4. STEREO-COR2 on board STEREO (SECCHI Suite)
- **General Comments**:
   - COR2 is another white-light coronagraph in the SECCHI suite, offering a larger field of view to image the solar corona and the early propagation of CMEs.
- **Supporting Quote**:
   - “Data from the COR2 coronagraph aboard STEREO-A are also used frequently.”
- 
#### Data Collection Period: Operational throughout the STEREO mission (with CME events observed between 2010 and 2020 falling within its period of operation)
- **Time Range**: 2010 – 2020 (within the ongoing operational period of the STEREO mission)
- **Wavelength(s)**: White-light imaging (visible light)
- **Physical Observable**:
   - Like COR1, it monitors the early-stage white-light brightness of the corona, tracking CME evolution.
- **Additional Comments**:
   - COR2 provides complementary observational data that helps contextualize the CME’s near-Sun evolution, even though this study primarily focuses on heliospheric imaging.

### 5. EUVI on board STEREO (SECCHI Suite)
- **General Comments**:
   - EUVI is an extreme ultraviolet (EUV) imager within the SECCHI suite that offers complementary views of the solar disk and corona at EUV wavelengths.
- **Supporting Quote**:
   - “...and one EUV-camera (EUVI; Wuelser et al., 2004).”
- 
#### Data Collection Period: Operational parallel to other SECCHI instruments (from STEREO launch in 2006 through the events analyzed from 2010 to 2020)
- **Time Range**: 2010 – 2020 (as part of the SECCHI observational campaign during CME events)
- **Wavelength(s)**: Extreme ultraviolet wavelengths (specific bands not detailed in the paper)
- **Physical Observable**:
   - EUVI captures images of the solar disk and low corona, allowing for monitoring of solar activity that may lead to CME initiation.
- **Additional Comments**:
   - While EUVI data are referenced within the SECCHI suite description, the primary CME tracking in this paper is performed with the HI instruments.

### 6. Wind Spacecraft at L1
- **General Comments**:
   - The Wind spacecraft provides in situ measurements (plasma parameters and magnetic field data) at the Lagrange point L1. These data are used to determine the actual arrival times and speeds of CMEs as they impact near-Earth space.
- **Supporting Quote**:
   - “...using data from the Wind spacecraft (see Section 7) to determine arrival of a CME at L1 by using the shock arrival time as the CME arrival time.”
- 
#### Data Collection Period: In situ measurements corresponding to each CME event analyzed in the study (spanning from 2010 to 2020)
- **Time Range**: 2010 – 2020 (matching the events’ in situ arrival data)
- **Wavelength(s)**: Not applicable (these are in situ plasma and magnetic field detectors, not optical instruments)
- **Physical Observable**:
   - Measurement of proton bulk speed, detection of shock arrival, and inference of CME arrival dynamics.
   - **Supporting Quote**:
      - “The CME speed at L1 is also obtained from Wind data. It is taken to be the mean proton bulk speed…”
- **Additional Comments**:
   - Wind serves as the ground truth for validating ELEvoHI predictions concerning arrival time and speed.

### 7. PUNCH Mission Wide-Angle HI Cameras (Planned)
- **General Comments**:
   - The Polarimeter to UNify the Corona and Heliosphere (PUNCH) mission is scheduled for launch into low Earth orbit in 2023. It will carry wide-angle heliospheric imagers akin to those on STEREO, aiming to enhance CME observations from a near-Earth vantage point.
- **Supporting Quote**:
   - “...with its planned launch into a low Earth orbit in 2023, the Polarimeter to UNify the Corona and Heliosphere (PUNCH) mission will also carry wide-angle HI cameras on board…”
- 
#### Data Collection Period: Future mission; not part of the present study but mentioned as a means to improve real-time CME predictions.
- **Time Range**: Expected post-2023 (future operational period)
- **Wavelength(s)**: White-light imaging (implied, similar to current heliospheric imagers)
- **Physical Observable**:
   - Expected to capture CME evolution via white-light imagery, improving prediction accuracy by offering higher quality real-time data.
- **Additional Comments**:
   - The PUNCH mission represents a prospective development to alleviate current limitations inherent in STEREO beacon data.

### 8. Proposed HI Instrument on a Future Lagrange L5 Mission
- **General Comments**:
   - The paper discusses the potential benefits of deploying an HI instrument on a spacecraft positioned at the Lagrange point L5. This vantage point would allow for continuous observation of Earth-directed CMEs along the Sun–Earth line.
- **Supporting Quote**:
   - “...a spacecraft carrying HI devices which is equipped for higher telemetry rates. The Lagrange point L5 would provide a perfect vantage point for the observation of Earth directed CMEs…”
- 
#### Data Collection Period: Prospective future mission; no current data collection period.
- **Time Range**: Future (post-mission development and deployment)
- **Wavelength(s)**: White-light imaging (as per typical HI instruments)
- **Physical Observable**:
   - Would track CME evolution in white-light, offering continuous monitoring and potentially improved CME prediction through a new viewing angle.
- **Additional Comments**:
   - This concept is discussed as an avenue for enhancing real-time space weather prediction capabilities.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper describes an advanced approach to modeling the evolution and propagation of coronal mass ejections (CMEs) by improving the ELEvoHI method. The study incorporates a deformable CME front that adapts to the ambient solar wind conditions along the entire CME front rather than only at its apex. The analysis relies on a variety of observational data from space‐borne instruments. In particular, white‐light images from heliospheric imagers track the CME evolution, coronagraph images help determine the CME’s three‐dimensional structure via Graduated Cylindrical Shell (GCS) fitting, and in situ data from the Wind spacecraft provide measurements of the solar wind magnetic field, plasma speed, and density. Additional magnetogram data from SOHO/MDI and photospheric magnetic field maps from the GONG network serve as input to the coronal and solar wind models (such as EUHFORIA, HUX, and HUXt) employed in the study.

## Instrumentation Details

### 1. STEREO Heliospheric Imagers (HI) – HI1 and HI2 on board STEREO-A and STEREO-B
- **General Comments**:
   - These wide-angle white-light imagers are used to observe and track the CME front as it propagates through the heliosphere. The HI instruments provide time-elongation maps that capture the white-light emission from the Thomson-scattered photospheric light.
- **Supporting Quote**:
   - “Most important are images from HI onboard STEREO (Eyles et al., 2009). The HI instrument on each STEREO spacecraft consists of two white-light wide-angle imagers, HI1 and HI2.”
   
#### Data Collection Details:
- **Time Range / Specific Observation Periods**:
   - **STEREO-A/HI**: The studied CME was first observed at **February 3, 2010 14:49 UT**.
     - **Supporting Quote**: “The studied CME was first observed in STEREO-A/HI on February 3, 2010 14:49 UT.”
   - **STEREO-B/HI**: The corresponding first observation occurred at **February 3, 2010 20:49 UT** (six hours after the STEREO-A observation).
     - **Supporting Quote**: “The first observation in STEREO-B occurred six hours later on February 3, 2010 20:49 UT.”
- **Wavelength(s)**:
   - These instruments observe in white-light, detecting the visible spectrum as scattered sunlight by free electrons in the CME plasma.
     - **Supporting Quote**: “...using wide-angle white light observations from heliospheric imagers (HI)...”
- **Physical Observable**:
   - The detectors measure the brightness in white-light images that is associated with the Thomson scattering of sunlight by electrons, allowing the tracking of the CME front evolution.
- **Additional Comments**:
   - HI1 has a field-of-view (FOV) from 4° to 24° elongation in the ecliptic, with a science image cadence of approximately 40 minutes and a bin size of 70 arc sec.
   - HI2 covers an angular FOV from 18.8° to 88.8° and has a science image cadence of 120 minutes with a bin size of 4 arc min.

---

### 2. STEREO Coronagraph (COR2) – on board STEREO-A and STEREO-B
- **General Comments**:
   - The COR2 instrument is used for coronagraph imaging that captures the CME in the inner corona. The white-light images help in performing three-dimensional reconstructions (such as with the GCS method) to determine propagation direction, half width, and other geometric parameters.
- **Supporting Quote**:
   - “Figure 2 shows STEREO-A coronagraph images used to perform GCS fitting. STEREO/COR2 have a FOV from 2 – 15 R⊙ with a cadence of the coronagraph science images of about 15 minutes.”
   
#### Data Collection Details:
- **Time Range / Specific Observation Periods**:
   - **COR2 Imaging Time**: The images used for GCS fitting were acquired at **February 3, 2010 15:54 UT**.
     - **Supporting Quote**: “GCS fitting was performed based on COR2 images from both, STEREO-A and STEREO-B spacecraft ... on February 3, 2010 15:54 UT.”
- **Wavelength(s)**:
   - The instrument records white-light observations (visible wavelengths) as part of the coronagraph measurements.
- **Physical Observable**:
   - COR2 captures the intensity of scattered photospheric light (white-light brightness), which is used to delineate the CME front in the corona.
- **Additional Comments**:
   - The FOV extends from 2 to 15 solar radii, making it sensitive to structures erupting from the solar corona.

---

### 3. Wind Spacecraft – In Situ Instrumentation
- **General Comments**:
   - The Wind spacecraft provides in situ measurements of the solar wind parameters critical to understanding the interplanetary propagation of CMEs. This includes the solar wind speed, density, and magnetic field components.
- **Supporting Quote**:
   - “Figure 1 shows the in situ solar wind parameters measured by the Wind spacecraft from February 6 – 9, 2010.”
   
#### Data Collection Details:
- **Time Range / Specific Observation Periods**:
   - **Data Period**: The plasma and magnetic field measurements span from **February 6 to February 9, 2010**.
   - **ICME Arrival**: A specific interplanetary CME (ICME) was identified with an in situ arrival at **February 7, 2010 18:04 UT**.
     - **Supporting Quote**: “The ICME in situ arrival time is indicated by the vertical solid black line, ... on February 7, 2010 18:04 UT.”
- **Wavelength(s)**:
   - Not applicable; the spacecraft records physical quantities rather than electromagnetic images.
- **Physical Observable**:
   - Observables include magnetic field components (total field, Bx, By, Bz), solar wind speed, and density.
- **Additional Comments**:
   - These measurements are essential for verifying the arrival time and kinematic properties of the CME as predicted by the ELEvoHI model.

---

### 4. SOHO/MDI – Michelson Doppler Imager on board SOHO
- **General Comments**:
   - The SOHO/MDI instrument provides synoptic magnetograms of the solar photosphere. For this study, its observations are used to construct a magnetic map for input to coronal models that feed into the EUHFORIA model.
- **Supporting Quote**:
   - “For this study, as input to the coronal model, a synoptic magnetogram constructed from SOHO/MDI observations for Carrington rotation 2093 was used.”
   
#### Data Collection Details:
- **Time Range / Specific Observation Periods**:
   - The specific data corresponds to **Carrington rotation 2093**. (An exact UT date is not provided; the rotation represents a period over which the solar magnetic field is observed for model input.)
- **Wavelength(s)**:
   - MDI observed the photospheric magnetic field using visible light (Doppler imaging in a narrow spectral band) but explicit wavelength details are not provided in the context.
- **Physical Observable**:
   - The physical observable is the photospheric line-of-sight magnetic field.
- **Additional Comments**:
   - These magnetograms help generate the coronal magnetic field models (via PFSS and SCS) used to drive the solar wind models.

---

### 5. GONG – Global Oscillation Network Group
- **General Comments**:
   - The GONG provides magnetic field maps of the solar photosphere which are used as boundary conditions for coronal magnetic field modeling. These maps are an important input for solar wind forecasting models.
- **Supporting Quote**:
   - “... we use magnetic maps of the photospheric magnetic field from the Global Oscillation Network Group (GONG) provided by the National Solar Observatory (NSO) as input to magnetic models of the corona.”
   
#### Data Collection Details:
- **Time Range / Specific Observation Periods**:
   - The context does not specify an explicit time range for the GONG observations; rather, they are used generally as input data for the corona modeling.
- **Wavelength(s)**:
   - GONG observations are based on the visible wavelengths of the solar photosphere.
- **Physical Observable**:
   - The observable is the photospheric magnetic field distribution.
- **Additional Comments**:
   - These maps are crucial for establishing the magnetic boundary conditions that feed into further coronal and heliospheric numerical models.

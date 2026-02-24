_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper presents a statistical study of coronal dimming events that accompany coronal mass ejections (CMEs). Using a sample of 62 events, the study extracts characteristic parameters such as the evolving dimming area, brightness changes, and magnetic flux content. Multi-wavelength observations from SDO are combined with soft X-ray (SXR) flare measurements from GOES to compare the temporal evolution of coronal dimmings with flare properties. Data are obtained in a 12‐hour time series (starting 30 minutes before the flare), with the highest cadence (12 s) employed during the first two hours to capture the impulsive phase of the dimming. The instruments provide complementary observables: extreme‐ultraviolet (EUV) emission to study plasma depletion, magnetograms to extract magnetic flux information, and SXR data to characterize the energy release in associated flares.

## Instrumentation Details

### 1. SDO/AIA on board the Solar Dynamics Observatory
- **General Comments**:
   - SDO/AIA (Atmospheric Imaging Assembly) is used to obtain high-cadence, high-resolution extreme-ultraviolet imaging of the solar corona. It observes in multiple channels, allowing a multi-thermal view of coronal dimmings.
   - Supporting Quote: "We statistically analyze coronal dimmings observed in seven different extreme-ultraviolet (EUV) filters of the Atmospheric Imaging Assembly (AIA; Lemen et al. 2012) on-board the Solar Dynamics Observatory (SDO; Pesnell et al. 2012)..."
- **Supporting Quote**: "For the first two hours the full-cadence (12 s) observations are used, while for the remaining time series the cadence of the observations is successively reduced to 1, 5, and 10 minutes."  
- **Data Collection Period**:
   - **Overall Time Range**: Each event is analyzed over a 12-hour time series starting 30 minutes before the associated flare.
   - **Cadence Details**: The initial two hours are captured with 12-second cadence (essential for resolving the impulsive phase), then later images are taken at lower cadences (1, 5, and 10 minutes).
   - Supporting Quote: "To study the evolution of coronal dimming events our time series covers 12 hours, starting 30 minutes before the associated flare."
- **Wavelength(s)**:
   - The instrument collects data in seven EUV channels. Key wavelengths include:
     - 211 Å (used predominantly for statistical analysis; detected in 100% of events)
     - 193 Å (100%)
     - 171 Å (92%)
     - 335 Å (94%)
     - 94 Å (63%)
     - 131 Å (47%)
     - 304 Å (15%)
   - Supporting Quote: "For the majority of events, dimming regions are observed in the quiet Sun coronal temperature channels (193 and 211 Å...while...304 Å)..."
- **Physical Observables**:
   - Measures coronal intensity and its decrease (using techniques like logarithmic base-ratio images and minimum intensity maps) to identify and track the dimming regions.
   - Provides information on the plasma evacuation from the low corona during CME expansion.
   - Additionally, the AIA 1600 Å filter is mentioned in the context of flare ribbon observations (as used in Kazachenko et al. 2017) to assess flare reconnection.
- **Additional Comments**:
   - The high temporal and multi-wavelength capabilities of AIA are critical for capturing the detailed dynamics and evolution of dimming events in relation to CME initiation and flare activity.

### 2. SDO/HMI on board the Solar Dynamics Observatory
- **General Comments**:
   - SDO/HMI (Helioseismic and Magnetic Imager) provides line-of-sight (LOS) magnetograms that are essential for assessing the magnetic properties (e.g., total unsigned magnetic flux, area of significant magnetic field) of coronal dimming regions.
   - Supporting Quote: "To study their magnetic properties, the 720 s line-of-sight (LOS) magnetograms of the SDO/Helioseismic and Magnetic Imager (HMI; Scherrer et al. 2012; Schou et al. 2012) are used."
- **Time Resolution**:
   - **Cadence**: The magnetograms used have a cadence of 720 seconds.
- **Data Processing**:
   - The HMI data are rebinned to 2048 × 2048 pixels under conditions of flux conservation and aligned with the AIA data using standard SolarSoft routines (aia_prep.pro and hmi_prep.pro).
   - Supporting Quote: "The data is rebinned to 2048 × 2048 pixels under the condition of flux conservation."
- **Wavelength(s) and Observables**:
   - Although HMI does not operate in a traditional wavelength band like EUV, it observes the photospheric magnetic field by measuring LOS magnetic flux density.
   - These magnetograms facilitate extracting parameters such as the magnetic area of the dimming and the balance between positive and negative magnetic flux.
- **Additional Comments**:
   - Co-alignment with AIA imaging enables correlation of magnetic field properties with the spatial and temporal evolution of coronal dimmings.

### 3. GOES SXR Observations (via GOES Satellites)
- **General Comments**:
   - The Geostationary Operational Environmental Satellites (GOES) provide soft X-ray (SXR) measurements used to monitor solar flare activity. These SXR observations are crucial for timing the flare and for comparing flare energetics with dimming evolution.
   - Supporting Quote: "The GOES SXR flux and its derivative are used to compare the dimming properties to basic flare quantities..."
- **Data Collection Period**:
   - **Timing**: GOES provides continuous SXR measurements during the observed flare events. Although specific cadence details are not provided in the text, these observations are used contemporaneously with the AIA and HMI data.
- **Wavelength(s) and Observables**:
   - **Bandpass**: GOES SXR measurements are typically recorded in the 1.0–8.0 Å band.
   - **Physical Observables**: Important parameters include the peak SXR flux (FP), the time derivative of the SXR flux (˙FP), and the total SXR fluence (FT), which serve as proxies for the flare’s energy release.
   - Supporting Quote: "the GOES 1.0-8.0 Å SXR flux and its derivative..." 
- **Additional Comments**:
   - The GOES SXR data help establish the timing relationship between the flare energy release and the initiation and evolution of the coronal dimming events.

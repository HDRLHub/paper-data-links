_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper presents the implementation of a new linear force‐free spheromak (LFFS) model for simulating magnetised coronal mass ejections (CMEs) within the heliospheric MHD model EUHFORIA. The study focuses on validating the new CME model by comparing simulation outputs with multi-source observational data. Observations used in the study include photospheric magnetic field maps from the Global Oscillation Network Group (GONG), coronagraph images from the SOHO/LASCO instrument (as compiled in the CACTUS catalogue), and in‐situ measurements from the Wind spacecraft. The observations span a series of eruptive events during a period in June 2015 (approximately from 17 to 29 June 2015). These observational inputs are essential for setting up the empirical coronal background, constraining CME kinematic and magnetic parameters, and ultimately benchmarking the performance of the new LFFS model against established data.

## Instrumentation Details

### 1. Global Oscillation Network Group (GONG) Magnetograph – National Solar Observatory
- **General Comments**:
  - This instrument provides standard synoptic maps of the photospheric magnetic field which are used as input for the semi-empirical coronal model. These magnetograms help to determine the ambient solar wind plasma environment at 0.1 au.
- **Supporting Quote**: 
  - "the standard synoptic maps of the photospheric magnetic ﬁeld observed by the Global Oscillation Network Group (GONG) of the National Solar Observatory (Harvey et al. 1996)."
  
#### Data Collection Period 1: Single Snapshot for Model Input
- **Time Range**: 2015-06-25T01:04 UT – 2015-06-25T01:04 UT
  - **Supporting Quote**: 
    - "we use a GONG magnetogram that was obtained at 01:04 UT on June 25 as input to the model."
- **Wavelength(s)**: Not explicitly provided (typically visible wavelengths for photospheric observations)
  - **Supporting Quote**: N/A
- **Physical Observable**: Photospheric magnetic field distribution
  - **Supporting Quote**: 
    - "standard synoptic maps of the photospheric magnetic ﬁeld..."
- **Additional Comments**: The snapshot at 01:04 UT on June 25 is used to establish the initial coronal magnetic field configuration for the model.

### 2. SOHO/LASCO Coronagraph Imaging – (as used in the CACTUS Catalogue)
- **General Comments**:
  - The coronagraph images are used to detect and characterise CMEs. Automated detection is performed via the CACTUS catalogue, which identifies transients in SOHO/LASCO data. These observations provide the kinematic and morphological parameters necessary for setting up both the Cone and LFFS CME models.
- **Supporting Quote**:
  - "During the period of 17–29 June 2015, the CACTUS catalogue for automated detection of transients in SOHO/LASCO coronagraph imaging observation (Robbrecht et al. 2009) lists a total of 51 events in this time period..."
  
#### Data Collection Period 1: Overall CME Observation Period
- **Time Range**: 2015-06-17 UT – 2015-06-29 UT
  - **Supporting Quote**:
    - "During the period of 17–29 June 2015,... lists a total of 51 events..."
- **Wavelength(s)**: Not explicitly specified; typically white-light imaging in the visible spectrum used for coronagraph observations.
  - **Supporting Quote**: N/A
- **Physical Observable**: CME morphology, kinematics, and brightness as derived from coronagraph images
  - **Supporting Quote**:
    - "the third CME, observed in coronagraph images for the ﬁrst time at 02:48 UT on June 21, 2015..."
- **Additional Comments**: The SOHO/LASCO data underpin the determination of key CME parameters (e.g., width, speed, launch time) necessary for model fitting. Although the catalogue spans a prolonged period, individual CMEs such as the one observed at 02:48 UT on June 21 are highlighted.

### 3. Wind Spacecraft – In Situ Plasma and Magnetic Field Measurements
- **General Comments**:
  - The Wind spacecraft provides in situ observations near Earth, measuring plasma properties such as radial speed, density, and magnetic field components. These data are used to validate the simulation outputs, especially the arrival time and magnetic structure of the modeled CME.
- **Supporting Quote**:
  - "In the vicinity of Earth, the events were observed by the Wind spacecraft (Ogilvie et al. 1995)."
  
#### Data Collection Period 1: In Situ Measurements During the CME Events
- **Time Range**: Approximately 2015-06-22 UT (shock arrival at 18:08 UT) to mid-June 2015 (with additional shocks detected until at least 05:02 UT on June 25, 2015)
  - **Supporting Quote**:
    - "the third CME, observed in coronagraph images for the ﬁrst time at 02:48 UT on June 21, 2015 produced an interplanetary shock that was observed at Earth at 18:08 UT on June 22, 2015."
    - "the fourth and ﬁfth CMEs drove interplanetary shocks that were observed at 13:07 UT on June 24, and 05:02 UT on June 25, respectively."
- **Wavelength(s)**: Not applicable (in situ particle and field measurements)
  - **Supporting Quote**: N/A
- **Physical Observable**: Solar wind plasma properties including radial speed, number density, magnetic field magnitude and components (Bx, By, Bz)
  - **Supporting Quote**:
    - "timelines at Earth for RUN2... are plotted as the radial speed, the number density, the magnitude of the magnetic ﬁeld and all three magnetic ﬁeld components in GSE coordinates..."
- **Additional Comments**: These in situ measurements are crucial for assessing the performance of the LFFS model in simulating the CME propagation and magnetic field configuration as the CME impacts Earth.

### 4. STEREO A and STEREO B Spacecraft – Remote Sensing for Heliospheric Context
- **General Comments**:
  - The STEREO A and B spacecraft are referenced in the simulation outputs to provide additional spatial context regarding the propagation of CMEs within the inner heliosphere. Their positions are indicated in simulation figures to help interpret the three-dimensional structure of the CME.
- **Supporting Quote**:
  - "the positions of the inner planets as well as locations for the STEREO A and B spacecraft are indicated as shown in the legend."
  
#### Data Collection Period 1: Simulation Context Markers
- **Time Range**: Referenced in simulation snapshots (e.g., June 22, 2015 at 10:03 UT; June 23, 2015 at 04:03 UT etc.)
  - **Supporting Quote**:
    - "Snapshots from the simulation showing the radial speed νr [km s−1] on June 22, 2015 at 10:03 UT, 19:03 UT and June 23, 2015 at 04:03 UT... positions for the STEREO A and B spacecraft are indicated..."
- **Wavelength(s)**: Not applicable (these are spacecraft position indicators for context within the simulation)
  - **Supporting Quote**: N/A
- **Physical Observable**: Their inclusion supports the spatial mapping of simulated plasma parameters, but they are not directly providing observational data on CME properties.
  - **Supporting Quote**: N/A
- **Additional Comments**: Although not used directly for quantitative measurements in the study, the STEREO A and B positions serve as reference points for the three-dimensional configuration and evolution of the simulated CME.

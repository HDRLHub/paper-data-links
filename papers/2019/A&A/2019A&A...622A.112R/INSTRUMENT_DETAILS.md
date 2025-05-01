_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This study investigates the relationship between trees of fragmenting granules (TFG) observed at the solar surface and the corresponding deep downflows using both high-resolution solar observations and 3D magneto-convection simulations. The paper compares TFG detections from intensity images and velocity fields (vertical and Doppler) and correlates these features with horizontal surface flows. Two sets of simulation data (a 24‐hour sequence and a 4‐hour sequence) and space‐based observations from Hinode and SOHO/MDI are employed. The work focuses on data collected at specific time intervals—most notably, a 6‐hour Hinode NFI observation on 14 April 2010 (from 7h to 13h UT) and a snapshot of SOHO/MDI magnetic field data at 11h UT on the same day—as well as simulation periods spanning t = 59.6 h to 83.6 h and t = 68.15 h to 72.25 h. These multiple data sources and time ranges provide complementary perspectives on both the surface manifestations of solar convection (TFG) and the deeper convective downflows.

## Instrumentation Details

### 1. Hinode Narrowband Filter Imager (NFI) – FeI 557.6 nm Data on board Hinode
- **General Comments**:
   - This instrument is used to collect solar spectral images in a narrow wavelength band centered on the FeI 557.6 nm line. It provides both intensity and Doppler shift information that serve as proxies for the solar granulation and vertical plasma motions.
   - It enables the detection of TFG in both intensity images (derived from the average of the line wings at -12 and +12 pm) and Doppler velocity maps (with Doppler shifts computed using a bisector technique near inflection points).
- **Supporting Quote**:
   - “In order to compare TFG detected from solar observations in intensity and Doppler, we used Hinode NFI FeI 557.6 nm data, a 6 h sequence on 14 April 2010 from t = 7h to 13h U.T.”
   
#### Data Collection Period 1: Hinode NFI 6-h Sequence on 14 April 2010
- **Time Range**: 14 April 2010, from 7:00 UT to 13:00 UT
   - **Supporting Quote**:
      - “a 6 h sequence on 14 April 2010 from t = 7h to 13h U.T.”
- **Wavelength(s)**: FeI 557.6 nm (with a Lyot filter of 6 pm theoretical resolution)
   - **Supporting Quote**:
      - “Hinode NFI FeI 557.6 nm data … Granulation intensity was derived from the average of wings at -12 and +12 pm … the theoretical resolution of the Lyot filter is 6 pm.”
- **Physical Observable**: Intensity (for granulation) and Doppler shifts (to infer vertical velocities, Vdop)
   - **Supporting Quote**:
      - “The Doppler shifts were computed with the bisector technique around inflexion points providing Vdop above the solar surface at z =130 km.”
- **Additional Comments**: 
   - The data have high spatial resolution (originally 0.08″, rebinned to 0.16″) and a temporal cadence of 28.75 s, facilitating detailed study of TFG and horizontal velocity fields via local correlation tracking (LCT).

### 2. SOHO/MDI – Michelson Doppler Imager
- **General Comments**:
   - The SOHO/MDI instrument provides context magnetic field data, specifically longitudinal magnetic field measurements. This observational snapshot is used to complement the determination of network magnetic features.
- **Supporting Quote**:
   - “Longitudinal magnetic field context from SOHO/MDI on 14 April 2010 (11 h U.T.)”
   
#### Data Collection Period 1: SOHO/MDI Snapshot on 14 April 2010
- **Time Range**: 14 April 2010 at 11:00 UT
   - **Supporting Quote**:
      - “Fig. 2. Longitudinal magnetic ﬁeld context from SOHO/MDI on 14 April 2010 (11 h U.T.)”
- **Wavelength(s)**: Not explicitly provided.
- **Physical Observable**: Longitudinal magnetic field
   - **Supporting Quote**:
      - “… NBPs (network bright points) observed in the intensity line correspond to hot spots that are considered as proxies of magnetic ﬁelds.”
- **Additional Comments**:
   - This instrument provides a contextual magnetic field map serving as a reference for identifying the magnetic network associated with the TFG.

### 3. Hinode Solar Optical Telescope (SOT)
- **General Comments**:
   - The Solar Optical Telescope (SOT) onboard Hinode is historically employed for high-resolution intensity observations at disc center, particularly for the detection of trees of fragmenting granules (TFG) on the quiet Sun.
- **Supporting Quote**:
   - “The TFG detection is generally derived in the quiet Sun at disc centre from intensity observations with the Solar Optical Telescope (SOT on board Hinode) (Roudier et al. 2016, 2003).”
   
#### Data Collection Period 1: Hinode SOT Observations
- **Time Range**: Specific time ranges for the SOT intensity observations are not explicitly provided in the current paper.
   - **Supporting Quote**:
      - “… intensity observations with the Solar Optical Telescope (SOT on board Hinode) …”
- **Wavelength(s)**: Not detailed in the context.
- **Physical Observable**: Intensity (representing granulation features)
- **Additional Comments**:
   - While no explicit time window is provided in this paper for the SOT observations, its role in previous TFG studies and its high-resolution capabilities are emphasized.

### 4. 3D Magneto-convection Simulation – First (24-hour) Simulation
- **General Comments**:
   - This data set comes from a 3D magneto-convection code (Stein & Nordlund 1998; Stein et al. 2009) designed to model solar convection. It provides emergent intensity and full velocity vector fields. The simulation is used to compare TFG detection from intensity and vertical velocity (Vz), ensuring consistency with observational results.
- **Supporting Quote**:
   - “The ﬁrst is a 24 h duration sequence of the emergent intensity, surface vertical velocity (Vx,Vy,Vz), and magnetic ﬁeld vector extracted between t = 59.6 h to 83.6 h …”
   
#### Data Collection Period 1: 24-hour Simulation Sequence
- **Time Range**: From t = 59.6 h to t = 83.6 h (24-hour sequence)
   - **Supporting Quote**:
      - “… extracted between t = 59.6 h to 83.6 h …”
- **Wavelength(s)**: The emergent intensity is computed at τ = 1 (z = 0 Mm) and then filtered by the Hinode PSF at 557.6 nm.
   - **Supporting Quote**:
      - “Both quantities (intensity and velocity) were filtered by the Hinode point spread function (PSF) at 557.6 nm.”
- **Physical Observable**: Emergent intensity, surface vertical velocity (Vx, Vy, Vz), and magnetic field vector.
- **Additional Comments**:
   - The simulation has a horizontal resolution of 48 km (rebinned from 0.065″ to 0.13″ for observational comparison) and covers a horizontal field of 96 Mm × 96 Mm, though analysis was restricted to 48 Mm × 48 Mm.

### 5. 3D Magneto-convection Simulation – Second (4-hour) Simulation
- **General Comments**:
   - This simulation data set specifically provides the vertical velocity component (Vz) as a function of depth, enabling the study of deep downdrafts relative to the TFG detected at the surface.
- **Supporting Quote**:
   - “Because of the huge volume of data in the second MHD simulation of 4 h duration, we used only the vertical velocity Vz as a function of depth between z = 0.48 Mm (top) to z = -20.3 Mm from t = 68.15 h to 72.25 h.”
   
#### Data Collection Period 1: 4-hour Simulation Sequence
- **Time Range**: From t = 68.15 h to t = 72.25 h (4-hour sequence)
   - **Supporting Quote**:
      - “… from t = 68.15 h to 72.25 h.”
- **Wavelength(s)**: Not applicable; these are simulation data.
- **Physical Observable**: Vertical velocity (Vz) as a function of depth (from z = 0.48 Mm at the top to z = -20.3 Mm at the bottom)
- **Additional Comments**:
   - The simulation data are rebinned in both the vertical (by a factor of 2) and horizontal directions and are applied to study the coupling between surface TFG and deep downflows across different depths, revealing multiple scales of convection.

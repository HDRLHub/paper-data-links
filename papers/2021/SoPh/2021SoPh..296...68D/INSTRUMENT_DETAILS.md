_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper develops and tests an algorithm designed to compare temporal signatures from remote-sensing observations of coronal activity (primarily coronal jets) with in situ measurements of the solar wind. By employing Empirical Mode Decomposition on both types of datasets, the study is able to correlate characteristic timescales (ranging from about 5 to 100 minutes) observed in extreme ultraviolet (EUV) intensities with solar wind parameters measured near 1 AU. The work utilizes data from multiple instruments—including imaging of the solar corona from SDO/AIA, in situ plasma and magnetic field observations from WIND, and photospheric magnetic field maps from the GONG network—to both test the method on synthetic and observational datasets and to refine estimates of solar wind travel times and acceleration.

## Instrumentation Details

### 1. Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO)
- **General Comments**:
   - AIA provides high-cadence, full-disk observations of the solar atmosphere in multiple ultraviolet and extreme ultraviolet (EUV) passbands. In this study, it is used to capture transient jetting events via light emission intensity variations, particularly via its 193 Å passband.
   - In synthetic tests, an artificial dataset (AIAsynth) was constructed with a 12-second cadence and a 1.5-hour duration; in the observational case study, actual SDO/AIA 193 data is employed.
   
- **Supporting Quote**:
   - “The Atmospheric Imaging Assembly (AIA; Lemen et al., 2012) onboard the Solar Dynamics Observatory (SDO; Pesnell et al., 2011) provides twelve second cadence, full-disk UV and EUV observations of the solar atmosphere …”
   - “To construct the remote-sensing signal, we employed EUV measurements of the 193 ˚A passband from SDO/AIA … The coronal region of interest was... from 15:00 to 16:35 UT on 9 November 2016.”
   
#### Data Collection Period 1: Observational EUV Imaging of the Corona (~193 Å)
- **Time Range**: 15:00 UT – 16:35 UT on 9 November 2016
   - **Supporting Quote**: “…we employed SDO/AIA 193 measurements from 15:00 to 16:35 UT on 9 November 2016.”
- **Wavelength(s)**: 193 Å (Extreme Ultraviolet)
   - **Supporting Quote**: “To construct the remote-sensing signal, we employed EUV measurements of the 193 ˚A passband…”
- **Physical Observable**: EUV emission intensity; capturing coronal bright point activity and jet-like brightening events.
   - **Supporting Quote**: “…light emission intensity measurements of the solar corona… capturing the dynamics associated with coronal jets.”

### 2. 3DP Instrument on board the WIND Spacecraft
- **General Comments**:
   - This in situ instrument measures key plasma parameters of the solar wind—including bulk flow velocity, proton number density, proton temperature, and computed mass flux.
   - It is employed in the study to detect transient variations in solar wind properties that may correspond to coronal events observed remotely.
   
- **Supporting Quote**:
   - “We use in situ solar wind measurements of plasma bulk ﬂow velocity from the 3DP instrument (3DP; Lin et al., 1995) onboard the Wind spacecraft (WIND; Harten and Clark, 1995)…”
   
#### Data Collection Period 1: In Situ Solar Wind Measurements
- **Time Range**: 06:00 UT on 12 November 2016 – 06:00 UT on 13 November 2016
   - **Supporting Quote**: “For the application of our algorithm, we used data from 06:00 UT on 12 November to 06:00 UT on 13 November 2016…”
- **Physical Observable**: Solar wind plasma velocity (Vx), proton number density (Np), proton temperature (Tp), and derived mass flux (Mf).
   - **Supporting Quote**: “From the 3DP instrument, we considered the solar wind velocity Vx, proton number density Np, proton temperature Tp, and calculated mass ﬂux radially away from the Sun, Mf = −Np ∗mp ∗Vx.”

### 3. MFI Instrument on board the WIND Spacecraft
- **General Comments**:
   - The Magnetic Field Investigation (MFI) instrument measures the vector magnetic field of the solar wind.
   - In this study, its data is used to derive the total magnetic field strength (BT) via the magnitude calculation, supplementing plasma measurements.
   
- **Supporting Quote**:
   - “From the MFI instrument (Lepping et al., 1995) we calculated total magnetic ﬁeld magnitude as BT = √(BX² + BY² + BZ²).”
   
#### Data Collection Period 1: In Situ Magnetic Field Observations
- **Time Range**: Same as for the 3DP dataset – approximately 06:00 UT on 12 November 2016 to 06:00 UT on 13 November 2016
   - **Supporting Quote**: Although an explicit time range is not separately given, the MFI data is analyzed alongside the plasma measurements within the same 24-hour period.
- **Physical Observable**: Total magnetic field strength from the in situ solar wind.
   - **Supporting Quote**: “From the MFI instrument … we calculated total magnetic ﬁeld magnitude as BX² + BY² + BZ².”

### 4. GONG Network Synoptic Magnetograms
- **General Comments**:
   - The Global Oscillation Network Group (GONG) provides synoptic maps of the solar photospheric magnetic field. These maps serve as the boundary condition for Potential Field Source Surface (PFSS) modeling.
   - In this paper, they are used to locate the magnetic footpoints and determine the solar source regions.
   
- **Supporting Quote**:
   - “We obtained remote sensing measurements of the photospheric magnetic ﬁeld as synoptic magnetograms. … The time of the selected GONG synoptic map was 18:00 UT on 9 November 2016…”
   
#### Data Collection Period 1: Photospheric Magnetic Field Mapping
- **Time Range**: 18:00 UT on 9 November 2016 (time of the synoptic map closest to the ejection time)
   - **Supporting Quote**: “The time of the selected GONG synoptic map was 18:00 UT on 9 November 2016.”
- **Physical Observable**: Photospheric magnetic field strength and polarity.
   - **Supporting Quote**: “These magnetograms contain measurements of the magnetic ﬁeld strength and polarity, and were used as the boundary condition for a Potential Field Source Surface model of the coronal magnetic ﬁeld.”

### 5. High Resolution Imager (part of EUI) on board the Solar Orbiter
- **General Comments**:
   - The High Resolution Imager is a component of the Extreme Ultraviolet Imager (EUI) aboard Solar Orbiter. While it is not directly used in the observational case study, its field-of-view characteristics are used for comparison when defining the size of the bounding box for the AIA cutout.
   - This comparison ensures that the remote sensing region of interest is of a similar scale to what EUI would observe when the spacecraft is at 0.3 AU.
   
- **Supporting Quote**:
   - “The size of this bounding box was chosen to be similar to the ﬁeld of view of the High Resolution Imager that is part of EUI, onboard Solar Orbiter, when the spacecraft is at 0.3 AU.”
   
#### Data Collection Period 1: (No specific time range provided)
- **Time Range**: Not specified in the paper; serves as a reference for spatial scale.
- **Wavelength(s)**: Not explicitly given; EUI operates in the extreme ultraviolet.
- **Physical Observable**: High-resolution imaging of the EUV solar atmosphere.
   - **Additional Comments**: This instrument is referenced for its spatial resolution and field-of-view rather than for acquiring time series data in the current study.

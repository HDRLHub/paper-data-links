_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper studies the connection between turbulence-generated coherent structures (e.g., current sheets and vortices) and plasma heating in space plasmas. The authors compare high‐time resolution, multi‐point measurements with single‐point proxies derived from the Partial Variance of Increments (PVI) method. Two sets of in‐situ observations from the MMS mission are used – one from the turbulent terrestrial magnetosheath (MSH) and another from a Kelvin–Helmholtz (KH) vortex event at the magnetopause – along with observations from the WIND spacecraft during an ICME sheath passage. The analysis focuses on the detection of discontinuities, magnetic field rotations, and velocity shears on specific time scales; thereby linking localized current sheets and enhanced vorticity with intermittent plasma heating.

## Instrumentation Details

### 1. FGM Instrument on board MMS
- **General Comments**:
   - The Fluxgate Magnetometer (FGM) onboard MMS is used for high-resolution measurements of the magnetic field. These measurements provide the basis for detecting current sheets and estimating curl values through the curlometer technique.
- **Supporting Quote**: 
   - “We use magnetic ﬁeld data measured by the FGM instrument (Russell et al. 2016) at sampling frequency 128 Hz…” 

#### Data Collection Period 1: Turbulent Magnetosheath Observations
- **Time Range**: 30 Nov 2015, 00:21 UTC – 30 Nov 2015, 00:26 UTC
   - **Supporting Quote**: 
      - “The ﬁrst time interval consists of MMS observations of the turbulent MSH on 30 Nov 2015 between 00:21-00:26 UTC…”
- **Wavelength(s)**: Not directly applicable; however, the high temporal resolution (128 Hz) allows detection of kinetic-scale magnetic fluctuations.
   - **Supporting Quote**: 
      - “The four MMS spacecraft are equipped with the same state-of-the-art suite of instruments providing unprecedented high temporal and spatial resolution plasma and electromagnetic ﬁeld measurements…”
- **Physical Observable**: Magnetic field fluctuations used to calculate discontinuities and to derive current densities via the curlometer |∇×B|.
   - **Supporting Quote**: 
      - “…the curlometer | ∇× B | (Dunlop et al. 2002) from the magnetic ﬁeld… clearly detects the current sheets and sharp gradients.”
- **Additional Comments**:
   - The FGM data are smoothed (using a time scale corresponding to the ion inertial length) to better correlate the observed magnetic fluctuations with current sheet signatures.

#### Data Collection Period 2: Kelvin–Helmholtz Vortex Observations
- **Time Range**: 8 Sep 2015, 10:07 UTC – 8 Sep 2015, 11:25 UTC
   - **Supporting Quote**: 
      - “The second interval is an observation of Kelvin–Helmholtz (KH) vortices at the dusk-side magnetopause on 8 Sep 2015, between 10:07-11:25 UTC…”
- **Wavelength(s)**: Not applicable. Instead, the focus is on resolving mesoscale magnetic field gradients which are associated with large-scale vortices.
   - **Supporting Quote**: 
      - “…the KH vortices are large-scale structures reaching the size of several RE… the magnetic field rotations detected by FGM help to identify the current sheets associated with these vortices.”
- **Physical Observable**: Variations in the magnetic field intensity and direction to reveal current sheets, rotations, and shear.
   - **Supporting Quote**:
      - “For example, the magnetic ﬁeld makes several rotations from 0◦ to 180◦ behind the IP shock…” (comparison context with WIND is provided later, but similar diagnostics are applied here.)
- **Additional Comments**:
   - In the KH interval the FGM data are compared with simultaneous plasma measurements to identify the co-location of current sheets with changes in plasma parameters.

---

### 2. FPI Instrument on board MMS
- **General Comments**:
   - The Fast Plasma Investigation (FPI) onboard MMS provides high time resolution measurements of electron and ion moments. These measurements are critical for estimating particle velocities, calculating vorticities, and evaluating plasma temperature and density changes.
- **Supporting Quote**:
   - “and electron and ion moments from the FPI instrument (Pollock et al. 2016) at sampling rate 150 and 30 ms, respectively.”

#### Data Collection Period 1: Turbulent Magnetosheath Observations
- **Time Range**: 30 Nov 2015, 00:21 UTC – 30 Nov 2015, 00:26 UTC
   - **Supporting Quote**: (Referenced in the same passage as the FGM data) “The ﬁrst time interval consists of MMS observations of the turbulent MSH on 30 Nov 2015 between 00:21-00:26 UTC…”
- **Wavelength(s)**: Not applicable; however, the high temporal resolution (150 ms for electrons and 30 ms for ions) ensures that kinetic-scale processes are captured.
   - **Supporting Quote**:
      - “…electron and ion moments… at sampling rate 150 and 30 ms, respectively.”
- **Physical Observable**: Ion and electron velocity fields used to compute vorticities (|∇×V|) and to detect flow shear and discontinuities via PVI(V).
   - **Supporting Quote**:
      - “…the PVI from MMS-1 (in black) is plotted, obtained for the time delay τ ∼0.15 s… and the vorticity is calculated from four spacecraft.”
- **Additional Comments**:
   - The FPI’s high time resolution is key in distinguishing small-scale plasma dynamics, such as identification of current sheets and intermittent plasma heating signatures.

#### Data Collection Period 2: Kelvin–Helmholtz Vortex Observations
- **Time Range**: 8 Sep 2015, 10:07 UTC – 8 Sep 2015, 11:25 UTC
   - **Supporting Quote**:
      - “The second interval is an observation of Kelvin–Helmholtz (KH) vortices at the dusk-side magnetopause on 8 Sep 2015, between 10:07-11:25 UTC…”
- **Wavelength(s)**: Not applicable; the focus remains on resolving mesoscale kinetic dynamics rather than a specific wavelength.
- **Physical Observable**: The electron and ion velocity fields are utilized to derive vorticity and PVI(V) signals, which help diagnose flow discontinuities and shears.
   - **Supporting Quote**:
      - “…the ion vorticity and PVI(Vi) clearly show the vortical structures associated with the KH instability.”
- **Additional Comments**:
   - Comparisons between electron data (with finer details) and ion data highlight the multi-scale nature of the turbulent structures.

---

### 3. WIND Instrumentation on board WIND Spacecraft
- **General Comments**:
   - WIND spacecraft measurements are used to study an ICME sheath event. The instrumentation comprises two key detectors: one for plasma parameters (proton data) and one for magnetic field observations.
- **Supporting Quote**: 
   - “We analyze 3 s solar wind proton data from the WIND 3-D Plasma and Energetic Particle Investigation instrument (Lin et al. 1995), and 0.092 s magnetic ﬁeld observations from the Magnetic Field Investigation (MFI) instrument (Lepping et al. 1995).”

#### Data Collection Period: ICME Sheath Observations
- **Time Range**: 17 Mar 2013, 05:23 UTC – 17 Mar 2013, 14:35 UTC
   - **Supporting Quote**:
      - “...the IP shock (magenta vertical line) at 05:23 UTC on 17 Mar 2013 and the leading edge of the magnetic cloud at ∼14:35 UTC…”
- **Wavelength(s)**: Not applicable; measurements are made in the time domain using sampling periods of 3 s for plasma and 0.092 s for magnetic field.
   - **Supporting Quote**:
      - “We analyze 3 s solar wind proton data… and 0.092 s magnetic ﬁeld observations…”
- **Physical Observable**: 
   - Magnetic field rotations and discontinuities (using MFI) and changes in proton parameters (density, temperature, and velocity) are used to assess current sheets, flow shears, and intermittent plasma heating in the turbulent ICME sheath.
   - **Supporting Quote**:
      - “...the magnetic ﬁeld makes several rotations… and there is strong plasma heating (panel h) as well as high correlations between PVI(B) and PVI(V) in active regions.”
- **Additional Comments**:
   - The WIND instrumentation, with its distinct time resolutions, enables the study of large-scale structures (blobs) within the sheath, where groups of current sheets and vortices are linked with enhanced temperature signatures.

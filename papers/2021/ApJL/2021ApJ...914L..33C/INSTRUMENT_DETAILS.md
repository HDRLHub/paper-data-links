_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper investigates the nonlinear interactions of narrowband, large-amplitude whistler-mode waves with solar wind electrons using a 3d particle tracing simulation. The study compares the scattering and energization of electrons by whistler waves observed at two distinct heliocentric distances: near 1 AU and inside approximately 0.3 AU. The observational inputs to the simulation include whistler properties and background plasma conditions obtained from spacecraft measurements. At 1 AU, STEREO‐A waveform capture data of coronal mass ejections (e.g., the March 24–25, 2017 event) provided insight into the electric field structures and wave characteristics. Inside ~0.3 AU, Parker Solar Probe (PSP) data reveal that narrowband whistlers occur for many hours in regions with variable magnetic fields (occasionally associated with switchbacks). In addition, electron distribution parameters based on Wind data at 1 AU (and PSP when available) supplement the simulation inputs to investigate how the whistler waves scatter the electron strahl to form an isotropic halo and affect the electron heat flux.

## Instrumentation Details

### 1. STEREO-A Whistler Wave Instrument
- **General Comments**:
   - This instrument onboard STEREO-A captured waveforms in the solar wind at ~1 AU. It provided critical data on narrowband whistler-mode waves observed during solar wind events, particularly by recording electric fields with both perpendicular and parallel components.
- **Supporting Quote**:
   - “An example of the association of the large-amplitude oblique whistler-mode waves with solar wind structures at 1 AU is shown in Figure 1, which plots a coronal mass ejection on March 24-25, 2017, identified by Jian et al.(2006) in data from STEREO-A … Vertical blue lines are less coherent whistler-mode waves and vertical gold lines are narrowband whistler mode waves …”
  
#### Data Collection Period 1: Observation During a CME
- **Time Range**: March 24–25, 2017
   - **Supporting Quote**:
      - “Figure 1. Example of a CME with whistler-mode waves. (a) Magnetic field… (b) solar wind velocity… Vertical blue lines are less coherent whistler-mode waves and vertical gold lines are narrowband whistler mode waves …”
- **Wavelength(s)**: The whistler-mode waves are described by a frequency of ~0.2 fce (where fce is the electron cyclotron frequency).
   - **Supporting Quote**:
      - “Studies utilizing STEREO waveform capture data revealed the existence of large amplitude narrowband waves (NBWM) at frequencies of ~0.2 fce …”
- **Physical Observable**: Electric field waveforms; both perpendicular and parallel electric field components are measured.
   - **Supporting Quote**:
      - “The four example 2.1s waveform capture electric fields, with one component perpendicular to the magnetic field in red, and the parallel component in blue …”
- **Additional Comments**: The instrument provided a detailed snapshot of the electric field variations during a CME, supporting analyses of whistler wavepackets and their role in electron scattering.

### 2. Parker Solar Probe (PSP) Whistler Wave Instrumentation
- **General Comments**:
   - Instruments aboard PSP are used to observe narrowband whistler-mode waves inside ~0.3 AU. The PSP observations provide data on wave occurrence over many hours as well as variations in wave propagation angles (ranging from near parallel to highly oblique, including some sunward propagating packets). These measurements are key to setting simulation parameters such as a higher background magnetic field (B₀ = 50 nT) and higher density (n = 300 cm⁻³) compared with 1 AU.
- **Supporting Quote**:
   - “Inside ~.3 AU, PSP data show that the narrowband whistlers are also often seen for many hours, usually occur in regions of smaller variable background magnetic fields, and sometimes in association with magnetic field switchbacks …”
  
#### Data Collection Period 1: Extended Observations Inside ~0.3 AU
- **Time Range**: Observations taken continuously over many hours inside ~0.3 AU (exact dates not specified)
   - **Supporting Quote**:
      - “Inside ~.3 AU, PSP data show that the narrowband whistlers are also often seen for many hours …”
- **Wavelength(s)**: Similar to the 1 AU observations, the waves are characterized by frequencies centered around ~0.15 fce to 0.2 fce.
   - **Supporting Quote**:
      - “…with a fixed frequency (0.15 fce) …” and “observations … narrowband whistler mode waves …”
- **Physical Observable**: Electric field structures (wave amplitudes ranging from 10s to over 100 mV/m) and associated magnetic field variations.
   - **Supporting Quote**:
      - “The waves have electric field amplitudes ranging from 10s to up to >100 mV/m …”
- **Additional Comments**: PSP measurements contribute to understanding the variability in whistler-mode wave properties closer to the Sun and allow comparison with the conditions observed at 1 AU.

### 3. Wind Spacecraft Electron Instrumentation
- **General Comments**:
   - Wind spacecraft data are used in the paper to provide initial electron distribution parameters at 1 AU. These data are essential for initializing the particle tracing simulations focusing on electron energies (from a few eV to a few keV) and their pitch angle distributions.
- **Supporting Quote**:
   - “Weighting of results is performed using electron parameters based on Wilson III et al. (2019) for 1 AU …”
  
#### Data Collection Period 1: Electron Distribution Measurements at 1 AU
- **Time Range**: Measurements pertaining to 1 AU conditions (specific date ranges are not provided)
   - **Supporting Quote**:
      - “…initial electron distributions based on Wind data at 1 AU (Wilson III et al., 2019) …”
- **Wavelength(s)**: Not applicable; the Wind instrument data here involve electron energy and pitch angle distributions rather than wave measurements.
- **Physical Observable**: Electron kinetic energies and pitch angles, used to assess the scattering and energization of electrons by the whistler-mode waves.
   - **Supporting Quote**:
      - “Electrons with initial energies from 0 eV to 2 keV, pitch angles from 0° to 180° …”
- **Additional Comments**: Although the Wind instrumentation is not measuring the waves directly, its electron distribution data are critical for setting up the simulation environment and interpreting the scattering processes observed.

### 4. Helios (Referenced Observations)
- **General Comments**:
   - Helios is mentioned in the context of multi-radial observations that have tracked changes in electron distributions (e.g., strahl and halo populations) as the solar wind propagates from about 0.2 AU to beyond 5 AU. These observations help frame the context for the simulation results regarding electron scattering and evolution with radial distance.
- **Supporting Quote**:
   - “…observed changes in strahl and halo made by both PSP and Helios …”
  
#### Data Collection Period 1: Multi-radial Observations from ~0.2 to >5 AU
- **Time Range**: The referenced Helios observations cover a range from approximately 0.2 AU to beyond 5 AU (exact dates are not provided)
   - **Supporting Quote**:
      - “If only adiabatic effects are included, the field-aligned suprathermal strahl electrons would narrow … instead, satellite observations from ~0.2 to >5 AU have shown that the pitch angle width increases …”
- **Wavelength(s)**: Not applicable; similar to Wind, Helios data are used for electron distribution properties.
- **Physical Observable**: Electron pitch angle distributions and energy spectra, which are used to understand the transition from the field-aligned strahl to a more isotropic halo.
   - **Supporting Quote**:
      - “…and that strahl may be completely scattered by ~5.5 AU (Graham et al., 2017) …”
- **Additional Comments**: Although the Helios instrument details are not elaborated in this paper, its observational data provide supportive context for the evolution of solar wind electrons over large radial distances.

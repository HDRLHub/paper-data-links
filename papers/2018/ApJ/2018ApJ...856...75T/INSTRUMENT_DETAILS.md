_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper presents a comprehensive, physics-based simulation of the 14 July 2000 "Bastille Day" solar eruption, with a focus on capturing its energetic initiation, coronal evolution, and the resulting interplanetary coronal mass ejection (ICME) that impacted Earth. The research constructs a magnetostatic and thermodynamically consistent pre-eruptive state, energized through inserted flux ropes constrained by observational data. The simulated eruption is then compared with direct observations, both remote sensing and in situ, to evaluate the simulation’s fidelity in reproducing various facets of the event (e.g., CME kinematics, EUV waves, flare evolution, and ICME structure at 1 AU). The primary data sources for constraining, validating, and comparing the simulation include full-disk and synoptic line-of-sight (LOS) photospheric magnetic field maps, EUV and soft X-ray solar images, white-light coronagraph images, and in situ plasma and magnetic field measurements near 1 AU. Key observational instruments used span from SOHO/MDI (magnetograms) and SOHO/EIT (EUV imaging), to LASCO (coronagraph), Yohkoh/SXT (soft X-ray telescope), SDO/AIA, TRACE, and in situ monitors ACE and WIND, with observational periods specified as the days immediately surrounding the 14 July 2000 eruption (with greater detail from ∼09:30 UT through 19 UT on 14 July 2000, and interplanetary monitoring through July 16). Instrument data set the boundary conditions, validate the physical realism of synthetic images, and provide metrics for direct comparison with modeled CME and MC arrival at Earth.

## Instrumentation Details

---

### Michelson Doppler Imager (MDI) onboard SOHO
- **General Comments**:
  - Used to obtain the synoptic map for Carrington rotation 1965 and full-disk line-of-sight magnetogram for 14 July 2000. The MDI magnetic map forms the boundary condition for the simulation’s pre-eruptive coronal environment and is critical for inserting a realistic photospheric magnetic field structure in NOAA AR 9077.
- **Supporting Quote**: "To this end, we combine a line-of- sight (LOS) Solar and Heliospheric Observatory (SOHO) Michelson Doppler Imager (MDI; Scherrer et al. 1995) syn- optic map for Carrington rotation 1965 (July 10 – August 6, 2000) with a LOS MDI magnetogram measured on 14 July 2000 at 09:35 UT, about half an hour prior to the ﬂare onset (Figure 1)."

#### Data Collection Period 1: Pre-eruption coronal configuration for simulation boundary
- **Time Range**: 2000-07-14, 09:35 UT (MDI full-disk LOS magnetogram); Carrington Rotation 1965 = 2000-07-10 to 2000-08-06 (used for synoptic map context)
  - **Supporting Quote**: "To this end, we combine a line-of- sight (LOS) Solar and Heliospheric Observatory (SOHO) Michelson Doppler Imager (MDI; Scherrer et al. 1995) syn- optic map for Carrington rotation 1965 (July 10 – August 6, 2000) with a LOS MDI magnetogram measured on 14 July 2000 at 09:35 UT, about half an hour prior to the ﬂare onset (Figure 1)."
- **Wavelength(s)**: Not specified; MDI standard LOS mapping (Ni I 6768 Å)
  - **Supporting Quote**: "we use a ﬂux-preserving method to resample the LOS MDI mag- netogram to a Carrington map with an angular resolution of ≈0.2 degrees (about the width of 2 MDI pixels)."
- **Physical Observable**: Photospheric line-of-sight magnetic field (Br)
  - **Supporting Quote**: "To calculate a po- tential magnetic ﬁeld that serves as the initial condition for the thermodynamic MHD model, we have to specify the ra- dial ﬁeld component, Br, at the boundary r = R⊙, where R⊙is the solar radius."
- **Additional Comments**: Used to set the detailed structure of NOAA AR 9077 for the corona/solar wind simulation.

---

### Extreme Ultraviolet Imaging Telescope (EIT) onboard SOHO
- **General Comments**:
  - Used for remote sensing EUV imaging to validate the thermodynamic MHD simulation’s coronal solution and to compare the synthetic EUV emission with observed coronal loop structures before/after eruption.
- **Supporting Quote**: "Panels (b) and (c) show, respectively, the pre-eruptive corona as observed by the Extreme Ultraviolet Imag- ing Telescope (EIT; Delaboudini`ere et al. 1995) onboard SOHO and the Soft X-ray Telescope (SXT; Tsuneta et al. 1991) onboard Yohkoh, together with synthetic emission im- ages obtained from the simulation."

#### Data Collection Period 2: Pre-eruption coronal context and flare/EUV wave response
- **Time Range**: 2000-07-14, 09:36 UT (immediately before eruption, for coronal context); additional references up to ∼11:12 UT and throughout July 14, 2000, as implied by event evolution analyses
  - **Supporting Quote**: "(b) SOHO/EIT 195 ˚A observation of the corona at 09:36 UT on 14 July 2000, about half an hour before eruption (left), and synthetic emission obtained from the simulation at t = 162, af- ter ﬂux-rope insertion and MHD relaxation (right)."
- **Wavelength(s)**: 195 Å
  - **Supporting Quote**: "(b) SOHO/EIT 195 ˚A observation of the corona at 09:36 UT on 14 July 2000..."
- **Physical Observable**: EUV emission, coronal loop morphology and EUV waves/dimming
  - **Supporting Quote**: "EUV waves, dimmings), in a more realistic manner (e.g., Downs et al. 2011)..."
- **Additional Comments**: Used as a direct observational basis for validating synthetic emission and tracking the CME/EUV wave evolution.

---

### Large Angle and Spectrometric Coronagraph (LASCO) onboard SOHO
- **General Comments**:
  - Provided white-light coronagraph imaging of the CME during and after eruption. Used to establish CME kinematics, halo morphology, and to directly compare synthetic coronagraph images from simulation (“synthetic coronagraph image obtained from the simulation, showing running-ratio brightness at t = 165.2, as viewed from Earth”).
- **Supporting Quote**: "Figure 7(a) shows the large halo CME observed with the Large Angle and Spectrometric Coronagraph (LASCO; Brueckner et al. 1995) onboard SOHO."

#### Data Collection Period 3: CME propagation in the corona/outer corona
- **Time Range**: 2000-07-14, from CME onset at ∼10:10 UT through multiple hours post-eruption (Figure 7 context; specific example t = 165.2 given)
  - **Supporting Quote**: "Figure 7(a) shows the large halo CME observed with the Large Angle and Spectrometric Coronagraph (LASCO; Brueckner et al. 1995) onboard SOHO."
- **Wavelength(s)**: White light
  - **Supporting Quote**: "Figure 7(a) shows the large halo CME observed with the Large Angle and Spectrometric Coronagraph (LASCO; Brueckner et al. 1995) onboard SOHO."
- **Physical Observable**: CME leading edge position, white-light excess brightness
  - **Supporting Quote**: "Figure 7(b) a synthetic white-light image, obtained by using running-ratio polarized brightness images."
- **Additional Comments**: Directly constrains morphological comparison of simulated CME output against real event.

---

### Soft X-ray Telescope (SXT) onboard Yohkoh
- **General Comments**:
  - Used for soft X-ray imaging of the pre-eruption and flaring corona to compare with simulation synthetic images and to assess thermal response in the active region.
- **Supporting Quote**: "Panels (b) and (c) show, respectively, the pre- eruptive corona as observed by the Extreme Ultraviolet Imag- ing Telescope (EIT; Delaboudini`ere et al. 1995) onboard SOHO and the Soft X-ray Telescope (SXT; Tsuneta et al. 1991) onboard Yohkoh, together with synthetic emission im- ages obtained from the simulation."

#### Data Collection Period 4: Pre-flare and flare imaging
- **Time Range**: 2000-07-14, "at a similar time" to 09:36 UT EIT image, thus near 09:30–09:40 UT before eruption
  - **Supporting Quote**: "(c) Yohhoh/SXT observation at a sim- ilar time, together with a synthetic Hinode/XRT image at t = 162."
- **Wavelength(s)**: Soft X-rays (0.25–4.0 nm nominal for SXT, precise filter not specified)
  - **Supporting Quote**: "the Soft X-ray Telescope (SXT; Tsuneta et al. 1991) onboard Yohkoh"
- **Physical Observable**: Soft X-ray emission, coronal plasma temperature distribution and flare morphology
  - **Supporting Quote**: "(c) Yohhoh/SXT observation at a sim- ilar time, together with a synthetic Hinode/XRT image at t = 162."
- **Additional Comments**: Used to validate the high-temperature response and morphology of the simulated coronal configuration.

---

### Transition Region And Coronal Explorer (TRACE)
- **General Comments**:
  - Used for high-cadence EUV imaging of the flare arcade and filament eruption, as well as for assessing the onset and expansion of the eruption in direct comparison to simulation.
- **Supporting Quote**: "For this we use SOHO/EIT and Transition Region And Coronal Explorer (TRACE; Handy et al. 1999) observations of the ﬂare arcade and ﬁlament eruptions (see Figures 7 and 9 below)."

#### Data Collection Period 5: Flare arcade and filament eruption imaging
- **Time Range**: 2000-07-14, from pre-eruption through eruption phases with high temporal detail; event-specific intervals referenced (e.g., "observed the flare arcade at ∼10:10 UT onward")
  - **Supporting Quote**: "For this we use SOHO/EIT and Transition Region And Coronal Explorer (TRACE; Handy et al. 1999) observations of the ﬂare arcade and ﬁlament eruptions (see Figures 7 and 9 below)."
- **Wavelength(s)**: EUV band (TRACE 171 Å, 195 Å, and/or 284 Å filters; specific channel not specified here)
  - **Supporting Quote**: "TRACE images"
- **Physical Observable**: EUV emission, filament and flare ribbon morphology, dynamic evolution of eruption
  - **Supporting Quote**: "The flare loops were noted for their striking mor- phology and pattern of growth from West to East, as was observed in TRACE images."
- **Additional Comments**: Informs placement and evolution of model flux rope, validates timings and dynamics of eruption.

---

### Advanced Composition Explorer (ACE)
- **General Comments**:
  - Used for in situ measurements of interplanetary plasma and magnetic field at L1 for direct assessment of modeled ICME/MC arrival, field rotation, and plasma properties at Earth.
- **Supporting Quote**: "The shock wave driven by the ICME associated with the eruption reached the WIND spacecraft (Lin et al. 1995; Lepping et al. 1995) and the Advanced Composition Explorer (ACE; Stone et al. 1998) in ≈28 hours, followed by a large MC that arrived ≈5 hours later, around 19 UT on July 15, with a ﬁeld strength of ≈50 nT and a speed of ≈1100 km s−1 (e.g., Smith et al. 2001)."

#### Data Collection Period 6: ICME and magnetic cloud passage at 1 AU
- **Time Range**: 2000-07-15, ∼19:00 UT till July 16, covering MC passage at Earth (event context: direct arrival of Bastille Day MC in ACE/WIND data)
  - **Supporting Quote**: "The shock wave driven by the ICME associated with the eruption reached the WIND spacecraft (Lin et al. 1995; Lepping et al. 1995) and the Advanced Composition Explorer (ACE; Stone et al. 1998) in ≈28 hours, followed by a large MC that arrived ≈5 hours later, around 19 UT on July 15, with a ﬁeld strength of ≈50 nT and a speed of ≈1100 km s−1 (e.g., Smith et al. 2001)."
- **Wavelength(s)**: Not applicable (in situ magnetic field/plasma instrument suite)
- **Physical Observable**: In situ magnetic field components, plasma velocity, density at 1 AU
  - **Supporting Quote**: "Figure 12(a) provides a comparison of synthetic in situ measurements at the Earth’s position (green curves) with one-hour-averaged OMNI data (blue curves)."
- **Additional Comments**: Used as the reference data for timing, magnetic cloud rotation, Bz polarity, and plasma parameters for the synthesized in situ extraction from the simulation.

---

### WIND
- **General Comments**:
  - Used in conjunction with ACE for in situ magnetic field and plasma observations at L1. Validates timing, shock arrival, and magnetic cloud signatures as context for simulated ICME output.
- **Supporting Quote**: "The shock wave driven by the ICME associated with the eruption reached the WIND spacecraft (Lin et al. 1995; Lepping et al. 1995)..."

#### Data Collection Period 7: ICME and magnetic cloud at L1
- **Time Range**: 2000-07-15, ∼19:00 UT and following hours/days (matches ACE context)
  - **Supporting Quote**: "The shock wave driven by the ICME associated with the eruption reached the WIND spacecraft (Lin et al. 1995; Lepping et al. 1995) and the Advanced Composition Explorer (ACE; Stone et al. 1998) in ≈28 hours, followed by a large MC that arrived ≈5 hours later, around 19 UT on July 15..."
- **Wavelength(s)**: Not applicable (in situ measurements)
- **Physical Observable**: In situ magnetic field and plasma parameters at 1 AU
  - **Supporting Quote**: "The in situ magnetic-ﬁeld measurements taken at ACE suggest that the spacecraft passed below the axis of a left-handed ﬂux rope (Yurchyshyn et al. 2001)."
- **Additional Comments**: Forms basis for direct 1 AU comparison and validation of simulated MC arrival and properties.

---

### Atmospheric Imaging Assembly (AIA) onboard SDO
- **General Comments**:
  - Used to produce synthetic emission for direct comparison; while 2010–present instrument, the AIA response functions are used for generating synthetic images from the Bastille Day-era simulation outputs.
- **Supporting Quote**: "The top panels show synthetic emission images obtained for the simulation for the 171 ˚A passband of the Atmospheric Imag- ing Assembly (AIA; Lemen et al. 2012) onboard the Solar Dynamics Observatory (SDO; Pesnell et al. 2012)."

#### Data Collection Period 8: Synthetic comparison for model emission (no direct 2000 data, model only)
- **Time Range**: Synthetic images only (no direct observational data from July 2000)
- **Wavelength(s)**: 171 Å, 193 Å, 131 Å
  - **Supporting Quote**: "The top panels show synthetic emission images obtained for the simulation for the 171 ˚A passband of the Atmospheric Imag- ing Assembly (AIA; Lemen et al. 2012) onboard the Solar Dynamics Observatory (SDO; Pesnell et al. 2012)."
- **Physical Observable**: Model-predicted EUV emission structure for validation against historical instrument equivalents (e.g., EIT, TRACE)
  - **Supporting Quote**: "Figure 4 shows the simulated AR before and after the ﬂux- rope insertion and subsequent MHD relaxation, viewed from the West along the main (East-West) section of the PIL. The top panels show synthetic emission images obtained for the simulation for the 171 ˚A passband of the Atmospheric Imag- ing Assembly (AIA; Lemen et al. 2012) onboard the Solar Dynamics Observatory (SDO; Pesnell et al. 2012)."
- **Additional Comments**: Used for direct synthetic vs. observed emission diagnostics, especially to match loop/flare structure as if observed with modern capabilities.

---

**NOTE:** No other instruments are confirmed as directly used for new data collection or analysis that forms the core result set of the paper. Instruments referenced in literature review, historical context, or for comparison to others' work (e.g., Hinode/XRT, data for synthetic purposes, or observatories not providing contemporaneous direct measurements for the 2000 event) are **excluded** per the requirements.

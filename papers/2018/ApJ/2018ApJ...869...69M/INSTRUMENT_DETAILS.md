_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper presents a multi-wavelength analysis of two X-class solar eruptive flares (X2.2 and X9.3) that occurred on 2017 September 6 in active region NOAA 12673. The study integrates high-resolution imaging, both in extreme ultraviolet (EUV) and soft X-rays, together with detailed magnetic field measurements and modeling to probe the pre-flare configuration, flux rope formation, and subsequent plasma eruptions associated with these energetic events. Observations span from early pre-flare phases (starting at 08:00 UT) through the flare peaks and decay phases (up to 14:00 UT), with key timings for individual flare events deduced from various channels. The paper also employs Differential Emission Measure (DEM) analysis and non-force-free magnetic field (NFFF) extrapolations to understand plasma heating and connectivity in both coronal and photospheric layers.

## Instrumentation Details

### 1. Atmospheric Imaging Assembly (AIA) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
   - AIA provides full-disk, high-resolution multi-wavelength images of the Sun. It is used extensively in this study to capture the evolution of coronal structures, filament activations, plasma eruptions, and flare ribbon dynamics in both pre-flare and impulsive phases.
- **Supporting Quote**: 
   - "In this paper, we use observational data from the Atmospheric Imaging Assembly (AIA; Lemen et al. 2012) on board the Solar Dynamics Observatory (SDO; Pesnell et al. 2012)."
- **Detector and Wavelength Details**:
   - **Detectors**: Produces full-disk images of 4096×4096 pixels with a spatial resolution of 0′′.6 pixel⁻¹.
   - **Wavelength(s)**: 
      - Seven EUV filters: 94 Å, 131 Å, 171 Å, 193 Å, 211 Å, 304 Å, and 335 Å.
      - Two UV filters: 1600 Å and 1700 Å.
      - One white light filter: 4500 Å.
   - **Temporal Cadence**: 12 s for EUV channels, 24 s for UV channels, and 3600 s for the white light channel.
- **Physical Observable**:
   - Emission from the corona and chromosphere; signatures of hot plasma through DEM analysis, flare ribbon dynamics, and filament activations.
- **Data Collection Period**:
   - **Overall Period**: "The investigation carried out in this paper corresponds to the observation of the active region NOAA 12673 on 2017 September 6 from 08:00 UT to 14:00 UT."
   - **Example Flare Timings**:
      - **X2.2 Flare**: Flare initiation at ∼09:00 UT with the impulsive phase captured around 09:00–09:15 UT and emission decay continuing until ∼09:36 UT.
         - **Supporting Quote**: "Flare initiation occurred at ∼09:00 UT when this loop like structure started broadening up... The ﬁlament activation ceased at ∼09:15 UT and the ﬂare emission started to decline thereafter."
      - **X9.3 Flare**: Signs of filament activation starting at ∼11:53 UT, with peak brightening around 12:05 UT and a decay phase progressing until about 13:09 UT.
         - **Supporting Quote**: "The ﬁlament, after going through a brief phase of rapid expansion at around 11:55 UT, eventually erupted at ∼11:56 UT... the X9.3 ﬂare reached its peak intensity earlier in 304 Å than in 94 Å emission by ∼4 minutes."

---

### 2. Helioseismic and Magnetic Imager (HMI) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
   - HMI provides high-resolution photospheric observations, including intensity images, line-of-sight (LOS) magnetograms, and vector magnetic field measurements. This instrument is utilized to study sunspot configurations, magnetic gradients, and the evolution of δ-sunspots in AR 12673.
- **Supporting Quote**:
   - "For studying the photospheric structures associated with the active region NOAA 12673, we have used HMI intensity and line-of-sight (LOS) magnetogram images."
   - Additionally, "the photospheric vector magnetograms from HMI" are used as input to the non-force-free-field magnetic field extrapolation model.
- **Detector and Measurement Details**:
   - **Detectors**: Full-disk images of 4096×4096 pixels with a spatial resolution of 0′′.5 pixel⁻¹.
   - **Temporal Cadence**: 45 s for LOS magnetograms; vector magnetograms are provided with a cadence of 720 s (from the 'hmi.sharp cea 720s' series).
   - **Processing**: HMI images processed using SSW routine hmi_prep.pro to match the AIA resolution (0′′.6 pixel⁻¹) and to adjust for the roll angle.
- **Physical Observable**:
   - Photospheric magnetic field strength, magnetic polarities, and magnetic gradients critical for identifying the complex δ-type sunspot configuration.
- **Data Collection Period**:
   - While not explicitly restated as a range, the HMI data corresponds to the same observational period as AIA, i.e., from 08:00 UT to 14:00 UT on 2017 September 6.
   - **Supporting Context**: The coordinated use of AIA and HMI ensures spatial alignment between coronal structures and underlying magnetic fields during both flare events.

---

### 3. Large Angle and Spectrometric Coronagraph (LASCO) on board Solar and Heliospheric Observatory (SOHO)
- **General Comments**:
   - LASCO C2 and C3 coronagraphs are used to observe coronal mass ejections (CMEs) associated with the solar flares. Their white light images provide measurements of CME lead edges, speeds, and angular widths.
- **Supporting Quote**:
   - "Coronal mass ejections associated with the X-class ﬂares were observed by the C2 and C3 of the Large Angle and Spectrometric Coronagraph (LASCO; Brueckner et al. 1995) on board the Solar and Heliospheric Observatory (SOHO; Domingo et al. 1995)."
- **Detector and Wavelength Details**:
   - **LASCO C2**:
      - **Field of View (FOV)**: Imaging from 1.5 to 6 R⊙.
      - **Wavelength**: White light.
   - **LASCO C3**:
      - **FOV**: Imaging from 3.7 to 30 R⊙.
      - **Wavelength**: White light.
- **Physical Observable**:
   - Detection and morphological characterization of CME leading edges, including positional information and propagation speeds.
- **Data Collection Period and Specific Timings**:
   - **For the X2.2 Flare**: 
      - CME detected at 11:00 UT at 5.02 R⊙ in the LASCO C2 field of view.
      - **Supporting Quote**: "The CME corresponding to the X2.2 ﬂare was detected at 11:00 UT at 5.02 R⊙ (half-max lead) ... in the ﬁeld of view of LASCO C2."
   - **For the X9.3 Flare**:
      - CME detected at 12:36 UT at 3.50 R⊙, observed with an angular width of 145°.
      - **Supporting Quote**: "The CME corresponding to the X9.3 ﬂare was detected at 12:36 UT at 3.50 R⊙ (half-max lead) which had an angular width of 145°."

---

### 4. GOES X-ray Sensors
- **General Comments**:
   - GOES X-ray sensors monitor the Sun’s soft X-ray flux in two distinct energy bands (1–8 Å and 0.5–4 Å), providing critical information on the timing and intensity of flare emissions.
- **Supporting Quote**:
   - "Panel (a): GOES X-ray ﬂux proﬁles in 1–8 Å and 0.5–4 Å from 08:00 UT to 14:00 UT on 2017 September 6, showing the occurrence of two X-class ﬂares..."
- **Detector and Wavelength Details**:
   - **Wavelength(s)**: Soft X-ray bands at 1–8 Å and 0.5–4 Å.
- **Physical Observable**:
   - Soft X-ray flux profiles that indicate flare initiation, peak, and decay phases. These measurements are used to time the impulsive and gradual phases of the observed flares.
- **Data Collection Period and Specific Timings**:
   - **Overall Period**: Continuous monitoring from 08:00 UT to 14:00 UT on 2017 September 6.
   - **X2.2 Flare**: 
      - Start: 08:59 UT, Peak: 09:10 UT, End: 09:36 UT.
      - **Supporting Quote (from Table 1)**: "X2.2: Start 08:59 UT, Peak 09:10 UT, End 09:36 UT."
   - **X9.3 Flare**:
      - Start: 11:53 UT, Peak: 12:02 UT, End: 13:09 UT.
      - **Supporting Quote (from Table 1)**: "X9.3: Start 11:53 UT, Peak 12:02 UT, End 13:09 UT."

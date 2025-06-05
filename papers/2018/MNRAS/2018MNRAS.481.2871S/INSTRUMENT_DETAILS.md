_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper investigates the impact of stellar variability – specifically pulsations and granulation – as noise sources in exoplanet transit spectroscopy. Using simulations that combine a stellar variability model with the ExoSim end-to-end transit spectroscopy simulator, the study focuses on two representative exoplanet systems: one orbiting the M4.5V star GJ 1214 and the other the G0V star HD 209458. The researchers simulate out-of-transit (OOT) observations over a 15‐hour period (with different time bases for the stellar variability: 15 s cadence for GJ 1214 and 60 s for HD 209458) to compare the integrated stellar noise against the photon noise. The ARIEL mission’s instrument suite is used to probe various wavelengths – from the visual range (0.5–1.1 µm) to the near- and mid-infrared (1.25–7.8 µm) – measuring photoelectron counts per exposure and deriving observable quantities such as the transit contrast ratio, (Rp/Rs)². Additionally, the paper uses real Solar data from the SOHO VIRGO/SPM red channel to validate aspects of the stellar variability modelling.

## Instrumentation Details

### 1. ARIEL AIRS (Main Infrared Spectrometer) on board the ARIEL Mission
- **General Comments**:
   - AIRS is the primary spectrometer on ARIEL, designed to obtain transmission and emission spectra of exoplanets by observing their transits.
   - It operates in the infrared and is divided into two channels, enabling the study of spectral features over a broad wavelength range.
- **Supporting Quote**: “The main ARIEL spectrometer (AIRS) covers the wavelength range 1.95–7.8 µm in two channels: Ch0 (1.95–3.9 µm... and Ch1 (3.9–7.8 µm at R ≥30)...” (p. 4)

#### Data Collection Period: Simulated 15-Hour Out-of-Transit Observation
- **Time Range**: A single simulated observation lasting 15 hours with consecutive 60 s exposures.
   - **Supporting Quote**: “For each stellar target, ExoSim simulated an OOT observation of 15 hours (the duration of the stellar variability timelines used) consisting of 60 s exposures.” (p. 4)
- **Wavelength(s)**:
   - Ch0: 1.95–3.9 µm
      - **Supporting Quote**: “AIRS Ch0 (1.95–3.9 µm, R ≥100)” (p. 4)
   - Ch1: 3.9–7.8 µm
      - **Supporting Quote**: “and Ch1 (3.9–7.8 µm at R ≥30)” (p. 4)
- **Physical Observable**:
   - The instrument measures spectral flux variations as photoelectron counts per spectral bin per exposure. These counts are used to determine the contrast ratio (transit depth, (Rp/Rs)²) as well as the integrated noise (στ and σcr) from both astrophysical and instrument effects.
      - **Supporting Quote**: “...the output of the pipeline gives the photoelectron count in a spectral bin (or photometric aperture) per exposure in the time series.” (p. 4)
- **Detector & Additional Comments**:
   - From Table 1, AIRS channels use detectors with a pixel length (δ) of 18 µm and a quantum efficiency (QE) of 0.55. For Ch0, the f-number is 19.3 and mid-band transmission (υ) is 0.65; for Ch1, the f-number is 13.2 and υ is 0.45.
   - Observations through AIRS are simulated with the same overall 15-hour period as other channels, enabling direct comparisons between stellar variability noise and photon noise.

### 2. ARIEL NIRSpec (Near-Infrared Low-Resolution Spectrometer) on board the ARIEL Mission
- **General Comments**:
   - NIRSpec is a spectroscopic channel focused on the near-infrared, complementing the mid-IR coverage of AIRS.
   - It is used to capture low-resolution spectra that help in analyzing the wavelength-dependent flux variations of the host star.
- **Supporting Quote**: “A low resolution near-infrared spectrometer (NIRSpec)...” (p. 4)
  
#### Data Collection Period: Simulated 15-Hour Out-of-Transit Observation
- **Time Range**: Observations simulated over a 15-hour period with exposures of 60 s each.
   - **Supporting Quote**: (Same as for AIRS, “...simulated an OOT observation of 15 hours...”) (p. 4)
- **Wavelength(s)**: 1.25–1.95 µm
   - **Supporting Quote**: “NIRSpec is a NIR low-resolution spectrometer” as indicated along with its wavelength range in Table 1.
- **Physical Observable**:
   - Measures the modulation in the stellar spectral energy distribution (SED) to derive flux variations crucial for transit depth determination.
- **Detector & Additional Comments**:
   - According to Table 1, NIRSpec uses detectors with a pixel length (δ) of 18 µm, a f-number of 31.3, a QE of 0.55, and a plate scale (φ) of 3.60.
   - The simulated exposures are consistent with those used in the AIRS channels, allowing cross-channel comparisons of noise attributes.

### 3. ARIEL Photometric Channels (FGS 1, FGS 2, and VisPhot) on board the ARIEL Mission
- **General Comments**:
   - These channels are primarily designed for photometry and fine guidance. They serve a dual role: providing stellar variability monitoring (which informs the fine guidance system) and helping to constrain features such as the Rayleigh scattering slope in exoplanet atmospheres.
- **Supporting Quote**: “...3 visual photometric channels are also included (Table 1) that can constrain the Rayleigh scattering slope and monitor for stellar variations. The latter are, in addition, used in the fine guidance system for the spacecraft attitude control system.” (p. 4)
  
#### a) FGS 1
- **Data Collection Period**: Simulated as part of the 15-hour OOT observation with 60 s exposures.
   - **Time Range**: 15-hour simulation (consistent with ARIEL channels)
- **Wavelength(s)**: 0.9 µm
   - **Supporting Quote**: “FGS 1 (0.9 µm)” (Table 1)
- **Physical Observable**: Measures the stellar flux in the visual band and contributes to fine guidance as well as to establishing the uncertainty on contrast ratios through transit photometry.
- **Detector & Additional Comments**:
   - Detector characteristics: f-number of 24.6, QE of 0.55, pixel length of 18 µm, and plate scale of 4.58 (from Table 1).

#### b) FGS 2
- **Data Collection Period**: Also part of the 15-hour OOT simulation (60 s exposures).
   - **Time Range**: 15-hour simulation.
- **Wavelength(s)**: 1.1 µm
   - **Supporting Quote**: “FGS 2 (1.1 µm)” (Table 1)
- **Physical Observable**: Provides additional photometric data to monitor stellar variability and supplement fine guidance measurements.
- **Detector & Additional Comments**:
   - From Table 1, FGS 2 has an f-number of 39.5, QE of 0.55, pixel length of 18 µm, and plate scale of 2.86.

#### c) VisPhot
- **Data Collection Period**: Simulated with the same 15-hour OOT window and 60 s exposures.
   - **Time Range**: 15-hour simulation.
- **Wavelength(s)**: 0.5 µm
   - **Supporting Quote**: “VisPhot (0.5 µm)” (Table 1)
- **Physical Observable**: Captures visual band photometry primarily for monitoring the stellar output in the Wien tail of the SED, assisting in constraining the Rayleigh scattering slope and quantifying stellar noise.
- **Detector & Additional Comments**:
   - Detector attributes include a f-number of 6.36, QE of 0.55, pixel length of 15 µm, and a plate scale of 1.23 (Table 1).

### 4. SOHO VIRGO/SPM (Solar and Heliospheric Observatory – Variability Instrument) Red Channel
- **General Comments**:
   - This instrument is not part of the ARIEL mission but is used in the paper for validation purposes.
   - The VIRGO/SPM red channel provides real solar data against which the power spectral density (PSD) profiles from the stellar variability model are compared.
- **Supporting Quote**: “For comparison, a 300 hour and 60 s cadence sequence was chosen arbitrarily from publicly available VIRGO/SPM red channel data…” (p. 2)
  
#### Data Collection Period: Historical Observations from Year 2002
- **Time Range**: A 300-hour timeline from archival data, with exposures at a 60 s cadence.
   - **Supporting Quote**: “...a 300 hour and 60 s cadence sequence was chosen arbitrarily from publicly available VIRGO/SPM red channel data from the year 2002…” (p. 2)
- **Wavelength(s)**: 0.86 µm (with a bandwidth of 0.01 µm)
   - **Supporting Quote**: “...VIRGO/SPM red channel (0.86 µm)…” (p. 2)
- **Physical Observable**:
   - Measures the solar power spectral density (PSD), particularly capturing the oscillatory “p-mode” features, which are compared to the stellar variability model.
- **Detector & Additional Comments**:
   - Detailed detector specifications are not provided in the context for VIRGO/SPM; however, its data serve as a benchmark for validating the simulated PSD profiles from the stellar models.

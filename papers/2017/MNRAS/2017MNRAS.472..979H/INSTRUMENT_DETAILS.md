_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This study investigates the asteroseismic properties of ∼50 red giant stars in the open star cluster NGC 6819, focusing on testing the asteroseismic mass scale, evaluating mass loss, and exploring evidence for stars with non-standard evolution. The primary data source is long-term high-precision photometry from the NASA Kepler mission, specifically in long cadence mode. Kepler's time series photometric data (with an integration time of 29.4 minutes) spanning observing quarters Q0–Q16 (approx. four years), forms the observational basis of the analysis. These light curves are subjected to extensive preprocessing and then analyzed to extract oscillation frequencies, heights, and linewidths for hundreds of oscillation modes using advanced fitting techniques. Data from the Solar and Heliospheric Observatory (SoHO) VIRGO instrument and the ground-based BiSON (Birmingham Solar Oscillations Network) were also incorporated for calibration, providing solar reference values for asteroseismic scaling. Only data from these instruments directly contribute to the analysis and the derivation of scientific results.

## Instrumentation Details

---

### Kepler Observatory (NASA Kepler Spacecraft)
- **General Comments**:
  - Kepler's long-cadence (29.4 min) photometric observations were used as the fundamental data set for extracting the asteroseismic oscillation parameters of red giant stars in NGC 6819. The time series data covered observing quarters Q0–Q16, spanning from the mission's start until quarter 16, with the exception of periods when the relevant CCD module had failed. Data from multiple quarters were combined, with specific pre-processing applied to optimize the extraction of stellar flux, and directly analyzed to extract global and individual oscillation frequencies.
- **Supporting Quote**: 
  - "**Kepler observations are divided into ‘quarters’ of approximately 3 months duration due to the roll of the spacecraft required to keep the solar panels pointing towards the Sun. In this work we have used Kepler data taken in long cadence (29.4 min) from observing quarters Q0–Q16. NGC 6819 falls on Kepler CCD module 3, which failed after the first year of operation (Q4). This means that the time series of NGC 6819 is unfortunately missing data for 3 months every year, but have otherwise been near continuously observed.**"

#### Data Collection Period 1: Asteroseismic monitoring of NGC 6819 cluster red giants
- **Time Range**: Q0–Q16 (Kepler mission quarters, approximately 2009 – 2013 for each star except for three-month gaps each year after Q4 due to CCD module 3 failure)
  - **Supporting Quote**: 
    - "**In this work we have used Kepler data taken in long cadence (29.4 min) from observing quarters Q0–Q16. NGC 6819 falls on Kepler CCD module 3, which failed after the first year of operation (Q4). This means that the time series of NGC 6819 is unfortunately missing data for 3 months every year, but have otherwise been near continuously observed.**"
- **Wavelength(s)**: Broad optical bandpass (Kepler's response: 420–900 nm)
  - **Supporting Quote**: 
    - "**The Kepler data… are here dealing with a relatively crowded field, this procedure was not ideal for all targets and all timeseries were therefore visually inspected to decide if the new or original masks performed better for each target with respect to contamination and overall scatter.**" [The full Kepler bandpass: 420–900 nm is standard and only implied by 'Kepler data'; direct statement in the paper citing this is not present, but the reliance on Kepler long cadence data implies the use of its full broad optical photometric passband.]
- **Physical Observable**: Photometric time-series capturing luminosity variations due to stellar oscillations (solar-like p-modes and mixed modes)
  - **Supporting Quote**: 
    - "**We present an extensive peakbagging effort on Kepler data of ∼50 red giant stars in the open star cluster NGC 6819. By employing sophisticated pre-processing of the time series and Markov Chain Monte Carlo techniques we extracted individual frequencies, heights and linewidths for hundreds of oscillation modes.**"
- **Additional Comments**:
  - The data were preprocessed following specific procedures, including pixel mask optimization and filtering, to improve signal extraction and prepare for asteroseismic analysis.
  - "**The raw Kepler data was preprocessed using the procedures described in Handberg & Lund (2014). Normally this procedure involves using the Kepler target pixel data to automatically redefine the pixel masks used for extracting the stellar flux using simple aperture photometry. ... Since we are here dealing with a relatively crowded field, this procedure was not ideal for all targets and all timeseries were therefore visually inspected to decide if the new or original masks performed better for each target with respect to contamination and overall scatter.**"

---

### VIRGO Instrument on SoHO (Solar and Heliospheric Observatory)
- **General Comments**:
  - The VIRGO instrument’s 12-year green channel power spectrum was used to determine a solar reference value for the asteroseismic parameter νmax,⊙, critical for calibrating the asteroseismic scaling relations applied to the red giant data.
- **Supporting Quote**: 
  - "**To do this for νmax we fitted a 12 year power spectrum from the green channel of the VIRGO instrument aboard the SoHO spacecraft with the prescription given in §3. This yields a solar value for νmax,⊙= 3090 µHz (Eq. 4).**"

#### Data Collection Period 1: Derivation of solar reference asteroseismic parameters
- **Time Range**: 12 year power spectrum (exact years not stated in the quote; refers to full available VIRGO SoHO data coverage, encompassing much of the SOHO mission starting in 1996)
  - **Supporting Quote**: 
    - "**To do this for νmax we fitted a 12 year power spectrum from the green channel of the VIRGO instrument aboard the SoHO spacecraft with the prescription given in §3.**"
- **Wavelength(s)**: VIRGO green channel (500 nm)
  - **Supporting Quote**: 
    - "**…12 year power spectrum from the green channel of the VIRGO instrument aboard the SoHO spacecraft…**"
- **Physical Observable**: Solar oscillation (p-mode) photometric variations, for determining νmax,⊙ for scaling relations
  - **Supporting Quote**:
    - "**To do this for νmax we fitted a 12 year power spectrum from the green channel of the VIRGO instrument aboard the SoHO spacecraft…**"
- **Additional Comments**:
  - Matching the measurement protocol applied to the Kepler red giant stars to ensure calibration consistency.

---

### BiSON (Birmingham Solar Oscillations Network)
- **General Comments**:
  - BiSON-provided solar oscillation frequencies were employed to derive an accurate solar value for the large frequency separation, ∆ν⊙, ensuring directly comparable solar reference points for the asteroseismic scaling relations.
- **Supporting Quote**: 
  - "**We obtained our reference value for ∆ν⊙= 134.9 ± 0.06 µHz by fitting the the solar frequencies from BiSON (Broomhall et al. 2009), but using only ℓ= 0 modes in the 6 central orders lying closest to the estimated νmax to mimic the procedure we apply to the the giants later.**"

#### Data Collection Period 1: Solar reference ∆ν calculation for asteroseismic scaling
- **Time Range**: Frequencies from Broomhall et al. (2009) (BiSON data; specific years not re-stated in main text but data covers long-term BiSON operation)
  - **Supporting Quote**: 
    - "**We obtained our reference value for ∆ν⊙= 134.9 ± 0.06 µHz by fitting the the solar frequencies from BiSON (Broomhall et al. 2009), but using only ℓ= 0 modes in the 6 central orders lying closest to the estimated νmax to mimic the procedure we apply to the the giants later.**"
- **Wavelength(s)**: Doppler velocity (integrated sunlight; BiSON observes the solar K line at 7699 Å)
  - **Supporting Quote**:
    - "**We obtained our reference value for ∆ν⊙= 134.9 ± 0.06 µHz by fitting the the solar frequencies from BiSON (Broomhall et al. 2009)...**"
- **Physical Observable**: Solar oscillation radial velocity variations (global helioseismology)
  - **Supporting Quote**:
    - "**...by fitting the the solar frequencies from BiSON (Broomhall et al. 2009), but using only ℓ= 0 modes in the 6 central orders lying closest to the estimated νmax to mimic the procedure we apply to the the giants later.**"
- **Additional Comments**:
  - Accurate emulation of the asteroseismic parameter derivation protocol used for Kepler data, using BiSON's precise solar frequency measurements.

---

*No other instruments are directly used for data collection or analysis in this study.*

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  The paper investigates coronal electron density, temperature, and solar spectral irradiance (SSI) variations during solar cycles 23 and 24, using a physics-based model (CODET). The CODET model depends critically on full-disk magnetograms from SOHO/MDI and SDO/HMI for magnetic boundary conditions and is constrained using Solar EUV Experiment (SEE) data from the NASA TIMED mission. The research spans observations covering at least July 1, 1996, through solar cycles 23 and 24, with detailed data comparisons specifically indicated over the period from July 1, 2010 to July 31, 2012, and for several select days from 2001 to 2016. SSI observations at 19.3 nm and 21.1 nm from TIMED/SEE serve as the primary direct observational constraints, and data from SDO/EVE and SDO/AIA are used for detailed model comparisons. Direct magnetogram data are assimilated into the CODET model to reconstruct electron density and temperature profiles and maps, as well as SSI variability, over these multi-year intervals.

## Instrumentation Details

### Michelson Doppler Imager (MDI) on board SOHO
- **General Comments**:
  - MDI/SOHO full-disk magnetograms are assimilated into the CODET model's flux transport simulation to describe the photospheric magnetic field evolution and serve as input boundary conditions for the subsequent potential field source surface (PFSS) extrapolations.
- **Supporting Quote**:  
  "The flux transport model employed line-of-sight magnetic field data from SOHO/MDI and SDO/HMI full-disk magnetograms. These data are assimilated into the flux transport model to describe the dynamics of the solar photosphere."

#### Data Collection Period 1: Assimilation for Solar Cycle Boundary Conditions
- **Time Range**: July 1, 1996 – at least February 5, 2015 (coverage includes solar cycles 23 and 24)
  - **Supporting Quote**:  
    "The evolving surface-flux assimilation model is sampled every six hours from 1 July 1996."
- **Wavelength(s)**: Full-disk LOS magnetograms; [wavelength not specified, standard Ni I 6768 Å line for MDI, but not explicitly stated in the paper]
  - **Supporting Quote**:  
    "The flux transport model employed line-of-sight magnetic field data from SOHO/MDI and SDO/HMI full-disk magnetograms."
- **Physical Observable**: Photospheric longitudinal magnetic field used as model input
  - **Supporting Quote**:  
    "In this approach we could not employ directly the magnetic field strength density from MDI/SOHO (Scherrer et al., 1995) and HMI/SDO (Scherrer et al., 2012). ... The assimilation procedure is a straightforward mapping: after re-binning to a resolution of 8 arcsec, each magnetogram pixel is assumed to correspond to a single concentration at the corresponding latitude and longitude."
- **Additional Comments**:  
  Data are incorporated into the CODET boundary conditions after spatial re-binning; full-disk coverage up to 60° from disk center is used.

---

### Helioseismic and Magnetic Imager (HMI) on board SDO
- **General Comments**:
  - SDO/HMI full-disk line-of-sight magnetograms are used in tandem with MDI/SOHO as assimilated input for the CODET model's boundary conditions.
- **Supporting Quote**:  
  "The flux transport model employed line-of-sight magnetic field data from SOHO/MDI and SDO/HMI full-disk magnetograms."

#### Data Collection Period 1: Assimilation for Solar Cycle Boundary Conditions
- **Time Range**: May 2010 – at least February 5, 2015 (overlap with AIA/SDO epoch, extends through solar cycle 24)
  - **Supporting Quote**:  
    "The evolving surface-flux assimilation model is sampled every six hours from 1 July 1996. The assimilation model assumes that the magnetic field from SOHO/MDI and SDO/HMI is strictly vertical and the magnetograms are incorporated within 60° from disk center."
- **Wavelength(s)**: Full-disk LOS magnetograms; [wavelength not specified, standard Fe I 6173 Å line for HMI, but not explicitly stated in the paper]
  - **Supporting Quote**:  
    "The flux transport model employed line-of-sight magnetic field data from SOHO/MDI and SDO/HMI full-disk magnetograms."
- **Physical Observable**: Photospheric longitudinal magnetic field for model input
  - **Supporting Quote**:  
    "These data are then used as boundary conditions for a series of potential-field source-surface (PFSS) extrapolations."
- **Additional Comments**:  
  Assimilated data from both MDI and HMI ensure full-cycle coverage; transition between instruments is not described in detail, but both are used as direct model boundary inputs.

---

### Solar EUV Experiment (SEE) on board TIMED
- **General Comments**:
  - Disk-integrated Solar Spectral Irradiance (SSI) measurements from the TIMED/SEE instrument, especially at 19.3 nm and 21.1 nm, are used as the primary observational constraints to tune and validate the CODET model output. The data forms the basis for model fitting and chi-squared minimization.
- **Supporting Quote**:  
  "The Solar Spectral Irradiance data used in this work is the TIMED/SEE from the NASA TIMED mission’s Solar EUV Experiment (SEE) EUV Grating Spectrograph (EGS) merged with a model driven by The SORCE XUV Photometer System (XPS). The Model uses GOES XRS measurement data and CHIANTI spectral models as well."

#### Data Collection Period 1: SSI Observations during Solar Cycles 23 and 24
- **Time Range**: February 1, 2003 – October 1, 2016 (explicit comparison dates); broader: July 1, 1996 – at least October 1, 2016 (full model/data span covers both cycles)
  - **Supporting Quote**:  
    "In this case, it was chosen a period of ten days during the solar cycle 23 and 24 (Feb. 01 (2003), Oct. 01 (2003), Oct. 01 (2004), Oct.01 (2005), Oct. 01 (2007) Oct. 01 (2008), Oct. 01 (2009), Oct. 01 (2011), Oct. 01 (2014), Oct. 01 (2016) at 12 : 00UT)."
- **Wavelength(s)**: 19.3 nm and 21.1 nm (with mention of 17.1 nm, but main results for 19.3 nm, 21.1 nm)
  - **Supporting Quote**:  
    "The optimization algorithm was applied to fit two wavelengths 19.3nm and 21.1nm."
- **Physical Observable**: Full-disk solar spectral irradiance (SSI) at EUV wavelengths
  - **Supporting Quote**:  
    "The Solar Spectral Irradiance data used in this work is the TIMED/SEE from the NASA TIMED mission’s Solar EUV Experiment (SEE) EUV Grating Spectrograph (EGS) merged with a model driven by The SORCE XUV Photometer System (XPS)."
- **Additional Comments**:  
  Used as the reference dataset for constraining model output; daily data and select 12:00UT values explicitly compared.

#### Data Collection Period 2: Short-Term SSI Comparison Interval
- **Time Range**: July 1, 2010 – July 31, 2012 (detailed short-scale variability analysis)
  - **Supporting Quote**:  
    "The specific interval from Jul. 01 (2010) to Jul. 31 (2012) was selected to highlight the variations in short temporal scale."
- **Wavelength(s)**: 19.3 nm, 21.1 nm  
  - **Supporting Quote**:  
    "Figure 3: Solar Spectral Irradiance (SSI) using the CODET model (green line) and Solar Spectral Irradiance from TIMED/SEE (blue line), SDO/EVE (black line) and SDO/AIA (red line). (a) SSI at 19.3 nm and 21.1 nm during the solar cycle 23 and 24. (b) The best fit interval of Solar Spectral Irradiance (SSI) from CODET model from Jul. 01 (2010) to Jul. 31 (2012)."
- **Physical Observable**: Full-disk SSI at EUV wavelengths
  - **Supporting Quote**:  
    "The variability was recovered and follow the observational data trend from EVE and AIA datasets (Figure 3 (b))."
- **Additional Comments**:  
  This period is intensively analyzed for model-observation agreement.

---

### Atmospheric Imaging Assembly (AIA) on board SDO
- **General Comments**:
  - AIA full-disk solar images at EUV wavelengths (primarily 19.3 nm and 21.1 nm) are used for direct point-by-point and temporal comparison with modelled emission maps and SSI variability. AIA is used specifically as a benchmark to validate the spatial/emission output of the CODET model.
- **Supporting Quote**:  
  "Figure 3: Solar Spectral Irradiance (SSI) using the CODET model (green line) and Solar Spectral Irradiance from TIMED/SEE (blue line), SDO/EVE (black line) and SDO/AIA (red line)."

#### Data Collection Period 1: Spatial Comparison and SSI Validation
- **Time Range**: February 5, 2015 (maps); July 1, 2010 – July 31, 2012 (SSI comparison)
  - **Supporting Quote**:  
    "The emission maps show regions with higher values in intensity over the Active Regions (ARs) and lower values in emission in areas where the filaments between ARs and the non-polar coronal holes are located, shown as dark regions close - or inside - the activity belts. ... in Feb. 05 (2015) with AIA/SDO."
- **Wavelength(s)**: 19.3 nm, 21.1 nm  
  - **Supporting Quote**:  
    "The emission maps were obtained using two wavelengths: 19.3nm and 21.1nm in three different layers of the solar atmosphere R = 1.33, 1.42 and 1.60 R, in specific days: Dec. 15 (2001), Nov. 15 (2003) and Feb. 05 (2015) were explored. ... in Feb. 05 (2015) with AIA/SDO."
- **Physical Observable**: EUV emission intensity and spatial distribution
  - **Supporting Quote**:  
    "The emission maps show regions with higher values in intensity over the Active Regions (ARs) and lower values in emission in areas where the filaments between ARs and the non-polar coronal holes are located..."
- **Additional Comments**:  
  AIA images are directly used for model validation on specific days for emission map checks.

#### Data Collection Period 2: SSI and Time-Series Analysis
- **Time Range**: July 1, 2010 – July 31, 2012
  - **Supporting Quote**:  
    "Figure 3: Solar Spectral Irradiance (SSI) using the CODET model (green line) and Solar Spectral Irradiance from TIMED/SEE (blue line), SDO/EVE (black line) and SDO/AIA (red line). (a) SSI at 19.3 nm and 21.1 nm during the solar cycle 23 and 24. (b) The best fit interval of Solar Spectral Irradiance (SSI) from CODET model from Jul. 01 (2010) to Jul. 31 (2012)."
- **Wavelength(s)**: 19.3 nm, 21.1 nm
  - **Supporting Quote**:  
    "The scatter plots were obtained in each case and the chi-squared test (χ​2​) was calculated. The chi-squared test was obtained for EVE/SDO (χ​2​ = 0.0745 at 19.3 nm and χ​2 = 0.1534 at 21.5 nm) and AIA/SDO (χ​2 = 0.8131 at 19.3 nm and χ​2 = 0.2994 at 21.5 nm) data to review the consistency of the modelled values in comparison with observed data."
- **Physical Observable**: EUV SSI as measured by full-disk imaging photometry
  - **Supporting Quote**:  
    "The variability was recovered and follow the observational data trend from EVE and AIA datasets (Figure 3 (b))."
- **Additional Comments**:  
  AIA/SDO data serve as a standard for comparison with both CODET output and other instruments.

---

### Extreme Ultraviolet Variability Experiment (EVE) on board SDO
- **General Comments**:
  - SDO/EVE EUV spectral irradiance measurements are used for detailed model/observation comparisons, chi-squared statistics, and trend analysis for the 19.3 nm and 21.1 nm lines.
- **Supporting Quote**:  
  "The scatter plots were obtained in each case and the chi-squared test (χ​2​) was calculated. The chi-squared test was obtained for EVE/SDO (χ​2 ​= 0.0745 at 19.3 nm and χ​2 = 0.1534 at 21.5 nm) and AIA/SDO (χ​2 = 0.8131 at 19.3 nm and χ​2 = 0.2994 at 21.5 nm) data to review the consistency of the modelled values in comparison with observed data."

#### Data Collection Period 1: SSI and Time-Series Validation
- **Time Range**: July 1, 2010 – July 31, 2012 (explicit); also likely includes entire EVE operational epoch overlapping with SDO launch onwards
  - **Supporting Quote**:  
    "The specific interval from Jul. 01 (2010) to Jul. 31 (2012) was selected to highlight the variations in short temporal scale. The variability was recovered and follow the observational data trend from EVE and AIA datasets (Figure 3 (b))."
- **Wavelength(s)**: 19.3 nm, 21.1 nm
  - **Supporting Quote**:  
    "The scatter plots were obtained in each case and the chi-squared test (χ​2​) was calculated. The chi-squared test was obtained for EVE/SDO (χ​2​ = 0.0745 at 19.3 nm and χ​2 = 0.1534 at 21.5 nm)..."
- **Physical Observable**: Solar spectral irradiance (SSI) at EUV wavelengths
  - **Supporting Quote**:  
    "the Solar Spectral Irradiance from TIMED/SEE (blue line), SDO/EVE (black line) and SDO/AIA (red line). (a) SSI at 19.3 nm and 21.1 nm during the solar cycle 23 and 24. (b) The best fit interval of Solar Spectral Irradiance (SSI) from CODET model from Jul. 01 (2010) to Jul. 31 (2012)."
- **Additional Comments**:  
  Used in direct quantitative comparisons to CODET output, especially for high-cadence variability.

---

### Extreme ultraviolet Imaging Telescope (EIT) on board SOHO
- **General Comments**:
  - EIT/SOHO images at 19.5 nm (Fe XII) are used for qualitative comparison/validation of emission structures, particularly for the days Dec. 15, 2001 and Nov. 15, 2003.
- **Supporting Quote**:  
  "The emission maps in both wavelengths are correlated to the observational data: in Dec. 15 (2001) and Nov. 15 (2003) with EIT/SOHO; in Feb. 05 (2015) with AIA/SDO."

#### Data Collection Period 1: Emission Map Comparison
- **Time Range**: December 15, 2001; November 15, 2003
  - **Supporting Quote**:  
    "The emission maps in both wavelengths are correlated to the observational data: in Dec. 15 (2001) and Nov. 15 (2003) with EIT/SOHO; in Feb. 05 (2015) with AIA/SDO."
- **Wavelength(s)**: 19.5 nm 
  - **Supporting Quote**:  
    "This is corroborated by visual inspection of the observed images from EIT/SOHO in 19.5nm and AIA/SDO in 19.3nm and 21.1nm."
- **Physical Observable**: EUV image intensity, active region and coronal hole spatial structure
  - **Supporting Quote**:  
    "The ARs and non-polar CHs are reconstructed adequately. Non-polar CHs and regions between ARs that may harbour filaments are also in agreement with observations."
- **Additional Comments**:  
  Primarily used for model spatial validation on specific dates.

---

**No other instruments are described as directly used for data collection or analysis in this paper.**

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This study presents the EMPIRE (EMPirical Irradiance REconstruction) model for reconstructing total solar irradiance (TSI) and spectral solar irradiance (SSI) across 115 to 170,000 nm from 14 February 1947 to 30 September 2016 at daily cadence. The core methodology empirically relates indices of solar activity—the Mg II index (from the IUP composite) and the Photometric Sunspot Index (PSI, from Balmaceda et al., 2009)—to irradiance measurements. Critically, satellite observations of SSI from key missions and instruments—including UARS/SOLSTICE, UARS/SUSIM, SORCE/SOLSTICE, and SORCE/SIM—form the basis for calibrating UV SSI variability in the model. The model’s TSI calibration relies on data from the SORCE/TIM instrument. All instrument data are directly analyzed for regression fitting, validation, or model construction within clearly specified time periods tied to solar cycles and instrument lifetimes. Physical quantities observed include irradiance over a broad UV-visible-IR range, and regression is performed at well-documented wavelength intervals with explicit attention to time, wavelength, and instrumental uncertainty.

## Instrumentation Details

### SORCE/SIM (Spectral Irradiance Monitor) on board SORCE
- **General Comments**:  
  SORCE/SIM data are used directly in the regression analysis to determine UV, visible, and infrared SSI variability, and for validation of SSI reconstructions produced by the EMPIRE model, specifically between 2003 and 2015.
- **Supporting Quote**:  
  "We made use of the SSI records from the SUSIM and SOLSTICE instruments onboard the UARS mission, and SIM and SOLSTICE onboard SORCE, described in Table 1."

#### Data Collection Period 1: UV, visible and IR SSI variability calibration and validation
- **Time Range**: 2003-05-14 to 2015-10-31
  - **Supporting Quote**:  
    "SIM | 2003.05.14 to 2015.10.31 [year.month.day]"
- **Wavelength(s)**: 310–2416 nm
  - **Supporting Quote**:  
    "SIM | ... Wavelength range | 310 to 2416 [nm]"
- **Physical Observable**:  
  Measurement of spectral solar irradiance (SSI) in the visible and infrared; direct analysis of SSI variability for model calibration and rotational variability validation.
  - **Supporting Quote**:  
    "We made use of the SSI records from the SUSIM and SOLSTICE instruments onboard the UARS mission, and SIM and SOLSTICE onboard SORCE, described in Table 1."
- **Additional Comments**:  
  "Rotational variability in the 1600 to 2416 nm segment of the record, provided by the electrical substitution radiometer in the instrument, is completely hidden by measurement uncertainty (Fig. 10d)."

#### Data Collection Period 2: Model/Observation Comparison for SSI trend analysis
- **Time Range**: 2003-06 to 2008-11 (comparison for solar cycle minimum)
  - **Supporting Quote**:  
    "We depict the difference between the average spectrum from June 2003 to August 2003 and the average spectrum from November 2008 to January 2009."
- **Wavelength(s)**: 420–1600 nm (visible) and 1600–2416 nm (IR)
  - **Supporting Quote**:  
    "...the horizontal dashed lines denote the zero level and the vertical dashed lines 420 and 1600 nm, drawn to aid the discussion (Sect. 4.2). The SSI difference between 700 and 3000 nm is magnified by a factor of ten for visibility."
- **Physical Observable**:  
  Changes in SSI across visible and IR for testing consistency and identifying possible instrumental artifacts.
  - **Supporting Quote**:  
    "The rise in 420 to 1600 nm SSI between 2003 and 2008 recorded by SIM is not reproduced in EMPIRE (Fig. 9a) or indeed any other model reported in the literature."

---

### SORCE/SOLSTICE (SOLar-STellar Irradiance Comparison Experiment) on board SORCE
- **General Comments**:  
  SORCE/SOLSTICE UV measurements are directly regressed against proxy indices to calibrate EMPIRE's UV SSI reconstruction between 2003 and 2015.
- **Supporting Quote**:  
  "We made use of the SSI records from the SUSIM and SOLSTICE instruments onboard the UARS mission, and SIM and SOLSTICE onboard SORCE, described in Table 1."

#### Data Collection Period 1: UV SSI variability calibration
- **Time Range**: 2003-04-14 to 2015-05-02
  - **Supporting Quote**:  
    "SORCE/SOLSTICE | 2003.04.14 to 2015.05.02 [year.month.day]"
- **Wavelength(s)**: 115–310 nm
  - **Supporting Quote**:  
    "SORCE/SOLSTICE | ... Wavelength range | 115 to 310 [nm]"
- **Physical Observable**:  
  Measurement of spectral solar irradiance (UV SSI); used for regression with Mg II and PSI proxies to obtain UV SSI variability in the EMPIRE model.
  - **Supporting Quote**:  
    "For the 115 to 2400 nm segment of the NRLSSI2 reconstruction, the scaling is similarly determined from SORCE/SOLSTICE 115 to 309 nm and SIM 309 to 2400 nm SSI [Coddington et al., 2016]. The authors multiplied the scaling coefficients so derived by a set of corrective factors on the assumption that the relationship between the proxy time series and SSI differ at rotational and solar cycle timescales."

---

### UARS/SUSIM (Solar Ultraviolet Spectral Irradiance Monitor) on board UARS
- **General Comments**:  
  The UARS/SUSIM instrument provides UV SSI observations directly used for regression calibration of EMPIRE’s model in the 1991–2001 time frame. SUSIM is also used for model validation and independent empirical reconstructions.
- **Supporting Quote**:  
  "We made use of the SSI records from the SUSIM and SOLSTICE instruments onboard the UARS mission, and SIM and SOLSTICE onboard SORCE, described in Table 1."

#### Data Collection Period 1: UV SSI variability calibration and reference for independent reconstructions
- **Time Range**: 1991-10-12 to 2001-09-24
  - **Supporting Quote**:  
    "UARS/SUSIM | 1991.10.12 to 2001.09.24 [year.month.day]"
- **Wavelength(s)**: 115–411 nm
  - **Supporting Quote**:  
    "UARS/SUSIM | ... Wavelength range | 115 to 411 [nm]"
- **Physical Observable**:  
  Direct UV SSI measurements, employed for regression with proxy time series to calibrate UV component of EMPIRE. Used as the basis for "Mea11" model.
  - **Supporting Quote**:  
    "Mea11 exploits the fact that the SUSIM record is sufficiently stable to exhibit solar cycle variability over its wavelength range (c.f. Sect. 4.1.1), allowing proxy modelling via the direct fitting of proxies of facular brightening and sunspot darkening to the record."
- **Additional Comments**:  
  "In SATIRE-S, solar irradiance is reconstructed from the same calculated intensity spectra of solar surface features by Unruh et al. [1999] described in Sect. 2.4.2. Taking spatially-resolved full-disc intensity images and magnetograms, the solar disc is segmented into quiet Sun, faculae and sunspots. SSI is derived by assigning the appropriate intensity spectrum to each disc position according to the segmentation and the distance from disc centre, and summing the result over the solar disc."

---

### UARS/SOLSTICE on board UARS
- **General Comments**:  
  UARS/SOLSTICE data are used alongside SUSIM for regression with Mg II and PSI proxies to determine EMPIRE's UV SSI variability, covering the same solar cycles as UARS/SUSIM.
- **Supporting Quote**:  
  "We made use of the SSI records from the SUSIM and SOLSTICE instruments onboard the UARS mission, and SIM and SOLSTICE onboard SORCE, described in Table 1."

#### Data Collection Period 1: UV SSI variability calibration
- **Time Range**: 1991-10-17 to 2001-09-24
  - **Supporting Quote**:  
    "UARS/SOLSTICE | 1991.10.17 to 2001.09.24 [year.month.day]"
- **Wavelength(s)**: 119–420 nm
  - **Supporting Quote**:  
    "UARS/SOLSTICE | ... Wavelength range | 119 to 420 [nm]"
- **Physical Observable**:  
  Spectral solar irradiance observations in the UV, used to perform regression analyses for extracting UV SSI variability at rotational and solar-cycle timescales.
  - **Supporting Quote**:  
    "For the wavelength range of 115 to 420 nm, we determined kF and kS from the regression of the rotational variability in the proxy time series to that in SSI observations, as typical of proxy models."
- **Additional Comments**:  
  "The NRLSSI1 reproduction (green dashed line, Fig. 8a) is given by the OLS analysis of UARS/SOLSTICE SSI from Sect. 2.4.1."

---

### SORCE/TIM (Total Irradiance Monitor) on board SORCE
- **General Comments**:  
  The SORCE/TIM TSI data are used as the reference observational record for the regression fitting of EMPIRE’s TSI model component and are the target for setting EMPIRE’s absolute TSI calibration.
- **Supporting Quote**:  
  "The coefficients of the TSI model (K terms in Equation 1) were fixed by the OLS regression of the proxy time series to the SORCE/TIM TSI record [version 17, Kopp et al., 2005]."

#### Data Collection Period 1: Calibration/Validation of TSI variability
- **Time Range**: 2003-02-25 to (data available up to at least) 2016-10-31
  - **Supporting Quote**:  
    "SORCE/TIM | 2003.02.25 to 2016.10.31 [year.month.day]"
- **Wavelength(s)**: Total Solar Irradiance (broadband, integrated over all wavelengths)
  - **Supporting Quote**:  
    "TSI is the wavelength-integrated and SSI the per unit wavelength Earthward solar radiative flux (i.e., energy per unit time and area) at the mean Sun-Earth separation."
- **Physical Observable**:  
  Total Solar Irradiance (TSI) used for regression fitting and absolute reference for EMPIRE TSI reconstruction.
  - **Supporting Quote**:  
    "The coefficients of the TSI model (K terms in Equation 1) were fixed by the OLS regression of the proxy time series to the SORCE/TIM TSI record [version 17, Kopp et al., 2005]. We constrained the regression such that the reconstruction matches the TIM record at the December 2008 solar cycle minimum."

---

### Reference Solar Spectra: WHI (Whole Heliosphere Interval) Reference Spectrum
- **General Comments**:  
  The WHI quiet Sun reference spectrum is used as the absolute reference for EMPIRE’s SSI (not as an active data collection instrument, but as an externally generated composite used for scaling model outputs).
- **Supporting Quote**:  
  "The 115 to 2400 nm segment of the reference spectrum is given by the Whole Heliosphere Interval or WHI [Thompson et al., 2011] quiet Sun reference spectrum [Woods et al., 2009], essentially the mean SSI in the period of 10 to 16 April 2008."
  
#### Data Collection Period 1: Scaling/calibration of model output
- **Time Range**: April 10, 2008 to April 16, 2008 (mean spectrum reference period)
  - **Supporting Quote**:  
    "The 115 to 2400 nm segment of the reference spectrum is given by the Whole Heliosphere Interval or WHI [Thompson et al., 2011] quiet Sun reference spectrum [Woods et al., 2009], essentially the mean SSI in the period of 10 to 16 April 2008."
- **Wavelength(s)**: 115–2400 nm
  - **Supporting Quote**:  
    "The 115 to 2400 nm segment of the reference spectrum is given by the Whole Heliosphere Interval or WHI [Thompson et al., 2011] quiet Sun reference spectrum [Woods et al., 2009]..."
- **Physical Observable**:  
  Solar irradiance spectral reference (used for absolute scaling, not direct model input).
  - **Supporting Quote**:  
    "Reconstructed SSI variability is set onto a reference spectrum to yield SSI. The 115 to 2400 nm segment of the reference spectrum is given by the Whole Heliosphere Interval or WHI [Thompson et al., 2011] quiet Sun reference spectrum [Woods et al., 2009], essentially the mean SSI in the period of 10 to 16 April 2008."

---

## End of Form

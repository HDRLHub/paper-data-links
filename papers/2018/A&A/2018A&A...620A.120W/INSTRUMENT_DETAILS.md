_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper reconstructs the solar total and spectral irradiance (TSI/SSI) over the last 9000 years, combining physics-based models with direct and proxy data. Its research objective is to provide the most up-to-date, physically consistent reconstruction of solar irradiance over the Holocene, essential for studies of solar influence on climate. The study utilizes actual data from cosmogenic isotope records (^14C and ^10Be) extracted from terrestrial archives (tree rings and ice cores) and, for the recent several centuries, the directly observed sunspot number record. While extensive reference is made to previous models, only select satellite-era measurements are used directly to calibrate the physics-based SATIRE model and to validate reconstructions from 1978 to present, including daily TSI measurements and solar UV data. Precise observation dates are specified for the input datasets (e.g., TSI since 1978, sunspot number since 1610, isotope data covering 6755 BC–1895 AD). All research findings are directly built on data from these instruments and observatories, making them foundational to the presented results.

## Instrumentation Details

### [Sunspot Observations] from multiple ground-based observatories (as compiled in the International Sunspot Number Version 2.0, WDC-SILSO)
- **General Comments**:
  - Used as the primary observational input to reconstruct solar magnetic field evolution and TSI/SSI from the Maunder minimum (~1639) to present, and as the calibration and validation baseline for the SATIRE-T model.
- **Supporting Quote**: 
  - "The longest record of direct solar observations is the sunspot number that extends back to the Maunder minimum, although with progressively degrading quality (see Sect. 2.2.1). SATIRE-T employs the sunspot numbers to first reconstruct the evolution of the solar photospheric magnetic fields through a set of ordinary differential equations (Solanki et al. 2000, 2002; Vieira & Solanki 2010), which is then used as input to the reconstruction of the solar irradiance (Balmaceda et al. 2007; Krivova et al. 2007, 2010)."
  
#### Data Collection Period 1: Direct sunspot number data (WDC-SILSO SNv2)
- **Time Range**: 1700 AD – present; extended using reconstructions to 1639 AD
  - **Supporting Quote**: "Here we therefore use the updated International (Zurich) sunspot number series (SN version 2.0, SNv2 hereafter) by WDC-SILSO1 as our input sunspot number. However, this SN series only extends back to 1700 which is the end phase of the Maunder minimum. Furthermore, this data set is problematic during the early eighteenth century due to the large amount of missing sunspot number data and the difficulty in calibrating between different observatories. Vaquero et al. (2015) have accounted for this issue and revised the sunspot number during this period. We therefore replace the sunspot number between the years 1639 and 1715 with the one reconstructed by Vaquero et al. (2015)."
- **Wavelength(s)**: Not applicable (proxy for solar photospheric activity)
- **Physical Observable**: Sunspot number; fractional disc area coverage by sunspots
  - **Supporting Quote**: "The calculated magnetic flux for each component as a function of time is converted to filling factors entering Eq. (1) as follows. First, the fractional disc area coverage by sunspots is obtained directly from the measured sunspot areas whenever these are available (Balmaceda et al. 2005, 2009; Yeo et al. 2017)... For the period prior to Greenwich observations (i.e. before 1874) when the area record is not available, we extrapolate this latter coverage using sunspot numbers."

### [PMOD Total Solar Irradiance Composite] (multiple space-based radiometers: Nimbus-7/ERB, SMM/ACRIM1, ERBS/ERBE, UARS/ACRIM2, SOHO/VIRGO etc., as compiled by PMOD/WRC)
- **General Comments**:
  - Employed for calibration and validation of the reconstructed TSI from 1978 onwards, serving as the key satellite TSI measurement record.
- **Supporting Quote**:
  - "The observations used to compare with and to fix the free parameters are: (1) PMOD TSI composite since 1978 (Fröhlich 2006, 2009)3..."

#### Data Collection Period 1: Space-based TSI measurements (PMOD composite)
- **Time Range**: November 1978 – 2015
  - **Supporting Quote**: "Figure 3a shows the TSI reconstruction (red dots) from the sunspot number (SNv2) overplotted on the PMOD composite (green lines) over the period 1978 – 2015."
- **Wavelength(s)**: 115 – 160,000 nm (broadband total solar output)
  - **Supporting Quote**: "Finally, TSI is calculated as an integral of SSI over the entire spectral range 115 – 160 000 nm."
- **Physical Observable**: Total solar irradiance (TSI) at 1 AU
  - **Supporting Quote**: "The total solar irradiance (TSI), which is dominated by radiation in the visible and infrared (IR) bands of the spectrum, is the spectrally integrated energy flux per unit area normalised to 1 AU..."

### [UARS/SUSIM (Solar Ultraviolet Spectral Irradiance Monitor) on UARS]
- **General Comments**:
  - Used as the empirical reference for solar UV irradiance in the 1990s, in comparison with SATIRE-S/T model output, and for empirical corrections in the SATIRE irradiance reconstruction (especially 180–300 nm).
- **Supporting Quote**: 
  - "Krivova et al. (2006) and Yeo et al. (2014) have shown that the SATIRE spectra need a correction below 300 nm. Following Yeo et al. (2014), between 180 and 300 nm we introduce an offset in the absolute values to match the whole hemispheric interval (WHI) reference solar spectrum (Woods et al. 2009), while in the range 115 – 180 nm, the variability is rescaled with empirical factors derived using the SORCE/SOLSTICE measurements (Snow et al. 2005)."

#### Data Collection Period 1: UARS/SUSIM solar UV measurements
- **Time Range**: October 1991 – August 2002
  - **Supporting Quote**: "The reference UV time series here is the reconstruction with SATIRE-S model which has previously been shown to be in close agreement (R2c=0.975) with the UARS/SUSIM record (blue line in Fig. 4a, Brueckner et al. 1993; Floyd et al. 2003)."
- **Wavelength(s)**: UV, specifically 115–400 nm, and in some comparisons 220–240 nm
  - **Supporting Quote**: "Figure 4a. The UV irradiance integrated over the range 220 – 240 nm as reconstructed here (red), modelled with SATIRE-S (black; reference data set from Yeo et al. (2014)) and measured by UARS/SUSIM (blue, Floyd et al. (2003))."
- **Physical Observable**: Solar spectral (UV) irradiance
  - **Supporting Quote**: "Solar spectral irradiance (SSI) spectral range, which includes ultraviolet (UV), is the flux per unit wavelength."

### [SORCE/SOLSTICE (Solar Radiation and Climate Experiment/Solar-Stellar Irradiance Comparison Experiment) Satellite Instrument]
- **General Comments**:
  - Provides observed solar UV spectral irradiance for empirical correction (180–300 nm: offset; 115–180 nm: variability rescaling) in the SATIRE model reconstruction.
- **Supporting Quote**: 
  - "in the range 115–180 nm, the variability is rescaled with empirical factors derived using the SORCE/SOLSTICE measurements (Snow et al. 2005)."

#### Data Collection Period 1: SORCE/SOLSTICE UV observations
- **Time Range**: May 2003 – 2015
  - **Supporting Quote**: "in the range 115–180 nm, the variability is rescaled with empirical factors derived using the SORCE/SOLSTICE measurements (Snow et al. 2005)."
- **Wavelength(s)**: 115–180 nm
  - **Supporting Quote**: "in the range 115–180 nm, the variability is rescaled with empirical factors derived using the SORCE/SOLSTICE measurements (Snow et al. 2005)."
- **Physical Observable**: Solar UV spectral irradiance
  - **Supporting Quote**: "Solar spectral irradiance (SSI) spectral range, which includes ultraviolet (UV), is the flux per unit wavelength."

### [Wilcox Solar Observatory (WSO), National Solar Observatory (NSO/KP), Mount Wilson Observatory (MWO)] Photospheric Magnetic Flux Data
- **General Comments**:
  - Used for calibration and validation of reconstructed total magnetic flux (TMF) at the Sun via Carrington-rotation-averaged full-disk magnetograms.
- **Supporting Quote**:
  - "The observations used to compare with and to fix the free parameters are: ... (2) ground-based total magnetic flux (TMF) measurements by Wilcox Solar Observatory (WSO), National Solar Observatory(NSO) and Mount Wilson Observatory (MWO) covering cycles 21 – 23 (Arge et al. 2002; Wang et al. 2005);"

#### Data Collection Period 1: Observed total photospheric magnetic flux
- **Time Range**: WSO: May 1976 – present; NSO/KP: February 1974 – September 2003; MWO: May 1967 – December 2012
  - **Supporting Quote**: "The reconstructed total magnetic flux (TMF) is compared with the observations in Fig. 2. Panel (a) shows the TMF over cycles 21–23. Data from different observatories are represented by different symbols: WSO (squares), KP NSO (diamonds), and MWO (triangles). Each individual symbol represents the total photospheric magnetic flux for a given Carrington rotation."
- **Wavelength(s)**: Measurements of the solar photospheric magnetic field (Fe I 525.0 nm for WSO, 868.8 nm for NSO/KP)
- **Physical Observable**: Total photospheric magnetic flux
  - **Supporting Quote**: "Panel (a) shows the TMF over cycles 21 – 23. Data from different observatories are represented by different symbols: WSO (squares), KP NSO (diamonds), and MWO (triangles). Each individual symbol represents the total photospheric magnetic flux for a given Carrington rotation."

### [Open Magnetic Flux reconstruction from aa geomagnetic index]
- **General Comments**:
  - Used for calibration and validation of the reconstructed open magnetic flux (OMF) from 1845–2010.
- **Supporting Quote**:
  - "The observations used to compare with and to fix the free parameters are: ... (3) OMF over the period 1845–2010 reconstructed by Lockwood et al. (2014a) from the aa-index;"

#### Data Collection Period 1: aa-index based OMF reconstruction
- **Time Range**: 1845 – 2010
  - **Supporting Quote**: "Panel (b) compares the modelled OMF (solid line, yearly averages) with the empirical reconstruction by Lockwood et al. (2014a, dashed line) based on the aa-index between 1850 and 2010."
- **Wavelength(s)**: Not applicable (magnetic field data)
- **Physical Observable**: Open solar magnetic flux (as reconstructed from geomagnetic data)
  - **Supporting Quote**: "The modelled open magnetic flux also agrees well with the independent reconstruction based on the aa-index over the last 150 years (Lockwood et al. 2014b)."

### [Cosmogenic isotope records: ^14C from tree rings, ^10Be from ice cores (multiple Antarctic and Greenland sites)]
- **General Comments**:
  - Serve as the main data sources for reconstructing solar activity prior to ~1610. Decadally averaged isotope records, processed with physical transport/production/geomagnetic models, are used to reconstruct sunspot number and thus irradiance.
- **Supporting Quote**:
  - "In this study, three series of decadal SN reconstructed from cosmogenic isotopes are used, as described below. The first, ^14C-based SN series ('U16-14', Usoskin et al. 2016a) is an extended and updated version of a series taken from Usoskin et al. (2014). It is calculated from an updated ^14C production rate record INTCAL09 (Reimer et al. 2009) and a new geomagnetic model (GMAG.9k) reconstructed by Usoskin et al. (2016a). Based on the geomagnetic model GMAG.9k, Usoskin et al. (2016a) also reconstructed a SN series ('U16-10Be') from the longest ^10Be data set from the Greenland Ice Core Project (GRIP; Yiou et al. 1997; Muscheler et al. 2004; Vonmoos et al. 2006)... To account for these issues, Wu et al. (2018) combined six ^10Be series with the global ^14C record into a consistent multi-isotope series, 'Wu18', the third series used in this study. This composite takes care of the temporal discrepancies between the seven individual series and minimises the difference between the modelled solar activity and the measured cosmogenic isotope data..."


#### Data Collection Period 1: Global ^14C and ^10Be records from tree rings and ice cores
- **Time Range**: 6755 BC – 1895 AD (U16-14C, Wu18 composite); 6755 BC – 1645 AD (U16-10Be)
  - **Supporting Quote**: "In this study, three series of decadal SN reconstructed from cosmogenic isotopes are used, as described below. The first, ^14C-based SN series ('U16-14', Usoskin et al. 2016a) is an extended and updated version of a series taken from Usoskin et al. (2014). It is calculated from an updated ^14C production rate record INTCAL09 (Reimer et al. 2009) and a new geomagnetic model (GMAG.9k) reconstructed by Usoskin et al. (2016a). Based on the geomagnetic model GMAG.9k, Usoskin et al. (2016a) also reconstructed a SN series ('U16-10Be') from the longest ^10Be data set from the Greenland Ice Core Project (GRIP; Yiou et al. 1997; Muscheler et al. 2004; Vonmoos et al. 2006)... To account for these issues, Wu et al. (2018) combined six ^10Be series with the global ^14C record into a consistent multi-isotope series, 'Wu18', the third series used in this study."
- **Wavelength(s)**: Not applicable (isotope concentration; indirect solar proxies)
- **Physical Observable**: Atmospheric ^14C concentration in tree rings; ^10Be concentration in polar ice
  - **Supporting Quote**: "The cosmogenic radioisotopes ^14C and ^10Be are produced in the terrestrial atmosphere by galactic cosmic rays (GCRs). After entering the Earth’s atmosphere, GCRs collide with nuclei (mainly oxygen and nitrogen) and produce these radionuclides. Since the GCR flux is modulated by the heliospheric magnetic field, this allows a reconstruction of the solar magnetic activity at the time of the isotope production (Lal & Peters 1967)."

---

[Repeat sections for additional instruments/data if directly analyzed—none found from the provided text outside those above.]

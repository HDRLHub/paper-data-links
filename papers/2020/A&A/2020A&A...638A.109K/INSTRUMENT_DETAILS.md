_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper focuses on improving the classical potential field source surface (PFSS) model by allowing the source surface to be elliptical rather than strictly spherical. To achieve this, the authors developed a finite-difference numerical solver that computes the coronal magnetic field on a three-dimensional grid. They compare the new elliptical implementation with the classical spherical harmonic coefficient (SHC) method and illustrate differences through three-dimensional renderings and Carrington-like synoptic maps at various heliocentric heights. The study employs input data from synoptic magnetograms of the solar photosphere taken from instruments such as the Wilcox Solar Observatory and the Michelson Doppler Imager (MDI) onboard SOHO. In addition, the authors discuss prospects for validating and improving these magnetic field models with data from upcoming in situ missions, namely the Parker Solar Probe and Solar Orbiter, which are especially pertinent given the changing solar activity phases.

---

### 1. Wilcox Solar Observatory Synoptic Magnetograms
- **General Comments**:
  - This facility provides synoptic magnetograms of the solar photosphere. These magnetograms give the line-of-sight component of the photospheric magnetic field used as a lower boundary (Dirichlet condition) for the PFSS model.
  - The input data from the Wilcox Solar Observatory is used for testing purposes and for comparison with benchmark data products.
  
- **Supporting Quote**:
  - "As input data, we used synoptic magnetograms from the Wilcox Solar Observatory for testing purposes and comparisons with data products published by Hoeksema (2020)."  
  - From the Acknowledgements: "Wilcox Solar Observatory data used in this study was obtained via the web site http://wso.stanford.edu at 2019:10:31_09:49:01 PDT courtesy of J.T. Hoeksema."
  
#### Data Collection Period 1: Single-epoch Data Capture for Model Testing
- **Time Range**: Data obtained at "2019:10:31_09:49:01 PDT" (exact timestamp as provided by the website access)
  - **Supporting Quote**: "Wilcox Solar Observatory data used in this study was obtained via the web site http://wso.stanford.edu at 2019:10:31_09:49:01 PDT..."
- **Wavelength(s)**: Not explicitly stated (the observatory measures the photospheric magnetic field via line-of-sight observations).
  - **Supporting Quote**: (Implied by usage) "synoptic (line of sight) magnetograms" (Section 2.5).
- **Physical Observable**: Line-of-sight magnetic flux density in the photosphere.
  - **Supporting Quote**: "the magnetic field configuration is known and is supplied to the algorithms by synoptic (line of sight) magnetograms" (Section 2.5).
- **Additional Comments**: The Wilcox data provide a lower-resolution benchmark for the PFSS model evaluations.

---

### 2. Michelson Doppler Imager (MDI) onboard SOHO
- **General Comments**:
  - The MDI instrument on board the Solar and Heliospheric Observatory (SOHO) provides high-resolution synoptic magnetograms. These observations are used to generate more detailed maps of the photospheric magnetic field.
  - In this paper, the high-resolution synoptic maps from MDI are scaled and processed for grid testing and for producing detailed Carrington maps of the coronal magnetic field.
  
- **Supporting Quote**:
  - "For high-resolution grid tests and for the plots presented in this work we employed synoptic magnetograms from the Michelson Doppler Imager (MDI) on board the Solar and Heliospheric Observatory (SOHO) (Scherrer et al. 1995)."
  
#### Data Collection Period 1: Carrington Rotation 2066 in Early 2008
- **Time Range**: "Carrington rotation 2066 during the minimum between solar activity cycles 23 and 24 in early 2008"
  - **Supporting Quote**: "we chose Carrington rotation 2066 during the minimum between solar activity cycles 23 and 24 in early 2008 to illustrate the differences the model parameters incur."
- **Wavelength(s)**: Not explicitly stated; the MDI magnetograms are derived from observations in the visible spectrum designed to measure Doppler shifts and magnetic field strengths.
- **Physical Observable**: The line-of-sight magnetic field (photospheric magnetic flux density) is the primary observable.
  - **Supporting Quote**: "the photospheric magnetograms ... [are] used as the boundary condition" (Section 2.5).
- **Additional Comments**: The high-resolution data from MDI are processed (scaled to 87×175 pixels) and corrected for monopole offset and polar data gaps to improve the numerical modeling.

---

### 3. Parker Solar Probe (PSP)
- **General Comments**:
  - The Parker Solar Probe is cited as an in situ mission already collecting data relatively close to the solar corona.
  - Its observations are expected to provide crucial magnetic field and solar wind data near the computational domain of the PFSS model, thereby facilitating direct comparisons between the model predictions and actual measurements.
  
- **Supporting Quote**:
  - "The Parker Solar Probe (Fox et al. 2016) is already collecting data..."
  
#### Data Collection Period 1: Ongoing Data Collection in the 2020s
- **Time Range**: While a precise start and end time are not provided, the context implies that PSP data are being gathered currently (with expectations during the 2020s).
  - **Supporting Quote**: "Data from both Solar Orbiter as well as the Parker Solar Probe are expected to be available during the 2020s."
- **Wavelength(s)**: Not applicable; the Parker Solar Probe primarily measures in situ magnetic field vectors, plasma properties, and particle distributions.
- **Physical Observable**: In situ magnetic field measurements and solar wind properties.
- **Additional Comments**: PSP’s proximity to the Sun (aiming for a perihelion heliocentric distance of less than 10 R⊙) is expected to reduce uncertainties in mapping coronal model predictions to spacecraft observations.

---

### 4. Solar Orbiter
- **General Comments**:
  - Solar Orbiter is another recent mission mentioned that will provide in situ measurements of the heliospheric magnetic field and plasma parameters.
  - Its unique orbit with a higher ecliptic inclination will allow it to observe solar regions, particularly near the poles, that are difficult to monitor from Earth.
  
- **Supporting Quote**:
  - "Solar Orbiter (Müller et al. 2013) was launched in February 2020."
  
#### Data Collection Period 1: From Launch in February 2020 Onwards
- **Time Range**: Operational since its launch in February 2020 with data collection continuing into the 2020s.
  - **Supporting Quote**: "Solar Orbiter (Müller et al. 2013) was launched in February 2020." and "Data from both Solar Orbiter as well as the Parker Solar Probe are expected to be available during the 2020s."
- **Wavelength(s)**: Not specified; like PSP, Solar Orbiter is designed primarily for in situ magnetic and plasma measurements.
- **Physical Observable**: In situ measurements of the heliospheric magnetic field and associated plasma characteristics.
- **Additional Comments**: Solar Orbiter’s high ecliptic inclination is expected to provide new insights into solar polar magnetic field configurations, improving the validation of PFSS-based models.

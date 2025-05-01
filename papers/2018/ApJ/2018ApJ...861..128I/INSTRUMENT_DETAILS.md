_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This study uses data from multiple space‐based instruments and databases to forecast whether solar flares will occur with associated coronal mass ejections (CMEs) and solar energetic particles (SEPs). The authors employ machine learning techniques—support vector machines (SVMs) and multilayer perceptrons (MLPs)—using observational data from DONKI (a NASA space weather database), GOES (which provides X‐ray flux measurements), and the SHARPs data product derived from the SDO/HMI instrument. The study period spans from 01 January 2010 to 31 January 2018. The paper also reviews previous work using instruments such as SOHO/MDI and includes references to satellite instrumentation affected during past extreme events (e.g., MIDORI-II on ADEOS-2 and star trackers).

---

### 1. DONKI (Space Weather Database Of Notiﬁcation, Knowledge, Information) – NASA Space Weather Research Center
- **General Comments**:
   - DONKI is a database that provides detailed information on solar eruptive events. It includes flare data with their classes, source active region (AR) numbers, and the start, peak, and end times of flares. It also supplies CME information—such as speeds, types, and start times—used in this study to classify solar events.
- **Supporting Quote**: 
   - "To predict which solar eruptive phenomena will be generated from an AR, [...] we use data from the Space Weather Database Of Notiﬁcation, Knowledge, Information (DONKI) of NASA Space Weather Research Center, for a period spanning from 01 January 2010 to 31 January 2018."
- **Data Collection Period 1: Full Study Duration**
   - **Time Range**: 01 January 2010 – 31 January 2018
      - **Supporting Quote**: 
         - "Using data from the DONKI [...] for a period spanning from 01 January 2010 to 31 January 2018."
   - **Wavelength(s)**: Not applicable; DONKI provides event metadata rather than direct spectral measurements.
      - **Supporting Quote**: (Not provided in the text)
   - **Physical Observable**: Event timings, flare classes, and CME parameters such as speeds and types.
      - **Supporting Quote**: 
         - "DONKI contains ﬂare data with their classes, source AR numbers, and their start, peak, and end times. This database also provides whether a ﬂare is accompanied with CMEs and/or SEPs."
   - **Additional Comments**:
      - The DONKI dataset is used in conjunction with other databases (such as GOES) to crosscheck flare times and active region identifications.

---

### 2. GOES (Geostationary Operational Environmental Satellite)
- **General Comments**:
   - GOES carries the X-ray Sensor (XRS) instrument, which measures the peak X-ray flux in the 1 to 8 Angstrom range. These measurements are used to classify solar flares (A, B, C, M, and X classes). In this study, GOES data augments DONKI data by providing cross-checks on flare timings and classifications.
- **Supporting Quote**:
   - "Based on their peak ﬂuxes in the 1 to 8 Angstrom range X-rays near Earth, as measured by XRS instrument on the Geostationary Operational Environmental Satellite (GOES), ﬂares are classiﬁed as A, B, C, M, and X."
- **Data Collection Period 1: Implicitly Parallel with Study Duration**
   - **Time Range**: Although no explicit start and end dates are provided for GOES in the paper, its data is used during the same period as DONKI and SHARPs – for example, the M3.0 flare on 06 March 2015 is cross-checked via GOES.
      - **Supporting Quote**:
         - "For example, the M3.0 class ﬂare with an accompanying CME and SEP that occurred on 06 March 2015. To ﬁll the unregistered AR numbers in DONKI [...] we use ﬂare data from GOES via SunPy Python package v0.8.2."
   - **Wavelength(s)**: 1 to 8 Angstroms (X-ray wavelengths)
      - **Supporting Quote**:
         - "Based on their peak ﬂuxes in the 1 to 8 Angstrom range X-rays [...] as measured by XRS instrument on the Geostationary Operational Environmental Satellite (GOES)."
   - **Physical Observable**: X-ray flux intensity, which is linked to the flare magnitude.
      - **Supporting Quote**: (Implied through the discussion on flare classifications)
   - **Additional Comments**:
      - GOES data is used to validate events from the DONKI database and ensures consistency in flare timing and AR attribution.

---

### 3. SHARPs (Space-Weather Heliospheric and Magnetic Imager Active Region Patches) Data from SDO/HMI
- **General Comments**:
   - SHARPs data, derived from the Helioseismic and Magnetic Imager (HMI) on board the Solar Dynamics Observatory (SDO), provides vector magnetic field measurements of solar active regions. The dataset includes a suite of 18 physical parameters (e.g., magnetic helicity, mean shear angle, photospheric magnetic free energy) that serve as proxies for the magnetic complexity and potential eruptivity of ARs.
- **Supporting Quote**:
   - "Following the veriﬁcation of the ﬂare data from the DONKI and the GOES databases, we use publicly available SHARPs data from the Joint Science Operations Center (JSOC), spanning from 01 January 2010 to 31 January 2018."
- **Data Collection Period 1: Full Study Duration**
   - **Time Range**: 01 January 2010 – 31 January 2018
      - **Supporting Quote**:
         - "we use publicly available SHARPs data from the Joint Science Operations Center (JSOC)2, spanning from 01 January 2010 to 31 January 2018."
   - **Wavelength(s)**: Not applicable; the measurements are based on polarimetric (Stokes vector) observations rather than a single wavelength band.
      - **Supporting Quote**:
         - "of a high-quality, meaning the data with reliable Stokes vectors (observables during good conditions)..."
   - **Physical Observable**: Vector magnetic field of solar active regions, including derived quantities such as magnetic helicity, shear angles, free energy density, and unsigned flux.
      - **Supporting Quote**:
         - "The SHARPs data contain vector magnetic ﬁeld measurements of the ARs and 18 keywords, which parametrise the measured physical quantities as well as proxies of physical quantities."
   - **Additional Comments**:
      - Data selection criteria include disambiguated vector fields, measurements taken while the SDO’s orbital velocity is <3500 m s⁻¹, and confinement within a ±70° longitudinal band during GOES peak time to ensure a high signal-to-noise ratio.

---

### 4. MDI (Michelson Doppler Imager) on SOHO (Solar and Heliospheric Observatory)
- **General Comments**:
   - The MDI instrument aboard SOHO has been used in earlier studies (e.g., Yu et al. 2009) for obtaining line-of-sight (LoS) magnetogram data of the solar photosphere. These magnetograms are used to forecast solar flares and related phenomena by analyzing the line-of-sight magnetic fields.
- **Supporting Quote**:
   - "Yu et al. (2009) used LoS magnetogram data from the Michelson Doppler Imager (MDI) on the Solar and Heliospheric Observatory (SOHO) to predict ﬂare occurrences within a forecast window of 48 hours."
- **Data Collection Details**:
   - **Time Range**: While the exact observational dates are not specified in this paper, the instrument is noted to have a long mission duration—approximately 22 years.
      - **Supporting Quote**:
         - "the mission duration of which has reached ∼22 years."
   - **Wavelength(s)**: Not explicitly stated; MDI typically observes in a spectral line suitable for capturing solar photospheric magnetic fields.
      - **Supporting Quote**: (Not detailed in the text)
   - **Physical Observable**: Line-of-sight magnetic field measurements, which are used to derive information on active regions.
      - **Supporting Quote**: (Implied in the reference to “LoS magnetogram data”)
   - **Additional Comments**:
      - MDI data represents an earlier generation of solar magnetic measurements compared to the vector data provided by SDO/HMI.

---

### 5. MIDORI-II on ADEOS-2 (Japanese Earth-Resource Satellite)
- **General Comments**:
   - MIDORI-II, part of the ADEOS-2 mission, is referenced as an Earth-resource satellite whose operational instruments (e.g., star trackers) were adversely affected by extreme solar events, specifically during the Halloween solar storms. Although not directly used in the forecasting study, its mention highlights the potential technological impact of solar eruptions.
- **Supporting Quote**:
   - "These ﬂares even killed the power supply of the Japanese Earth-resource satellite, the MIDORI-II (ADEOS-2), and left it inoperative."
- **Data Collection/ Event Period**:
   - **Time Range**: The referenced events occurred during the Halloween solar storms in mid-October to early November 2003.
      - **Supporting Quote**: 
         - "Since the 1950s, a series of the most powerful ﬂares and their accompanying CMEs have occurred between mid-October to early November 2003 peaking around 28 and 29 October (the so-called Halloween solar storms)..."
   - **Wavelength(s)**: Not applicable.
   - **Physical Observable**: Not applicable; the reference serves to illustrate the impact of strong solar eruptions on satellite instrumentation.
   - **Additional Comments**:
      - MIDORI-II is mentioned in the context of highlighting historical solar storm impacts rather than as a data source for the study.

---

### 6. Additional Mention: Star Trackers (onboard Various Satellites)
- **General Comments**:
   - Star trackers, which are instruments used for determining a satellite’s orientation, are mentioned as being affected during severe solar events. Their malfunction during solar storms underscores the disruptive effects of extreme solar activity on satellite operations.
- **Supporting Quote**:
   - "Since the 1950s, [...] these ﬂares even caused radio blackouts on Earth, and problems in diﬀerent instruments of the satellites, such as star trackers."
- **Data Collection/ Event Period**:
   - **Time Range**: While no specific observational time range is provided, the reference is associated with the effects seen during historical solar storms (e.g., the Halloween solar storms of 2003).
   - **Wavelength(s)**: Not applicable.
   - **Physical Observable**: Not applicable; the mention is purely in the context of instrument failure due to solar activity.
   - **Additional Comments**:
      - This mention reinforces the importance of forecasting solar eruptions to mitigate the impacts on sensitive satellite instrumentation.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper develops a machine learning–based predictive tool for estimating key properties (specifically, the minimum value of the Bz component and the maximum total magnetic field Bt) of the magnetic obstacle within interplanetary coronal mass ejections (ICMEs). The study relies on in situ measurements from multiple spacecraft—Wind, STEREO-A, and STEREO-B—gathered over a period from January 1, 2007 to April 1, 2021. Data from instruments measuring both magnetic field and bulk plasma properties are used to compute statistical features across ICME events, which then serve as inputs for various machine learning models. The paper details the training, testing, and validation of the predictive tool and discusses its potential use in operational space weather forecasting.

## Instrumentation Details

### 1. MFI Instrument on board Wind
- **General Comments**:
   - The Magnetic Field Investigation (MFI) instrument on the Wind spacecraft is used to obtain high-resolution in situ magnetic field measurements. These measurements include the vector components (Bx, By, Bz) and the total magnetic field (Bt), which are essential for quantifying the magnetic structure within ICMEs.
   - It is referenced in the paper alongside the SWE instrument, emphasizing its role in recording magnetic field data at the Sun–Earth L1 point.
- **Supporting Quote**: 
   - "In particular, we study in situ measurements from the MFI and SWE instruments on the Wind spacecraft (Ogilvie et al., 1995; Lepping et al., 1995)."
   
#### Data Collection Period 1: ICME Observations at 1 AU
- **Time Range**: January 1, 2007 – April 1, 2021
   - **Supporting Quote**: 
      - "from 558 ICMEs observed close to 1 AU, at the Sun-Earth L1 point and by STEREO-A/B, during the time interval 2007 January 1 to 2021 April 1."
- **Wavelength(s)**: Not applicable (in situ magnetic field measurements do not involve specific wavelengths)
   - **Supporting Quote**: *(No specific wavelength information provided)*
- **Physical Observable**: Magnetic field components including Bx, By, Bz, and total magnetic field Bt.
   - **Supporting Quote**: 
      - "predict the minimum value of the Bz component and the maximum value of the total magnetic field, Bt, in the magnetic obstacle."
- **Additional Comments**: 
   - Approximately 149 ICME events in the ICME catalog are attributed to observations by Wind.
   
### 2. SWE Instrument on board Wind
- **General Comments**:
   - The Solar Wind Experiment (SWE) on Wind measures the bulk plasma properties such as proton temperature, proton density, and the plasma speed (vt). These measurements complement the magnetic field data from MFI in characterizing the physical conditions within ICMEs.
   - SWE plays a crucial role in computing statistical measures that serve as features in the predictive tool.
- **Supporting Quote**: 
   - "we study in situ measurements from the MFI and SWE instruments on the Wind spacecraft (Ogilvie et al., 1995; Lepping et al., 1995)."
   
#### Data Collection Period 1: ICME Observations at 1 AU
- **Time Range**: January 1, 2007 – April 1, 2021
   - **Supporting Quote**: 
      - "observed close to 1 AU, at the Sun-Earth L1 point and by STEREO-A/B, during the time interval 2007 January 1 to 2021 April 1."
- **Wavelength(s)**: Not applicable (the instrument measures particle velocities and densities rather than electromagnetic wavelengths)
   - **Supporting Quote**: *(No specific wavelength information provided)*
- **Physical Observable**: Bulk plasma properties including proton temperature (Tp), proton density (Np), and flow speed (vt).
   - **Supporting Quote**: 
      - "we compute the features for machine learning from in situ plasma and magnetic field measurements of 348 ICMEs. In particular, we examine the timelines of 7 different physical properties (Bt, Bx, By, Bz, vt, Tp, Np)..."
- **Additional Comments**: 
   - The SWE measurements help in constructing the feature set (statistical measures) required for the predictive model.

### 3. IMPACT Instrument on board STEREO-A and STEREO-B
- **General Comments**:
   - The IMPACT (In-situ Measurements of Particles and CME Transients) instrument on the STEREO spacecraft provides in situ measurements of the magnetic field and energetic particles. It is fundamental for capturing the magnetic environment as ICMEs pass by and for contributing to the overall dataset used in the study.
   - IMPACT measurements are used in conjunction with PLASTIC data from the same spacecraft.
- **Supporting Quote**: 
   - "and the IMPACT and PLASTIC instruments on the STEREO-A and STEREO-B spacecraft (Luhmann et al., 2008; Galvin et al., 2008)."
   
#### Data Collection Period 1: ICME Observations at 1 AU
- **Time Range**: January 1, 2007 – April 1, 2021
   - **Supporting Quote**: 
      - "observed close to 1 AU, at the Sun-Earth L1 point and by STEREO-A/B, during the time interval 2007 January 1 to 2021 April 1."
- **Wavelength(s)**: Not applicable (the instrument is designed for in situ particle and magnetic field measurements rather than electromagnetic spectral imaging)
   - **Supporting Quote**: *(No specific wavelength information provided)*
- **Physical Observable**: In situ magnetic field parameters and energetic particles that help characterize the structure and dynamics of ICMEs.
   - **Supporting Quote**: 
      - While detailed physical observables aren’t itemized specifically for IMPACT in the text, its role aligns with capturing magnetic field and plasma information as needed for Bz prediction.
- **Additional Comments**:
   - The instrument contributes to the dataset from STEREO spacecraft, with 135 ICME events attributed to STEREO-A measurements and additional events from STEREO-B.

### 4. PLASTIC Instrument on board STEREO-A and STEREO-B
- **General Comments**:
   - The PLASTIC (PLasma And SupraThermal Ion Composition) instrument on the STEREO spacecraft measures solar wind plasma properties, including ion composition, densities, and velocities. This information is critical in conjunction with the IMPACT instrument to provide a comprehensive in situ characterization of ICMEs.
   - PLASTIC data are used to compute several statistical features that feed into the machine learning models.
- **Supporting Quote**: 
   - "and the IMPACT and PLASTIC instruments on the STEREO-A and STEREO-B spacecraft (Luhmann et al., 2008; Galvin et al., 2008)."
   
#### Data Collection Period 1: ICME Observations at 1 AU
- **Time Range**: January 1, 2007 – April 1, 2021
   - **Supporting Quote**: 
      - "observed close to 1 AU, at the Sun-Earth L1 point and by STEREO-A/B, during the time interval 2007 January 1 to 2021 April 1."
- **Wavelength(s)**: Not applicable (PLASTIC focuses on plasma properties rather than spectral wavelengths)
   - **Supporting Quote**: *(No specific wavelength information provided)*
- **Physical Observable**: Plasma characteristics such as density, temperature, and bulk speed which are essential for computing the statistical measures used in the forecasting tool.
   - **Supporting Quote**: 
      - "we compute the features for machine learning from in situ plasma and magnetic field measurements of 348 ICMEs... (vt, Tp, Np)."
- **Additional Comments**:
   - PLASTIC complements IMPACT on STEREO-A and STEREO-B by providing the necessary plasma measurements for the machine learning prediction of magnetic storm features.

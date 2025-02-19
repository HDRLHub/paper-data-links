_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper introduces a new inversion method based on spherical harmonics to reconstruct the coronal electron density, primarily at heights where the corona approximates a radial structure (around 5–5.5R⊙). The methodology is demonstrated through tests on synthetic data—with both a simple density model and a more complex, narrowly peaked density model—and then applied to real coronagraph observations. The observational data are obtained from white-light coronagraph instruments, and the paper specifically compares reconstruction results from two instruments over different time periods. These instruments provided measurements of the K-coronal brightness, an observable related to coronal electron density via Thomson scattering. The observations used in the study come from a synthetic test period during 2007 as well as a half-Carrington rotation period centered on 2009/03/20 12:00. The method includes techniques for regularization to control high-frequency artifacts in the reconstructions.

---

### 1. LASCO C2 on board SOHO
- **General Comments**:
  - LASCO C2 is a coronagraph that observes the visible light K-corona. In this work, it is used both for creating synthetic test observations and for obtaining real data from which the coronal electron density is reconstructed.
  - The instrument records the integrated brightness due to Thomson scattering in the corona, which is then processed using the spherical harmonic inversion method.
- **Supporting Quote**:
  - “Synthetic observations are made by specifying an uniform vector of pixels describing a circle centered on the solar disk as observed from the perspective of LASCO C2 during 2007/03/15-30.” (Section 3)
  
#### Data Collection Period 1: Synthetic Observations for Method Testing
- **Time Range**: 2007/03/15 – 2007/03/30
  - **Supporting Quote**: “...observed from the perspective of LASCO C2 during 2007/03/15-30.” (Section 3)
- **Wavelength(s)**: Visible light (white-light coronagraph imaging capturing the K-corona brightness)
  - **Supporting Quote**: “...coronal visible light observations...” (Introduction)
- **Physical Observable**: K-coronal brightness from Thomson scattering of coronal electrons.
  - **Supporting Quote**: “…the observed K-coronal (electron) brightness Bk is the line-of-sight summation of the product of density and a factor g…” (Section 2.1)
- **Additional Comments**:
  - These synthetic observations were used to test the inversion method using a prescribed density model based on spherical harmonics.

#### Data Collection Period 2: Real Observations
- **Time Range**: Half-Carrington rotation period centered on 2009/03/20 12:00 (approximately two weeks; exact start and end dates are not explicitly provided)
  - **Supporting Quote**: “This section applies the tomography to observations made by the LASCO C2 and the STEREO SECCHI COR2 A coronagraphs for a half-Carrington rotation period centered on 2009/03/20 12:00.” (Section 7)
- **Wavelength(s)**: Visible light (as with standard coronagraph imaging in white light)
  - **Supporting Quote**: “...the brightness of the corona observed at 5.5R⊙…” (Figure 12a caption)
- **Physical Observable**: K-coronal brightness used to derive the coronal electron density.
  - **Supporting Quote**: “The LASCO C2 data is ﬁtted with a mean absolute deviation of 10.6%...” (Section 7)
- **Additional Comments**:
  - The data from LASCO C2 are rebinned into position-angle and time arrays and then used in the inversion method to extract the spherical harmonic coefficients that describe the coronal density structure.

---

### 2. STEREO SECCHI COR2 A on board STEREO A
- **General Comments**:
  - STEREO SECCHI COR2 A is a coronagraph instrument aboard the STEREO A spacecraft. In this study, its observations complement those of LASCO C2 and enable a comparative analysis of the reconstructed coronal density.
  - The instrument measures the same K-coronal brightness in visible light, allowing direct comparisons despite differences in spacecraft position.
- **Supporting Quote**:
  - “...observations made by the LASCO C2 and the STEREO SECCHI COR2 A coronagraphs for a half-Carrington rotation period centered on 2009/03/20 12:00.” (Section 7)
  
#### Data Collection Period: Real Observations
- **Time Range**: Half-Carrington rotation period centered on 2009/03/20 12:00 (approximately two weeks; exact start and end dates are not explicitly provided)
  - **Supporting Quote**: “...for a half-Carrington rotation period centered on 2009/03/20 12:00.” (Section 7)
- **Wavelength(s)**: Visible light (white-light coronagraph imaging)
  - **Supporting Quote**: “...observed by the COR2 A instrument.” (Figure 12c caption)
- **Physical Observable**: K-coronal brightness, related to coronal electron density through Thomson scattering.
  - **Supporting Quote**: “For COR2 A the values are 7.0%, λ = 5.1 × 10^4 and ρmin = 6.5 × 10^3cm^−3.” (Section 7)
- **Additional Comments**:
  - At the time of observation, STEREO A was separated by 60° from SOHO, providing an advantageous viewing geometry for the tomographical reconstruction.
  - The COR2 A reconstructed density shows more tightly defined features in the streamer belt compared to LASCO C2, suggesting differences in sensitivity and observational geometry.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This paper presents a study of the solar meridional circulation's subsurface structure, utilizing over 21 years of helioseismic Dopplergram data. The primary research objective is to achieve high-precision measurements of subsurface meridional flow by combining and analyzing full-disk velocity observations from two consecutive space-based instruments: SOHO/MDI (May 1996 – April 2010) and SDO/HMI (May 2010 – April 2017). The paper details advanced data preparation, alignment, and systematic effect mitigation (such as P-angle correction, surface magnetic field masking, and center-to-limb variation correction), as well as forward modeling of the helioseismic travel-time differences. These long-term observations are central to the derived results, including solar cycle and hemispheric asymmetries in the meridional flow over two solar cycles.

## Instrumentation Details

---

### Michelson Doppler Imager (MDI) on board Solar and Heliospheric Observatory (SOHO)
- **General Comments**:
  - The SOHO/MDI instrument provided the medium-degree (medium-ℓ) Dopplergram velocity data from May 1996 to April 2010 at a 60-second cadence. The MDI dataset forms the basis of the helioseismic analyses for cycle 23 and the first part of cycle 24, contributing to the temporal merging and continuity with later HMI data. Its data were specifically processed for systematic corrections and subjected to comprehensive quality control for the study.
- **Supporting Quote**:  
  "We use the medium-ℓDopplergrams spanning from 1 May 1996 to 30 April 2010 made by SOHO/MDI at a cadence of 60 s."

#### Data Collection Period 1: Measurement of Subsurface Meridional Flow in Solar Cycle 23 and Overlap with Cycle 24
- **Time Range**: 1996-05-01 – 2010-04-30 (full context: covers cycle 23, merging with HMI in overlap period May 2010 – April 2011)
  - **Supporting Quote**:  
    "We use the medium-ℓDopplergrams spanning from 1 May 1996 to 30 April 2010 made by SOHO/MDI at a cadence of 60 s."
- **Wavelength(s)**:  
  Line-of-sight Doppler velocity images (full-disk, Ni I 6768 Å, sensitive to oscillation modes up to ℓ ≈ 300)
  - **Supporting Quote**:  
    "These medium-ℓDopplergrams are produced by smoothing and subsampling the full-resolution line-of-sight velocity images (Kosovichev et al. 1997). They have an image scale of ∼10 arcsec pixel−1 and are sensitive to oscillation modes in the regime where spherical harmonic degree ℓ≤300."
- **Physical Observable**:  
  Subsurface solar oscillation velocities (helioseismic p-modes) used to compute travel-time differences probing meridional circulation
  - **Supporting Quote**:  
    "The south-north travel-time diﬀerences are measured by applying time-distance helioseismology to the MDI and HMI medium-degree Dopplergrams covering May 1996–April 2017."
- **Additional Comments**:  
  MDI instrument images were quality-filtered for artifacts and systematic errors, with only those images retained where the position angle was nominal (CROTA2 = 0). Also, surface magnetic field magnetograms from the same period were used for masking active regions.
  - **Supporting Quote**:  
    "The line-of-sight magnetic ﬁeld data are retrieved from the mdi.fd_m_96m_lev182 ... in the same period as for the Dopplergrams."

---

### Helioseismic and Magnetic Imager (HMI) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
  - The SDO/HMI instrument provided medium-ℓ Dopplergram velocity data with higher temporal cadence (45 seconds) from May 2010 to April 2017. HMI data enabled continuity in the helioseismic time series, allowed detailed overlap comparison and cross-calibration with MDI, and extended the data set into cycle 24. Both Dopplergrams and magnetic field observations were used for travel-time analysis and masking procedures.
- **Supporting Quote**:  
  "from 1 May 2010 to 30 April 2017 made by SDO/HMI at a cadence of 45 s. They are retrieved from the mdi.vw_v and hmi.vw_v_45s data series in the Joint Science Operations Center1 (JSOC) data system."

#### Data Collection Period 1: Measurement of Subsurface Meridional Flow in Solar Cycle 24 and Overlap with MDI
- **Time Range**: 2010-05-01 – 2017-04-30 (full context: includes the overlap window May 2010 – April 2011 for cross-calibration)
  - **Supporting Quote**:  
    "from 1 May 2010 to 30 April 2017 made by SDO/HMI at a cadence of 45 s."
- **Wavelength(s)**:  
  Line-of-sight Doppler velocity images (full-disk, Fe I 6173 Å, sensitive to oscillation modes up to ℓ ≈ 300)
  - **Supporting Quote**:  
    "These medium-ℓDopplergrams are produced by smoothing and subsampling the full-resolution line-of-sight velocity images (Kosovichev et al. 1997). They have an image scale of ∼10 arcsec pixel−1 and are sensitive to oscillation modes in the regime where spherical harmonic degree ℓ≤300."
- **Physical Observable**:  
  Subsurface solar oscillation velocities (helioseismic p-modes) used to compute travel-time differences probing meridional circulation
  - **Supporting Quote**:  
    "The south-north travel-time diﬀerences are measured by applying time-distance helioseismology to the MDI and HMI medium-degree Dopplergrams covering May 1996–April 2017."
- **Additional Comments**:  
  HMI instrument data received P-angle correction based on Venus and Mercury transits, as provided by the HMI team. Also, line-of-sight magnetograms for masking active regions were extracted from this instrument for the same time range.
  - **Supporting Quote**:  
    "For HMI data, we used the P-angle correction provided by the HMI team based on the Venus and Mercury transits."
  - **Supporting Quote**:  
    "The line-of-sight magnetic ﬁeld data are retrieved from... hmi.m_45s data series in the same period as for the Dopplergrams."

---

## Validation Checklist

- [x] Every quote is exact text from the paper
- [x] No interpretive or explanatory text added to quotes
- [x] Time ranges include both start and end times with COMPLETE DATES and event context
- [x] ALL time ranges specify the full date (year-month-day) even if mentioned elsewhere in the paper
- [x] Event context is included with time ranges when relevant
- [x] Only instruments with direct data usage are included
- [x] Physical observables are clearly specified

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This paper documents a new methodology for creating a Total Solar Irradiance (TSI) composite by directly combining data from multiple radiometric space-based instruments. The study focuses on constructing a continuous, statistically rigorous TSI record spanning from November 17, 1978, to December 31, 2015, by incorporating and analyzing daily TSI observations from eight key satellite instruments. Data from these instruments are processed, decomposed into multiple timescales, and merged using a maximum likelihood estimator that accounts for uncertainties, precision, stability, and instrument-specific characteristics. The analysis forms the basis for evaluating long-term solar variability. The temporal limits for the composite are explicitly defined by the time ranges covered by these eight instruments and their periods of operation.

## Instrumentation Details

### HF (NIMBUS-7 ERB) on board NIMBUS-7
- **General Comments**:
  - The HF instrument is one of the earliest satellite radiometers included in the study, providing daily TSI data forming part of the composite’s early temporal coverage.
- **Supporting Quote**:  
  "The eight instruments that are routinely used for making the TSI composite are listed in Table 1 and their records are illustrated in Fig. 1. Most observe on a daily basis, with occasional interruptions and outliers..."

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 1978/11 – 1993/01
  - **Supporting Quote**:  
    "HF / NIMBUS-7 ERB         1978/11    1993/01"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "we apply it to the total solar irradiance (TSI), which is the spatially- and spectrally-integrated radiant output from the Sun at a mean Sun-Earth distance of 1 astronomical unit (Kopp, 2014)."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "The TSI has been continuously measured since November 1978 by over a dozen instruments..."
- **Additional Comments**:  
  HF data are among those requiring artifact corrections for early signal increases.

---

### ACRIM1 on board SMM
- **General Comments**:
  - Provides a daily TSI measurement forming a critical coverage during the 1980s.
- **Supporting Quote**:  
  "Daily TSI observations actually mask disparities: all instruments make several observations per day (with a cadence of up to 50 seconds for TIM) and then average these to produce a daily average."

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 1980/02 – 1989/07
  - **Supporting Quote**:  
    "ACRIM1 / SMM         a      1980/02    1989/07"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "reconstruction of the total solar irradiance (TSI), which is the spatially- and spectrally-integrated radiant output from the Sun..."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "Let Ij(t) be the TSI from ACRIM3, VIRGO, and TIM, which are the three instruments that have the longest overlapping period (10.5 years)."
- **Additional Comments**:  
  The period immediately following ACRIM1's cessation left a gap filled only by ERBE.

---

### ERBE on board ERBS
- **General Comments**:
  - This instrument filled significant gaps when other instruments were offline, though with a lower measurement cadence.
- **Supporting Quote**:  
  "ERBE, however, on average observes the Sun once every 14 days for 3 minutes."

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 1984/10 – 2003/08
  - **Supporting Quote**:  
    "ERBE / ERBS           1984/10    2003/08"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "all instruments agree well on the amplitude of relative variations but differ in their baseline. The two most recent radiometers (TIM and PREMOS) are the only ones that accounted for internal-instrument scatter effects prior to launch..."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "ERBE, however, on average observes the Sun once every 14 days for 3 minutes."
- **Additional Comments**:  
  Known for not having a degradation-correction monitor.

---

### ACRIM2 on board UARS
- **General Comments**:
  - Provided daily TSI data, largely used for filling the 1990s observational coverage.
- **Supporting Quote**:  
  "ACRIM2 / UARS      b      1991/10    2000/09"

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 1991/10 – 2000/09
  - **Supporting Quote**:  
    "ACRIM2 / UARS        b      1991/10    2000/09"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "We concentrate on this methodology and introduce a novel, probabilistic approach that can be readily exported to other contexts."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "The composite should combine the original records with no reliance on any external proxy by using state-of-the-art statistical methods."
- **Additional Comments**:  
  Helped end the significant data gap from the late 1980s to early 1990s.

---

### VIRGO on board SOHO
- **General Comments**:
  - Provides ongoing TSI observations from 1996 onward, with precise daily data.
- **Supporting Quote**:  
  "VIRGO / SOHO     c      1996/01      active"

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 1996/01 – active (at least through 2015/12/31 for this study)
  - **Supporting Quote**:  
    "VIRGO / SOHO     c      1996/01      active"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "their records are illustrated in Fig. 1. Most observe on a daily basis, with occasional interruptions and outliers."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "Let Ij(t) be the TSI from ACRIM3, VIRGO, and TIM, which are the three instruments that have the longest overlapping period (10.5 years)."
- **Additional Comments**:  
  Considered one of the long-term reference datasets in this composite.

---

### ACRIM3 on board ACRIMSAT
- **General Comments**:
  - Continued the ACRIM series’ daily monitoring of TSI into the 21st century.
- **Supporting Quote**:  
  "ACRIM3 / ACRIMSAT    d      2000/04    2013/02"

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 2000/04 – 2013/02
  - **Supporting Quote**:  
    "ACRIM3 / ACRIMSAT    d      2000/04    2013/02"
- **Wavelength(s)**: Total Solar Irradiance (broadband)
  - **Supporting Quote**:  
    "Let Ij(t) be the TSI from ACRIM3, VIRGO, and TIM, which are the three instruments that have the longest overlapping period (10.5 years)."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "The power spectral density of the residual error scales almost as 1/f, where f is the frequency, and thus strongly departs from a white-noise assumption. The same scaling is observed for any combination of TSI instruments with overlapping observations, regardless of their duration, and thus is a robust result."
- **Additional Comments**:  
  Key part of the late-2000s–early-2010s composite core.

---

### TIM on board SORCE
- **General Comments**:
  - One of the most precise TSI instruments, used as a reference for the composite’s absolute scale.
- **Supporting Quote**:  
  "The two most recent radiometers (TIM and PREMOS) are the only ones that accounted for internal-instrument scatter effects prior to launch, and thus do not require subsequent large corrections as the others do."

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 2003/03 – active (through at least 2015/12/31 for this study)
  - **Supporting Quote**:  
    "TIM / SORCE        e      2003/03      active"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "The TSI has been continuously measured since November 1978 by over a dozen instruments..."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "This value is also consistent with that reported by Kopp and Lean (2011)."
- **Additional Comments**:  
  Serves as a reference for absolute TSI value in this study.

---

### PREMOS on board PICARD
- **General Comments**:
  - The only modern TSI instrument included with a completed mission, also used as an absolute reference.
- **Supporting Quote**:  
  "For that purpose, we use as an absolute value the average of TIM and PREMOS, which agree with only small differences that are well within their estimated accuracy uncertainties."

#### Data Collection Period 1: Full Operational Span
- **Time Range**: 2010/07 – 2014/02
  - **Supporting Quote**:  
    "PREMOS / PICARD      f      2010/07    2014/02"
- **Wavelength(s)**: Total Solar Irradiance (broadband, all wavelengths)
  - **Supporting Quote**:  
    "The two most recent radiometers (TIM and PREMOS) are the only ones that accounted for internal-instrument scatter effects prior to launch..."
- **Physical Observable**: Total Solar Irradiance (TSI)
  - **Supporting Quote**:  
    "For TIM and PREMOS, these values are within a factor of two of the precisions stated by the instrument teams."
- **Additional Comments**:  
  Used in conjunction with TIM to anchor the composite's absolute calibration.

---

**Note**: All eight named instruments provide the essential dataset for the novel composite described, as demonstrated by explicit data selection, combination, and analysis throughout the study.

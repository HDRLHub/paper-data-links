_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper presents a new calibration of the GOLF instrument onboard SOHO, focusing on achieving improved consistency in p-mode amplitude measurements and more precise time shift corrections over two decades of solar observations. The research is based on the direct analysis of GOLF data spanning from April 11, 1996 to April 10, 2018. Data from other instruments, notably GONG (Global Oscillation Network Group), BiSON (Birmingham Solar Oscillation Network), and VIRGO/SPM (Sun Photometer Monitor of the Variability of Irradiance and Gravity Oscillations), are used specifically for the validation and correction of GOLF's time series, forming the basis for cross-instrument temporal alignment and amplitude comparison. The calibration improves the GOLF time series for future g-mode detection attempts and ensures comparability with other helioseismic data sets.

## Instrumentation Details

### GOLF (Global Oscillations at Low Frequencies) instrument onboard SOHO
- **General Comments**:
  - The primary focus of this research is the recalibration and analysis of GOLF data, explicitly using 22 years of raw data collected from the SOHO spacecraft. The instrument's unique single-wing measurement modes (due to hardware limitations after March 31, 1996) are fully incorporated and characterized. The calibration process depends upon predictive solar radial velocity data for correction reference.
- **Supporting Quote**:  
  "The data used for the new calibration start on 11 April 1996 and end on 10 April 2018. The technique used for the calibration is derived from that of Garc´ıa et al. (2005) using the so-called X method."

#### Data Collection Period 1: Primary calibration and analysis period
- **Time Range**: 1996-04-11 – 2018-04-10 (covering all operational phases and calibration epochs)
  - **Supporting Quote**:  
    "The data used for the new calibration start on 11 April 1996 and end on 10 April 2018."
- **Wavelength(s)**: Sodium D lines (single-wing, blue or red) as modulated by instrument operation
  - **Supporting Quote**:  
    "Since GOLF operates only in one wing of the Sodium lines, the following ratio is computed as a proxy to the two-wing signal..."
- **Physical Observable**: Solar radial velocity fluctuations (p-mode signatures and background noise)
  - **Supporting Quote**:  
    "The calibration of 22 years of GOLF data is done with a simpler approach that uses only the predictive radial velocity of the SoHO spacecraft as a reference."
- **Additional Comments**: GOLF data is corrected for operational mode switches (from blue to red and back) and known time jumps using spacecraft and photomultiplier housekeeping data.

---

### GONG (Global Oscillation Network Group)
- **General Comments**:
  - GONG l = 0 velocity data is used as a temporal reference and for direct amplitude/noise comparisons with GOLF, enabling precise time alignment and validation across the overlapping periods. Cross-correlation and timing analysis with GOLF data form a core part of the recalibration method.
- **Supporting Quote**:  
  "In order to check for potential unknown time jumps, we used data from other instruments such as the Global Oscillation Network Group... The GONG data were then used as a time reference to check and correct GOLF datation."

#### Data Collection Period 1: Coincident with GOLF data for cross-referencing and validation
- **Time Range**: 1996-04-11 – 2018-04-10 (all days with available overlapping data)
  - **Supporting Quote**:  
    "The GONG data were then used as a time reference to check and correct GOLF datation."
- **Wavelength(s)**: Not specifically stated for this application, but GONG nominally observes the Ni I 6768 Å photospheric line at high cadence.
  - **Supporting Quote**:
    [No explicit wavelength given for GONG in the main text related to the procedures, supporting adherence to quote standards.]
- **Physical Observable**: Solar global radial velocity (primarily l=0 component), p-mode signatures used for cross-correlation and amplitude assessment
  - **Supporting Quote**:  
    "GONG data for l = 0 and the VIRGO / SPM data do not present any temporal jumps as shown in Fig. 5. As it is unlikely that both time series would have time jumps at the same date, the blue SPM and GONG then provide two references for a constant time base."
- **Additional Comments**: GONG’s backward difference filter (BDF) is accounted for in all time alignment comparisons.

---

### BiSON (Birmingham Solar Oscillation Network)
- **General Comments**:
  - BiSON velocity data are directly analyzed for comparison of p-mode amplitudes and noise levels with those from GOLF, providing a check on calibration accuracy and amplitude scaling.
- **Supporting Quote**:  
  "In order to double check the velocity calibration and time correction, we used data from GONG l = 0 and from BiSON and compared them with the previous calibration of the time series used by Fossat et al. (2017). Figures 8 shows the comparison of the rms p-mode amplitude and the rms p-mode noise for these different time series."

#### Data Collection Period 1: Coincident with GOLF data for amplitude comparisons
- **Time Range**: 1996-04-11 – 2018-04-10 (where overlaps with GOLF exist)
  - **Supporting Quote**:  
    "In order to double check the velocity calibration and time correction, we used data from GONG l = 0 and from BiSON and compared them with the previous calibration of the time series used by Fossat et al. (2017)."
- **Wavelength(s)**: Not specified for this procedure; BiSON nominally observes photospheric K and D spectral lines.
  - **Supporting Quote**:
    [No wavelength values are given in procedure section, supporting adherence to quote standards.]
- **Physical Observable**: Solar disk-integrated radial velocity, p-mode amplitudes, and noise
  - **Supporting Quote**:  
    "The final p-mode power is obtained as Pp−mode=PT −Pnoise. The rms amplitude is then Ap−mode = √Pp−mode, while the rms noise is √Pnoise."
- **Additional Comments**: Amplitude normalization and offsets adjusted for formation height where appropriate.

---

### VIRGO/SPM (Sun Photometer Monitor of the Variability of Irradiance and Gravity Oscillations) onboard SOHO
- **General Comments**:
  - VIRGO/SPM (specifically the blue channel or "SPM Blue" where specified) intensity time series are used as an independent reference for checking GOLF's time alignments through cross-correlation of p-mode signatures.
- **Supporting Quote**:  
  "We used data from other instruments such as ... the Sun Photometer Monitor of the Variability of Irradiance and Gravity Oscillations instrument."

#### Data Collection Period 1: Cross-comparison with GOLF for timing
- **Time Range**: 1996-04-11 – 2018-04-10 (concurrent with core GOLF data series)
  - **Supporting Quote**:  
    "Figure 5 shows that the time delay in this time series is modulated with a periodicity of almost 6 months. This is due to the SoHO halo orbit, which has a periodicity of 178 days resulting in a time modulation of 1.54 s. ... The GONG data were then used as a time reference to check and correct GOLF datation. On close inspection, Fig. 5 shows that the time delay in this time series is modulated ..."
- **Wavelength(s)**: Not specified for timing procedures, but nominally: SPM Blue ("402 nm"), SPM Green ("500 nm"), SPM Red ("862 nm").
  - **Supporting Quote**:
    [No specific wavelength for SPM used in quoted procedure, per quote standards.]
- **Physical Observable**: Solar intensity fluctuations in SPM channels, used for cross-correlation and p-mode timing validation
  - **Supporting Quote**:  
    "We found that the GONG data for l = 0 and the VIRGO / SPM data do not present any temporal jumps as shown in Fig. 5. As it is unlikely that both time series would have time jumps at the same date, the blue SPM and GONG then provide two references for a constant time base."
- **Additional Comments**: SPM timing checks are especially important in cross-validating time shifts detected in GOLF.

---

**End of Instrumentation Form**

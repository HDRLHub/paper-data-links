_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper investigates the multifractal characteristics in high-precision time-series data of Sun‐like stars to study surface differential rotation (DR). The analysis is based on photometric observations from space missions. The authors use a multifractal detrended moving average (MFDMA) algorithm to characterize the scaling and fluctuation behaviours in the light curves. The stellar dataset consists of 662 active stars observed with Kepler, whose data were obtained in a specific quarter (Q3) with a long-cadence mode, ensuring a uniform ~90-day time window for analyses. In addition, continuous solar observations from the VIRGO/SPM instrument onboard SOHO, with observations spanning nearly two decades and a selected subinterval during the Sun’s active phase, are used to compare solar and stellar behaviour.

---

## Instrumentation Details

### 1. Kepler Photometer on board the Kepler Space Mission
- **General Comments**:
   - This instrument provides high-precision photometric data used to monitor brightness variations in stars. Its long-cadence mode, with a typical sampling every 29.4 minutes, enables the study of stellar rotation and associated starspot modulations.
   - The analysis in this paper is specifically based on Quarter 3 (Q3) data, which corresponds to an observational window of approximately 90 days.
- **Supporting Quote**: 
   - “The Kepler space mission now offers the ability to measure the rotation periods of thousands of stars based on high‐precision photometry … Based on a working sample adopted by Reinhold et al. (2013) with well‐determined rotation periods, we constructed our light curves using only Quarter 3 (Q3) long‐cadence data.”
- **Data Collection Period 1: Quarter 3 (Q3) Long-Cadence Data**
  - **Time Range**: Approximately a 90‑day observational period during Kepler’s Quarter 3. (Exact calendar dates are not provided in the paper; the emphasis is on the Q3 window.)
    - **Supporting Quote**: “... all light curves have been normalized to the median value of Q3.”
  - **Wavelength(s)**: Observations are in optical wavelengths, as typical for Kepler photometry.
    - **Supporting Quote**: “... based on high‐precision photometry.”
  - **Physical Observable**: Stellar brightness (flux) variations used to extract rotation periods and detect signatures of differential rotation.
    - **Supporting Quote**: “The measurement opens a new perspective for the study of DR.”
  - **Additional Comments**: The Kepler data also come with alternative processing pipelines (such as SAP and PDC) that affect the detrending and outlier removal. Different processing versions (SAP4, SAP4QLI, etc.) are compared to study the effect of instrumental processing artifacts on the multifractal indexes.

---

### 2. VIRGO/SPM Instrument on board the SOHO Spacecraft
- **General Comments**:
   - The VIRGO experiment, which is a part of the SOHO payload, consists of several instruments dedicated to monitoring the Sun’s irradiance and oscillations. For this study, the authors use data from the Sun PhotoMeter (SPM) channel of VIRGO, which provides measurements in two optical bands (green and red).
   - This instrument contributes solar observations that serve as a benchmark for comparison with stellar measurements.
- **Supporting Quote**: 
   - “Our sample also included a dataset of continuous solar observations obtained by Variability of solar Irradiance and Gravity Oscillations (VIRGO)… In the present paper, we use the VIRGO data in the green (500 nm) and red (862 nm) bandwidths of the SPM instrument…”
- **Data Collection Period 1: Full VIRGO/SPM SSI Dataset**
  - **Time Range**: April 11, 1996 to March 30, 2014  
    - **Supporting Quote**: “The VIRGO data analysed in the present work consist of the spectral solar irradiance (SSI) time series with a temporal cadence of 1 min and a date range from April 11, 1996 to March 30, 2014, corresponding to solar cycles 23 and 24.”
  - **Wavelength(s)**: Two distinct optical channels – green centered at 500 nm and red centered at 862 nm.
    - **Supporting Quote**: “... in the green (500 nm) and red (862 nm) bandwidths…”
  - **Physical Observable**: Spectral solar irradiance (SSI) used to capture variations in the solar brightness and to serve as a proxy for solar magnetic activity.
    - **Supporting Quote**: “… a dataset of continuous solar observations… which was within the Sun’s active phase.”
  - **Additional Comments**: Although the full dataset spans nearly 18 years, for a proper comparison with the stellar Q3 window, a subset with fewer data gaps was chosen.
  
- **Data Collection Period 2: Selected VIRGO/SPM Subset for Active Phase Analysis**
  - **Time Range**: April 22, 1999 to July 20, 1999  
    - **Supporting Quote**: “... we chose a region in the VIRGO/SPM data with few large gaps from April 22, 1999 to July 20, 1999, which was within the Sun’s active phase.”
  - **Wavelength(s)**: Retains the same SPM channels – green (500 nm) and red (862 nm).
    - **Supporting Quote**: Same as above.
  - **Physical Observable**: This subset captures the solar active phase to enable a direct comparison with the rotational modulation observed in the stellar sample.
  - **Additional Comments**: Data were averaged into 30-minute cadences for a proper comparison with the Kepler long-cadence data, which has a sampling interval close to 29.4 minutes.

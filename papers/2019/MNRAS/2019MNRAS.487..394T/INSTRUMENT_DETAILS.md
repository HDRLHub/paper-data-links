_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This paper investigates the ability of current Solar-wind (SW) models to correct for electron-density‐induced dispersive delays in pulsar timing data. Focusing on high-precision timing corrections essential for pulsar timing arrays (PTAs), the authors test the traditional spherical (T2) and two-phase (Y07) SW models. The study uses a four-year, high-cadence dataset of pulsar J0034−0534 observed with German stations of the LOw Frequency ARray (LOFAR) operating at low frequencies (∼150 MHz). Detailed analyses include comparing the models’ performance, the impact of coronal mass ejections (CMEs) using white-light coronagraph data from SOHO LASCO, and the evaluation of systematic effects by using additional solar magnetic field maps from the Wilcox Solar Observatory (WSO). These observations with clearly defined time ranges and frequency setups underpin the investigation into separating interstellar and Solar contributions in pulsar timing measurements.

## Instrumentation Details

### 1. LOFAR – German Station DE601
- **General Comments**:
  - DE601 is one of the LOFAR stations used in the high-cadence monitoring campaign of pulsar J0034−0534.
  - It operates as part of the international LOFAR telescope that covers frequencies between 30 and 240 MHz with two types of antennas (for low and high bands).
  - The station digitises the signal and uses a polyphase filterbank to channelise the data into 195 kHz-wide subbands which are later coherently dedispersed.
  
- **Supporting Quote**:  
  “...observed by four German stations of LOFAR (the LOw Frequency ARray, van Haarlem et al. 2013)...” and “Station DE601: 2013-08-21 to 2018-02-17” (from Table 1).

#### Data Collection Period:
- **Data Collection Period 1: Observations of PSR J0034−0534 using DE601**
  - **Time Range**: 2013-08-21 to 2018-02-17 (UT dates as provided in Table 1)
    - **Supporting Quote**: “DE601 … Timespan 2013-08-21 to 2018-02-17”
  - **Wavelength(s)**: Observations centered at ∼149.9 MHz (with additional details noting a central frequency around 153.8 MHz in some setups)
    - **Supporting Quote**: “...a central frequency of ∼153.8 MHz (149.9 MHz for DE601)...”
  - **Physical Observable**: Radio-frequency signals from pulsar J0034−0534; digitised voltage streams processed to obtain precise times-of-arrival (ToAs)
    - **Supporting Quote**: “...the signal is digitised at the station and channelised by a polyphase ﬁlterbank into 195 kHz-wide subbands.”

### 2. LOFAR – German Station DE602
- **General Comments**:
  - DE602 is another German LOFAR station participating in the monitoring campaign.
  - It uses similar hardware and processing as DE601, with observations aimed at high-cadence pulsar timing.
  
- **Supporting Quote**:  
  “...observations by four German LOFAR stations, namely DE601, DE602, DE603, DE605...” and from Table 1 “DE602 … Timespan 2015-01-31 to 2018-02-17.”

#### Data Collection Period:
- **Data Collection Period 1: Observations of PSR J0034−0534 using DE602**
  - **Time Range**: 2015-01-31 to 2018-02-17
    - **Supporting Quote**: “DE602 … Timespan 2015-01-31 to 2018-02-17”
  - **Wavelength(s)**: Central frequency of 153.8 MHz and a bandwidth of approximately 71.48 MHz
    - **Supporting Quote**: “153.8 MHz, Bandwidth 71.48 MHz” (from Table 1)
  - **Physical Observable**: Pulsar radio emission properties (pulse profiles and dispersion measures)
    - **Supporting Quote**: “...the final pulsar observation covers a bandwidth of ∼71.5 MHz centered at 153.8 MHz...”

### 3. LOFAR – German Station DE603
- **General Comments**:
  - DE603 provided data in two different observational setups, reflecting changes in central frequency and bandwidth.
  - Its observations contribute to understanding both high-band and low-band performance in pulsar timing.
  
- **Supporting Quote**:  
  “DE603 … 2014-02-12 to 2015-02-01 … and 2015-02-07 to 2018-02-17” (as reported in Table 1).

#### Data Collection Periods:
- **Data Collection Period 1: Early Campaign with DE603**
  - **Time Range**: 2014-02-12 to 2015-02-01
    - **Supporting Quote**: “DE603 2014-02-12 to 2015-02-01”
  - **Wavelength(s)**: Central frequency of 149.9 MHz with a bandwidth of 95.31 MHz
    - **Supporting Quote**: “fc: 149.9 MHz, Bandwidth: 95.31 MHz” (from Table 1)
  - **Physical Observable**: Pulsar dispersion measure (DM) variations derived from the pulsar’s radio signal

- **Data Collection Period 2: Later Campaign with DE603**
  - **Time Range**: 2015-02-07 to 2018-02-17
    - **Supporting Quote**: “DE603 … 2015-02-07 to 2018-02-17”
  - **Wavelength(s)**: Central frequency of 153.8 MHz with a bandwidth of 71.48 MHz
    - **Supporting Quote**: “fc: 153.8 MHz, Bandwidth: 71.48 MHz” (from Table 1)
  - **Physical Observable**: High-precision DM measurements obtained via frequency-resolved ToAs

### 4. LOFAR – German Station DE605
- **General Comments**:
  - DE605 was used in two separate observation periods, again with differing frequency setups.
  - It forms an integral part of the GLOW dataset enabling long-term monitoring.
  
- **Supporting Quote**:  
  “DE605 … 2014-03-07 to 2015-01-23 and 2015-02-06 to 2018-02-11” (from Table 1).

#### Data Collection Periods:
- **Data Collection Period 1: Early Observations with DE605**
  - **Time Range**: 2014-03-07 to 2015-01-23
    - **Supporting Quote**: “DE605 … 2014-03-07 to 2015-01-23”
  - **Wavelength(s)**: Central frequency of 149.9 MHz and a bandwidth of 95.31 MHz
    - **Supporting Quote**: “fc: 149.9 MHz, Bandwidth: 95.31 MHz” (from Table 1)
  - **Physical Observable**: Pulsar radio emission, used to compute DM time series

- **Data Collection Period 2: Later Observations with DE605**
  - **Time Range**: 2015-02-06 to 2018-02-11
    - **Supporting Quote**: “DE605 … 2015-02-06 to 2018-02-11”
  - **Wavelength(s)**: Central frequency of 153.8 MHz with a bandwidth of 71.48 MHz
    - **Supporting Quote**: “fc: 153.8 MHz, Bandwidth: 71.48 MHz” (from Table 1)
  - **Physical Observable**: High-precision timing and DM variations across the observed bandwidth

### 5. Wilcox Solar Observatory (WSO) with CSS Extrapolation
- **General Comments**:
  - The Wilcox Solar Observatory provides synoptic magnetic field maps critical for extrapolating the Solar corona’s magnetic structure.
  - These maps are employed in conjunction with the CSS extrapolation scheme to infer heliographic coordinates of the neutral field line.
  
- **Supporting Quote**:  
  “charts of the coronal magnetic ﬁeld provided by the Wilcox Solar Observatory (WSO)...” and “The synoptic charts can be found at: http://wso.stanford.edu/forms/prsyn.html.”

#### Data Collection Period:
- **Time Range**: Not explicitly provided in the paper; the WSO maps are updated regularly (weekly) as indicated by their use for magnetic field mapping at given Modified Julian Dates (e.g. MJD 57132).
- **Wavelength(s)/Physical Observable**:  
  - Not directly related to radio frequencies; the instrument measures magnetic fields (in µT) based on photospheric observations extrapolated to the corona.

### 6. SOHO – LASCO Coronagraph
- **General Comments**:
  - The Large Angle and Spectrometric Coronagraph onboard the SOlar and Heliospheric Observatory (SOHO LASCO) is used to identify and catalogue coronal mass ejections (CMEs).
  - It provides white-light coronagraph images showing the polarized brightness of the Solar corona, which are essential for studying transient SW events.
  
- **Supporting Quote**:  
  “...the catalogue provided by the Large Angle and Spectrometric COronagraph onboard of the SOlar and Heliospheric Observatory satellite (LASCO/SOHO)...” and “the catalogue lists detected CMEs only up to the end of October 2017.”

#### Data Collection Period:
- **Time Range**:  
  - The CME catalogue used in the paper covers events up to the end of October 2017.  
  - **Supporting Quote**: “...the catalogue lists detected CMEs only up to the end of October 2017,” while the pulsar dataset extends until 17 February 2018.
- **Wavelength(s)/Physical Observable**:  
  - Observations in white-light (visible wavelengths), with polarization measurements to detect brightness variations in the Solar corona corresponding to CMEs.

### 7. Nançay Radio Telescope
- **General Comments**:
  - Mentioned in the context of earlier pulsar timing experiments and for collecting data on solar passages, specifically for PSR J1824−2452A.
  - It serves as an example of previous work (e.g. by You et al. 2007) that relied on low-frequency pulsar observations.
  
- **Supporting Quote**:  
  “...datasets collected at the Nançay Radio Telescope during four solar passages of PSR J1824−2452A (with an ecliptic latitude of −1.55 degrees)...”
  
#### Data Collection Period:
- **Time Range**:  
  - Not specified in this paper.
- **Wavelength(s)/Physical Observable**:  
  - Operates primarily in radio frequencies (typically L-band and other bands); here it is mentioned in relation to pulsar timing and DM correction.

### 8. Westerbork Synthesis Radio Telescope (WSRT)
- **General Comments**:
  - Referenced as one of the telescopes used in high-precision pulsar-timing observations, for example in the European Pulsar Timing Array (EPTA) projects.
  - Its data are compared with those from other instruments (such as the Nançay Radio Telescope) in timing analyses.
  
- **Supporting Quote**:  
  “...observations collected with the Nançay Radio Telescope at L-band and the Westerbork Synthesis Radio Telescope at three different frequencies from P- to L-band.” 

#### Data Collection Period:
- **Time Range**:  
  - Not explicitly provided in the paper.
- **Wavelength(s)/Physical Observable**:  
  - Observations cover a range from P-band to L-band; these observations contribute to the precise timing (e.g. ToA measurements) of pulsars in the context of PTA experiments.

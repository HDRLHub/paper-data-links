_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper

- **Content Summary**: This study presents a statistical analysis of solar phenomena associated with global EUV waves. The authors apply the automated CorPITA algorithm to high-cadence synoptic data from the Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO), focusing on the 211 Å EUV wavelength band, to systematically identify and track global coronal EUV waves from 2010–2016. The wave events are linked to solar flares, CMEs, solar energetic particle (SEP) events, and type II radio bursts. For in-situ SEP measurements, data from the 3D EESA/PESA instruments on the Wind spacecraft are analyzed for each wave event. Type II radio burst data are sourced from NOAA/SWPC daily lists, covering radio frequency observations contemporaneous with the EUV events. The integral findings depend on the direct analysis of AIA/SDO imaging (for wave detection and characterization), Wind 3DP (for SEP flux/time-of-arrival analysis), and NOAA event lists (for radio burst association), all referenced back to specific, precisely logged event dates and times.

## Instrumentation Details

---

### Atmospheric Imaging Assembly (AIA) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
  - The primary instrument used for direct observation and analysis of global EUV waves. Almost all wave kinematics, detections, and subsequent physical interpretations are derived from high-cadence AIA 211 Å images, as processed by the CorPITA algorithm. The 211 Å passband is selected based on optimal wave visibility.
- **Supporting Quote**: "CorPITA is an automated code designed to identify, track and analyse global EUV waves using science quality data from the SDO/AIA 211 ˚A passband."

#### Data Collection Period 1: Global Wave Detection and Tracking (Event Catalogue)
- **Time Range**: 12 June 2010 – 17 September 2015 (full date context for processed events)
  - **Supporting Quote**: "Due to limitations inherent to the approach taken by CorPITA, it was not possible to analyse all of the events identiﬁed by Nitta et al. (2013)... As a result, of the 410 wave events identiﬁed by Nitta et al. (2013), only 362 could be analysed using CorPITA. 164 events were classiﬁed as having global waves by CorPITA, with no waves found for the remaining 198 events. The output from CorPITA for all events studied is listed in Table 1."
- **Wavelength(s)**: 211 Å (EUV)
  - **Supporting Quote**: "CorPITA is an automated code designed to identify, track and analyse global EUV waves using science quality data from the SDO/AIA 211 ˚A passband."
- **Physical Observable**: Propagation of global coronal EUV waves (also referenced as “EIT waves”)
  - **Supporting Quote**: "The 211 ˚A passband was used here as it observes slightly hotter plasma than the 193 ˚A passband and as a result does not have as much emission from the background corona, making the global wave easier to identify and characterise."
- **Additional Comments**: Data include synoptic imaging for each event start/end time as presented in the large catalogue in the Appendix (Table 1)—each row represents a specific event date/time.

---

### 3-Dimensional Electron Electrostatic Analyzer/Proton Electrostatic Analyzer (3D EESA/PESA) on board Wind
- **General Comments**:
  - Used for in-situ detection of solar energetic particles (SEP) (electrons and protons) to identify particle events temporally associated with EUV waves. The analysis involves energy-differentiated fluxes and event onset detection.
- **Supporting Quote**: "The SEP events associated with each global wave event were identiﬁed using measurements from the 3D EESA/PESA (Lin et al., 1995) instrument onboard the Wind spacecraft."

#### Data Collection Period 2: SEP Event Detection for Each Wave
- **Time Range**: 8 hours before to 16 hours after the associated solar flare for each event between 12 June 2010 – 17 September 2015 (for each entry in Table 1, contextualized to flare/wave start date)
  - **Supporting Quote**: "The data for electrons of energies between ≈1.3 keV and ≈27 keV and protons of energies between ≈195 keV and ≈4.4 MeV were exam-ined for 24 hours around (8 hours before and 16 hours after) the start time of the associated solar ﬂare."
- **Wavelength(s)/Channel(s)**: Not applicable; particle detector, but specific energy channels used: electrons ≈1.3–27 keV, protons ≈195 keV–4.4 MeV
  - **Supporting Quote**: "The data for electrons of energies between ≈1.3 keV and ≈27 keV and protons of energies between ≈195 keV and ≈4.4 MeV were exam-ined for 24 hours around (8 hours before and 16 hours after) the start time of the associated solar ﬂare."
- **Physical Observable**: SEP fluxes of electrons and protons; velocity dispersion and onset analysis to infer SEP release times
  - **Supporting Quote**: "The onset times were then calculated using a Poisson cumulative sum (CUSUM) method (cf. Huttunen-Heikinmaa, Valtonen, and Laitinen, 2005)... Once an onset time was determined for each energy level, a velocity dispersion analysis was used to determine the release time of the particles from the Sun (e.g. Reames, 2009)."
- **Additional Comments**: Data are obtained from the NASA CDAW website for each event and include differential flux measurements per energy channel, linked directly to each AIA/SDO event’s flare start time.

---

### NOAA Space Weather Prediction Center (SWPC) – International Radio Burst Event Lists
- **General Comments**:
  - Used to identify the presence, timing, frequency, and drift speeds of type II radio bursts for correlation with the timing of each AIA/SDO wave event. Not a physical detector but an event log derived from a global network of ground-based solar radio observatories.
- **Supporting Quote**: "The type II radio bursts associated with each global wave event were identiﬁed using the daily lists of radio bursts collated by the Space Weather Prediction Centre located at the National Oceanic and Atmospheric Administration (NOAA/SWPC)."

#### Data Collection Period 3: Radio Type II Burst Association for Each Wave
- **Time Range**: For each wave event, ±90 minutes from the flare/wave start time over 12 June 2010 – 17 September 2015 as per event catalogue
  - **Supporting Quote**: "A window 90 minutes either side of the start time of the global wave was used to look for associated events in the NOAA/SWPC list."
- **Wavelength(s)**: Radio frequencies (frequency range determined by each individual event entry in the SWPC list)
  - **Supporting Quote**: "For each candidate radio burst associated with a global wave, the SWPC list provides an associated start time, end time, observatory used to make the observation, frequency range of the burst and estimated drift speed."
- **Physical Observable**: Type II solar radio bursts (shock signatures in the corona at metric to decametric frequencies); drift rates and durations
  - **Supporting Quote**: "For each candidate radio burst associated with a global wave, the SWPC list provides an associated start time, end time, observatory used to make the observation, frequency range of the burst and estimated drift speed."
- **Additional Comments**: Used as an event-matching reference, not as primary radio data; direct association with AIA/SDO event dates/times.

---

**Note**: SOHO/LASCO and STEREO spacecraft, though extensively discussed in background, were not used directly for data analysis in this paper; their catalogues were only referenced for event association or discussion, per instructions these instruments are excluded.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper presents the Automated detection of coronaL MAss ejecta origiNs for space weather AppliCations (ALMANAC) software package, which forecasts early signatures of coronal mass ejections (CMEs) in the low solar atmosphere in real time. The primary objective is to improve CME arrival time predictions and their potential impact on Earth. The method is applied to historical data sets, specifically focusing on observations by the Atmospheric Imaging Assembly (AIA) aboard the Solar Dynamics Observatory (SDO). The study includes a proof of concept test on a limited set of data associated with twenty halo CMEs recorded by the Coordinated Data Analysis Workshop (CDAW) catalogue near the activity maximum of solar cycle 24. The results show promising accuracy in detecting CME source locations and times, providing a foundation for future work in automated CME alert and forecasting systems.

## Instrumentation Details

### Atmospheric Imaging Assembly (AIA) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
   - The AIA instrument is used to detect and estimate the central coordinates of CME eruptions in Extreme Ultraviolet (EUV) data. The method aims to provide early alerts and initial estimates of CME direction for geometrical modeling.
- **Supporting Quote**: "In this work, ALMANAC is applied to observations by the Atmospheric Imaging Assembly (AIA) aboard the Solar Dynamics Observatory (SDO)."

#### Data Collection Period 1: General CME detection and analysis
- **Time Range**: Various dates and times, including specific periods such as 2010-08-14 08:40 – 2014-12-21 10:50 UT
   - **Supporting Quote**: "SDO/AIA data for each event is processed at 6 minute cadence to identify the on-disk location and time of each CME."
- **Wavelength(s)**: 193 Å
   - **Supporting Quote**: "In this work, the wavelength used for CME detection is 193 Å due to this being the channel with the best signal."
- **Physical Observable**: Rapid changes in the low solar corona, including CME eruptions
   - **Supporting Quote**: "The method detects and estimates the central coordinates of CME eruptions in Extreme Ultraviolet (EUV) data."
- **Additional Comments**: The AIA data is processed at a 6-minute cadence to identify CME events, and the method is tested on a selected sample of Halo CME events from the CDAW catalogue.

#### Data Collection Period 2: Verification against CDAW catalogue
- **Time Range**: Various dates and times, including specific periods such as 2017-10-25 06:45 – 2021-11-17 08:00 UT
   - **Supporting Quote**: "To verify the robustness of ALMANAC, an additional twenty eight – hour periods (Table 2) are analysed where no events, halo - CME or otherwise, are listed in the CDAW catalogue."
- **Wavelength(s)**: 193 Å
   - **Supporting Quote**: "In this work, the wavelength used for CME detection is 193 Å due to this being the channel with the best signal."
- **Physical Observable**: Detection of false positives and verification of non-CME events
   - **Supporting Quote**: "ALMANAC is correctly and effectively detecting and recording temporal changes in the low corona, although it is prone to false positives."
- **Additional Comments**: The verification process includes analyzing periods with no listed events in the CDAW catalogue to assess the false positive rate of ALMANAC.

---

This detailed list includes all instruments mentioned in the provided context, along with their respective time ranges, specific detectors, wavelengths of light, and physical observables used. The information is organized to ensure clarity and completeness.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This study investigates the East-West (longitudinal) asymmetric distribution of solar proton events (SPEs) observed near Earth's orbit over the period 1996–2011. The research analyzes a data set of 78 SPEs with a focus on the longitudinal position of solar sources relative to the observer's nominal Parker spiral magnetic footpoint. The analysis is statistical and draws results from direct observation data, specifically the timing, source, proton flux, flare association, and solar wind conditions for each event. Data from the Space Weather Prediction Center (SWPC) of NOAA for proton events, and in-situ solar wind speeds measured by two spacecraft—SOHO and ACE—were used to form the basis of the research findings. The study utilizes GOES spacecraft for proton event detection, and SOHO and ACE for event-associated solar wind conditions covering the full period from 1996 to 2011.

## Instrumentation Details

### GOES Spacecraft (Geostationary Operational Environmental Satellite)
- **General Comments**:
  - Proton fluxes that define and characterize the solar proton events were obtained from the GOES spacecraft, as indicated by the SPE event listing source and acknowledgments.
- **Supporting Quote**: "The 78 solar proton events affecting the Earth environment detected during 1996-2011 are collected from Space Weather Prediction Center of National Oceanic and Atmospheric Administration (NOAA)."  
- **Supporting Quote**: "We benefited from the solar proton events data provided by the Space Weather Prediction Center of NOAA and the instrument teams of GOES spacecraft."

#### Data Collection Period 1: Statistical dataset for all analyzed solar proton events
- **Time Range**: 1996-01-01 – 2011-12-31 (all events studied occurred during this interval)
  - **Supporting Quote**: "The 78 solar proton events affecting the Earth environment detected during 1996-2011 are collected from Space Weather Prediction Center of National Oceanic and Atmospheric Administration (NOAA)."
- **Wavelength(s)**: Not specified (GOES proton detectors measure particle flux, not wavelength)
  - **Supporting Quote**: "The maximum intensity of each solar proton event for energies > 10 MeV is larger than 10 particle flux units (pfu)."
- **Physical Observable**: Solar proton flux events with >10 MeV energy (SPEs)
  - **Supporting Quote**: "The maximum intensity of each solar proton event for energies > 10 MeV is larger than 10 particle flux units (pfu). Note that 1 pfu=1 particles/(cm2 −sr −s)."
- **Additional Comments**: The event list is based explicitly on GOES measurements as curated by the NOAA SWPC, with selection criteria involving energy (>10 MeV) and event threshold (≥10 pfu).

---

### SOHO (Solar and Heliospheric Observatory)
- **General Comments**:
  - SOHO is used to provide routine in-situ solar wind speed measurements, which are essential to determine the nominal Parker spiral footpoint location for each SPE during its maximum phase.
- **Supporting Quote**: "The last three columns in Table A1 provide the solar wind speeds measured by spacecraft Solar and Heliospheric Observatory (SOHO), ACE, and the mean value of them, respectively."

#### Data Collection Period 1: Solar wind speeds at SPE event maxima
- **Time Range**: For each event, ±2 hours around the event maximum for every event in the 1996-01-01 to 2011-12-31 range; default to full day if specific data is missing.
  - **Supporting Quote**: "By averaging SOHO or ACE data measured in the time interval [Tmax −2hr, Tmax +2hr], in which Tmax indicates the maximum time of the corresponding SEP event, we can obtain the solar wind speed in each SEP event."
  - **Supporting Quote**: "if there are not valid solar wind speed data in the time range [Tmax −2hr, Tmax +2hr] for a certain solar proton event, the averaged solar wind speed obtained from the complete observational data on the whole day when the maximum of the event occurred will be used."
- **Wavelength(s)**: Not applicable (SOHO in-situ plasma measurements; not electromagnetic wavelengths)
  - **Supporting Quote**: "solar wind speeds measured by spacecraft Solar and Heliospheric Observatory (SOHO)..."
- **Physical Observable**: Solar wind bulk speed (km/s)
  - **Supporting Quote**: "The last three columns in Table A1 provide the solar wind speeds measured by spacecraft Solar and Heliospheric Observatory (SOHO), ACE, and the mean value of them, respectively."
- **Additional Comments**: SOHO solar wind data is used either alone or averaged with ACE data, depending on concurrent data availability for each event.

---

### ACE (Advanced Composition Explorer)
- **General Comments**:
  - ACE is used along with SOHO for in-situ solar wind speed at times corresponding to the maximum proton flux for each event in the analyzed interval.
- **Supporting Quote**: "The last three columns in Table A1 provide the solar wind speeds measured by spacecraft Solar and Heliospheric Observatory (SOHO), ACE, and the mean value of them, respectively."
- **Supporting Quote**: "otherwise, the solar wind speed derived from the measurements by a single spacecraft (SOHO or ACE) will be used."

#### Data Collection Period 1: Solar wind speeds at SPE event maxima
- **Time Range**: For each event, ±2 hours around event maximum for all events in 1996-01-01 to 2011-12-31; fallback to complete day if targeted data is unavailable.
  - **Supporting Quote**: "By averaging SOHO or ACE data measured in the time interval [Tmax −2hr, Tmax +2hr], in which Tmax indicates the maximum time of the corresponding SEP event, we can obtain the solar wind speed in each SEP event."
- **Wavelength(s)**: Not applicable (in-situ plasma measurement)
  - **Supporting Quote**: "solar wind speeds measured by spacecraft... ACE..."
- **Physical Observable**: Solar wind bulk speed (km/s)
  - **Supporting Quote**: "The last three columns in Table A1 provide the solar wind speeds measured by spacecraft Solar and Heliospheric Observatory (SOHO), ACE, and the mean value of them, respectively."
- **Additional Comments**: ACE data is used either independently or averaged with SOHO, for every event depending on availability.

---

**End of Instrumentation Form**

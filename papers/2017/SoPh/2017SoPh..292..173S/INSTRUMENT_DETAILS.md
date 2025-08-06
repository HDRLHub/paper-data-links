_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper

- **Content Summary**: This paper evaluates and compares the effectiveness of different forecasting algorithms for Solar Energetic Particle (SEP) events by directly analyzing historical data. The study defines, implements, and tests several simple algorithms based on fast CME events and X-class solar flares, as well as a hybrid combining both parameters, in their relationship to SEP events detected at Earth. SEP event identification is rigorously defined by threshold increases in >40 MeV proton intensities as recorded by the suite of GOES spacecraft from April 1980 through March 2013, using energy channels specific to each satellite and utilizing both raw and intercalibrated data. CME parameters are derived from the CDAW SOHO/LASCO CME catalog based on visual inspection of LASCO C2 and C3 coronagraph data; flare parameters and heliographic coordinates come from the GOES SXR Flare List, with supplemental position information from SolarSoft and EUV imagery from SOHO/EIT and SDO/AIA at 195 Å and 193 Å, respectively. The study period covers two significant time ranges: January 11, 1996 – March 31, 2013 for simultaneous CME and flare data, and April 1, 1980 – March 31, 2013 for flare data. The foundational data for the results consists entirely of direct instrument observations as listed below.

## Instrumentation Details

---

### X-Ray Sensor (XRS) on board GOES [Geostationary Operational Environmental Satellites]

- **General Comments**:
  - GOES/XRS data are the principal dataset for identifying, classifying, and timing solar flares. The 1–8 Å SXR (soft X-ray) channel is used for quantitative flare class assignment and timing in the forecasting algorithms.
- **Supporting Quote**:  
  "Solar ﬂares are classiﬁed by their peak SXR emission as measured in the 1 - 8 ˚A channel of the Geostationary Observational Environmental Satellites (GOES) (Grubb, 1975) X-ray Sensor (XRS) instruments."

#### Data Collection Period 1: Flare dataset for algorithm application and analysis
- **Time Range**: 1980-04-01 – 2013-03-31 (with main focus 1996-01-11 – 2013-03-31 for combined CME-flare association)
  - **Supporting Quote**:  
    "We evaluate both the forecasting algorithms over the time range from 11 January 1996 until 31 March 2013 (“time range 1”); for algorithm A.2 we are also able to examine a longer period, between 1 April 1980 and 31 March 2013 (“time range 2”)."
- **Wavelength(s)**: 1–8 Å (soft X-ray)
  - **Supporting Quote**:  
    "Solar ﬂares are classiﬁed by their peak SXR emission as measured in the 1 - 8 ˚A channel of the Geostationary Observational Environmental Satellites (GOES) (Grubb, 1975) X-ray Sensor (XRS) instruments."
- **Physical Observable**: Peak soft X-ray emission (flare class), heliographic coordinates, flare start/peak/end times.
  - **Supporting Quote**:  
    "Flares with a peak ﬂux in this energy channel above 10^{-4} W m^{-2} are designated to be of class X; those with a peak ﬂux between 10^{-5} and 10^{-4} W m^{-2} are of class M; classes C, B, and A are deﬁned in a similar fashion."
- **Additional Comments**:
  - "As our source for solar ﬂare data we have used the GOES SXR Flare List which has been continuously maintained since 1975, and which may be downloaded from the website3 of the Heliophysics Integrated Observatory (Bentley et al., 2011)."

---

### Energetic Particle Sensors (EPS) and related proton detectors on board GOES spacecraft

- **General Comments**:
  - Direct measurement of >40 MeV proton intensities for SEP event identification across a multi-decade period, using the GOES Energetic Particle Sensors suite. Specific satellite and channel assignments are listed, with data downloaded and intercalibrated by the SEPEM (ESA Solar Energetic Particle Environment Monitor) team when available.
- **Supporting Quote**:  
  "For this study we have used GOES SEP data because they allow us to study SEP events over a time period of more than 30 years. No one instrument has been in continuous operation during that time, and so we have had to use data from a number of diﬀerent GOES satellites. Table 2 sets out which spacecraft we have used and the energy channel considered to establish the occurrence of an SEP event."

#### Data Collection Period 1: Proton flux measurements for >40 MeV SEP identification
- **Time Range**: 1980-04-01 – 2013-03-31; spacecraft epochs as follows:  
    - GOES 2: 1980-04-01 – 1983-12-31  
    - GOES 6: 1984-01-01 – 1987-03-31  
    - GOES 7: 1987-04-01 – 1995-02-28  
    - GOES 8: 1995-03-01 – 2003-01-07  
    - GOES 12: 2003-01-08 – 2009-12-31  
    - GOES 11: 2010-01-01 – 2010-12-31  
    - GOES 13: 2011-01-01 – 2013-03-31
  - **Supporting Quote**:  
    "Table 2 sets out which spacecraft we have used and the energy channel considered to establish the occurrence of an SEP event. There are slight diﬀerences in the energy channels, particularly in the case of GOES 2, but we take the view that the diﬀerences are so small as to have a negligible eﬀect upon our results."
- **Wavelength(s)**: N/A (Particle energies: see energy bands below)
  - **Supporting Quote**:  
    "Table 2. Instruments used to obtain data on proton intensity, the dates between which data from that instrument was used, and the energy channels which have been analysed. ... Column 4 shows the range of proton energies measured by the instrument we have used, and column 5 whether the data was raw or had been cleaned by the SEPEM team."
- **Physical Observable**: >40 MeV proton flux, time profile, and SEP event identification according to specified threshold increase.
  - **Supporting Quote**:  
    "Particles accelerated by solar events include electrons, protons, and heavier ions, but we have chosen to analyse high energy (> 40 MeV) protons. ... We set Ithr to be a 2.5-fold increase in proton intensity over the quiet-time background level."
- **Additional Comments**:
  - "We downloaded data from the European Space Agency’s Solar Energetic Particle Environment Monitor (SEPEM) website (Crosby et al., 2010)6. Data from 1 April 1987 onwards had been cleaned and intercalibrated by the SEPEM team; prior to that date we used their raw data."

---

### LASCO C2 and C3 Coronagraphs on board SOHO [Solar and Heliospheric Observatory]

- **General Comments**:
  - Major source of CME parameterization, including speed (linear fit), width, and first appearance time, using manual identifications from LASCO C2 and C3 images through the CDAW CME Catalog.
- **Supporting Quote**:  
  "As our source for CME data we have used the Co-ordinated Data Analysis Workshop (CDAW) CME catalogue2 (Gopalswamy et al., 2009). This catalogue is produced manually, CMEs being identiﬁed visually from images obtained by the C2 and C3 coronagraphs of the Large Angle and Spectrometric Coronagraph Experiment (LASCO) (Brueckner et al., 1995)) on board the Solar and Heliospheric Observatory (SOHO) spacecraft."

#### Data Collection Period 1: CME dataset for algorithm application and analysis
- **Time Range**: 1996-01-11 – 2013-03-31
  - **Supporting Quote**:  
    "We evaluate both the forecasting algorithms over the time range from 11 January 1996 until 31 March 2013 (“time range 1”)"
- **Wavelength(s)**: White light coronagraph; not WAVELENGTH per se, but visible light (optical)
  - **Supporting Quote**:  
    "...CMEs being identiﬁed visually from images obtained by the C2 and C3 coronagraphs..."
- **Physical Observable**: CME speed (linear), width, first appearance time, position angle.
  - **Supporting Quote**:  
    "Information is published in the catalogue on various CME parameters including, inter alia, the time it is ﬁrst seen in the LASCO images, its width, and its position angle. CDAW publishes three values for the speed of CMEs in its catalogue, each calculated by diﬀerent means: we use the ﬁrst, the “linear” speed, which is obtained simply by ﬁtting a straight line to the height-time measurements."
- **Additional Comments**:
  - "All the CMEs in our sample were from the front-side of the Sun and had an associated ﬂare which was used to determine the coordinates."

---

### Extreme ultraviolet Imaging Telescope (EIT) on board SOHO

- **General Comments**:
  - Used to estimate heliographic coordinates of solar flares for events not adequately listed in standard catalogs, and to confirm flare–CME associations.
- **Supporting Quote**:  
  "Making our own estimate of co-ordinates by watching movies of 195 ˚A images taken by the Extreme ultraviolet Imaging Telescope (EIT) on board the SOHO spacecraft or of 195 ˚A images taken by the Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO)."

#### Data Collection Period 1: Position estimation and event association
- **Time Range**: 1996-01-11 – 2013-03-31 (as needed, event-driven)
  - **Supporting Quote**:  
    "We developed a method of making associations between CMEs and ﬂares automatically which we set out in Appendix A. ... to be sure we also viewed 195 ˚A (obtained by the EIT on board SOHO) and 193 ˚A (obtained by the AIA on board SDO) movies of each solar event."
- **Wavelength(s)**: 195 Å (EUV)
  - **Supporting Quote**:  
    "...movies of 195 ˚A images taken by the Extreme ultraviolet Imaging Telescope (EIT) on board the SOHO spacecraft..."
- **Physical Observable**: Flare and CME source region identification, visual confirmation of eruption, active region position.
  - **Supporting Quote**:  
    "For each of the intense ﬂares, identiﬁcation was done visually from the AIA / SDO movies. We looked for increases in intensity on the solar surface at the time of the ﬂare speciﬁed by the GOES SXR list, but in cases where the site of the ﬂare was not obvious we accepted the reported coordinates."
- **Additional Comments**:
  - Used to help confirm event associations where automatic catalog association was ambiguous or unavailable.

---

### Atmospheric Imaging Assembly (AIA) on board SDO [Solar Dynamics Observatory]

- **General Comments**:
  - Used for visual identification and confirmation of flare source regions and flare–CME temporal/spatial associations, particularly using 193 Å channel movies.
- **Supporting Quote**:  
  "...movies of 195 ˚A images taken by the Extreme ultraviolet Imaging Telescope (EIT) on board the SOHO spacecraft or of 195 ˚A images taken by the Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO)."

#### Data Collection Period 1: Position estimation and event association
- **Time Range**: 2010-02-11 (SDO launch) – 2013-03-31 (used as needed for event analysis during overlap with EIT data)
  - **Supporting Quote**:  
    "We also viewed 195 ˚A (obtained by the EIT on board SOHO) and 193 ˚A (obtained by the AIA on board SDO) movies of each solar event."
- **Wavelength(s)**: 193 Å (EUV)
  - **Supporting Quote**:  
    "...movies ... 193 ˚A (obtained by the AIA on board SDO)..."
- **Physical Observable**: Flare/CME source region discrimination, visual confirmation of eruption or dimming, active region localization.
  - **Supporting Quote**:  
    "...we watched movies at 193 ˚A of each one of these events, each movie having been created from data obtained by the Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO) spacecraft."
- **Additional Comments**:
  - Used in combination with EIT for events occurring after SDO launch.

---

### SolarSoft 'Latest Events Flares List' (gevloc) [data compilation, not an instrument, but includes observational support]

- **General Comments**:
  - Used as an additional resource to obtain heliographic coordinates for flares when not available in the primary GOES SXR Flare List.
- **Supporting Quote**:  
  "In these cases we have used values for co-ordinates from the following sources: 1. Co-ordinates reported in the SolarSoft Latest Events Flares List (gevloc) (which may also be obtained through Helio)."

#### Data Collection Period: Event-driven supplementation across the main data window
- **Time Range**: As needed, 1980-04-01 – 2013-03-31
  - **Supporting Quote**:  
    "In these cases we have used values for co-ordinates from the following sources ..."
- **Wavelength(s)**: Not directly relevant (derivative of other telescopic observations)
- **Physical Observable**: Heliographic coordinates for solar flare events.
  - **Supporting Quote**:  
    "...Co-ordinates reported in the SolarSoft Latest Events Flares List (gevloc)..."
- **Additional Comments**:
  - Used only for events lacking primary catalog coordinates, not as a principal data source.

---

**End of Instrumentation Extraction**

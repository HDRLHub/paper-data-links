_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper presents the development and validation of CAT-PUMA, a machine learning tool for predicting CME (Coronal Mass Ejection) arrival times at Earth, using statistical relationships derived from observational data. The algorithm is trained and tested on a set of 182 geo-effective partial and full-halo CMEs observed from 1996 to 2015. The primary data sources for CME features (onset time, angular width, average speed, final speed, mass, position angle, and source region information) are the SOHO LASCO CME Catalog and the SOHO LASCO Halo CME Catalog. In-situ background solar wind parameters (magnetic field components, plasma density, temperature, velocity, pressure, etc.) are obtained from the OMNIWeb database, covering the propagation period of each event. The observational time range encompasses 182 individual events between 1996 and 2015, with solar wind parameters averaged from CME onset to 6 hours after onset for each event. The direct usage of these observations forms the basis for the machine learning model development and performance assessment.

## Instrumentation Details

### Large Angle and Spectrometric Coronagraph (LASCO) on board SOHO
- **General Comments**:
  - SOHO/LASCO observations are the sole basis for CME feature extraction, including CME onset times, speeds, acceleration, angular width, mass, and position angle. These features directly inform the input vectors for the machine learning model. The studies use cataloged and manual analysis of LASCO observations specifically for each CME between 1996 and 2015 that arrived at Earth.
- **Supporting Quote**: "The SOHO LASCO CME Catalog (https://cdaw.gsfc.nasa.gov/CME_list/) provides a database of all CMEs observed by SOHO LASCO from 1996 to 2016 (Gopalswamy et al. 2009). Via matching the onset time of CMEs in our list with the onset time of CMEs recorded in the SOHO LASCO CME Catalog, we obtain various parameters of them including the angular width, average speed, acceleration, final speed in the FOV of LASCO, estimated mass and main position angle (MPA, corresponding to the position angle of the fastest moving part of the CME’s leading edge). The location of the source region of full halo CMEs can be obtained from the SOHO/LASCO Halo CME Catalog (https://cdaw.gsfc.nasa.gov/CME_list/halo/halo.html). CMEs that have no source-region information in the above catalog are further investigated manually, one-by-one, to determine their source region location."

#### Data Collection Period 1: Extraction and analysis of SOHO LASCO CME events for machine learning dataset
- **Time Range**: 1996–2015 (individual CME events, each with precise onset times, included exclusively if they arrived at Earth)
  - **Supporting Quote**: "We obtain a list of 182 events containing geo-effective CMEs from 1996 to 2015, of which 56 are partial-halo CMEs and 126 are halo CMEs."
- **Wavelength(s)**: White-light coronagraphy; ~2–30 solar radii field of view
  - **Supporting Quote**: "The SOHO LASCO CME Catalog ... provides a database of all CMEs observed by SOHO LASCO from 1996 to 2016 ... we obtain various parameters of them including the angular width, average speed, acceleration, final speed in the FOV of LASCO, estimated mass and main position angle (MPA, corresponding to the position angle of the fastest moving part of the CME’s leading edge)."
- **Physical Observable**: CME onset time in C2 field of view, average speed, final speed, acceleration, angular width, estimated mass, main position angle (MPA), and source region location
  - **Supporting Quote**: "CME features and solar wind parameters, we build a prediction engine ... all inputs will be only observables ... we obtain various parameters of them including the angular width, average speed, acceleration, final speed in the FOV of LASCO, estimated mass and main position angle (MPA, corresponding to the position angle of the fastest moving part of the CME’s leading edge). The location of the source region of full halo CMEs can be obtained from the SOHO/LASCO Halo CME Catalog."
- **Additional Comments**: CME parameters are acquired from both catalog and, when necessary, manual reanalysis of SOHO LASCO data.

---

### OMNI (Omniweb/OMNIWeb Plus) Database (multi-spacecraft compiled solar wind data at 1 AU)
- **General Comments**:
  - OMNIWeb Plus is used for in-situ solar wind parameter extraction at Earth for each CME event, including magnetometer and plasma data, over the period from CME onset until 6 hours after onset for each event. These parameters serve as input features for the machine learning analysis.
- **Supporting Quote**: "In-situ solar wind observations at the Earth, including solar wind Bx, By, Bz, plasma density, alpha to proton ratio, flow latitude (North/South direction), flow longitude (East/West direction), plasma beta, pressure, speed and proton temperature, are downloaded from the OMNIWeb Plus (https://omniweb.gsfc.nasa.gov/)."

#### Data Collection Period 1: Averaged in-situ solar wind parameters after each CME onset
- **Time Range**: For each CME event from 1996–2015, OMNI data are averaged from the CME onset time to six hours post-onset; this is repeated for all 182 events
  - **Supporting Quote**: "Because, currently it is not feasible to determine the actual background solar wind plasma where a CME is immersed, therefore we use averaged in-situ solar wind parameters at Earth detected from the onset of the CME to m hours later to approximate the actual solar wind parameters at the CME location ... we found, using 6-hour averaged solar wind parameters after the CME onset can result in the best output."
- **Wavelength(s)**: Not applicable—these are in-situ measurements of magnetic field and plasma by multiple spacecraft (OMNI is a merged near-Earth database)
  - **Supporting Quote**: "In-situ solar wind observations at the Earth, including solar wind Bx, By, Bz, plasma density, alpha to proton ratio, flow latitude (North/South direction), flow longitude (East/West direction), plasma beta, pressure, speed and proton temperature, are downloaded from the OMNIWeb Plus (https://omniweb.gsfc.nasa.gov/)."
- **Physical Observable**: Magnetic field components (Bx, By, Bz), plasma density, proton temperature, solar wind speed, plasma beta, pressure, alpha/proton number ratio, flow latitude, flow longitude
  - **Supporting Quote**: "Solar wind features including magnetic field Bz and Bx ... proton temperature, plasma pressure, plasma speed, flow longitude (toroidal direction of the solar wind plasma flow) ... alpha particle to proton number density ratio in solar wind also ranks high in all the features... we use averaged in-situ solar wind parameters at Earth detected from the onset of the CME to m hours later ..."
- **Additional Comments**: Only those features with normalized F-score above 0.01 (plus CME MPA) are used as input for the final model; time-averaging period for solar wind is 6 hours after each onset.

---

#### Note:
No other space- or ground-based instruments are directly used for data analysis/modeling in this paper. All other observational references (STEREO, etc.) are discussed only in context of previous work or comparative literature and are not sources of directly analyzed data in the construction or validation of the CAT-PUMA model.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This paper describes the construction and operation of the Interactive Multi-Instrument Database of Solar Flares (IMIDSF), which aggregates, processes, and makes accessible solar flare observations from numerous distinct instruments and catalogs. The research objectives are centered on building a tool that enables multi-instrument, multi-wavelength analysis of flares, providing integrated physical descriptors and event metadata such as start, peak, and end times, flare position, GOES class, maximum temperature, and emission measure. Primary data sources include the GOES X-ray Sensor (XRS) onboard GOES satellites, RHESSI, and the Atmospheric Imaging Assembly (AIA) on SDO, as well as secondary sources like IRIS, Hinode, Fermi GBM, Nobeyama Polarimeter, OVSA, CACTus CME catalog, Filament eruption catalog, and Konus-Wind. Data recording periods span January 2002 through the present (for most instruments), except for instruments with limited operation durations. Light curves and physical parameter time profiles are generated and visualized, and each data source's coverage is detailed, offering concrete dates and observing context.

## Instrumentation Details

---

### GOES X-ray Sensor (XRS) onboard GOES Satellites
- **General Comments**:
  - The GOES XRS instrument provides soft X-ray observations (1–8 Å and 0.5–4 Å bands) for flare detection and classification. Its data underpins the main list of solar flares in the database, with further derived temperature and emission measure calculated for every event using the TEBBS background subtraction algorithm.
- **Supporting Quote**:  
  "The daily lists of events observed by the GOES satellites in the 1-8 ˚A channel are available from June 2002 to present. The reported characteristics include the GOES class, the X-ray peak ﬂux during the event, and the information about the active region and coordinates of the event (not for all events)."  

#### Data Collection Period 1: GOES daily flare detection and parameter derivation
- **Time Range**: January 2002 – current time (present); (continuous daily coverage)
  - **Supporting Quote**:  
    "GOES ﬂare list. The daily lists of events observed by the GOES satellites in the 1-8 ˚A channel are available from June 2002 to present."
- **Wavelength(s)**: 1–8 Å and 0.5–4 Å
  - **Supporting Quote**:  
    "GOES X-ray light curves (two channels 0.5-4 ˚A and 1-8 ˚A)."
- **Physical Observable**: Integrated soft X-ray flux; derived flare characteristics (start, peak, end times, GOES class, X-ray peak flux, active region number, and, where possible, coordinates; plus Temperature and Emission Measure time profiles)
  - **Supporting Quote**:  
    "Important physical properties derived from the GOES X-ray observations are Temperature (T) and Emission Measure (EM) ... These parameters can be deﬁned for each moment of time, and provide T and EM proﬁles for every ﬂare. In our database, we characterize ﬂares by the peak values of these parameters (Tmax and EMmax), as well as by the times when these peak values are reached."
- **Additional Comments**:  
  - Data are updated daily. T and EM derived using the TEBBS algorithm, which is applied "for every event."  
  - Data available as downloadable and visualized light curves.

---

### RHESSI (Reuven Ramaty High Energy Solar Spectroscopic Imager) X-ray Telescope
- **General Comments**:
  - RHESSI data are directly used for identification and description of solar flares in the database, specifically targeting hard X-ray emission across multiple energy bands. For each RHESSI flare, the highest energy observed and counts are recorded and matched with other data sources when integrating event listings.
- **Supporting Quote**:  
  "RHESSI ﬂare list. The list of the ﬂares observed by the RHESSI X-ray telescope from February 2002 to present. Besides the usual descriptors (the ﬂare times and position), the catalog contains the highest energy band in which the ﬂares were observed, the number of counts during the ﬂares, and a variety of observational quality ﬂags."

#### Data Collection Period 1: RHESSI event detection and energy band analysis
- **Time Range**: February 2002 – current time (present)
  - **Supporting Quote**:  
    "RHESSI ﬂare list. The list of the ﬂares observed by the RHESSI X-ray telescope from February 2002 to present."
- **Wavelength(s)**: X-ray, 6 keV to >300 keV (multiple energy bands)
  - **Supporting Quote**:  
    "RHESSI observes the X-ray radiation of ﬂares in a wide range of energies, from 6 keV to > 300 keV."
- **Physical Observable**: Hard X-ray flux, highest observed energy band, number of counts per flare, times and positions of each event
  - **Supporting Quote**:  
    "the catalog contains the highest energy band in which the ﬂares were observed, the number of counts during the ﬂares, and a variety of observational quality ﬂags."
- **Additional Comments**:  
  - Flare entries from RHESSI are matched by time and position with GOES and HEK events, Unified Event IDs are constructed.

---

### SDO/AIA (Atmospheric Imaging Assembly) on Solar Dynamics Observatory
- **General Comments**:
  - The AIA instrument (as incorporated through the HEK Flare list) provides high-cadence EUV imaging that is directly processed to detect flare events using image processing algorithms. Flare event parameters include different detected wavelengths, event coordinates, and intensity parameters. 
- **Supporting Quote**:  
  "HEK SDO/AIA event list. The events detected in the EUV images from the AIA/SDO instrument from February 2010 to present. The events reported in this catalog are characterized by a variety of diﬀerent parameters (besides the common ones): the wavelength in which the event was detected, the coordinates in a variety of coordinate systems, peak ﬂuxes, web links to quick-look images and movies, etc."

#### Data Collection Period 1: Automated EUV Flare Detection with AIA
- **Time Range**: February 2010 – current time (present)
  - **Supporting Quote**:  
    "HEK SDO/AIA event list. The events detected in the EUV images from the AIA/SDO instrument from February 2010 to present."
- **Wavelength(s)**: Multiple EUV bands (Specific band reported per event)
  - **Supporting Quote**:  
    "the wavelength in which the event was detected"
- **Physical Observable**: EUV brightenings attributed to flares, with parameters including time, position, detected wavelength, and derived flux
  - **Supporting Quote**:  
    "The events reported in this catalog are characterized by a variety of diﬀerent parameters...the wavelength in which the event was detected, the coordinates in a variety of coordinate systems, peak ﬂuxes..."
- **Additional Comments**:  
  - Light curves and quicklook images/movies are generated for each event.

---

### SDO/EVE ESP (EUV SpectroPhotometer) on Solar Dynamics Observatory
- **General Comments**:
  - EVE/ESP diode channel data are provided as background observation for all covered events, giving solar irradiance time profiles at four EUV wavelengths.
- **Supporting Quote**:  
  "SDO/EVE ESP light curves (four diode channels: 18 nm, 26 nm, 30 nm, 36 nm)."

#### Data Collection Period 1: Solar EUV irradiance monitoring during flares
- **Time Range**: [Implied to be February 2010 – current time, coverage as available]
  - **Supporting Quote**:  
    "SDO/EVE ESP light curves (four diode channels: 18 nm, 26 nm, 30 nm, 36 nm)."
- **Wavelength(s)**: 18 nm, 26 nm, 30 nm, 36 nm (discrete diode channels)
  - **Supporting Quote**:  
    "SDO/EVE ESP light curves (four diode channels: 18 nm, 26 nm, 30 nm, 36 nm)."
- **Physical Observable**: EUV solar irradiance variations during flare intervals
  - **Supporting Quote**:  
    "SDO/EVE ESP light curves (four diode channels: 18 nm, 26 nm, 30 nm, 36 nm)."
- **Additional Comments**:  
  - 10-second averaging applied to ESP data for event visualizations.

---

### Interface Region Imaging Spectrograph (IRIS)
- **General Comments**:
  - The IRIS instrument's observing logs and summary data are cross-matched by time and pointing to flares in the database; events are associated where IRIS spatially and temporally overlaps with a flare. Quicklook data links and coverage descriptors are provided.
- **Supporting Quote**:  
  "The Interface Region Imaging Spectrograph data (IRIS, De Pontieu et al. 2014). IRIS obtains the slit-jaw UV images, as well as spectra of the Sun. The ﬂare events are associated with IRIS observations based on the time and pointing stored in the form of instrument observing logs. The quicklook data web links allow the users to select the events of interest."

#### Data Collection Period 1: IRIS coverage/association with flare events
- **Time Range**: July 2013 – current time (coverage per IRIS operation schedule)
  - **Supporting Quote**:  
    "IRIS observing logs       Jul, 2013 — current time            http://iris.lmsal.com/search/"
- **Wavelength(s)**: UV imaging and spectra (exact bands dependent on IRIS observing mode)
  - **Supporting Quote**:  
    "IRIS obtains the slit-jaw UV images, as well as spectra of the Sun."
- **Physical Observable**: UV images and spectra during solar flares; slit positions, field of view
  - **Supporting Quote**:  
    "IRIS obtains the slit-jaw UV images, as well as spectra of the Sun."
- **Additional Comments**:  
  - The database tracks coverage, slit positions, and summarizes overlap with flare events.

---

### Hinode Spacecraft Instruments
- **General Comments**:
  - Observation logs from Hinode (multiple potential instruments) are matched with GOES-listed flares, allowing identification of flares observed by Hinode and their associated instrument Quicklooks and coverage data.
- **Supporting Quote**:  
  "Hinode ﬂare catalog (Watanabe et al. 2012). The original catalog includes the events from the GOES ﬂare list observed by the Hinode spacecraft. This catalog includes the availability of observations for each Hinode instrument, and quicklook data links."

#### Data Collection Period 1: Hinode observations during GOES-listed flares
- **Time Range**: November 2006 — July 2016
  - **Supporting Quote**:  
    "Hinode ﬂare catalog      Nov, 2006 — July, 2016   http://st4a.stelab.nagoya-u.ac.jp/hinode_flare/"
- **Wavelength(s)**: Varies by Hinode instrument; database logs presence or absence of coverage
  - **Supporting Quote**:  
    "This catalog includes the availability of observations for each Hinode instrument, and quicklook data links."
- **Physical Observable**: Coordinated EUV/X-ray/optical (as instrument specific) observations of flares
  - **Supporting Quote**:  
    "availability of observations for each Hinode instrument, and quicklook data links."
- **Additional Comments**:  
  - Database records event coverage rather than downloads of raw instrument data.

---

### Fermi Gamma-ray Burst Monitor (GBM)
- **General Comments**:
  - Fermi GBM flare data (counts, duration, highest energy range) are integrated as secondary physical descriptors for relevant flare events.
- **Supporting Quote**:  
  "Fermi Gamma-ray Burst Monitor (GBM, Meegan et al. 2009) solar ﬂare catalog. The list of the ﬂares observed by the Fermi GBM in the 8 keV-40 MeV energy range from November 2008 to present. This catalog includes duration of the observed ﬂares and number of counts during the ﬂares."

#### Data Collection Period 1: Fermi GBM detections of solar flares
- **Time Range**: November 2008 — current time
  - **Supporting Quote**:  
    "Fermi GBM ﬂare catalog   Nov, 2008 — current time  https://hesperia.gsfc.nasa.gov/fermi/gbm/qlook/"
- **Wavelength(s)**: 8 keV – 40 MeV (gamma-ray and hard X-ray range)
  - **Supporting Quote**:  
    "The list of the ﬂares observed by the Fermi GBM in the 8 keV-40 MeV energy range from November 2008 to present."
- **Physical Observable**: Flare-associated hard X-ray/gamma-ray photon counts, event durations
  - **Supporting Quote**:  
    "This catalog includes duration of the observed ﬂares and number of counts during the ﬂares."
- **Additional Comments**:  
  - Data used for additional event description and cross-catalog queries.

---

### Nobeyama Radio Polarimeter (NoRP)
- **General Comments**:
  - Nobeyama's polarimetric radio observations provide daily light curves (six frequencies, two polarizations each) that are extracted and visualized for every flare event falling within Nobeyama's operational observing window.
- **Supporting Quote**:  
  "Nobeyama Radio-polarimeter light curves (Nakajima et al. 1994). The polarimetric measurements from Nobeyama Radio Observatory are available for almost every day, usually approximately 8 hours per day."

#### Data Collection Period 1: Routine radio polarimeter coverage and light curves
- **Time Range**: January 2010 — current time (approximately daily, coverage during NoRP operating hours)
  - **Supporting Quote**:  
    "Nobeyama coverage check   Jan, 2010 — current time    ftp://solar-pub.nao.ac.jp/pub/nsro/norp/xdr/"
- **Wavelength(s)**: 1 GHz, 2 GHz, 3.75 GHz, 9.4 GHz, 17 GHz, 35 GHz (each in I and V polarizations)
  - **Supporting Quote**:  
    "Nobeyama Polarimeter data (six frequency bands, two polarizations: 1 GHz, 2 GHz, 3.75 GHz, 9.4 GHz, 17 GHz, 35 GHz, I and V polarizations for each frequency)."
- **Physical Observable**: Time variation of solar radio flux and polarization during flares
  - **Supporting Quote**:  
    "Nobeyama Polarimeter data (six frequency bands, two polarizations: 1 GHz, 2 GHz, 3.75 GHz, 9.4 GHz, 17 GHz, 35 GHz, I and V polarizations for each frequency)."
- **Additional Comments**:  
  - 10-second averaging of NoRP data is applied for smoothing before visualization.

---

### OVSA (Owens Valley Solar Array)
- **General Comments**:
  - OVSA's microwave flare events (summaries in 1–18 GHz) are included for the period 2001–2003 for short time intervals where available.
- **Supporting Quote**:  
  "OVSA legacy ﬂare catalog (Nita et al. 2004), which includes short-time summaries of events observed by the Ovens Valley Solar Array in the 1-18 GHz microwave range, from 2001 to 2003 only."

#### Data Collection Period 1: OVSA microwave event records
- **Time Range**: January 2002 — December 2003
  - **Supporting Quote**:  
    "OVSA ﬂare catalog       Jan, 2002 — Dec, 2003            http://www.ovsa.njit.edu/data/"
- **Wavelength(s)**: 1–18 GHz (microwave)
  - **Supporting Quote**:  
    "short-time summaries of events observed by the Ovens Valley Solar Array in the 1-18 GHz microwave range"
- **Physical Observable**: Microwave emission during flares (event summary parameters)
  - **Supporting Quote**:  
    "short-time summaries of events observed by the Ovens Valley Solar Array in the 1-18 GHz microwave range"
- **Additional Comments**:  
  - Coverage limited to designated flare events within OVSA operational period.

---

### CACTus CME Catalog (SOHO LASCO CME Analyses)
- **General Comments**:
  - LASCO/SOHO CME observations are cross-referenced to flare records in the database using the CACTus CME catalog, which lists onset time, principal angle, and velocity for each CME event.
- **Supporting Quote**:  
  "Computer Aided CME Tracking (CACTus) catalog (Robbrecht & Berghmans 2004; Robbrecht et al. 2009). This catalog collects records of CMEs detected by the LASCO/SOHO coronograph, and contains a variety of CME properties, including the onset time, principal angle, velocity, etc."

#### Data Collection Period 1: Association of CACTus CME events with flares
- **Time Range**: January 2002 — current time
  - **Supporting Quote**:  
    "CACTus CME catalog    Jan, 2002 — current time             http://sidc.oma.be/cactus/"
- **Wavelength(s)**: White-light coronagraphic imaging (LASCO on SOHO)
  - **Supporting Quote**:  
    "CACTus CME catalog … records of CMEs detected by the LASCO/SOHO coronograph"
- **Physical Observable**: CME parameters—onset time, principal angle, and velocity; associated with solar flare time and location
  - **Supporting Quote**:  
    "contains a variety of CME properties, including the onset time, principal angle, velocity, etc."
- **Additional Comments**:  
  - CME–flare matching is performed based on predefined adjustable time intervals.

---

### Filament Eruption Catalog
- **General Comments**:
  - The database associates flare events with filament eruptions using time and position data from this catalog, which records parameters of solar filament eruptions based on SDO/AIA.
- **Supporting Quote**:  
  "Filament eruption catalog (McCauley et al. 2015). The ﬁlament-ﬂare event matching is based on the time and position of the eruptions. A variety of ﬁlament parameters are available. The catalog production was stopped on Oct, 19, 2014."

#### Data Collection Period 1: Filament eruptions associated with flare events
- **Time Range**: April 2010 — October 19, 2014
  - **Supporting Quote**:  
    "Filament eruption catalog    Apr, 2010 — Oct, 2014         http://aia.cfa.harvard.edu/filament/"
- **Wavelength(s)**: SDO/AIA EUV imaging (wavelength not specified in quote; database uses catalog event descriptors)
  - **Supporting Quote**:  
    "Filament eruption catalog (McCauley et al. 2015). The ﬁlament-ﬂare event matching is based on the time and position of the eruptions."
- **Physical Observable**: Filament eruption event parameters; temporal and spatial association to flare events
  - **Supporting Quote**:  
    "A variety of ﬁlament parameters are available."
- **Additional Comments**:  
  - Only catalog events before October 19, 2014.

---

### Konus-Wind Flare Catalog (Konus Instrument on Wind Spacecraft)
- **General Comments**:
  - The Konus-Wind space-based hard X-ray/gamma-ray detector's flare events are integrated into the database for cross-matching, including corresponding event times and gamma-ray detections.
- **Supporting Quote**:  
  "Konus-Wind ﬂare catalog (Aptekar et al. 1995; Pal’shin et al. 2014). The original catalog includes the events from the GOES ﬂare list observed by the Konus-Wind spacecraft."

#### Data Collection Period 1: Konus-Wind gamma-ray flare event association
- **Time Range**: January 2002 — July 2016
  - **Supporting Quote**:  
    "Konus-Wind ﬂare catalog     Jan, 2002 — Jul, 2016       http://www.ioffe.ru/LEA/Solar/index.html"
- **Wavelength(s)**: Gamma-ray/hard X-ray (energy range not specified)
  - **Supporting Quote**:  
    "Konus-Wind ﬂare catalog ... includes the events from the GOES ﬂare list observed by the Konus-Wind spacecraft."
- **Physical Observable**: Cataloged gamma-ray flare events with temporal association to GOES
  - **Supporting Quote**:  
    "The original catalog includes the events from the GOES ﬂare list observed by the Konus-Wind spacecraft."
- **Additional Comments**:  
  - Data used for catalog-level integration and event parameter augmentation.

---

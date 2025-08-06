_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  The paper investigates the subsurface horizontal flows in the largest active region of solar cycle 24, NOAA 12192, and compares its properties to those of NOAA 10486, a similar major active region from cycle 23. The primary research objective is to understand the differences in subsurface flow characteristics and their connection to flare and CME productivity. The study analyzes data spanning multiple Carrington rotations for AR 12192 (CR 2155–2158, corresponding to September–December 2014) and AR 10486 (CR 2009–2010, corresponding to October–November 2003). Subsurface flows are derived using the ring-diagram technique applied to high-cadence Dopplergrams from the Global Oscillation Network Group (GONG+), supplemented by line-of-sight magnetograms for magnetic activity indexing. Statistical baselining is conducted using magnetogram and velocity data from the solar activity minimum in 2008 for quiet Sun references. Frontside and farside imaging employ EUV observations from SDO/AIA and STEREO, as well as helioseismic maps from GONG and SDO/HMI, to track the AR evolution. However, direct quantitative analysis and flow derivation is performed on GONG+ Dopplergram data and accompanying GONG and SOHO/MDI magnetograms, forming the empirical foundation of the paper's results.

## Instrumentation Details

---

### Global Oscillation Network Group (GONG+) Doppler Imager
- **General Comments**:
  - GONG+ Dopplergrams form the principal data set for helioseismic analysis using the ring-diagram technique to derive subsurface flows beneath AR 12192 (2014) and AR 10486 (2003); data are analyzed at a cadence of 60 s with a spatial format of 1k × 1k pixels.
- **Supporting Quote**:  
  "We utilize 1k × 1k continuous Doppler images from GONG at a cadence of 60 s."

#### Data Collection Period 1: AR 12192 tracked across four Carrington rotations
- **Time Range**: 2014 September 21 – 2014 December 21, for multiple 1664-min time series per disk location, specifically detailed as:  
  - CR 2155: 2014 Sep 21 16:28UT – 2014 Sep 30 19:07UT  
  - CR 2156: 2014 Oct 18 23:18UT – 2014 Oct 28 02:05UT  
  - CR 2157: 2014 Nov 15 06:32UT – 2014 Nov 24 09:26UT  
  - CR 2158: 2014 Dec 12 14:07UT – 2014 Dec 21 17:06UT
  - (Individual time series for each 15° longitude step; see Table 3 for precise times)
  - **Supporting Quote**:  
    "The start and end of each time series representing AR 12192 and AR 10486 at different disk locations are listed in Tables 3 and 4, respectively."
- **Wavelength(s)**: Ni I 6768 Å line for photospheric Doppler velocity
  - **Supporting Quote**:  
    "All these instruments use photospheric lines; the GONG and MDI observations are in the Ni I 6768˚A line as opposed to HMI observations in Fe I 6173˚A line."
- **Physical Observable**: Line-of-sight Doppler velocity, used to infer horizontal subsurface flows via the ring-diagram technique
  - **Supporting Quote**:  
    "In the ring-diagram method, high-degree waves propagating in localized areas over the solar surface are used to obtain acoustic mode parameters in the region of interest."
- **Additional Comments**:
  - Data are processed with the GONG ring-diagram pipeline, version 3.6.1.
  - **Supporting Quote**:  
    "It should be noted that we have used custom patches processed through the latest version of the GONG ring-diagram pipeline (version 3.6.1)."

#### Data Collection Period 2: AR 10486 tracked across two Carrington rotations
- **Time Range**: 2003 October 24 – 2003 November 30, for multiple 1664-min time series per disk location, specifically:  
  - CR 2009: 2003 Oct 24 15:58UT – 2003 Nov 02 18:45UT  
  - CR 2010: 2003 Nov 20 23:22UT – 2003 Nov 30 02:11UT
  - (See Table 4 for exact times)
  - **Supporting Quote**:  
    "The start and end of each time series representing AR 12192 and AR 10486 at different disk locations are listed in Tables 3 and 4, respectively."
- **Wavelength(s)**: Ni I 6768 Å line for photospheric Doppler velocity
  - **Supporting Quote**:  
    "All these instruments use photospheric lines; the GONG and MDI observations are in the Ni I 6768˚A line as opposed to HMI observations in Fe I 6173˚A line."
- **Physical Observable**: Line-of-sight Doppler velocity, used to infer horizontal subsurface flows via the ring-diagram technique
  - **Supporting Quote**:  
    "In the ring-diagram method, high-degree waves propagating in localized areas over the solar surface are used to obtain acoustic mode parameters in the region of interest."
- **Additional Comments**:
  - Data cover regions near ±52.5° from disk center where feasible, and duty cycle is monitored.
  - **Supporting Quote**:  
    "Since the duty cycle in GONG observations varies from day-to-day, primarily due to the changing weather conditions at observing sites or to system maintenance/breakdown, the results may be altered. To authenticate our results, we also include duty cycles in Table 3 and Figure 7 for each timeseries."

#### Data Collection Period 3: Quiet Sun reference calibration
- **Time Range**: 2008 September – 2008 December, covering the period of solar minimum for all 15 longitude steps across the disk at 15°S latitude
  - **Supporting Quote**:  
    "The period of 2008 September thru December is used to determine the quiet-region values."
- **Wavelength(s)**: Ni I 6768 Å line for Doppler velocity
  - **Supporting Quote**:  
    "All these instruments use photospheric lines; the GONG and MDI observations are in the Ni I 6768˚A line as opposed to HMI observations in Fe I 6173˚A line."
- **Physical Observable**: Line-of-sight Doppler velocity, for reference calculation of quiet Sun subsurface flows
  - **Supporting Quote**:  
    "We further calculate the components of horizontal velocity corresponding to these quiet regions and compute error-weighted averages of 13 ring days at each location as for MAIs."
- **Additional Comments**:
  - Averages are computed for each 15° longitudinal grid to provide matched baselining for AR/quiet comparisons.

---

### GONG Magnetograms
- **General Comments**:
  - GONG network magnetograms sampled every 32 minutes are used to derive the Magnetic Activity Index (MAI) for all time periods not covered by MDI (specifically 2008 and 2014), enabling quantification of surface magnetic field strength in both AR and quiet Sun reference regions.
- **Supporting Quote**:  
  "we use...GONG magnetograms sampled every 32 minutes for 2008 and 2014."

#### Data Collection Period 1: MAI for AR 12192 and quiet regions
- **Time Range**: 2014 September – 2014 December (aligned with AR 12192 analysis), and 2008 September – 2008 December (for quiet Sun calibration)
  - **Supporting Quote**:  
    "we use...GONG magnetograms sampled every 32 minutes for 2008 and 2014."
- **Wavelength(s)**: GONG magnetograms (line details not specified in text for magnetograms)
- **Physical Observable**: Line-of-sight photospheric magnetic flux density
  - **Supporting Quote**:  
    "we also quantify the magnetic activity in various regions by calculating the Magnetic Activity Index (MAI) in each sample using the line-of-sight magnetic field from the magnetograms."
- **Additional Comments**:
  - Lower threshold of 8.8 G; MAI calculated for each 1664-min "ring day" and then averaged.
  - **Supporting Quote**:  
    "Lower threshold values of 50 and 8.8 G are used for MDI (Basu et al. 2004) and GONG (Tripathy et al. 2015), respectively, which are approximately 2.5 times the estimated noise in the individual magnetograms."

---

### SOHO/MDI (Michelson Doppler Imager) Magnetograms
- **General Comments**:
  - 96-min cadence MDI magnetograms are utilized specifically for the AR 10486 analysis (2003) to calculate MAI, together with the GONG+ Dopplergram analysis.
- **Supporting Quote**:  
  "Since the entire period under study is not covered by the MDI magnetograms alone, we use the 96 minute MDI magnetograms for 2003 and GONG magnetograms sampled every 32 minutes for 2008 and 2014."

#### Data Collection Period 1: MAI for AR 10486 and quiet region reference
- **Time Range**: 2003 October – November (during AR 10486 disk passage and associated quiet region reference periods)
  - **Supporting Quote**:  
    "we use the 96 minute MDI magnetograms for 2003"
- **Wavelength(s)**: Ni I 6768 Å for MDI magnetograms
  - **Supporting Quote**:  
    "All these instruments use photospheric lines; the GONG and MDI observations are in the Ni I 6768˚A line as opposed to HMI observations in Fe I 6173˚A line."
- **Physical Observable**: Line-of-sight photospheric magnetic flux density
  - **Supporting Quote**:  
    "we also quantify the magnetic activity in various regions by calculating the Magnetic Activity Index (MAI) in each sample using the line-of-sight magnetic field from the magnetograms."
- **Additional Comments**:
  - Lower threshold of 50 G applied for MAI determination.
  - **Supporting Quote**:  
    "Lower threshold values of 50 and 8.8 G are used for MDI (Basu et al. 2004) and GONG (Tripathy et al. 2015), respectively"

---

### SDO/AIA and STEREO (for context: not used for quantitative flow analysis)
- **General Comments**:
  - Used only for qualitative EUV imaging and tracking of AR growth/decay and evolutionary context; NO quantitative data from these instruments is directly analyzed for flows or kinetic energy in this paper.
- **Supporting Quote**:  
  "To track the growth and decay of AR 12172 and AR 12173, respectively, in particular on the invisible surface the the Sun, we use 'all Sun' EUV Carrington maps as described in Liewer et al. (2014). These maps are produced by combining EUV frontside images from Atmospheric Imaging Assembly (AIA) on board Solar Dynamics Observatory (SDO) with the backside images from Solar Terrestrial Relations Observatory (STEREO)."

---

### SDO/HMI and GONG Far-side (Helioseismic) Imaging
- **General Comments**:
  - Used for context and visualization of AR evolution on the farside, not for direct subsurface flow or kinetic energy derivations.
- **Supporting Quote**:  
  "Daily helioseismic maps of far side are available at http://jsoc.stanford.edu/data/farside/ using HMI and http://gong2.nso.edu/products/ using GONG observations. The evolution of AR 12192 in multiple CRs is summarized in Table 1."

---

**(End of Instrumentation Form)**

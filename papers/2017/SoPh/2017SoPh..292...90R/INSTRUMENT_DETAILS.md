_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This paper investigates the origin and ion charge state evolution of solar wind transients observed by the ACE spacecraft on 4 – 7 August 2011, which caused a geomagnetic storm. The study identifies associated solar sources, namely three flares and CMEs from AR 11261 on 2 – 4 August 2011. The researchers use multi-instrument observations and numerical simulations to analyze the CME initiation, plasma diagnostics, and charge state evolution. Data from SDO/AIA (EUV images), SDO/HMI (magnetic field maps), ACE (in situ solar wind and ion composition), GOES (X-ray flares), and STEREO-A/EUVI and SOHO/LASCO (CME propagation) provide the basis for the results. Specific observation dates and time periods are meticulously tracked for each event and instrument, forming the foundation for the analysis of CME kinematics, plasma properties, and the comparison between modelled and observed ion charge states.

## Instrumentation Details

---

### Advanced Composition Explorer (ACE)

- **General Comments**:
  - ACE in situ solar wind and ion composition data form the basis for identification of interplanetary CMEs, assessment of plasma parameters, and derivation of ion charge state evolution, especially for the period 4 – 7 August 2011.
- **Supporting Quote**:  
  "We present study of the complex event consisting of several solar wind transients detected by Advanced Composition Explorer (ACE) on 4 – 7 August 2011, that caused a geomagnetic storm with Dst= −110 nT."

#### Data Collection Period 1: In situ solar wind and ion composition during geomagnetic storm
- **Time Range**: 2011-08-04T00:00 UT – 2011-08-07T23:59 UT (inclusive of storm events, using RC ICME list time boundaries and context)
  - **Supporting Quote**:  
    "Figure 1 shows the level 2 one-hour averaged ACE solar wind data for the period 4 – 8 August 2011."
- **Wavelength(s)**: Not applicable (in situ plasma and ion composition, not remote sensing)
- **Physical Observable**:  
  Proton velocity (Vp), proton density (np), proton temperature (Tp), magnetic field (B), charge state ratios of C, O, and Fe (C6+/C5+, O7+/O6+, QFe), Fe/O abundance ratio.
  - **Supporting Quote**:  
    "The solar wind data including the ICME parameters and charge states of C, O and Fe ions were extracted from the ACE data (Stone et al., 1998)."
- **Additional Comments**:  
  The data are used to extract event boundaries, transients, and directly compared with modelled ion charge states for validation.

#### Data Collection Period 2: ICME and charge state identification
- **Time Range**: 2011-08-05T03:00 UT – 2011-08-07T22:00 UT (three transients)
  - **Supporting Quote**:  
    "Table 3. Ion composition parameters of the solar wind transients determined from the QFe enhancements (Figure 2)... Ntrans 1: Aug. 5 03:00 / Aug. 5 14:00... Ntrans 2: Aug. 7 02:00 / Aug. 7 22:00... Ntrans 3: Aug. 6 06:00 / Aug. 7 01:00"
- **Physical Observable**:  
  Ion ratios C6+/C5+, O7+/O6+, mean Fe charge QFe, Fe/O; boundaries of transients in time determined from QFe enhancements.
  - **Supporting Quote**:  
    "The analysis of the ion charge state of the solar wind revealed three transients with enhanced temperature-dependent ratios C6+/C5+ , O7+/O6+ and a mean charge of iron ions QFe, which can be associated with hot plasma released in the coronal sources."

---

### Solar Dynamics Observatory / Atmospheric Imaging Assembly (SDO/AIA)

- **General Comments**:
  - SDO/AIA multi-wavelength EUV images are used for diagnostics of CME initiation, dimmings, expanding loops, plasma temperature, and density measurements via DEM methods.
- **Supporting Quote**:  
  "In the analysis, we used the data from the Solar Dynamic Observatory (SDO): the solar EUV images from the Atmospheric Imaging Assembly telescope (AIA: Lemen et al., 2012)... temperature and density of the outﬂow plasma were deﬁned by the diﬀerential emission measure (DEM) method using the AIA multi-wavelength EUV images."

#### Data Collection Period 1: CME initiation and plasma diagnostics 
- **Time Range**: 2011-08-02T05:30 UT – 2011-08-02T06:10 UT (focus on CME1 formation and DEM diagnostics)
  - **Supporting Quote**:  
    "Figure 4a represents a group of expanding loop-like features in the 211˚A running-diﬀerence image at 05:58:02 UT, 2 August 2011, in the initial stage of CME1 formation (Table 1)."
- **Wavelength(s)**: 94 Å, 131 Å, 171 Å, 193 Å, 211 Å, 335 Å (EUV channels)
  - **Supporting Quote**:  
    "The DEM analysis was carried out, using intensities in six SDO/AIA EUV channels: 94 ˚A, 131 ˚A, 171 ˚A, 193 ˚A, 211 ˚A, and 335 ˚A."
- **Physical Observable**:  
  Running-difference EUV images of expanding CME loops, plasma temperature, electron density derived via DEM, eruptive morphology, and brightness changes.
  - **Supporting Quote**:  
    "We studied the formation of three CMEs on 2 – 4 August 2011 in the low corona using the SDO/AIA images in diﬀerent wavelength channels. After preliminary processing level 1 to level 1.5 data we produced running-diﬀerence images to identify the moving coronal structures associated with a CME."
- **Additional Comments**:  
  Used for quantitative plasma diagnostics in CME source regions and for direct comparison and validation of simulation results.

#### Data Collection Period 2: DEM analysis at specific times 
- **Time Range**: 2011-08-02T05:32 UT, 2011-08-02T05:44 UT, 2011-08-02T05:50 UT (flare region); additional points along CME propagation up to ~06:00 UT
  - **Supporting Quote**:  
    "Table 4. Averaged values of the electron temperature and density in the ﬂare on 2 August 2011 (the parameters were obtained in the region marked with a red cross on the Figure 4a)."
- **Physical Observable**:  
  DEM-derived Te and ne in flare kernel and expanding CME shell.
  - **Supporting Quote**:  
    "The averaged temperatures and densities for the ﬂare on 2 August 2011 are given in Table 4."

---

### Solar Dynamics Observatory / Helioseismic and Magnetic Imager (SDO/HMI)

- **General Comments**:
  - SDO/HMI vector magnetograms are used as input to generate boundary conditions for 3D magnetic field extrapolation and MHD simulation of the CME source region.
- **Supporting Quote**:  
  "The Helioseismic and Magnetic Imager (HMI) magnetic ﬁeld maps were used as the input data for the 3D magnetohydrodynamic (MHD) model to describe the ﬂux rope ejection (Pagano, Mackay, and Poedts, 2013b)."

#### Data Collection Period 1: Time series for model input
- **Time Range**: 2011-07-31T05:00:41 UT – 2011-08-02T06:00:41 UT (magnetograms every 60 minutes)
  - **Supporting Quote**:  
    "In the present application we use 50 magnetograms from 31 July 2011 at 05:00:41 UT to 2 August 2011 at 06:00:41 UT sampled every 60 minutes."
- **Wavelength(s)**: Not applicable (photospheric LOS magnetic field)
- **Physical Observable**:  
  Photospheric magnetic field maps (vector and/or LOS)
  - **Supporting Quote**:  
    "the time series of magnetograms (Mackay, Green, and van Ballegooijen, 2011; Gibb et al., 2014)"
- **Additional Comments**:  
  Used directly as boundary input for non-linear force-free field (NLFF) and subsequent MHD coronal simulations.

---

### Geostationary Operational Environmental Satellite (GOES)

- **General Comments**:
  - GOES soft X-ray flux data are used for timing and diagnostics of solar flare events associated with CME onset.
- **Supporting Quote**:  
  "Diagnostics of ﬂares in the coronal sources were fulﬁlled using the Geostationary Operational Environmental Satellite system (GOES) X-ray data..."

#### Data Collection Period 1: Flare timing during CME initiation
- **Time Range**: 2011-08-02T05:00 UT – 2011-08-02T06:00 UT (CME1 event)
  - **Supporting Quote**:  
    "The solid line corresponds to the the ﬂux from GOES 1.0 – 8.0 ˚A in 10−4 W m−2) (the ﬂare occurred on 2 August 2011)."
- **Wavelength(s)**: 1.0–8.0 Å (soft X-ray)
  - **Supporting Quote**:  
    "GOES 1.0 – 8.0 ˚A"
- **Physical Observable**:  
  Soft X-ray emission, flare magnitude, flare timing coincident with CME initiation
  - **Supporting Quote**:  
    "Table 2. Flares and CMEs occurred on 2 – 4 August 2011 using data from GOES..."

---

### Solar Terrestrial Relations Observatory / Extreme Ultraviolet Imager (STEREO-A/EUVI/COR2)

- **General Comments**:
  - STEREO-A EUVI and COR2 data are used for tracking CME expansion above the limb, kinematic measurements, and cross-validation of velocities from other instruments and simulations.
- **Supporting Quote**:  
  "triangles to the CME expansion above the limb seen by STEREO-A/EUVI, and the diamonds to the CME expansion seen by LASCO/C2... We associated the transverse distances from the LASCO data with height, assuming the self-similar expansion of the CME, when the vertical, dr, and horizontal, dh, displacements are in the same relation as the radial speed of the CME, vr, measured by STEREO-A/COR2, and the transverse speed, vh, measured by LASCO..."

#### Data Collection Period 1: CME kinematics above the limb 
- **Time Range**: 2011-08-02T06:02:15 UT (first EUVI running-difference image); 2011-08-02T05:54 UT onward (CME1 onset, continuing through CME expansion as tracked)
  - **Supporting Quote**:  
    "The running-diﬀerence image of the CME seen by STEREO-A/EUVI in 171 ˚A at 06:02:15 UT."
- **Wavelength(s)**: 171 Å (EUVI), visible/white-light (COR2)
  - **Supporting Quote**:  
    "the height variation of the CME in the low corona, seen in EUV AIA images (channel 211˚A), and above the limb, seen by STEREO-A/EUVI in 171˚A (Figure 4b) and in the ﬁeld of view of the LASCO C2 coronagraph."
- **Physical Observable**:  
  Projected heights and velocities of expanding CME leading edge, kinematics above the limb
  - **Supporting Quote**:  
    "The visual tracking of the CME in the STEREO images lets us follow the apex of the expanding loops that initiate the CME motion (cross points in Figure 10a)."

---

### Solar and Heliospheric Observatory / Large Angle Spectrometric Coronagraph (SOHO/LASCO C2)

- **General Comments**:
  - LASCO C2 coronagraph data are used for measuring CME expansion into the corona and correlating low-corona to corona (2–6 Rsun) velocities.
- **Supporting Quote**:  
  "above the limb, seen by STEREO-A/EUVI in 171˚A (Figure 4b) and in the ﬁeld of view of the LASCO C2 coronagraph."

#### Data Collection Period 1: CME kinematics in outer corona
- **Time Range**: 2011-08-02T06:36 UT onward (coronal CME observations)
  - **Supporting Quote**:  
    "Table 2. Flares and CMEs occurred on 2 – 4 August 2011 using data from GOES, STEREO-A/COR2 (A) and SOHO/LASCO (L)... 2 Aug. 2011... CME (L) onset time, [UT] 06:36"
- **Wavelength(s)**: Visible/white-light (coronagraphic)
- **Physical Observable**:  
  Position and velocity of CME leading edge above 2 Rsun
  - **Supporting Quote**:  
    "we associated the transverse distances from the LASCO data with height, assuming the self-similar expansion of the CME..."

---

**End of Instrumentation Form**

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper investigates the critical decay index (nc) that governs the eruption of solar prominence (flux rope) structures. By combining stereoscopic measurements of three-dimensional prominence heights with extrapolated coronal magnetic fields, the study determines the critical height at which the prominences transition from a slow- to fast-rise phase. The observations are carried out using multiple instruments – including extreme-ultraviolet imagers, magnetographs, and soft X‐ray and coronagraph detectors – on spacecraft such as SDO, STEREO, GOES, and SOHO. The analysis spans a series of events from 7 March 2011 to 9 May 2015, and emphasizes how the background coronal magnetic field (derived from HMI and PFSS modeling) couples with dynamic indicators (from AIA, EUVI, GOES, LASCO) to pinpoint the onset of torus instability and the associated kinematic acceleration, as well as to evaluate the relative roles of magnetic reconnection and ideal MHD instabilities.

## Instrumentation Details

### 1. Atmospheric Imaging Assembly (AIA) on board the Solar Dynamics Observatory (SDO)
- **General Comments**:
   - AIA is a high-resolution EUV imager that captures full-disk images of the solar corona. It plays a critical role in this study by providing 304 Å images that are used for the tie-pointing method to determine the 3D apex position of erupting prominences.
   - It features a high cadence (12 s) and a fine pixel scale (0″.6), which is essential for accurately tracking rapid changes during both slow- and fast-rise phases.
- **Supporting Quote**: “AIA images the solar corona with a pixel size of 0′′.6 and a high cadence of 12 s…” and “we use simultaneous observations in 304 ˚A waveband of SDO/AIA and STEREO-A.”
  
#### Data Collection Period 1: Representative Event P1
- **Time Range**: Observations on 07-Mar-2011 beginning at approximately 18:49 UT (as seen in the tie-pointing interface) through the fast-rise phase onset at 19:33 UT, with continued imaging during the associated M-class flare (flare onset at 19:42 UT and continuing until at least 20:58 UT as indicated in the model fits).
   - **Supporting Quote**: “Panels in Figure 1(a & b) show the HMI LOS magnetogram and AIA 304 ˚A image of the prominence eruption event P1…”
- **Wavelength(s)**: 304 Å
   - **Supporting Quote**: “…observations in 304 ˚A waveband…”
- **Physical Observable**: EUV intensity images that reveal the morphology and motion (height–time evolution) of the eruptive prominence.

#### Data Collection Period 2: Representative Event P3
- **Time Range**: Observations on 12-Jun-2011 with the tie-pointing initiated around 12:30:00 UT (as marked in Fig. 2) and tracking the prominence through its slow-rise and fast-rise phases, with the fast-rise onset determined at approximately 13:34 UT.
   - **Supporting Quote**: “Start Time (12-Jun-11 12:30:00)” as indicated in Figure 2 and the description of the P3 eruption.
- **Wavelength(s)**: 304 Å
   - **Supporting Quote**: “…using SDO/AIA and STEREO-A… in wavelength passband of 304 ˚A…”
- **Physical Observable**: EUV imaging used to capture prominence dynamics and assist in 3D coordinate determination.

### 2. Extreme Ultraviolet Imager (EUVI) on board STEREO
- **General Comments**:
   - EUVI is part of the SECCHI suite on STEREO and provides EUV images complementary to AIA. Its role is crucial for stereoscopic (dual-view) observations, allowing the determination of the true three-dimensional positions of eruptive features.
   - It captures images in the 304 Å passband with a larger pixel scale and lower cadence relative to AIA.
- **Supporting Quote**: “EUVI images from STEREO have a pixel size of 1′′.6 and obtained at a cadence of 10 minutes.”
  
#### Data Collection Period 1: Representative Event P1
- **Time Range**: Simultaneous with the AIA observations of the P1 event on 07-Mar-2011 (beginning around 18:49 UT through the fast-rise phase); exact EUVI time stamps are coordinated with AIA for tie-pointing.
   - **Supporting Quote**: “...we used near simultaneous observations of SDO/AIA and STEREO-A in wavelength passband of 304 ˚A in scc_measure.pro routine…”
- **Wavelength(s)**: 304 Å
- **Physical Observable**: EUV intensity used for triangulation; contributes to the 3D coordinate measurements of the prominence apex.

#### Data Collection Period 2: Representative Event P3
- **Time Range**: Coordinated with AIA observations on 12-Jun-2011, used for tie-pointing the prominence features simultaneously captured by both STEREO and SDO.
- **Wavelength(s)**: 304 Å
- **Physical Observable**: EUV images that enable 3D reconstruction of the prominence height and structure.

### 3. Helioseismic and Magnetic Imager (HMI) on board the Solar Dynamics Observatory (SDO)
- **General Comments**:
   - HMI provides full-disk line-of-sight (LOS) magnetograms and daily-updated synoptic charts of the photospheric radial magnetic field. These maps are used as the boundary conditions for the potential field source surface (PFSS) model to extrapolate the coronal magnetic field.
   - Its data are indispensable for computing the horizontal component of the background magnetic field, and subsequently the decay index as a function of height.
- **Supporting Quote**: “the daily-updated synoptic chart of the photospheric radial magnetic field observations of the Helioseismic and Magnetic Imager (HMI; Schou et al. 2012) on board SDO.”

#### Data Collection Period: For All Events (e.g., P1)
- **Time Range**: The HMI synoptic maps corresponding to the event date are used; for example, the HMI LOS magnetogram shown in Figure 1(a) for the P1 event on 07-Mar-2011.
- **Wavelength(s)/Observable**: Magnetically sensitive spectral lines (specific wavelength not detailed here) providing LOS magnetic field data.
- **Physical Observable**: Photospheric magnetic field strength and polarity distributions critical for constructing coronal field extrapolations via the PFSS model.

### 4. Geostationary Operational Environmental Satellite (GOES)
- **General Comments**:
   - GOES provides continuous full-disk soft X-ray (SXR) flux measurements of the Sun. These data are used to characterize flare onset times, classification (e.g., M3.7, B8.1, etc.), and correlate the timing with the kinematic phases of prominence eruptions.
- **Supporting Quote**: “Geostationary Operational Environmental Satellite (GOES) provides the soft X-ray (SXR) flux integrated from the full solar disk…”

#### Data Collection Period 1: Representative Event P1
- **Time Range**: For the P1 event on 07-Mar-2011, the GOES SXR flux is plotted beginning from around the onset of the fast-rise phase (19:33 UT) and clearly marks flare onset at 19:42 UT, with the flare evolution monitored through at least 20:58 UT.
   - **Supporting Quote**: “Red vertical dashed line (19:42 UT) marks the onset of the M3.7 ﬂare associated with this eruption.”
- **Wavelength(s)**: Soft X-rays (no specific passband given; integrated full-disk measurement).
- **Physical Observable**: SXR flux serving as a proxy for flare energy release and magnetic reconnection signatures.

#### Data Collection Period 2: Representative Event P10
- **Time Range**: For the P10 event on 09-May-2015, GOES observations capture the flare onset at 01:11 UT following the fast-rise phase that begins at 01:01 UT.
   - **Supporting Quote**: “The time of onset of ﬂare during P1 and P10 events are 19:42 UT and 01:11 UT respectively…”
- **Wavelength(s)**: Soft X-rays.
- **Physical Observable**: Variations in the soft X-ray flux indicating the timing and magnitude of the flare-associated energy release.

### 5. LASCO (Large Angle and Spectrometric Coronagraph) on board SOHO
- **General Comments**:
   - LASCO is used to detect and track coronal mass ejections (CMEs) in the extended corona. Its coronagraph images help identify the CME attributes following prominence eruptions.
   - The instrument’s data complement the disk observations by providing information on the subsequent propagation of ejecta beyond the low corona.
- **Supporting Quote**: “…the eruption leads to a halo CME observed in LASCO C2/C3 FOV” and “CME linear speed (obtained from SOHO LASCO CME catalog: https://cdaw.gsfc.nasa.gov/CME_list/).”

#### Data Collection Period: For Relevant CME Events (e.g., P1, P3)
- **Time Range**: Although specific time stamps for LASCO observations are not given in detail, the CME is observed after the prominence eruptions (e.g., following P1’s fast-rise phase on 07-Mar-2011 and P3 on 12-Jun-2011). The LASCO fields-of-view (C2/C3) capture the CME as it propagates outward.
- **Wavelength(s)/Observable**: White-light coronagraph images capturing scattered photospheric light from the CME plasma.
- **Physical Observable**: CME morphology and propagation speed, which are used to compute linear speeds (e.g., 2125 km/s for P1, 493 km/s for P3).

### 6. SECCHI 3D Coordinate Measuring Interface (Part of the STEREO Suite)
- **General Comments**:
   - Although primarily an analysis tool rather than a stand-alone instrument, the SECCHI 3D coordinate measuring interface is used to triangulate the three-dimensional positions of prominence features by combining STEREO-A EUVI images with SDO/AIA images.
   - This interface allows the researcher to select a feature in one image, display the corresponding epipolar line in the other, and thereby determine the true height of the prominence apex.
- **Supporting Quote**: “Screenshot of SECCHI 3D coordinate measuring interface. STEREO-A and SDO images are in left and right panels respectively…” (see Fig. 3).
- **Data Collection Period**: 
   - **Time Range**: Utilized during the P1 event on 07-Mar-2011 when the tie-pointing method was applied to obtain the true 3D coordinate of the prominence feature.
- **Wavelength(s)/Observable**: Works with EUV images in the 304 Å passband provided by both STEREO and SDO.
- **Physical Observable**: Provides the three-dimensional coordinate (height) measurements required for de-projection of the prominence motion.

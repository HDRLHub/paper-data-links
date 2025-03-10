_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper introduces CAMEL, a novel automatic tool that employs deep learning and computer vision techniques for the detection and tracking of coronal mass ejections (CMEs). The research primarily uses white-light coronagraph images – especially from the LASCO C2 instrument onboard SOHO – to classify, detect, and track CMEs. The paper details the three-module pipeline (image classification using a convolutional neural network, CME region co-localization via PCA and deep descriptor transforming, and region refinement with a graph cut method) and demonstrates its performance through comparisons with existing catalogs that employ different detection methods. The observations used in the study are drawn from two main observational periods: one for training (10-month LASCO C2 data from January to October 2011, during solar maximum) and the other for detection and tracking (running-difference images from November 2011 to April 2012). In addition, the paper briefly mentions data obtained by other instruments and missions (namely STEREO’s SECCHI package with COR1 and COR2 coronagraphs, and curated datasets from SDO) as part of broader CME study efforts.

## Instrumentation Details

### 1. LASCO C2 on board SOHO
- **General Comments**:
   - LASCO C2 is the primary instrument used in this study for obtaining white-light coronagraph images that contain CME structures. The tool processes the raw Level 0.5 FITS files, performs calibration (including dark current, flat field, stray light, distortion, vignetting, photometry, time and position corrections), and then produces Level 1 data. The images are initially 1024×1024 in resolution and then down-sampled to 512×512 for CME detection and tracking.
   - **Supporting Quote**: “Before we going through the pipeline, all coronagraph data are processed in the following way: the downloaded level 0.5 LASCO C2 fits files are read with lasco_readfits.pro from the Solar Software (SSW), and then processed to level 1 data using reduce_level_1.pro...”
  
#### Data Collection Period 1: Training Dataset
- **Time Range**: January 2011 – October 2011  
   - **Supporting Quote**: “The training set of data are ten‐month LASCO C2 images from January to October 2011 around the solar maximum whose category label is known.”
- **Wavelength(s)**: White-light  
   - **Supporting Quote**: “...a given white‐light coronagraph image to CME‐detected category or CME‐not‐detected category.”
- **Physical Observable**: CME structures (brightness variations / running-difference features)
   - **Supporting Quote**: “Our goal is to detect and track pixel-level CME regions in a set of white-light coronagraph images by using machine learning methods.”
- **Additional Comments**: This dataset is used to train the convolutional neural network (LeNet-5 architecture) for image classification and initial localization of CME features.

#### Data Collection Period 2: Detection and Tracking Dataset
- **Time Range**: November 2011 – April 2012  
   - **Supporting Quote**: “By applying the method described above, we have detected and tracked the CMEs from the LASCO C2 running-difference images in the time range from November 2011 to April 2012.”
- **Wavelength(s)**: White-light (processed as running-difference images)  
   - **Supporting Quote**: “The input of the system is a sequence of running-difference images observed by LASCO C2 and processed to level 1.”
- **Physical Observable**: CME evolution observed as variations in the white-light intensity in running-difference images; extraction of fundamental parameters such as first appearance time, central position angle, angular width, and velocity.
   - **Supporting Quote**: “For a tracked CME we offer the following five fundamental parameters: first appearance time in the LASCO C2 FOV (Tstart), central position angle (CPA), angular width (AW), median and maximal velocities (Vmed and Vmax).”
- **Additional Comments**: The high-resolution detection and tracking pipeline, including image pre-processing and coordinate transformation (cartesian to polar), is optimized for these LASCO C2 data.

### 2. COR1 and COR2 on board STEREO (SECCHI Instrument Package)
- **General Comments**:
   - The paper mentions that with the launch of the STEREO mission, CME observations benefit from dual perspectives provided by two coronagraphs, COR1 and COR2. These instruments are part of the Sun Earth Connection Coronal and Heliospheric Investigation (SECCHI) package.
   - **Supporting Quote**: “Since the launch of the Solar TErrestrial RElations Observatory (STEREO) mission, CMEs can be observed from two diﬀerent perspectives with the coronagraphs COR 1 and COR 2 in the Sun Earth Connection Coronal and Heliospheric Investigation (SECCHI, Howard et al. 2008) instrument package.”
- **Time Range**: Not explicitly specified in the context.
- **Wavelength(s)**: Not detailed in the context.
- **Physical Observable**: CME structures as observed in white-light coronagraph imagery from different perspectives.
   - **Supporting Quote**: The context does not provide explicit details on the detectors or specific analysis methods for COR1/COR2 observations.
- **Additional Comments**: While these instruments are mentioned to highlight the evolution of CME observational capabilities, they are not directly used in the CAMEL pipeline described in the paper.

### 3. Solar Dynamics Observatory (SDO)
- **General Comments**:
   - The SDO mission is mentioned as an example of another source of solar observational datasets that have been curated in a format suitable for machine learning studies. This highlights the broader context in which machine learning is being applied in solar physics.
   - **Supporting Quote**: “Very recently, Galvez et al. (2019) even compiled a curated dataset for the Solar Dynamics Observatory (SDO) mission in a format suitable for the booming machine learning research.”
- **Time Range**: Not specified in the context.
- **Wavelength(s)**: Not provided; SDO typically observes in multiple wavelengths, but the paper does not elaborate on specifics.
- **Physical Observable**: Although not detailed in this paper, SDO observations generally include high-resolution images of the solar disk in ultraviolet and extreme ultraviolet wavelengths to study various solar phenomena.
- **Additional Comments**: The SDO reference serves to underscore the growing availability of curated solar datasets aimed at applying machine learning techniques, although it is not the data source used in the CAMEL pipeline.

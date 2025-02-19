_This commentary was initially drafted by an AI model. Please use with caution_

1. SOHO/LASCO (Large Angle and Spectrometric Coronagraph)
   - **General Comments**:  
     SOHO’s LASCO instrument is used to capture coronagraph images that reveal the structure and propagation of coronal mass ejections (CMEs). It provides crucial images for determining the CME start time and for deriving three‐dimensional CME input parameters via techniques such as the Graduated Cylindrical Shell (GCS) model.
   - **Supporting Quote**:  
     “Typically, coronagraph images from the Large Angle and Spectrometric Coronagraph Experiment (LASCO: Brueckner et al. [1995]) instrument on the SO‐lar and Heliospheric Observatory (SOHO: Domingo et al. [1995]), and the Sun Earth Connection Coronal and Heliospheric Investigation [SECCHI: Howard et al., 2008] instruments on the Solar TErrestrial RElations Observatory (STEREO: Kaiser et al. [2008]) Ahead (A)/Behind (B) spacecraft are used.”
   - **Data Collection Period Examples**:  
     - *Training Event Example*:  
       - **Time Range**: For Event 1 in Table 8, the CME “input” is recorded with a “CME start time” around the event date 2010-04-03. In this example, the magnetogram timestamp associated with the measurement is “mrbqs 2010-04-03T11:54” and the “time at 21.5R⊙” is given as “(2010-04-03T15:00)”.  
       - **Supporting Quote** (from Table 8 context): “Event 1 … Event date time (CDAW catalog) 2010-04-03 10:33 UT … time at 21.5R⊙ (2010-04-03T15:00)”.
     - *Validation Event Periods*:  
       - The validation event set (which relies on observations from instruments like LASCO) is drawn from two periods: 1 January 2011 – 31 December 2012 and 1 January 2015 – 31 December 2015.

2. STEREO/SECCHI
   - **General Comments**:  
     The SECCHI instruments onboard the STEREO spacecraft (both Ahead and Behind) capture stereoscopic coronagraph images that are utilized for 3D reconstruction of CMEs. These observations help in estimating the CME kinematics (such as velocity and angular width) when combined with forward modeling techniques.
   - **Supporting Quote**:  
     “... and the Sun Earth Connection Coronal and Heliospheric Investigation [SECCHI: Howard et al., 2008] instruments on the Solar TErrestrial RElations Observatory (STEREO: Kaiser et al. [2008]) Ahead (A)/Behind (B) spacecraft are used.”
   - **Data Collection Period Details**:  
     - *Availability Distinction*:  
       The paper notes a deliberate split into two validation periods partly to distinguish periods with and without available STEREO-B data.  
       - **Time Range (for period with STEREO-B)**: 1 January 2011 – 31 December 2012.
       - **Time Range (for period without STEREO-B)**: 1 January 2015 – 31 December 2015.

3. SDO/AIA (Solar Dynamics Observatory/Atmospheric Imaging Assembly)
   - **General Comments**:  
     The SDO/AIA instrument, observing in multiple wavelengths (for example the 193 Å channel), is mentioned as one of the instruments that can be associated with the CME onset. It provides high-resolution images of the solar corona which are useful for identifying the onset time and context of CME-associated activity.
   - **Supporting Quote**:  
     “CME: CME onset time – Associated instrument(s) e.g. SDO/AIA 193 ˚A”
   - **Time Range Details**:  
     Specific time stamps for SDO/AIA observations are not directly provided in the text. However, its data is implied to contribute to the CME onset determination during various events in the validation and training sets.

4. GONG (Global Oscillation Network Group) – as utilized in ADAPT-driven magnetograms
   - **General Comments**:  
     GONG ground-based observatories provide magnetogram data that feed into models such as ADAPT and subsequently into heliospheric simulations (e.g., via WSA-ENLIL). This magnetogram data is essential for determining the photospheric magnetic field conditions that are later used as boundary conditions for solar wind and CME propagation models.
   - **Supporting Quote**:  
     “Currently SWPC operational forecasts use … driven by data from the Global Oscillation Network Group [GONG: Harvey et al., 1996] ground observatories … For the purposes of this project …”
   - **Data Collection Period Details**:  
     - For the SWPC/CCMC project, a set of 33 historical events over a three-year period from 2012–2014 is mentioned, with output from GONG-instrument-driven models used as inputs.  
     - In simulations using time-dependent sequences of input magnetograms from GONG, a six-hour time cadence is used.

5. mrbqs Magnetogram Data (as recorded in Table 8)
   - **General Comments**:  
     The “mrbqs” magnetograms are referenced in the training event set (Table 8) as the specific magnetogram timestamps associated with the CME measurements. They provide the timing for the magnetogram images that serve as inputs for the CME fitting procedures.
   - **Supporting Quote**:  
     In Table 8, the following magnetogram timestamps are provided:  
     “mrbqs 2010-04-03T11:54”, “mrbqs 2013-03-15T07:14”, “mrbqs 2014-01-07T19:14”, “mrbqs 2015-03-15T02:04”.
   - **Data Collection Periods**:  
     - **Event 1**: 2010-04-03T11:54  
     - **Event 2**: 2013-03-15T07:14  
     - **Event 3**: 2014-01-07T19:14  
     - **Event 4**: 2015-03-15T02:04  
     These timestamps are examples drawn from the core training event set and illustrate when magnetogram data (as collected by the mrbqs system) are used to determine solar source properties prior to CME propagation analysis.

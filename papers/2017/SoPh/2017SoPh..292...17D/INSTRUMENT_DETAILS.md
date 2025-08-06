_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**:  
  This paper investigates the relationship between coronal mass ejection (CME) speeds and two primary observational factors: (i) the total photospheric magnetic flux swept out by flare ribbons during eruptive events, and (ii) the rate of decay of horizontal magnetic fields with height above eruption sites as determined from potential field coronal models. The study analyzes 16 Earth-directed ("halo") CME events occurring from 1998 to 2005. Data sources include line-of-sight magnetograms from the Michelson Doppler Imager (MDI) onboard the SOHO spacecraft and flare ribbon observations from the Big Bear Solar Observatory (BBSO) in Hα as well as the UV channel of the Transition Region and Coronal Explorer (TRACE) spacecraft. CME speeds were obtained from the CDAW CME list, which uses data from the Large Angle Spectroscopic Coronagraph (LASCO) onboard SOHO. The authors use these data to create event-specific source region masks, perform potential field extrapolations, calculate decay indices, and correlate these parameters with CME velocities to assess their respective roles in CME acceleration.

## Instrumentation Details

---

### Michelson Doppler Imager (MDI) on board SOHO
- **General Comments**:
  - MDI LOS magnetograms were the basis for estimating the photospheric and chromospheric magnetic field maps at the active region source of each CME. These data were directly analyzed for mapping magnetic flux swept by flare ribbons and served as the lower boundary for potential field extrapolation to compute overlying field decay indices for all events studied.
- **Supporting Quote**:  
  "Full-disk, line-of-sight (LOS) magnetograms for these events were recorded by the Michelson Doppler Imager (MDI; Scherrer et al. 1995), and Qiu and collaborators extrapolated from the photospheric level to 2000 km, to estimate the ﬂux density near the expected height of formation of ribbon emission."

#### Data Collection Period 1: CME Source Region Mapping and Potential Field Modeling
- **Time Range**: 1998-04-29 to 2005-05-13 (inclusive of all 16 studied events; each event specified by its date and time in Table 1)
  - **Supporting Quote**:  
    "To do so, we study a sample of 16 CME events from a seven year span, from 1998 to 2005. In Table 6, we show event times, solar source locations, CME speeds, and other parameters discussed below."
- **Wavelength(s)**: Measurements of the photospheric magnetic field (no wavelength; LOS magnetograms)
  - **Supporting Quote**:  
    "Full-disk, line-of-sight (LOS) magnetograms for these events were recorded by the Michelson Doppler Imager (MDI; Scherrer et al. 1995)..."
- **Physical Observable**: Photospheric/chromospheric line-of-sight magnetic field strength; structure and total unsigned magnetic flux within flare-affected source regions
  - **Supporting Quote**:  
    "Here, the LOS ﬁeld was used directly as an approximate measure of the radial magnetic ﬁeld, and pixel areas were not corrected for foreshortening from the viewing angle."
- **Additional Comments**:  
  - "Magnetogram data were interpolated onto the grid corresponding to the Hα/TRACE pixels."
  - "To model the ﬁelds overlying a CME’s source area, we extrapolate the potential magnetic ﬁeld’s components above each RPP pixel."

---

### Transition Region and Coronal Explorer (TRACE) Satellite
- **General Comments**:
  - TRACE 1600 Å UV imagery was employed to provide direct observations of flare ribbon emission during some events, serving as the basis for defining ribbon masks to determine the area swept out by flare signatures. These masks were then combined with the co-aligned MDI magnetograms for calculating the associated swept magnetic flux for each event.
- **Supporting Quote**:  
  "Images of ﬂare ribbons were recorded either at Big Bear Solar Observatory, in Hα, or by the TRACE satellite, in UV."

#### Data Collection Period 1: Flare Ribbon Mapping in UV
- **Time Range**: For events specifically identified as TRACE events:  
  2000-07-25 01:39:01,  
  2001-04-10 04:48:02,  
  2001-04-26 09:36:03,  
  2003-10-28 09:35:03,  
  2003-10-29 19:11:03,  
  2003-11-18 06:23:03,  
  2004-11-07 14:23:03  
  (event dates and times as shown in Table 1 for those labeled "T")
  - **Supporting Quote**:  
    "CME  Label,  data  sources  are  identiﬁed by H(Hα) and T(TRACE)."
- **Wavelength(s)**: 1600 Å (UV channel)
  - **Supporting Quote**:  
    "Observers often study ribbons in Hα and UV images (e.g., in the 1600 Å channel of the Transition Region and Coronal Explorer (TRACE) satellite (Handy et al. 1999)."
- **Physical Observable**: Flare ribbon emission—chromospheric/transition region brightenings associated with magnetic reconnection
  - **Supporting Quote**:  
    "Flare ribbons overlie strongly magnetized areas of the photosphere within and near active regions (ARs)..."
- **Additional Comments**:  
  - "TRACE’s 0.5'' pixels were summed 2 x 2."
  - "Magnetogram data were interpolated onto the grid corresponding to the Hα/TRACE pixels."

---

### Big Bear Solar Observatory (BBSO)
- **General Comments**:
  - BBSO was the ground-based source of Hα images capturing flare emission ribbon evolution for events not observed by TRACE. These images were directly used to construct the flare ribbon masks critical to determining reconnected flux.
- **Supporting Quote**:  
  "Images of ﬂare ribbons were recorded either at Big Bear Solar Observatory, in Hα, or by the TRACE satellite, in UV."

#### Data Collection Period 1: Flare Ribbon Mapping in Hα
- **Time Range**: For events specifically identified as Hα events:  
  2000-01-18 16:03:02,  
  2000-08-09 14:23:01,  
  2000-11-24 20:48:02,  
  2001-09-28 07:59:02,  
  2002-03-20 16:00:01,  
  2002-07-26 19:11:00,  
  2005-05-13 16:03:02,  
  1998-04-29 15:59:04,  
  1998-11-05 15:36:04  
  (event dates and times as shown in Table 1 for those labeled "H")
  - **Supporting Quote**:  
    "CME  Label,  data  sources  are  identiﬁed by H(Hα) and T(TRACE)."
- **Wavelength(s)**: Hα spectral line (6563 Å)
  - **Supporting Quote**:  
    "Images of ﬂare ribbons were recorded either at Big Bear Solar Observatory, in Hα..."
- **Physical Observable**: Optical chromospheric flare ribbon emission
  - **Supporting Quote**:  
    "The ﬂare ribbon locations for this event, found from Hα ﬂare observations, are shown (yellow contours) in Figure 1a, plotted over the corresponding magnetogram."
- **Additional Comments**:  
  - Masks defining the cumulative area swept by ribbons were derived from these images and were used to calculate swept unsigned magnetic flux.

---

### Large Angle Spectroscopic Coronagraph (LASCO) on board SOHO
- **General Comments**:
  - LASCO provided the white-light observations necessary for direct measurement of CME velocities. For each event, the plane-of-sky CME speed was sourced from the CDAW CME catalog, derived from LASCO coronagraph data.
- **Supporting Quote**:  
  "The CME speeds that we cite are plane-of-sky speeds; CMEs’ true speeds might be faster, which is an additional source of discrepancy between our simplistic model and the observations."
  - "The speed of each CME, vCME, was taken from the CDAW CME list."
- **Physical Observable**: CME leading-edge position versus time, yielding CME plane-of-sky speed
  - **Supporting Quote**:  
    "Also, ﬂux above an eruption site that is not entrained would still need to be pushed aside, and might thereby impose an “eﬀective drag” on the erupting CME, since this pushing would require doing work against magnetic pressure. Consistent with this picture, Xu et al. (2012) studied 38 CMEs and compared plane-of-sky CME speeds from the Large Angle Spectroscopic Coronagraph (LASCO; Brueckner et al. 1995) CME catalog with decay indices derived from local, Green’s function potential field extrapolations above manually identified PILs."
- **Time Range**: Each event date/time as listed in Table 1 (matches the 16 CME events, 1998-04-29 to 2005-05-13)
  - **Supporting Quote**:  
    "The CME speed data and ribbon flux yield a linear correlation coefficient of 0.76, with coefficient of determination 0.58; see Figure 5a."
- **Wavelength(s)**: White-light (visible, broad-band filtered)
  - **Supporting Quote**:  
    "The CME speeds that we cite are plane-of-sky speeds..."

---

## (End of Instrumentation Form)

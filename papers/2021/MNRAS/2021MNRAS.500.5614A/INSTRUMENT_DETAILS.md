_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper reports on a search for high‐energy muon neutrinos in spatial and temporal coincidence with 784 gamma‐ray bursts (GRBs) using nearly 10 years of ANTARES data. It describes the methodology used to model the expected neutrino flux from GRBs in the internal shock framework (using the NeuCosmA numerical tool), the treatment of uncertainties in model parameters (redshift, minimum variability timescale, and bulk Lorentz factor), and the stacking analysis that compares the predicted GRB neutrino signal with the atmospheric background. In addition, the study discusses complementary electromagnetic observations of GRBs as provided by space‐based instruments (such as Swift, Fermi, and Konus‑Wind) and ground‐based imaging atmospheric Cherenkov telescopes, and it contrasts its derived neutrino flux and corresponding upper limits with those obtained by IceCube.

## Instrumentation Details

### 1. ANTARES Neutrino Telescope
- **General Comments**:
  - ANTARES is a large-volume water-Cherenkov neutrino telescope located in the deep waters of the Mediterranean Sea off Toulon (France). It is designed to detect upward‐going muon tracks from charged-current interactions of muon neutrinos. Its primary role in the paper is to provide the neutrino data sample used for the search for a GRB-connected signal.
- **Supporting Quote**: 
  "ANTARES (Ageron et al., 2011) is a large volume water-Cherenkov neutrino telescope in the Northern hemisphere, located in the deep water of the Mediterranean Sea, oﬀshore Toulon (France), and fully operational since May 2008."
  
#### Data Collection Period 1: Operational Data for GRB Analysis
- **Time Range**: End of 2007 – 2017  
  - **Supporting Quote**: 
    "Using ANTARES data from the end of 2007 to 2017, a search for upward going muon neutrinos ... in spatial and temporal coincidence with 784 GRBs has been performed."
- **Wavelength(s)**: Not applicable (sensitive to Cherenkov light, typically in the visible/UV range produced by muon tracks)
  - **Supporting Quote**: (implied in the detector description)
- **Physical Observable**: Upward-going muon tracks induced by neutrino charged-current interactions.
  - **Supporting Quote**: 
    "the most relevant neutrino signals for the study of astrophysical sources are the track-like signatures provided by muons, produced by 𝜈𝜇 charged-current interactions."

### 2. Swift Satellite Instruments
- **General Comments**:
  - Swift is a space-based observatory dedicated to the detection and follow-up of GRBs. It provides crucial GRB parameters including burst position, duration, redshift (via its UV/optical and X-ray instruments), and gamma-ray spectral measurements. Within Swift, several instruments play complementary roles: Swift-BAT detects prompt gamma rays, Swift-UVOT delivers rapid optical imaging for precise positioning, and Swift-XRT provides X-ray afterglow observations.
- **Supporting Quote**:
  "GRB parameters needed for the search (time, direction) and the simulation of expected neutrino ﬂuences... are collected from published results of Swift (Gehrels et al., 2004)..."
  
#### Data Collection Period 1: GRB Observations by Swift
- **Time Range**: 2005 – 2017  
  - **Supporting Quote**: 
    "Figure 2: Swift redshift distribution for GRBs detected from 2005 to 2017 (data are available in https://swift.gsfc.nasa.gov/archive/grb_table/)."
- **Wavelength(s)**: Gamma rays (keV range for BAT), X-rays (for XRT), and UV/optical (for UVOT)
  - **Supporting Quote**: 
    "GRBs have historically been observed by space-based facilities, through photons in the energy band from the keV to hundreds of GeV."
- **Physical Observable**: Prompt gamma‐ray emission (BAT), X-ray afterglow (XRT), and UV/optical counterparts (UVOT) used to determine burst positions, durations, and redshifts.
  - **Supporting Quote**: 
    "When physical parameters of a GRB are measured by diﬀerent detectors, the adopted criteria are: (i) The burst’s position is taken from the detector with the smallest angular error (typically Swift-UVOT, then Swift-XRT, Swift-BAT and ﬁnally Fermi-GBM)."

### 3. Fermi Satellite Instruments
- **General Comments**:
  - Fermi is a space-based observatory equipped with instruments that observe GRBs over a wide range of gamma-ray energies. Fermi-GBM is used to capture prompt gamma-ray emission (typically in the 0.01–1 MeV band), while Fermi-LAT covers higher energy gamma rays up to hundreds of GeV.
- **Supporting Quote**:
  "GRB parameters ... are collected from published results of ... Fermi2 (Atwood et al., 2009; Meegan et al., 2009)..."
  
#### Data Collection Period 1: GRB Observations by Fermi
- **Time Range**: While no explicit GRB observation dates are provided in the text, Fermi has been operational since 2008 and its GRB detections have contributed to the sample analyzed.
  - **Supporting Quote**: 
    (Refer to Table 1 which attributes 68.8% (position) and 71.6% (spectrum) contributions to Fermi.)
- **Wavelength(s)**: Gamma rays in the energy range typically from ~0.01 MeV up to hundreds of GeV.
  - **Supporting Quote**:
    "GRBs have historically been observed ... through photons in the energy band from the keV to hundreds of GeV."
- **Physical Observable**: Gamma-ray spectra (prompt emission) used to characterize the GRB energy output.
  - **Supporting Quote**: 
    "the gamma-ray spectrum has to be measured. This is typically ﬁtted with a broken power-law, a cut-oﬀ power-law or a smoothly broken power-law function."

### 4. Konus‑Wind
- **General Comments**:
  - Konus‑Wind is a space-based instrument (operated on the Wind spacecraft) that detects GRBs in the energy range from approximately 0.02 to 10 MeV. It is used particularly to obtain the GRB fluence and spectral measurements over an extended energy band.
- **Supporting Quote**:
  "the burst’s duration, spectrum and ﬂuence are taken from the satellite reporting measurements in the most extended energy band (typically Konus-Wind 0.02 −10 MeV, then Fermi 0.01 −1 MeV, and ﬁnally Swift 0.015 −0.15 MeV)."
  
#### Data Collection Period 1: GRB Observations by Konus‑Wind
- **Time Range**: The exact operational dates are not explicitly provided in the text; however, Konus‑Wind has been providing GRB data (accessible via the GCN archive) during the period relevant to the GRB sample selection.
  - **Supporting Quote**:
    "Konus-Wind information is only available through the GCN archive: http://gcn.gsfc.nasa.gov/gcn3_archive.html"
- **Wavelength(s)**: Gamma rays over the energy interval 0.02–10 MeV.
  - **Supporting Quote**:
    "typically Konus-Wind 0.02 −10 MeV..."
- **Physical Observable**: GRB fluence and spectral shape used for estimating the GRB's electromagnetic energy output.
  - **Supporting Quote**:
    "the spectrum is taken from the satellite with the most extended energy band."

### 5. Ground-based Imaging Atmospheric Cherenkov Telescopes (IACTs)
- **General Comments**:
  - These are ground-based telescopes that detect Cherenkov light produced by particle cascades in the Earth’s atmosphere following the incidence of very high-energy (sub‑TeV) gamma rays. They have recently enabled the detection of GRBs at sub‑TeV energies.
- **Supporting Quote**:
  "Recently, the ﬁrst detections of photons in the sub-TeV energy band from GRB180720B (Abdalla et al., 2019), GRB190114C (Acciari et al., 2019) and from the low-luminous GRB190829A (Valeev et al., 2019; de Naurois, 2019) have been carried out with ground-based imaging atmospheric Cherenkov telescopes."
  
#### Data Collection Period 1: Recent GRB Detections by IACTs
- **Time Range**: Detections reported for events GRB180720B, GRB190114C, and GRB190829A indicate observations in the most recent years (circa 2018–2019).
  - **Supporting Quote**:
    (See above quote regarding the first sub-TeV detections.)
- **Wavelength(s)**: Sub‑TeV gamma rays.
  - **Supporting Quote**:
    "the ﬁrst detections of photons in the sub-TeV energy band..."
- **Physical Observable**: Very high-energy gamma-ray emission observed during or following the GRB prompt or early afterglow phase.
  - **Supporting Quote**:
    "Such a novel energetic component has provided further evidence of the powerfulness of this class of accelerators."

### 6. IceCube Neutrino Observatory
- **General Comments**:
  - IceCube is a cubic-kilometer scale neutrino detector located at the South Pole, designed to observe high-energy astrophysical neutrinos. It is frequently referenced in multi-messenger studies and compared against ANTARES in terms of sensitivity to GRB-related neutrino flux.
- **Supporting Quote**:
  "High-energy astrophysical neutrinos were discovered few years ago (Aartsen et al., 2013; Aartsen et al., 2014; Aartsen et al., 2015)..."
  
#### Data Collection Period 1: IceCube Neutrino Data Samples
- **Time Range**: IceCube analyses referenced include a 10-year νμ track data sample and a 7.5-year High-Energy Starting Events (HESE) sample.
  - **Supporting Quote**:
    "IceCube stacking (tracks + showers): 1172 GRBs ... IceCube best ﬁts... for 𝜈𝜇tracks in 10 years (Stettner et al., 2019) and for HESE events in 7.5 years of collected data (Schneider et al., 2019)."
- **Wavelength(s)**: Not applicable (IceCube detects Cherenkov light in Antarctic ice).
  - **Supporting Quote**: (Implied in the instrument description.)
- **Physical Observable**: High-energy neutrino events (primarily track-like muon events and cascades) used to probe astrophysical neutrino flux.
  - **Supporting Quote**:
    "the track-like signatures provided by muons, produced by 𝜈𝜇 charged-current interactions."

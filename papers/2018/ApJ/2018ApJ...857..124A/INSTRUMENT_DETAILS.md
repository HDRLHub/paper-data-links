_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper investigates the pre-eruptive magnetic reconnection within a multi-flux-rope system in the solar corona, focusing on a C1.1-class flare in NOAA active region 12371 on 2015 June 22. The study employs multi-wavelength imaging (EUV and optical), spectroscopic and hard X-ray data to capture signatures of reconnection such as plasma heating, nonthermal particle acceleration, and bi-directional outflows. The primary data sources are SDO/AIA and HMI for coronal and magnetic field observations, Hinode/SOT and IRIS for lower-atmosphere imaging, and RHESSI for hard X-ray imaging and spectroscopy. Specific observation periods are detailed, such as 16:18–16:52 UT for the flare precursor and main phase analysis, with direct data on plasma temperatures, emission measures, and energy content forming the basis of the results.

## Instrumentation Details

---

### Atmospheric Imaging Assembly (AIA) onboard Solar Dynamics Observatory (SDO)
- **General Comments**:
  - AIA was used for EUV imaging to analyze flare morphology, evolution, and temperature diagnostics during the event.
- **Supporting Quote**: "We analyzed the EUV images obtained by Atmospheric Imaging Assembly (AIA; Lemen et al. 2012) onboard Solar Dynamics Observatory (SDO)."

#### Data Collection Period 1: Analysis of flare precursor and evolution
- **Time Range**: "from ∼16:18 UT when the emission level becomes persistently elevated" to "main phase at 16:45 UT (peak time) on 22 June 2015"
  - **Supporting Quote**: "Small, intermittent enhancements can be seen in the soft X-ray (SXR) 1–8 ˚A lightcurve as early as ∼1 hour before the C-class ﬂare at 16:34 UT (Figure 4a), but we focused on activities from ∼16:18 UT when the emission level becomes persistently elevated."
- **Wavelength(s)**: "AIA’s six EUV passbands in 94, 131, 171, 193, 211, and 335 ˚A have distinctive temperature responses and cover a wide temperature range from 0.5–30 MK..."
  - **Supporting Quote**: "AIA’s six EUV passbands in 94, 131, 171, 193, 211, and 335 ˚A have distinctive temperature responses and cover a wide temperature range from 0.5–30 MK, which enables us to reconstruct the temperature distribution of plasma emitting along the line of sight in the optically thin corona, known as diﬀerential emission measure (DEM)."
- **Physical Observable**: "morphological investigation... mainly used three passbands, i.e., 131 ˚A (Fe XXI with peak response temperature log T = 7.05; Fe VIII, log T = 5.6), 171 ˚A (Fe IX, log T = 5.85), and 304 ˚A (He II, log T = 4.7)...to highlight the braided structure in the EUV images"
  - **Supporting Quote**: "For the morphological investigation we mainly used three passbands, i.e., 131 ˚A (Fe XXI with peak response temperature log T = 7.05; Fe VIII, log T = 5.6), 171 ˚A (Fe IX, log T = 5.85), and 304 ˚A (He II, log T = 4.7)."
- **Additional Comments**: DEM was reconstructed from AIA data for plasma diagnostics.
  - **Supporting Quote**: "Here we employed an algorithm providing positive deﬁnite DEM solutions by solving a linear system based on the concept of sparsity (Cheung et al. 2015)."

---

### Helioseismic Magnetic Imager (HMI) onboard Solar Dynamics Observatory (SDO)
- **General Comments**:
  - HMI was used for vector magnetogram data of the active region to model the coronal magnetic field and inform NLFFF extrapolations.
- **Supporting Quote**: "We studied the magnetic ﬁeld conﬁguration by examining magnetograms from Helioseismic Magnetic Imager (HMI; Scherrer et al. 2012) onboard SDO. To extrapolate the coronal magnetic ﬁeld, we employed Space-Weather HMI Active Region Patches (data product of hmi.sharp cea series) vector magnetograms at 12-minute cadence."

#### Data Collection Period 1: NLFFF extrapolation of coronal topology before and after C1.1 flare
- **Time Range**: "at 16:34:25 UT and 17:22:25 UT, respectively"
  - **Supporting Quote**: "A composite of Q and Tw maps in the X-Z plane at 16:34:25 UT and 17:22:25 UT, respectively, is plotted in Figure 1(d and e) (see also Figure 2)."
- **Physical Observable**: Magnetic topology, twist number, and squashing factor of the flux rope system.
  - **Supporting Quote**: "The vector magnetograms are pre-processed to best suit the force-free condition before being fed into the “weighted optimization” NLFFF code as the photospheric boundary (Wiegelmann et al. 2006). Here we built the NLFFF over a uniform grid of 840 × 452 × 452 pixels (pixel size 0.36 Mm) and investigated magnetic connectivities by tracing ﬁeld lines...to calculate the squashing factor Q...Simultaneously we mapped twist number Tw..."

---

### Ruven Ramaty High-Energy Solar Spectroscopic Imager (RHESSI)
- **General Comments**:
  - RHESSI was used for hard X-ray imaging and spectroscopy to characterize thermal and nonthermal emission, electron energy spectra, and energetics of the C1.1-class flare.
- **Supporting Quote**: "The hard X-ray (HXR) emission from the ﬂaring region is recorded by Rueven Ramaty High-Energy Solar Spectroscopic Imager (RHESSI ; Lin et al. 2002)). We synthesized HXR images with detectors 1, 3, 5, 6, 7, and 9, employing the PIXON algorithm (Hurford et al. 2002)."

#### Data Collection Period 1: Precursor and main phase HXR diagnostics
- **Time Range**: "from 16:29 UT on 2015 June 22" to "16:52 UT"
  - **Supporting Quote**: "Because RHESSI crosses the South Atlantic Anomaly (SAA), HXR data is only available from 16:29 UT on 2015 June 22. We prepared HXR spectra during 16:29 UT–16:52 UT with a time bin of 32 sec..."
- **Wavelength(s)/Energy Range**: "in 6–12 keV (red) and 12–25 keV (magenta) energy bands"; "HXR source in 12–25 keV at 16:30 UT"
  - **Supporting Quote**: "The HXR source in 12–25 keV at 16:30 UT (Figure 7b) corresponds to the power-law component of the photon spectrum (Figure 7f)."
- **Physical Observable**: Detection and characterization of nonthermal electrons, high-temperature plasma, and nonthermal energy content.
  - **Supporting Quote**: "The spectral ﬁtting reveals the presence of non-thermal electron ﬂux with a spectral index (δ) of 6.3 and of hot plasma at 20 MK, consistent with the DEM analysis."
- **Additional Comments**: PIXON algorithm and forward-fitting with SPEX were utilized for imaging and spectral diagnostics.
  - **Supporting Quote**: "We synthesized HXR images with detectors 1, 3, 5, 6, 7, and 9, employing the PIXON algorithm...performed forward fitting with a theoretical photon spectrum combining iso-thermal and thick-target bremsstrahlung models available in the SPectral EXecutive (SPEX) package within the SolarSoftWare (SSW) distribution."

---

### Solar Optical Telescope (SOT) onboard Hinode
- **General Comments**:
  - SOT Ca II images were used for lower atmosphere (chromospheric) response studies at the flare footpoints.
- **Supporting Quote**: "We also analyzed Ca II images obtained by the Solar Optical Telescope (SOT) onboard Hinode (Kosugi et al. 2007)...to investigate the lower atmosphere response to the energy release during the ﬂare."

#### Data Collection Period 1: Chromospheric imaging of flare footpoints
- **Time Range**: Around "∼16:30 UT" on 2015 June 22 (flare precursor and impulsive phase)
  - **Supporting Quote**: "At ∼16:30 UT (Figure 5(e-g)), three brightened emission kernels (labeled K1, K2 and K3) are seen at both 131 and 304 ˚A. K1 is also seen in the Ca II image, suggesting that it is a footpoint emission in the low atmosphere."
- **Wavelength(s)**: Ca II line (specific wavelength not stated, but implied)
  - **Supporting Quote**: "We also analyzed Ca II images obtained by the Solar Optical Telescope (SOT) onboard Hinode..."
- **Physical Observable**: Lower-atmospheric (chromospheric) response to flare energy release, footpoint brightenings
  - **Supporting Quote**: "K1 is also seen in the Ca II image, suggesting that it is a footpoint emission in the low atmosphere."

---

### Interface Region Imaging Spectrograph (IRIS)
- **General Comments**:
  - IRIS 1400 Å (Si IV) slit-jaw images were used for studying response in the upper chromosphere/lower transition region.
- **Supporting Quote**: "We also analyzed ... Si IV 1400 ˚A images from Interface Region Imaging Spectrograph (IRIS; De Pontieu et al. 2014) to investigate the lower atmosphere response to the energy release during the ﬂare."

#### Data Collection Period 1: Transition-region imaging of flare footpoints
- **Time Range**: Around "∼16:30 UT" on 2015 June 22 (concurrent with flare precursor)
  - **Supporting Quote**: "These emission kernels are associated with the enhanced emission co-spatial to NFP, as distinctly seen in the 1400 ˚A image (white arrow), as well as to SFP (yellow arrow), which is in agreement to the scenario of reconnection within diﬀerent ﬂux-rope branches: energy is released at the reconnection site as indicated by nonthermal hard X-ray (HXR) emission (see Figure 5e and below) and further deposited at the ﬂux-rope footpoints."
- **Wavelength(s)**: 1400 Å (Si IV)
  - **Supporting Quote**: "We also analyzed ... Si IV 1400 ˚A images from Interface Region Imaging Spectrograph (IRIS; De Pontieu et al. 2014)..."
- **Physical Observable**: Transition-region response to energy deposition from reconnection events at flux rope footpoints
  - **Supporting Quote**: "These emission kernels are associated with the enhanced emission co-spatial to NFP, as distinctly seen in the 1400 ˚A image..."

---

### Large Angle and Spectrometric Coronagraph (LASCO) onboard Solar and Heliospheric Observatory (SOHO)
- **General Comments**:
  - LASCO C2 data were used to identify the CME associated with the M6.5 flare that follows the event of interest.
- **Supporting Quote**: "a major eruption associated with a full-halo CME observed by the Large Angle and Spectrometric Coronagraph Experiment onboard the Solar and Heliospheric Observatory."

#### Data Collection Period 1: Observation of CME on 22 June 2015
- **Time Range**: "erupt[s] about 1 hr later" than "C-class ﬂare at 16:45 UT (peak time) on 22 June 2015"
  - **Supporting Quote**: "erupts about 1 hr later as a full-halo CME propagating at about 1200 km s−1 in the outer corona (Figure 9)."
- **Wavelength(s)**: White-light coronagraph (2.2–7 solar radii for C2)
  - **Supporting Quote**: "Full-halo CME recorded by LASCO’s C2 coronagraph (2.2–7 solar radii)."
- **Physical Observable**: CME morphology and propagation
  - **Supporting Quote**: "The CME is associated with the M6.5 ﬂare immediately after the C1.1 ﬂare under investigation."

---

### Advanced Composition Explorer (ACE) and Wind (for Interplanetary Analysis)
- **General Comments**:
  - Plasma and magnetic field in situ measurements were used to study the ICME signature at Earth corresponding to the CME driven by the eruption.
- **Supporting Quote**: "ICME observed by two near-Earth spacecrafts, Advanced Composition Explorer (ACE) and Wind. The shaded region during 2015 June 25–26 is identiﬁed as the interplanetary counterpart of the CME associated with the M6.5 ﬂare that occurred on 22 June 2015, which is preceded by a shock (blue vertical line)."

#### Data Collection Period 1: ICME passage at Earth from this event
- **Time Range**: "during 2015 June 25–26"
  - **Supporting Quote**: "The shaded region during 2015 June 25–26 is identiﬁed as the interplanetary counterpart of the CME associated with the M6.5 ﬂare that occurred on 22 June 2015..."
- **Wavelength(s)/Channels**: Magnetic field and solar wind plasma, Fe charge states, and composition
  - **Supporting Quote**: "Data on magnetic ﬁeld, ionic charge states, and composition are given by ACE, while data on bulk plasma by Wind, as the corresponding ACE data have large gaps."
- **Physical Observable**: ICME structure, charge states, magnetic fields, and geomagnetic effects
  - **Supporting Quote**: "Its characteristics are typical of ICMEs (Zurbuchen & Richardson 2006): the speed declines smoothly like a single stream expanding as a whole, the plasma β (ratio of thermal and magnetic pressure) and proton temperature Tp are depressed..."

---

**End of Instrument Listings**

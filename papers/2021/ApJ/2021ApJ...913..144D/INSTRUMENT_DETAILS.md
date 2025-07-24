_This commentary was initially drafted by an AI model. Please use with caution_

1. Electric Field Instrument (EFI) on ARTEMIS  
   - Role: Measures the 3D electric field and waves, providing burst mode captures for detailed waveform analysis.  
   - Sampling and Mode Details:  
     • Burst mode duration is on the order of ~10 seconds.  
     • Sampling frequency in burst mode is 16,384 samples per second.  
   - Usage: Used to identify electric field wave packets and to analyze wave modes (e.g., ion acoustic, TFES, solitary waves) within and near shock regions.  
   - Supporting References in Text: “The EFI measures the 3D electric field and waves [Bonnell et al., 2008].”  

2. Search Coil Magnetometer (SCM) on ARTEMIS  
   - Role: Measures 3D magnetic field fluctuations and waves, complementing the electric field data from the EFI.  
   - Sampling and Mode Details:  
     • Burst mode duration is also ~10 seconds.  
     • Sampling frequency in burst mode is 1,024 samples per second.  
   - Usage: Employed to capture magnetic field wave burst data, critical for identifying wave polarization characteristics and associating magnetic power spectra with observed wave modes.  
   - Supporting References in Text: “The SCM measures the 3D magnetic field fluctuations and waves [Roux et al., 2008].”  

3. Fluxgate Magnetometer (FGM) on ARTEMIS  
   - Role: Measures the 3D quasi-static magnetic fields, essential for determining the background magnetic field used in aligning the wave burst data and for shock analysis.  
   - Sampling and Mode Details:  
     • Operates in fast survey mode at 4 samples per second or in particle burst mode at 128 samples per second.  
   - Additional Details:  
     • A data cleaning algorithm is applied to remove spin periodic effects and achieve stable quasi-static magnetic field measurements.  
   - Supporting References in Text: “The FGM measures the 3D quasi-static magnetic fields [Auster et al., 2008].”  

4. ElectroStatic Analyzer (ESA) on ARTEMIS  
   - Role: Measures electron and ion distributions; provides particle data essential for calculating plasma moments (velocity, density, temperature) and for identifying shock parameters.  
   - Measurement Ranges and Modes:  
     • Electrons: Energy range from several eV up to 30 keV.  
     • Ions: Energy range from several eV up to 25 keV.  
     • Operational Modes: Full packets (low time resolution ~1 sample per minute but high angular resolution of ~2°), Reduced packets (higher time resolution ~15 samples per minute with lower angular resolution ~22°), and Burst packets (high time and angular resolutions used when the spacecraft is in burst mode).  
   - Usage: The ESA data are critical for recalculating ion velocity, density, and temperature moments—especially in the presence of secondary ion populations—to feed into shock parameter estimation.  
   - Supporting References in Text: “The ElectroStatic Analyzer (ESA) measures the electron and ion distributions over the energy range of several eV to 30 keV for electrons and several eV to 25 keV for ions [McFadden et al., 2008].”

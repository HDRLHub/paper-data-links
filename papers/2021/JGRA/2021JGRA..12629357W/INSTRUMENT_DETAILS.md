_This commentary was initially drafted by an AI model. Please use with caution_

1. Magnetospheric Multiscale (MMS) Spacecraft Suite  
   - General Comments:  
     MMS is the main platform used in the study to capture high‐resolution, three-dimensional measurements of electric and magnetic fields in the Earth’s bow shock. This dataset is central to the analysis of bipolar electrostatic structures, their correction procedure, and interferometry analysis.  
     
   - Instruments and Detectors:  
     • Digital and Analogue Fluxgate Magnetometers  
       - Measurement: DC-coupled magnetic field  
       - Data Cadence: Burst mode at 128 samples per second; additional fast mode measurements at 16 S/s for the shock region  
       - Supporting Context: “We used burst mode measurements of DC-coupled magnetic ﬁeld at 128 S/s resolution provided by Digital and Analogue Fluxgate Magnetometers [61], … and fast mode measurements of DC-coupled magnetic ﬁeld at 16 S/s resolution…”  
     
     • Axial Double Probe and Spin-Plane Double Probe Electric Field Instruments  
       - Measurement: AC-coupled electric fields obtained from voltage differences between spatially separated voltage-sensitive probes  
       - Detector Details:  
           - Axial double probe: Mounted along the spacecraft spin axis with 14.6-meter axial antennas  
           - Spin-Plane double probe: Mounted in the spacecraft spin plane with 60-meter antennas  
       - Frequency Response Factors (FRFs): Optimal ratio determined around 1.65 (axial) to 1.8 (spin-plane) to minimize distortions in measured electric field waveforms  
       - Sampling: High-resolution waveform measurements at 8,192 samples per second  
       - Supporting Context: “… AC-coupled electric ﬁeld at 8,192 S/s resolution provided by Axial Double Probe [57] and Spin-Plane Double Probe [58] …” and “… the optimal ratio of frequency response factors of axial and spin plane antennas for the bipolar structures is around 1.65/1.8.”  
       
     • Fast Plasma Investigation Instrument  
       - Measurements: Electron moments (at 0.03 s cadence) and ion moments (at 0.15 s cadence)  
       - Additional plasma parameters are obtained in fast mode at 4.5 s cadence from upstream and downstream regions  
       - Supporting Context: “… electron moments at 0.03s cadence and ion moments at 0.15s cadence provided by the Fast Plasma Investigation instrument [62].”
       
   - Data Collection and Correction:  
     - The study uses voltage signals from six voltage-sensitive probes (labeled P1–P6) mounted on the axial and spin‐plane antennas to reconstruct the electric field.  
     - A correction procedure is implemented to compensate for distortions caused by the short spatial scale of bipolar structures relative to probe separations.
     

2. Wind Spacecraft  
   - General Comments:  
     Wind measurements are used in this study to obtain proton temperature estimates which serve as a proxy for the upstream plasma conditions, since MMS proton temperature estimates in the solar wind are deemed less accurate.  
     
   - Instrument and Measurement Details:  
     • Proton Temperature Detector (via Wind spacecraft measurements)  
       - Measurement: Proton temperature with 1-minute cadence and time-shifted data  
       - Supporting Context: “We use proton temperature estimates provided by the Wind spacecraft … because MMS estimates of proton temperature in the solar wind are not accurate.”

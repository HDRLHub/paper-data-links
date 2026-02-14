_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## 1. Fermi-GBM on board the Fermi Gamma-Ray Space Telescope
- **General Comments**:
   - This gamma‐ray instrument was the primary detector for GRB 200415A. It consists of two types of scintillator detectors – thallium‐doped Sodium Iodide (NaI) detectors and Bismuth Germanate (BGO) detectors. The instrument provided high time‐resolution Time-Tagged Event (TTE) data with measurements in a broad energy range, enabling detailed temporal and spectral studies of the giant flare.
- **Supporting Quote**: 
   - “On April 15th 2020 at 08:48:05.563746 UTC, the Gamma-ray Burst Monitor (GBM) onboard the Fermi Gamma-Ray Space Telescope (Fermi) was triggered by an extremely bright, short and spectrally hard event, initially classified as a short Gamma-ray Burst (GRB), GRB 200415A [14]…”  

#### Data Collection Period 1: Initial Pulse Clean Data
- **Time Range**: -4.4 ms to -3.4 ms (relative to the trigger at 08:48:05.563746 UTC on April 15, 2020)
   - **Supporting Quote**: 
      - “Interval (1): −4.4 to −3.4 ms … contains the first pulse, present in both GBM and BAT. It is a ‘clean’ pulse, not affected by saturation…”  
- **Wavelength(s)**: 
   - BGO channel: 0.2–40 MeV; NaI channel: ~8–1000 keV  
   - **Supporting Quote**: 
      - “Figure 1: Temporal and Spectral Variability of GRB 200415A. (Left:) Lightcurves with 0.2 ms resolution for a Fermi GBM BGO detector … and Fermi-GBM (NaI) (8-1000 keV).”
- **Physical Observable**: 
   - Lightcurve structure, pulse shape, and early spectral characteristics.
   - **Supporting Quote**: 
      - “The very high rate might cause the electronic signals of photons to overlap (pulse pile-up), … The spectral shape of the detector counts are only slightly modified …”

- **Additional Comments**: 
   - This interval is unsaturated and is used to precisely measure the rapid rise time (Trise ≈ 77 µs) of the initial pulse.

#### Data Collection Period 2: Brightest Interval (Saturated)
- **Time Range**: -3.4 ms to -0.8 ms  
   - **Supporting Quote**: 
      - “Interval (2): −3.4 to −0.8 ms, the brightest part of the lightcurve, affected by TTE saturation in GBM.”
- **Wavelength(s)**: 
   - Same as above – primarily measured in the NaI and BGO detectors.
   - **Supporting Quote**: 
      - “Combined effective spectral range of both the NaI and BGO detectors are ∼8 keV to 40 MeV.”
- **Physical Observable**: 
   - High photon count rate used for spectral fitting (e.g. Comptonized model parameters) despite saturation effects.
- **Additional Comments**: 
   - A correction factor was applied comparing GBM flux to Swift-BAT, as summarized in Table 1.

#### Data Collection Period 3: Hard Spectral Peak
- **Time Range**: -0.8 ms to 3.0 ms  
   - **Supporting Quote**: 
      - “Interval (3): −0.8 to 3.0 ms, identified as the hardest interval with peak energy Ep ≈ 1.9 MeV.”
- **Wavelength(s)**: 
   - BGO detectors (sensitive in the MeV range) alongside NaI detectors.
   - **Supporting Quote**: 
      - (In Table 1 and associated text it is specified that the spectral fits use data across the range up to 40 MeV.)
- **Physical Observable**: 
   - Peak energy (Ep), photon index, and energy flux derived from the Comptonized spectral fits.
   - **Supporting Quote**: 
      - “The differential photon number spectrum (dN/dE) in all four intervals is best described by a power law with an exponential cutoff … with Interval (3) having Ep = 1.9 MeV.”
- **Additional Comments**: 
   - This interval provided crucial constraints on the relativistic outflow properties given the high energy emission.

#### Data Collection Period 4: Extended Decay
- **Time Range**: 3.0 ms to 136.4 ms  
   - **Supporting Quote**: 
      - “Interval (4): 3.0 to 136.4 ms, where the fourth interval has a featureless decay out to 136.4 ms and contains most of the fluence.”
- **Wavelength(s)**: 
   - Maintains the same broad energy range (8 keV to 40 MeV).
   - **Supporting Quote**: 
      - “The spectral range used for these measurements was 8 keV to 10 MeV.”
- **Physical Observable**: 
   - An exponentially decaying energy flux and spectral peak energy with a decay timescale of 45 ms (flux) and 100 ms (peak energy).
   - **Supporting Quote**: 
      - “Panels a, b and c show the energy flux or F … and the decay timescale of 45 ± 3 ms for F and 100 ± 1 ms for Ep.”
- **Additional Comments**: 
   - This interval is critical for understanding the tail emission and the implications of relativistic Doppler boosting.

## 2. Swift-BAT on board the Neil Gehrels Swift Observatory
- **General Comments**:
   - The Burst Alert Telescope (BAT) provides coded-mask imaging with moderate spectral resolution in the 15–350 keV range, and was operated in TTE mode for GRB 200415A using the GUANO pipeline. Although the source was outside the nominal coded field-of-view, its brightness allowed detection through the graded-Z shield.
- **Supporting Quote**: 
   - “Using the BAT TTE data to determine the duration due to bandwidth saturation of the high-time resolution GBM TTE data … the T90 duration of GRB 200415A … is 140.8+0.5−0.6 ms.”
   
#### Data Collection Period: GRB 200415A Event
- **Time Range**: The TTE data span the burst event with T90 = 140.8 ms (measured from the cumulative count distribution during the GRB event on April 15, 2020 at 08:48:05.563746 UTC)
   - **Supporting Quote**: 
      - “The BAT lightcurve (panel (c) in Fig. 1) … was used for timing analysis and to estimate the T90 and T50 durations.”
- **Wavelength(s)**: 
   - Primarily in the 15–350 keV range, with sensitivity up to ∼500 keV.
   - **Supporting Quote**: 
      - “The BAT is a coded-mask imaging instrument with a 2 steradian field-of-view in the 15–350 keV energy band … capable of recording photons with energies up to ∼500 keV.”
- **Physical Observable**: 
   - Temporal profiles (T90 and T50 durations) and overlap with the high time-resolution GBM measurements.
   - **Supporting Quote**: 
      - “The BAT data were also used for timing analysis, such as the T90 and T50 durations, shown in ED Fig. 1.”
- **Additional Comments**: 
   - Custom Detector Response Matrices (DRMs) were generated to correct for the off-axis response due to the non-standard illumination by the burst.

## 3. Fermi-LAT on board the Fermi Gamma-Ray Space Telescope
- **General Comments**:
   - The Large Area Telescope (LAT) on Fermi provided constraints on the high-energy end of the emission by detecting GeV photons, which are used to place limits on the bulk Lorentz factor of the relativistic outflow.
- **Supporting Quote**: 
   - “This GBM limit is consistent with the stronger constraints due to the detection of GeV photons by Fermi-LAT [15].”
   
#### Data Collection Period: (No specific interval provided)
- **Time Range**: No explicit time ranges are provided for the LAT detection within the paper; its observations are referenced for comparison with the GBM’s constraints.
- **Wavelength(s)**: 
   - GeV energies (high-energy gamma-ray regime).
- **Physical Observable**: 
   - Detection (or non-detection) of high-energy photons used to set lower bounds on the bulk Lorentz factor (Γ > 6).
- **Additional Comments**: 
   - The Fermi-LAT data complement the GBM observations by extending the energy constraints, although detailed timing information is not provided in the text.

## 4. Karl G. Jansky Very Large Array (VLA)
- **General Comments**:
   - The VLA was used to search for associated radio emission from GRB 200415A (and its likely host, NGC 253). The radio observations were conducted in the 1–2 GHz L-Band and provided flux measurements and RMS noise estimations.
- **Supporting Quote**: 
   - “Four observations of the NGC 253 taken with the Karl G. Jansky Very Large Array (VLA) [20], 4.3 to 51.2 days after the event trigger …”
   
#### Data Collection Period 1: First Observation
- **Time Range**: April 19, 16:12:36 UTC (4.31 days post burst)
   - **Supporting Quote**: 
      - “Date: April 19, 16:12:36 … ∆Tburst: 4.31 days …”
- **Wavelength(s)**: 
   - 1–2 GHz (L-Band)
   - **Supporting Quote**: 
      - “taken with the full 1–2 GHz L-Band.”
- **Physical Observable**: 
   - Radio flux measurements with an RMS noise of 0.28 mJy/beam.
   - **Supporting Quote**: 
      - “... along with its accompanying RMS noise are listed in Table 2.”

#### Data Collection Period 2: Second Observation
- **Time Range**: April 25, 16:26:53 UTC (10.3 days post burst)
   - **Supporting Quote**: 
      - “Date: April 25, 16:26:53 … ∆Tburst: 10.3 days …”
- **Wavelength(s)**: 
   - 1–2 GHz (L-Band)
- **Physical Observable**: 
   - Radio flux measurements with an RMS noise of 0.43 mJy/beam.

#### Data Collection Period 3: Third Observation
- **Time Range**: May 7, 15:04:53 UTC (42.3 days post burst)
   - **Supporting Quote**: 
      - “Date: May 7, 15:04:53 … ∆Tburst: 42.3 days …”
- **Wavelength(s)**: 
   - 1–2 GHz (L-Band)
- **Physical Observable**: 
   - Radio flux measurement with an RMS noise of 0.40 mJy/beam.

#### Data Collection Period 4: Fourth Observation
- **Time Range**: June 5, 12:43:29 UTC (51.2 days post burst)
   - **Supporting Quote**: 
      - “Date: June 5, 12:43:29 … ∆Tburst: 51.2 days …”
- **Wavelength(s)**: 
   - 1–2 GHz (L-Band)
- **Physical Observable**: 
   - Radio flux measurement with an RMS noise of 0.29 mJy/beam.
- **Additional Comments**: 
   - No significant variable or transient emission was identified upon comparing these radio observations.

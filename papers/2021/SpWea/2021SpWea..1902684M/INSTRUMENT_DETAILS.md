_This commentary was initially drafted by an AI model. Please use with caution_

1. DMSP Particle Precipitation Instruments (SSJ/4 and SSJ/5)
   - General Comments:
     • The Defense Meteorological Satellite Program (DMSP) satellites form the backbone of the database used in the study. They measure particle precipitation in the form of total electron energy flux.
     • Two versions of the onboard particle spectrograph are used: the SSJ/4 instrument on pre‐F16 spacecraft and the SSJ/5 on post‐F16 satellites.
   - Data Collection Time Ranges:
     • The complete DMSP database spans 17 distinct years, specifically during 1987–1988 and 2000–2014, amounting to a total of 51 satellite years of observations.
     • Specific examples highlighted in the paper include a DMSP F13 pass over mesoscale undulations on February 6, 2002 and DMSP F16 data used in validation during the year 2010.
   - Detector, Wavelengths, and Physical Observables:
     • Detector: Particle spectrographs (SSJ/4 and SSJ/5) that record energetic electron precipitation.
     • Wavelengths: Not applicable, since the instruments do not capture electromagnetic wavelengths but rather count and energy‐distribute charged particles.
     • Physical Observable: Total electron energy flux (reported in units such as eV·cm⁻²·sr⁻¹·s⁻¹ and represented in log₁₀ scale), which is used to characterize the precipitation that couples the magnetosphere to the ionosphere.
     
2. Polar Visible Imaging System (VIS)
   - General Comments:
     • The Polar VIS, aboard the Global Geospace Science Polar spacecraft, is used to capture global auroral imagery that serves as an independent observational dataset.
     • It is employed in the paper to compare the auroral brightness maps obtained from the machine learning model (PrecipNet) against actual auroral emission observations.
   - Data Collection Time Range:
     • In the study, Polar VIS data are specifically presented for a case study event on January 25, 2000, when global polar high‐latitude auroral emissions were observed during geomagnetically active conditions.
   - Detector, Wavelengths, and Physical Observables:
     • Detector: A visible imaging system that records auroral emissions.
     • Wavelengths: Operates in the visible spectral range (specific band details are not provided, but the measured brightness is given in Rayleighs, a standard unit for airglow/auroral emissions).
     • Physical Observable: Auroral emission brightness (measured in kRayleighs) which, in this context, functions as a proxy for the precipitation intensity impacting the high‐latitude ionosphere.
     
3. Global Ultraviolet Imager (GUVI) on TIMED Satellite
   - General Comments:
     • GUVI is mentioned in the context of extending precipitation modeling. In one of the OVATION model extensions (labeled OVATION Prime 2013), auroral imagery data acquired by GUVI are used to better specify precipitation at higher disturbance levels (Kp > 6).
     • Although not the primary focus of the current model evaluation, GUVI provides complementary ultraviolet observations of the aurora.
   - Data Collection Time Range:
     • A specific time range for GUVI observations is not directly provided in the paper; however, its usage is tied to the OVATION Prime 2013 extension efforts.
   - Detector, Wavelengths, and Physical Observables:
     • Detector: An ultraviolet imaging instrument aboard the TIMED (Thermosphere, Ionosphere, Mesosphere Energetics, and Dynamics) satellite.
     • Wavelengths: Operates in the ultraviolet part of the spectrum (exact wavelength bands are not specified in the text).
     • Physical Observable: Auroral emissions in the ultraviolet wavelengths, which are used to quantify aspects of particle precipitation complementary to the visible and in situ particle measurements.
     
4. SuperMAG Ground-Based Magnetometer Network
   - General Comments:
     • The SuperMAG initiative is referenced as the source of substorm onset data. It aggregates measurements from a network of ground-based magnetometers, providing essential information on geomagnetic activity.
     • These observations are used in the paper to contextualize the timing and location of substorm-related phenomena as compared to satellite precipitation observations.
   - Data Collection Time Range:
     • While an explicit time range is not provided, SuperMAG data are used in conjunction with the DMSP database covering the same extensive periods (e.g., during the 17-year span of the satellite observations) to identify substorm onsets.
   - Detector, Wavelengths, and Physical Observables:
     • Detector: Ground-based magnetometers.
     • Wavelengths: Not applicable.
     • Physical Observable: Variations in the Earth’s magnetic field that indicate substorm onsets and geomagnetic disturbances.
     
5. OMNI Data Set (Aggregated Solar Wind and IMF Measurements)
   - General Comments:
     • The OMNI data set is utilized to provide solar wind and interplanetary magnetic field (IMF) parameters. These act as organizing inputs and drivers for the ML model.
     • Although OMNI is a reprocessed and propagated data product collected from multiple spacecraft, it is essential for aligning solar wind conditions with in situ particle precipitation measurements.
   - Data Collection Time Range:
     • The OMNI data are temporally aligned with the DMSP observations over the full period of the study (1987–1988 and 2000–2014), ensuring a comprehensive match between solar wind conditions and magnetosphere–ionosphere events.
   - Detector, Wavelengths, and Physical Observables:
     • Detector: Not a single instrument but a dataset compiled from multiple spacecraft missions (e.g., ACE, Wind) providing solar wind plasma and magnetic field observations.
     • Wavelengths: Not applicable.
     • Physical Observable: Solar wind plasma parameters and IMF measurements which serve as key inputs (features) for predicting particle precipitation.

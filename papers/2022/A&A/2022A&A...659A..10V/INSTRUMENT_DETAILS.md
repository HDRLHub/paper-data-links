_This commentary was initially drafted by an AI model. Please use with caution_

1. ACE SWICS (Advanced Composition Explorer – Solar Wind Ion Composition Spectrometer)
   - General Comments:
     - This instrument, carried on the ACE spacecraft, is referenced as a key source of in‐situ solar wind plasma and composition data.
     - It is used to measure ion composition, density, temperature, velocity, dynamic pressure, and the interplanetary magnetic field (IMF) components.
   - Time Range(s) & Supporting Context:
     - Data for several ICME events are provided using ACE SWICS data in combination with OMNIWeb. For example, the 16/07/2000 event is noted at “16/07/2000 (02 : 20 h)” and the event on “31/03/2001 (01 : 20 h)” uses ACE SWICS plus OMNIWeb. These discrete snapshots cover events between 1997 and 2020.
   - Specific Observables:
     - Detected parameters include solar wind density (cm⁻³), temperature (10³ K), radial velocity (km/s), dynamic pressure (nPa), and the vector IMF components (Bx, By, Bz in nT).
   - Detector Details / Relevant Characteristics:
     - ACE SWICS is designed to separate solar wind ions by mass and charge with an energy-per-charge analyzer; although the paper does not give further technical details, its role in providing composition and plasma parameters is central to the paper’s simulation inputs.

2. DSCOVR (Deep Space Climate Observatory) Instruments
   - General Comments:
     - DSCOVR provides near-real–time solar wind plasma and magnetic field measurements.
     - The data from DSCOVR are used in several simulation inputs to represent solar wind conditions for ICME events.
   - Time Range(s) & Supporting Context:
     - Specific event data obtained from DSCOVR are given, for instance:
       • “03/08/2016 (05 : 00 h)”
       • “27/05/2017 (21 : 50 h)”
       • “16/07/2017 (09 : 30 h)”
       • “20/04/2020 (08 : 50 h)”
     - These times indicate that DSCOVR measurements from the later part of the study period (2016–2020) were used.
   - Specific Observables:
     - Measured parameters include solar wind density, temperature, velocity (including radial components), dynamic pressure, and the IMF magnitude and components.
   - Detector Details / Relevant Characteristics:
     - DSCOVR carries instruments to monitor the solar wind plasma and the interplanetary magnetic field (exact detector names not repeated in the paper, but its role is similar to ACE SWICS in providing in–situ measurements).

3. OMNIWeb Data Set (incorporating data from several spacecraft including Wind)
   - General Comments:
     - OMNIWeb is a data service that compiles high–resolution solar wind and IMF measurements from multiple spacecraft.
     - It is used repeatedly in the paper as a primary repository for the input solar wind parameters across many ICME events.
   - Time Range(s) & Supporting Context:
     - The paper’s Table D.1 lists numerous events with timestamps such as “15/05/1997 (07 : 30 h)”, “22/10/1999 (06 : 30 h)”, “31/03/2001 (01 : 20 h)” and beyond. This indicates OMNIWeb data span from at least 1997 through events in the 2000s.
   - Specific Observables:
     - OMNIWeb provides the solar wind density, temperature, velocity, dynamic pressure, and IMF components used as key simulation inputs.
   - Detector Details / Relevant Characteristics:
     - Although OMNIWeb itself is a data aggregator, its underlying measurements come from instruments onboard missions such as Wind and ACE; for example, the text mentions “High Resolution OMNI data based on the Global Geospace Science (GGS) Wind satellite.”

4. Ovation Prime Model (via the integrated Space Weather Analysis System – iSWA)
   - General Comments:
     - Ovation Prime, while a model rather than a hardware instrument, is used in the paper to forecast the latitude and longitude of visible aurora.
     - It serves as an “observational” tool by providing energy flux estimates that can be compared against the simulation outputs.
   - Time Range(s) & Supporting Context:
     - Its output is compared for the 27/05/2017 ICME simulation, where Ovation Prime forecasts of auroral energy flux at the North and South Hemispheres are shown.
   - Specific Observables:
     - The model provides predicted energy fluxes along with the spatial (latitudinal and longitudinal) distribution of the aurora.
   - Detector Details / Relevant Characteristics:
     - Although not a physical detector, Ovation Prime uses empirical relationships to map solar wind–driven energy deposition and auroral precipitation; its inclusion bridges simulation predictions with observational forecast techniques.

5. Wind (Global Geospace Science – GGS Wind Satellite)
   - General Comments:
     - The Wind spacecraft is referenced indirectly via OMNIWeb and is one of the primary platforms that have provided high–resolution solar wind data.
   - Time Range(s) & Supporting Context:
     - The OMNIWeb data set includes measurements originally from Wind. Although specific Wind observation times are not separately tabulated, events dating from 1997 onward (as in Table D.1) include Wind’s contribution.
   - Specific Observables:
     - Wind’s instruments measure solar wind plasma properties and magnetic field components.
   - Detector Details / Relevant Characteristics:
     - Wind typically utilizes far–aday cup instruments and magnetometers; while the paper does not go into technical detail here, its role is embedded in the combined OMNIWeb dataset.

6. Geosynchronous and Other Satellite Observations (GOES, THEMIS, Cluster)
   - General Comments:
     - The paper discusses comparisons with and implications for various near–Earth satellites (e.g. GOES, THEMIS, Cluster) in the context of magnetopause stand–off distance and plasma precipitation.
     - These satellites provide in–situ observations which help validate simulation results and forecast hazards to spacecraft.
   - Time Range(s) & Supporting Context:
     - Although precise instrument time ranges are not detailed in the simulation tables, several event dates are associated with magnetopause crossings:
       • For example, GOES satellites are noted in relation to events such as the 24/10/2003 ICME, where magnetopause crossing predictions are compared.
       • THEMIS and Cluster missions are mentioned in past studies (e.g., “Cluster magnetopause crossings” during the 31/03/2001 event), indicating observations over similar ICME periods.
   - Specific Observables:
     - These spacecraft generally record magnetic field intensity, plasma density, and electric field measurements which are compared against simulation-derived parameters such as the magnetopause and bow shock locations.
   - Detector Details / Relevant Characteristics:
     - GOES carries magnetometers, energetic particle sensors, and plasma instruments.
     - THEMIS and Cluster carry multi–point instruments for measuring plasma and field parameters.
     - Although the paper does not detail the instrument specifications, their mention supports the argument that simulation outputs are consistent with spacecraft observations.

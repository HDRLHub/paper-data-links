_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper investigates the association of solar radio type IV bursts with active region locations on the Sun during solar cycle 24. It categorizes active regions associated with moving and stationary type IV bursts based on their proximity to the disk center. The study also examines the relationship between these bursts and coronal mass ejections (CMEs). The data spans from January 1, 2009, to December 31, 2019, and includes observations from various instruments and observatories, such as the Radio Solar Telescope Network (RSTN), the Large Angle and Spectrometric Coronagraph (LASCO) on SOHO, and the SECCHI instruments on STEREO.

## Instrumentation Details

### Radio Solar Telescope Network (RSTN)
- **General Comments**:
   - The RSTN is used to report solar radio bursts, including type IV bursts, which are classified based on their spectral and temporal appearance in the solar dynamic spectra.
- **Supporting Quote**: "For radio events, the Radio Solar Telescope Network (RSTN) and a couple of other observatories contribute in reporting the bursts."

#### Data Collection Period 1: General observation of type IV bursts
- **Time Range**: January 1, 2009 – December 31, 2019
   - **Supporting Quote**: "The type IV bursts information from January 01, 2009 - December, 31, 2019 were extracted from the entire event list."
- **Wavelength(s)**: 25 – 180 MHz
   - **Supporting Quote**: "The frequency range of this stationary type IV bursts was ≈25 −180 MHz."
- **Physical Observable**: Type IV radio bursts
   - **Supporting Quote**: "The radio bursts are classified based on their spectral and temporal appearance in the solar dynamic spectra."
- **Additional Comments**: The RSTN data includes the start and end time, start and end frequency, reporting station, and associated active region for the type IV bursts.

### Large Angle and Spectrometric Coronagraph (LASCO) on board SOHO
- **General Comments**:
   - LASCO is used to detect CMEs and their association with type IV radio bursts.
- **Supporting Quote**: "For the CME association, we used the list provided at the coordinated data analysis website (CDAW; Yashiro et al., 2004)3, which contains the manual detection of CMEs with the Large Angle and Spectrometric Coronagraph (LASCO) onboard the Solar and Heliospheric Observatory (SOHO; Brueckner et al., 1995)."

#### Data Collection Period 1: CME detection and association with type IV bursts
- **Time Range**: January 1, 2009 – December 31, 2019
   - **Supporting Quote**: "The type IV bursts information from January 01, 2009 - December, 31, 2019 were extracted from the entire event list."
- **Wavelength(s)**: Not specified
- **Physical Observable**: Coronal Mass Ejections (CMEs)
   - **Supporting Quote**: "For the CME association, we used the list provided at the coordinated data analysis website (CDAW; Yashiro et al., 2004)3, which contains the manual detection of CMEs with the Large Angle and Spectrometric Coronagraph (LASCO) onboard the Solar and Heliospheric Observatory (SOHO; Brueckner et al., 1995)."
- **Additional Comments**: The CME list includes manual detections and associations with type IV bursts based on temporal correlation and position angle.

### SECCHI on board STEREO
- **General Comments**:
   - SECCHI instruments on STEREO are used to detect CMEs and their association with type IV radio bursts.
- **Supporting Quote**: "We also used CMEs detected with the Cor1 and Cor2 coronagraphs from the Sun-Earth Connection Coronal and Heliospheric Investigation (SECCHI; Howard et al., 2008) onboard the Solar Terrestrial Relations Observatory (STEREO)."

#### Data Collection Period 1: CME detection and association with type IV bursts
- **Time Range**: January 1, 2009 – December 31, 2019
   - **Supporting Quote**: "The type IV bursts information from January 01, 2009 - December, 31, 2019 were extracted from the entire event list."
- **Wavelength(s)**: Not specified
- **Physical Observable**: Coronal Mass Ejections (CMEs)
   - **Supporting Quote**: "We also used CMEs detected with the Cor1 and Cor2 coronagraphs from the Sun-Earth Connection Coronal and Heliospheric Investigation (SECCHI; Howard et al., 2008) onboard the Solar Terrestrial Relations Observatory (STEREO)."
- **Additional Comments**: The CME list includes detections from both STEREO-A and STEREO-B, and associations with type IV bursts are based on temporal correlation and position angle.

### Sagamore Hill Solar Radio Observatory
- **General Comments**:
   - This observatory provides dynamic spectra of type IV bursts, including start time, duration, and frequency range.
- **Supporting Quote**: "Figure 1 shows dynamic spectra of type IV burst on September 24, 2011, with the Sagamore Hill Solar Radio Observatory."

#### Data Collection Period 1: Observation of a specific type IV burst
- **Time Range**: September 24, 2011
   - **Supporting Quote**: "Figure 1 shows dynamic spectra of type IV burst on September 24, 2011, with the Sagamore Hill Solar Radio Observatory."
- **Wavelength(s)**: 25 – 180 MHz
   - **Supporting Quote**: "The frequency range of this stationary type IV bursts was ≈25 −180 MHz."
- **Physical Observable**: Type IV radio burst
   - **Supporting Quote**: "Figure 1 shows dynamic spectra of type IV burst on September 24, 2011, with the Sagamore Hill Solar Radio Observatory."
- **Additional Comments**: The burst started at ≈12:50 UT and lasted for ≈4 hours.

---

Reasoning: Let's think step by step in order to produce the script. We need to query the VSO for data from the LASCO instrument on SOHO and the SECCHI instrument on STEREO-A and STEREO-B for the time range from January 1, 2009, to December 31, 2019. We will use the `Fido` interface from SunPy to construct these queries. The script will print out the query results and have the `Fido.fetch` commands commented out.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper reports the detection and detailed analysis of radio bursts from the Galactic magnetar SGR 1935+2154. In a coordinated multi‐telescope campaign during a roughly one‐month period in late April to late May 2020, several radio instruments (operating at various frequency bands from low‐frequency P-band up to high‐frequency X- and C-bands) recorded radio bursts with precise time resolutions, full-polarisation information, and characteristic scattering signatures. In parallel, the study compares these radio detections with simultaneous X-ray observations from instruments such as NICER, Swift/XRT, Fermi/GBM, and HXMT, as well as making use of independent detections by CHIME/FRB, STARE2, and FAST. The varied frequency coverages, detector configurations (2-bit baseband data recorded in VLBI Data Interchange Format) and the different physical observables (burst fluence, intrinsic pulse width, polarisation properties, dispersion measure, scattering time scales) form the basis for exploring the emission mechanism of fast radio bursts and their potential connection to magnetars.

## Instrumentation Details

### 1. Westerbork RT1 (Wb)
- **General Comments**:
   - Westerbork RT1 is a 25-m single-dish radio telescope that participated in the campaign.
   - It operated in two distinct frequency ranges during the campaign by splitting its observations into two setups: one in P-band and one in L-band.
   - The telescope recorded 2-bit baseband data (in circular polarisations) in the VLBI Data Interchange Format (VDIF).
- **Supporting Quote**: 
   - “Westerbork RT1: Wb observed in two diﬀerent frequency ranges, covering 313.49–377.49 MHz (P-band) split into eight 8 MHz wide subbands during part of each run. The other part of a run covered 1260–1388 MHz (L-band) …” (Section 6.1.1)
- **Data Collection Period**:
   - **Overall Campaign**: Observations were performed as part of a coordinated campaign spanning from 2020 April 29 UT 22:45 (MJD 58968.94791) to 2020 May 25 UT 09:00 (MJD 58994.37500).
   - *Note*: Multiple observing blocks are listed in Table 4 for Wb; the overall period is indicated above.
   - **Supporting Quote**: “Since the announcement of FRB 200428, we observed SGR 1935+2154 daily … between 2020 April 29 UT 22:45 … and 2020 May 25 UT 09:00.” (Section 6.1.1)
- **Wavelength(s)**:
   - P-band: 313.49–377.49 MHz.
   - L-band: 1260–1388 MHz.
   - **Supporting Quote**: “... covering 313.49–377.49 MHz (P-band) … and 1260–1388 MHz (L-band) …” (Section 6.1.1)
- **Physical Observable**:
   - The observations targeted the detection of radio bursts from SGR 1935+2154. Data products include full-polarisation burst profiles, fluence measurements, pulse widths (both intrinsic and observed), and scattering time scales.
   - **Supporting Quote**: “The bursts are plotted … using a dark cyan bar representing the full-width at half-maximum …” (Figure 1 caption)
- **Additional Comments**:
   - Data from Wb were processed with a dedicated pipeline using pulsar software (e.g. Heimdall and FETCH) to search for single pulses.

### 2. Onsala 25-m Dish (O8)
- **General Comments**:
   - The Onsala 25-m telescope operated as a single-dish instrument at L-band during the campaign.
   - It used a variable frequency setup; early observations recorded the full available bandwidth (512 MHz between 1222–1739 MHz), later settling for a 128 MHz sub-band configuration (split into eight 16 MHz bands between 1360–1488 MHz) to mitigate radio-frequency interference.
- **Supporting Quote**:
   - “Onsala: The Onsala 25-m dish (O8) observed at L-band with varying frequency ranges and bandwidths over 14 nights… eventually, we settled for a 128 MHz wide band … between 1360–1488 MHz.” (Section 6.1.1)
- **Data Collection Period**:
   - **Overall Campaign**: As for all radio observations, O8 observed SGR 1935+2154 during the period from 2020 April 29 UT 22:45 (MJD 58968.94791) to 2020 May 25 UT 09:00 (MJD 58994.37500).
   - *Note*: Specific observing sessions for O8 are detailed in Table 4.
- **Wavelength(s)**:
   - Early configuration: 1222–1739 MHz (512 MHz bandwidth).
   - Later configuration: 1360–1488 MHz (128 MHz bandwidth).
- **Physical Observable**:
   - The L-band observations were used to detect radio burst fluence, dynamic spectra, and polarisation properties.
- **Additional Comments**:
   - Test sources (e.g. PSR J0358+5413 or PSR J1935+1616) were observed for system verification.

### 3. Onsala 20-m Telescope (O6)
- **General Comments**:
   - The Onsala 20-m telescope joined the campaign for two observing runs to cover a higher frequency range.
   - It operated in X-band and recorded the data similarly as a single dish.
- **Supporting Quote**:
   - “For two runs (06–08 May) the Onsala 20-m telescope (O6) joined the observations covering the frequency range 8080–8592 MHz (X-band), split into sixteen 32 MHz wide subbands.” (Section 6.1.1)
- **Data Collection Period**:
   - **Specific Runs**: Observations with O6 were conducted during two runs between 06 May and 08 May 2020.
   - **Supporting Quote**: “For two runs (06–08 May) …” (Section 6.1.1)
- **Wavelength(s)**:
   - X-band: 8080–8592 MHz.
- **Physical Observable**:
   - Measurements at X-band provided additional constraints on the radio burst brightness and broadened the frequency coverage.
- **Additional Comments**:
   - Data were recorded as 2-bit baseband VDIF files and later processed in the same burst-search pipeline as the other radio instruments.

### 4. Toruń 32-m Dish (Tr)
- **General Comments**:
   - The Toruń 32-m telescope was used to observe SGR 1935+2154 at C-band.
   - It provided an independent data set with coverage of a higher radio frequency range than the low-frequency instruments.
- **Supporting Quote**:
   - “Toruń: The 32-m dish at Toruń (Tr) observed at C-band for about 8 hrs during a total of 19 nights … We recorded the entire 256 MHz of bandwidth covering the frequency range of 4550–4806 MHz…” (Section 6.1.1)
- **Data Collection Period**:
   - **Overall Campaign**: Observations occurred on 19 nights within the campaign period (2020 April 29 UT to 2020 May 25 UT); a typical observing block lasted about 8 hours.
   - *Note*: Specific start and end times for each block are detailed in Table 4.
- **Wavelength(s)**:
   - C-band: 4550–4806 MHz.
- **Physical Observable**:
   - The C-band data facilitated the detection and timing analysis of the bursts, including peak flux density and spectral energy density.
- **Additional Comments**:
   - Regular test scans on pulsars were performed at the beginning and end of each run for gain calibration.

### 5. CHIME/FRB
- **General Comments**:
   - The Canadian Hydrogen Intensity Mapping Experiment Fast Radio Burst Project (CHIME/FRB) is an external instrument whose detection of an extremely bright burst from SGR 1935+2154 served as a major breakthrough.
   - It provided one of the first alerts that linked magnetar activity to bright radio bursts.
- **Supporting Quote**:
   - “On 2020 April 28 a breakthrough was made when independently detected an extremely bright radio burst from the Galactic magnetar SGR 1935+2154, using the Canadian Hydrogen Intensity Mapping Experiment Fast Radio Burst Project (CHIME/FRB)…” (Introduction)
- **Data Collection Period**:
   - The CHIME/FRB detection of the bright burst (FRB 200428) occurred on 2020 April 28.
- **Wavelength(s)**:
   - Observations were conducted at L-band (around 1.4 GHz).
- **Physical Observable**:
   - The instrument measured an extremely high burst fluence (∼MJy ms) and provided key information on the burst energy.
- **Additional Comments**:
   - This detection, in tandem with STARE2, reinforced the magnetar–FRB connection.

### 6. STARE2
- **General Comments**:
   - The Survey for Transient Astronomical Radio Emission 2 (STARE2) is another external radio instrument which independently detected the bright radio burst from SGR 1935+2154.
- **Supporting Quote**:
   - “... and the Survey for Transient Astronomical Radio Emission 2 (STARE2) … the reported burst ﬂuence was 1.5 MJy ms at 1.4 GHz.” (Introduction)
- **Data Collection Period**:
   - The detected burst occurred on 2020 April 28, coincident with the CHIME/FRB detection.
- **Wavelength(s)**:
   - Approximately 1.4 GHz (L-band).
- **Physical Observable**:
   - Measured a very high burst fluence that, when compared to other events, helped define the large energy range spanned by SGR 1935+2154.
- **Additional Comments**:
   - STARE2’s detection is used both for cross-validation and to assess the upper end of radio burst energies.

### 7. FAST (Five-hundred-meter Aperture Spherical Radio Telescope)
- **General Comments**:
   - FAST is a highly sensitive large-aperture radio telescope.
   - It independently detected a much fainter radio burst from SGR 1935+2154, complementing the bright bursts detected by CHIME/FRB and STARE2.
- **Supporting Quote**:
   - “A few days after the announcement … Zhang et al. used the Five-hundred-meter Aperture Spherical radio Telescope (FAST) to detect a much fainter (ﬂuence 60 mJy ms) burst from SGR 1935+2154.” (Introduction)
- **Data Collection Period**:
   - The exact observing dates aren’t detailed in this paper; the FAST detection is referenced as a follow-up event to the bright burst detection.
- **Wavelength(s)**:
   - Though not explicitly stated here, FAST observations of magnetars are typically performed in L-band.
- **Physical Observable**:
   - Detected a burst with a fluence of 60 mJy ms and high linear polarisation, providing insight into the lower-energy end of burst emissions.
- **Additional Comments**:
   - FAST’s detection highlights the wide dynamic range (over seven orders of magnitude) in observed burst energies from the same source.

### 8. NICER (Neutron star Interior Composition Explorer)
- **General Comments**:
   - NICER is an X-ray telescope aboard the International Space Station.
   - It performed pointed observations of SGR 1935+2154 during the radio campaign.
- **Supporting Quote**:
   - “Publicly available pointed observations were taken by the Neutron star Interior Composition ExploreR (NICER)… observing SGR 1935+2154 … during the radio campaign.” (Section 6.1.2)
- **Data Collection Period**:
   - NICER observed the source on seven occasions (ObsIDs 3020560107/8/25/33/37/40/42) during the overall campaign period (roughly 2020 April 29 to 2020 May 25).
- **Wavelength(s)/Energy Range**:
   - X-rays; the exact energy range is not specified but typical for NICER.
- **Physical Observable**:
   - NICER provided light curves and helped search for X-ray burst counterparts to the radio events.
- **Additional Comments**:
   - NICER data reduction followed standard HEAsoft procedures and was used to confirm the lack of X-ray bursts simultaneous with most of the radio events.

### 9. Swift/XRT (X-ray Telescope)
- **General Comments**:
   - Swift’s X-ray Telescope (XRT) is part of the Neil Gehrels Swift Observatory.
   - It performed pointed observations of SGR 1935+2154 concurrently with the radio campaign.
- **Supporting Quote**:
   - “Publicly available pointed observations were taken by … the Neil Gehrels Swift Observatory… observing SGR 1935+2154 … ten times during the radio campaign.” (Section 6.1.2)
- **Data Collection Period**:
   - Swift/XRT observed the source on ten separate occasions during the campaign (ObsIDs listed in the text), overlapping the 2020 April 29 to May 25 period.
- **Wavelength(s)/Energy Range**:
   - X-rays (typical Swift/XRT energy range, though the exact band is not specified here).
- **Physical Observable**:
   - Observations were used to extract light curves and search for possible X-ray bursts, with fluence and T90 measurements.
- **Additional Comments**:
   - Data reduction used standard procedures with xrtpipeline and xselect.

### 10. Fermi/GBM (Gamma-ray Burst Monitor)
- **General Comments**:
   - Fermi/GBM is a gamma-ray instrument on board the Fermi spacecraft used to monitor high-energy transients.
   - It provided high time resolution data to search for X-ray/gamma-ray counterparts to the radio bursts.
- **Supporting Quote**:
   - “While the source was in the ﬁeld of view of Fermi/GBM during the two radio bursts on 2020 May 24, no simultane-ous X-ray bursts were detected …” (Section 4.3)
   - Also: “For the GBM trigger on an X-ray burst … on 2020 May 20, 21:47:07.548 UT…” (Section 6.2.6)
- **Data Collection Period**:
   - Key events include a trigger on 2020 May 20 at 21:47:07.548 UT and TTE data collected on 2020 May 24 between 22:00–23:00 UT.
- **Wavelength(s)/Energy Range**:
   - High-energy gamma-rays and hard X-rays; the energy range mentioned in the paper spans roughly 1 to 500 keV.
- **Physical Observable**:
   - Fermi/GBM data were used to extract burst spectra and fluence estimates of X-ray bursts, even though no counterpart was identified for the radio bursts.
- **Additional Comments**:
   - Analysis involved dedicated tools (e.g. gtbin, gspec) to process cspec and TTE data.

### 11. HXMT (Hard X-ray Modulation Telescope / Insight-HXMT)
- **General Comments**:
   - HXMT is a hard X-ray instrument that provided an independent record of X-ray bursts overlapping with the radio monitoring.
   - It is also used in the compilation of burst lists that set upper limits on simultaneous radio emission.
- **Supporting Quote**:
   - “… we considered the observing schedule and burst list from the Hard X-ray Modulation Telescope (HXMT) …” (Section 4.3)
   - Table 3 lists numerous HXMT burst detection times.
- **Data Collection Period**:
   - HXMT detected multiple X-ray bursts with timestamps ranging from 2020-04-30 to 2020-05-25. For example, one burst is quoted as “2020-04-30T09:25:22.750” and the latest listed burst in Table 3 is “2020-05-25T00:57:45.000”.
- **Wavelength(s)/Energy Range**:
   - Hard X-rays, with reported energy ranges between 1 and 500 keV.
- **Physical Observable**:
   - HXMT provided burst fluences (e.g. up to 2.01×10^−6 erg cm^−2) and T90 values, serving to contrast the radio detections.
- **Additional Comments**:
   - The HXMT burst list is used to underscore that the majority of X-ray bursts observed are not associated with a detected radio burst.

### 12. AGILE
- **General Comments**:
   - AGILE is mentioned as one of the satellites that detected a hard X-ray burst simultaneously with the bright radio burst from SGR 1935+2154.
- **Supporting Quote**:
   - “Temporally coincident with the radio pulse, a bright, hard X-ray burst was detected independently by the Konus-Wind, INTEGRAL, AGILE and Insight-HXMT satellites.” (Introduction)
- **Data Collection Period**:
   - The AGILE detection is associated with the event on 2020 April 28.
- **Wavelength(s)/Energy Range**:
   - Hard X-rays.
- **Physical Observable**:
   - AGILE contributed to the measurement of the burst fluence in the X-ray band.

### 13. INTEGRAL
- **General Comments**:
   - INTEGRAL is another high-energy observatory that independently detected a hard X-ray burst simultaneously with the radio burst.
- **Supporting Quote**:
   - “Temporally coincident with the radio pulse, a bright, hard X-ray burst was detected … by INTEGRAL …” (Introduction)
- **Data Collection Period**:
   - The INTEGRAL detection is linked to the burst event on 2020 April 28.
- **Wavelength(s)/Energy Range**:
   - Hard X-rays (across energy ranges roughly 1–500 keV).
- **Physical Observable**:
   - Provided measurements of the burst’s high-energy fluence.

### 14. Konus-Wind
- **General Comments**:
   - Konus-Wind is cited as having independently detected the bright X-ray counterpart of the radio burst.
- **Supporting Quote**:
   - “Temporally coincident … a bright, hard X-ray burst was detected independently by the Konus-Wind, … satellites.” (Introduction)
- **Data Collection Period**:
   - The Konus-Wind detection is associated with the 2020 April 28 event.
- **Wavelength(s)/Energy Range**:
   - Hard X-rays.
- **Physical Observable**:
   - Measured the high-energy burst properties in coincidence with the radio detection.

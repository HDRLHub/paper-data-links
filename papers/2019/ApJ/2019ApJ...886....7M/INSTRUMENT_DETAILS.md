_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper develops a comprehensive uncertainty quantification model for sunspot counts by analyzing 66 years of observations (from January 1, 1947 to December 31, 2013). Data from a network of 21 ground‐based observatories are used to construct estimates for the number of spots (Ns), groups (Ng), and the composite index Nc = Ns + 10Ng. The work details robust estimation procedures, pre‐processing methods (including scaling using ordinary least-squares regression), and error modelling in both short-term and long-term regimes. In addition, a comparison is made with a sunspot catalogue obtained from space using an automated algorithm (STARA) applied to images from the MDI instrument on SOHO, which provides an independent reference for the solar signal over the period May 1996 to October 2010.

## Instrumentation Details

### 1. Athens Observatory (A3) – Athens (Greece)
- **General Comments**:
  - A professional observatory operated by a team, contributing sunspot counts to the network.
- **Supporting Quote**: 
  - "A3 Athens Observatory Athens (Greece) Prof. team 1949-1995" (see Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1949 – December 1995
  - **Supporting Quote**: "Observing period: 1949-1995" (Table 1)
- **Wavelength(s)**: Not specified (observations are made on white light images)
  - **Supporting Quote**: "On white light images, sunspots are visible as dark areas" (Section 1.1)
- **Physical Observable**: Sunspot counts (Ns), sunspot groups (Ng) and composite index (Nc)
  - **Supporting Quote**: "…each station reports the daily number of spots Ns, groups Ng and the composite Nc…" (Section 2)
- **Additional Comments**: The reported data are later rescaled and used to estimate the underlying solar signal.

---

### 2. WFS Observatory (SONNE) – Berlin, Germany (BN-S)
- **General Comments**:
  - An amateur team observatory contributing to the network with its own scaling factor.
- **Supporting Quote**:
  - "BN-S WFS Observatory (SONNE) Berlin (Germany) Am. team 1965-2013" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1965 – December 2013
  - **Supporting Quote**: "Observing period: 1965-2013" (Table 1)
- **Wavelength(s)**: Not specified; observations assumed on white light images.
- **Physical Observable**: Counts of sunspots, groups, and the derived composite number.
- **Additional Comments**: Its scaling factor (level = 1.179) indicates that it routinely reports around 18% more spots than the network median.

---

### 3. Catania Observatory – Catania, Italy (CA)
- **General Comments**:
  - A professional team observatory contributing long-term sunspot count data.
- **Supporting Quote**:
  - "CA Catania Observatory Catania (Italy) Prof. team 1950-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1950 – December 2019
  - **Supporting Quote**: "Observing period: 1950-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily counts of sunspots and groups used to compute the composite index.
- **Additional Comments**: A key station for long-term solar activity reconstruction.

---

### 4. T. Cragg (AAVSO) – Australia (CRA)
- **General Comments**:
  - An individual amateur observer contributing to the sunspot count network.
- **Supporting Quote**:
  - "CRA T. Cragg (AAVSO) Australia Am indiv. 1947-2009" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1947 – December 2009
  - **Supporting Quote**: "Observing period: 1947-2009" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Sunspot counts and derived composite numbers.
- **Additional Comments**: As part of a long-standing series, its data contribute to the statistical robustness of the uncertainty model.

---

### 5. Fujimori – Nagano, Japan (FU)
- **General Comments**:
  - An individual amateur observatory known for consistent sunspot observations.
- **Supporting Quote**:
  - "FU Fujimori Nagano (Japan) Am indiv. 1968-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1968 – December 2019
  - **Supporting Quote**: "Observing period: 1968-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Records daily sunspot counts, groups, and composite values.
- **Additional Comments**: Its level of 1.055 suggests a modest scaling relative to the network median.

---

### 6. Hedewig (SONNE) – Germany (HD-S)
- **General Comments**:
  - An individual amateur observatory that contributes to the network’s dataset.
- **Supporting Quote**:
  - "HD-S Hedewig (SONNE) Germany Am indiv. 1967-2013" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1967 – December 2013
  - **Supporting Quote**: "Observing period: 1967-2013" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily sunspot counts used in constructing statistical models.
- **Additional Comments**: The reported level is slightly lower (0.931), indicating fewer counts relative to the median.

---

### 7. Public Observatory – Hurbanovo, Slovakia (HU)
- **General Comments**:
  - An amateur team observatory contributing sunspot data over several decades.
- **Supporting Quote**:
  - "HU Public Observatory Hurbanovo (Slovakia) Am team 1969-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1969 – December 2019
  - **Supporting Quote**: "Observing period: 1969-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Sunspot counts, groups, and composite index.
- **Additional Comments**: Its scaling factor of 1.004 indicates near agreement with network medians.

---

### 8. KOERI – Kandilli, Turkey (KH)
- **General Comments**:
  - A professional team observatory providing systematic sunspot observations.
- **Supporting Quote**:
  - "KH KOERI Kandilli (Turkey) Prof. team 1967-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1967 – December 2019
  - **Supporting Quote**: "Observing period: 1967-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily sunspot and group counts.
- **Additional Comments**: Its mean scaling factor is 0.968, closely tracking the network average.

---

### 9. I. Koyama – Japan (KOm)
- **General Comments**:
  - An individual amateur observatory contributing early and long-duration observations.
- **Supporting Quote**:
  - "KOm I. Koyama Japan Am indiv. 1947-1996" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1947 – December 1996
  - **Supporting Quote**: "Observing period: 1947-1996" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Records of sunspot counts that are used to estimate the true solar signal.
- **Additional Comments**: Its level of 1.052 reflects a slightly higher count compared to the network median.

---

### 10. Observatory – Kislovodsk, Russia (KS2)
- **General Comments**:
  - An individual professional observatory known for extensive sunspot data collection.
- **Supporting Quote**:
  - "KS2 Observatory Kislovodsk (Russia) Prof. indiv. 1954-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1954 – December 2019
  - **Supporting Quote**: "Observing period: 1954-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Continuous daily measurements of spot counts used in statistical analyses.
- **Additional Comments**: Its long data record aids in establishing reliable network statistics.

---

### 11. University of Graz – Kanzelhohe, Austria (KZm)
- **General Comments**:
  - A professional team observatory providing extensive data since the mid-20th century.
- **Supporting Quote**:
  - "KZm University of Graz Kanzelhohe (Austria) Prof. team 1944-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1944 – December 2019
  - **Supporting Quote**: "Observing period: 1944-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: The daily sunspot counts are integrated into the composite index Nc.
- **Additional Comments**: With a scaling factor of 1.110, it typically reports a higher number of spots relative to many other stations.

---

### 12. H. Luft – New York, USA (LFm)
- **General Comments**:
  - An individual amateur observatory that contributed sunspot counts for several decades.
- **Supporting Quote**:
  - "LFm H. Luft New York (USA) Am indiv. 1944-1988" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1944 – December 1988
  - **Supporting Quote**: "Observing period: 1944-1988" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Sunspot and group counts.
- **Additional Comments**: The level of 0.985 suggests observations very close to the network benchmark.

---

### 13. Specola Solare Locarno – Locarno, Switzerland (LO)
- **General Comments**:
  - A professional individual observatory that serves as a current reference in the network; its counts are often used as a benchmark.
- **Supporting Quote**:
  - "LO Specola Solare Locarno (Switzerland) Prof. indiv. 1958-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1958 – December 2019
  - **Supporting Quote**: "Observing period: 1958-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily counts note particularly a higher average count (level = 1.260) attributed to its method of counting larger spots.
- **Additional Comments**: The Locarno station is highlighted in the analysis as a reference point given its low short-term variability.

---

### 14. Manila – Philippines (MA)
- **General Comments**:
  - A professional team observatory contributing to the network for a defined period.
- **Supporting Quote**:
  - "MA Manila (Philippines) Prof. team 1971-1988" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1971 – December 1988
  - **Supporting Quote**: "Observing period: 1971-1988" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Recorded sunspot and group counts for use in the composite index.
- **Additional Comments**: With a level of 1.023, its observations are integrated into the network with modest scaling adjustments.

---

### 15. Mochizuki – Urawa, Saitama, Japan (MO)
- **General Comments**:
  - An individual amateur observatory noted for stable observations over a long span.
- **Supporting Quote**:
  - "MO Mochizuki (Urawa) Saitama (Japan) Am indiv. 1978-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1978 – December 2019
  - **Supporting Quote**: "Observing period: 1978-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Counts of sunspots used to compute Ns, Ng, and Nc.
- **Additional Comments**: Its scaling factor (1.073) and noted short-term stability mark it as a reliable contributor.

---

### 16. Observatory Postdam – Germany (PO)
- **General Comments**:
  - A professional team observatory that recorded sunspot data over several solar cycles.
- **Supporting Quote**:
  - "PO Observatory Postdam (Germany) Prof. team 1955-1999" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1955 – December 1999
  - **Supporting Quote**: "Observing period: 1955-1999" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily sunspot counts leading to composite indices.
- **Additional Comments**: With a level of 0.991, its data adhere closely to the network median.

---

### 17. PAGASA Weather Bureau – Quezon, Philippines (QU)
- **General Comments**:
  - An individual professional observatory that provides sunspot counts and exhibits notable short-term variability.
- **Supporting Quote**:
  - "QU PAGASA weather Bureau Quezon (Philippines) Prof. indiv. 1957-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1957 – December 2019
  - **Supporting Quote**: "Observing period: 1957-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily counts used in the overall uncertainty analysis.
- **Additional Comments**: Its lower level (0.829) indicates that it generally records fewer spots compared to the network median.

---

### 18. Schulze (SONNE) – Germany (SC-S)
- **General Comments**:
  - An individual amateur observatory with a long record of sunspot observations.
- **Supporting Quote**:
  - "SC-S Schulze (SONNE) Germany Am indiv. 1960-2007" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1960 – December 2007
  - **Supporting Quote**: "Observing period: 1960-2007" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Sunspot and group counts utilized in the composite index.
- **Additional Comments**: Its measurements help define the short-term error distributions explored in the paper.

---

### 19. Skalnate Pleso Observatory – Vysoke Tatry, Slovakia (SK)
- **General Comments**:
  - A professional team observatory that provides consistent sunspot observations.
- **Supporting Quote**:
  - "SK Skalnate Pleso Obs. Vysoke Tatry (Slovakia) Prof. team 1950-2012" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1950 – December 2012
  - **Supporting Quote**: "Observing period: 1950-2012" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Daily counts feeding into statistical assessments of solar activity.
- **Additional Comments**: Its scaling level (0.992) is near unity, suggesting close agreement with network-wide measurements.

---

### 20. San Miguel – Argentina (SM)
- **General Comments**:
  - A professional team observatory known for recording noticeable long-term drifts along with short-term variability.
- **Supporting Quote**:
  - "SM San Miguel (Argentina) Prof. team 1967-2013" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1967 – December 2013
  - **Supporting Quote**: "Observing period: 1967-2013" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: Counts of sunspots, groups and the derived composite index.
- **Additional Comments**: With a high scaling factor (1.220), SM is noted for substantial long-term variability.

---

### 21. USET – Uccle, Belgium (UC)
- **General Comments**:
  - A professional team observatory contributing a long-term series of sunspot measurements.
- **Supporting Quote**:
  - "UC USET Uccle (Belgium) Prof. team 1949-2019" (Table 1)
  
#### Data Collection Period 1: Observing Period for Sunspot Recordings
- **Time Range**: January 1949 – December 2019
  - **Supporting Quote**: "Observing period: 1949-2019" (Table 1)
- **Wavelength(s)**: Not specified.
- **Physical Observable**: The daily number of spots, groups, and composite index Nc.
- **Additional Comments**: Its level of 0.991 illustrates a close adherence to the network’s median activity.

---

### 22. MDI Instrument on SOHO (via the STARA Sunspot Catalogue)
- **General Comments**:
  - A space-based instrument used to obtain sunspot counts from satellite images. Its automated sunspot detection (via the STARA algorithm) provides a reference for comparison with ground-based observations.
- **Supporting Quote**:
  - "…we use the Sunspot Tracking And Recognition Algorithm (STARA) sunspot catalogue (Watson & Fletcher 2010), regrouping observations from May 1996 to October 2010 (solar cycle 23). This number is extracted using an automated detection algorithm from the images obtained by the MDI instrument on SOHO." (Section 5.2)
  
#### Data Collection Period 1: Satellite-based Sunspot Observations
- **Time Range**: May 1996 – October 2010
  - **Supporting Quote**: "regrouping observations from May 1996 to October 2010" (Section 5.2)
- **Wavelength(s)**: Not specified; observations are based on solar images acquired by the MDI instrument.
- **Physical Observable**: Sunspot counts derived from automated detection on satellite images.
- **Additional Comments**: Although the MDI instrument provides data with lower variability due to automated procedures, its measurements are biased by detection rules (e.g., exclusion of pores) and mainly serve as a benchmark for comparison with ground-based count estimators.

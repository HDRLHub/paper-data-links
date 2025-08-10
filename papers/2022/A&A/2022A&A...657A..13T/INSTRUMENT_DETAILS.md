_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper explores the classification of gamma‐ray bursts (GRBs) using graph‐based clustering methodologies. Different GRB samples collected by several high-energy astrophysics instruments are examined in a two‐dimensional parameter space defined by burst duration (T₉₀ or T₉₉) and a hardness ratio (H32 or its instrument‐specific counterpart). The study compares the outcomes of various graph‐based methods (such as continuous k-nearest neighbour, CutPC, connectivity-based, and fast density peaks) on data sets from multiple instruments. Although the exact observation dates or a specific time range for individual instruments is not provided, each instrument’s sample size and derived physical observables (e.g. duration and hardness ratio, along with fluence in specific energy bands) play a central role in the analyses and conclusions regarding the existence of two or three GRB classes.

## Instrumentation Details

### 1. Fermi Gamma-Ray Space Telescope
- **General Comments**:
   - The Fermi data set comes from the third catalogue and includes GRBs with measurements of durations and hardness ratios. Its role is to provide a large sample for statistical clustering analysis.
- **Supporting Quote**: 
   - "The Fermi data set from the third catalogue consists of 1376 GRBs with measured T₉₀ and H32..." 
- **Data Collection Period 1: General Fermi GRB Observations**
   - **Time Range**: Not specified in the paper.
     - **Supporting Quote**: There is no explicit start and end time provided for the Fermi observations.
   - **Wavelength(s)**: Not explicitly detailed; the instrument provides fluence measurements in designated energy bands that define the hardness ratio H32.
     - **Supporting Quote**: "For each instrument, fluences in different energy bands are available, hence the definitions of H32 are as follows: H32 = Fₒₑ for Swift; ..." (by analogy, Fermi’s H32 is used).
   - **Physical Observable**: Duration (T₉₀/T₉₉) and hardness ratio (H32) are the primary observables.
     - **Supporting Quote**: "GRBs ... are confidently divided into two classes: short and long... the bimodal distribution of durations T₉₉... and [the] hardness ratio H32..."
   - **Additional Comments**: The Fermi sample aids in comparing clustering outcomes with other instruments despite no specified observation time span.

### 2. BATSE (Burst And Transient Source Experiment)
- **General Comments**:
   - BATSE, onboard the Compton Gamma-Ray Observatory, provided a comprehensive GRB catalog with measurements of durations and hardness ratios in slightly different energy bands compared to other instruments.
- **Supporting Quote**:
   - "The Burst And Transient Source Experiment (BATSE) onboard the Compton Gamma-Ray Observatory observed 1954 GRBs with T₉₀ and H32, with the hardness ratio computed within slightly different energy bands: H3 = £09-300v..."
- **Data Collection Period 1: BATSE GRB Observations**
   - **Time Range**: Not specified in the paper.
     - **Supporting Quote**: The paper does not list explicit start and end dates for BATSE's observations.
   - **Wavelength(s)**: Different energy band definition is mentioned; although the precise numerical limits are only partially legible, it is understood that the energy band differs from that of other instruments.
     - **Supporting Quote**: "…with the hardness ratio computed within slightly different energy bands: H3 = £09-300v..."
   - **Physical Observable**: T₉₀ (or T₉₉) durations and the corresponding hardness ratio H32 are used for clustering.
     - **Supporting Quote**: "…observed 1954 GRBs with T₉₀ and H32..."
   - **Additional Comments**: After certain outliers were excluded, the sample used consists of 1953 GRBs.

### 3. Swift Burst Alert Telescope (BAT)
- **General Comments**:
   - The Swift instrument provides a catalogue of GRBs with a focus on both short and long burst durations, with the additional benefit of sensitivity to softer energy bands.
- **Supporting Quote**:
   - "The following four data sets are also considered: 1028 GRBs from the Swift Burst Alert Telescope catalogue (Lien et al. 2016)..."
- **Data Collection Period 1: Swift GRB Observations**
   - **Time Range**: Not specified in the paper.
     - **Supporting Quote**: There is no mention of explicit dates or UT ranges for the Swift observations.
   - **Wavelength(s)**: While the exact energy band limits are not clarified, Swift’s hardness ratio is derived from its fluence measurements in the designated energy ranges.
     - **Supporting Quote**: "For each instrument, fluences in different energy bands are available, hence the definitions of H32 are as follows: H32 = Fₒₑ for Swift..."
   - **Physical Observable**: Burst duration and hardness ratio (via fluence in selected bands) are the observables.
     - **Supporting Quote**: "...identification of short and long GRBs is confirmed by differences in T₉₀ (or T₉₉) and H32."
   - **Additional Comments**: The Swift data set is noted to exhibit non-uniform density of points, affecting the clarity of clustering outcomes.

### 4. Konus-Wind
- **General Comments**:
   - Konus-Wind provides a sizeable GRB sample and contributes to the multi-instrument comparison by offering its own definitions for the hardness ratio.
- **Supporting Quote**:
   - "…1143 GRBs observed by Konus-Wind (Svinkin et al. 2016)..."
- **Data Collection Period 1: Konus-Wind GRB Observations**
   - **Time Range**: Not specified in the paper.
     - **Supporting Quote**: The paper does not provide any explicit time range for Konus-Wind observations.
   - **Wavelength(s)**: Its hardness ratio, labeled H3.2 in the text, is defined from fluence measurements in a specific energy band, though exact numerical values are not fully legible.
     - **Supporting Quote**: "…for each instrument, fluences in different energy bands are available, hence the definitions of H32 are as follows: ... H3.2 = ==" for Konus..."
   - **Physical Observable**: The main observables are the GRB duration and hardness ratio.
     - **Supporting Quote**: "…with measurements of T₉₀ and the corresponding hardness ratios..."
   - **Additional Comments**: In the clustering results, Konus data sometimes exhibit partitions into more than two groups; however, the predominant division aligns with the short-long dichotomy.

### 5. RHESSI
- **General Comments**:
   - RHESSI contributes an independent GRB sample with its own instrumental characteristics and energy band definitions.
- **Supporting Quote**:
   - "…426 GRBs detected by RHESSI (Ripa et al.…)…"
- **Data Collection Period 1: RHESSI GRB Observations**
   - **Time Range**: Not specified in the paper.
     - **Supporting Quote**: There is no provided observation period (start and end dates) for RHESSI in the text.
   - **Wavelength(s)**: The hardness ratio for RHESSI is defined (referred to as H3, with units in keV) based on fluence measurements.
     - **Supporting Quote**: "…for each instrument, fluences in different energy bands are available, hence the definitions of ... Ay = [value] for RHESSI..."
   - **Physical Observable**: As with the other instruments, GRB durations (T₉₀/T₉₉) and the hardness ratio are the key observables.
     - **Supporting Quote**: "…utilised GRB samples with measured T₉₀ (or T₉₉) and hardness ratios..."
   - **Additional Comments**: The clustering of RHESSI GRBs most confidently divides the data into two groups – consistent with standard short and long classification.

### 6. Suzaku Wide-Band All-Sky Monitor
- **General Comments**:
   - Suzaku’s GRB sample, although smaller and refined by removing duplicates, serves as an additional dataset to cross-check the clustering results obtained from the larger instruments.
- **Supporting Quote**:
   - "…257 GRBs from Suzaku Wide-Band All-Sky Monitor (mori et al. 2016) … two duplicates in the Suzaku sample were removed..."
- **Data Collection Period 1: Suzaku GRB Observations**
   - **Time Range**: Not specified in the paper.
     - **Supporting Quote**: The manuscript does not list a specific starting or ending date for Suzaku observations.
   - **Wavelength(s)**: The hardness ratio for Suzaku, denoted as H3, is defined using fluence measurements in its respective energy band (with units in keV).
     - **Supporting Quote**: "…and H3, = ae for Suzaku keV:" (noting the corrupted but indicative text for energy band specification).
   - **Physical Observable**: The principal observables are the GRB duration and hardness ratio.
     - **Supporting Quote**: "…where for each instrument, fluences in different energy bands are available, hence the definitions of H32 (or H3, for Suzaku)..."
   - **Additional Comments**: The clustering outcomes from Suzaku data tend to confidently reveal two groups, aligning with the short-long GRB dichotomy.

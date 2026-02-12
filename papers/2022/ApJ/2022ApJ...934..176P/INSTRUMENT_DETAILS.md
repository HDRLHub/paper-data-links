_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper focuses on developing a machine learning model to predict the geoeffectiveness of coronal mass ejections (CMEs) using solar onset parameters. The study employs various machine learning techniques, including logistic regression, K-Nearest Neighbors, Support Vector Machines, and neural networks, to classify CMEs based on their potential to cause geomagnetic storms. The research utilizes data from the Solar and Heliospheric Observatory (SOHO) Large Angle and Spectrometric Coronagraph (LASCO) catalog, the Solar H-alpha Flare Index, and the Richardson & Cane catalog, covering the period from 1996 to 2014. The study addresses challenges such as class imbalance and class overlap in the dataset and aims to provide early warnings for potentially geoeffective CMEs.

## Instrumentation Details

### Large Angle and Spectrometric Coronagraph (LASCO) on board Solar and Heliospheric Observatory (SOHO)
- **General Comments**:
   - LASCO is used to observe CMEs and their attributes, providing essential data for the study's machine learning models.
- **Supporting Quote**: "The dataset utilized for this research contains aggregated data from 3 different sources: the Solar and Heliospheric Observatory (SOHO; Domingo et al. 1995) Large Angle and Spectrometric Coronagraph (LASCO; Brueckner et al. 1995) catalog, provided by the ‘Coordinated Data Analysis Workshops (CDAW) Data Center’1, for the CMEs’ attributes..."

#### Data Collection Period 1: General observation of CMEs
- **Time Range**: 1996 – 2014
   - **Supporting Quote**: "Since its launch in 1995, LASCO has been producing synoptic observations with a cadence of 12 minutes per coronagraph, to the present day... Therefore, the collected data covers the period between 1996 and 2014."
- **Wavelength(s)**: Not specified
   - **Supporting Quote**: Not explicitly mentioned in the provided context.
- **Physical Observable**: CMEs' attributes such as Central Position Angle (CPA), Angular Width (AW), Measurement Position Angle (MPA), Linear Speed (LS), etc.
   - **Supporting Quote**: "All other attributes available in the catalog (i.e., Central Position Angle - CPA, Angular Width - AW, Measurement Position Angle - MPA, Linear Speed - LS, 2nd order Speed at final height, 2nd order Speed at 20 Rs, Acceleration - Acc) were taken into consideration."
- **Additional Comments**: The LASCO catalog is used to identify geoeffective events by correlating with the Richardson & Cane catalog.

### Solar H-alpha Flare Index (FI)
- **General Comments**:
   - The Solar H-alpha Flare Index is used to quantify daily flare activity, which is considered a significant driver for intense geomagnetic storms.
- **Supporting Quote**: "In addition to the above-mentioned parameters, we use the FI as input for our models, similar to Uwamahoro et al. (2012)’s approach concerning the use of neural networks for predicting the geoeffectiveness of halo CMEs."

#### Data Collection Period 1: General observation of solar flares
- **Time Range**: 1976 – 2014
   - **Supporting Quote**: "Due to the FI only being made available for the 1976-2014 timeframe, we needed to also restrict the data from the LASCO catalog up until 2014 only."
- **Wavelength(s)**: Not specified
   - **Supporting Quote**: Not explicitly mentioned in the provided context.
- **Physical Observable**: Daily flare activity
   - **Supporting Quote**: "The index’s purpose is to quantify the daily flare activity."
- **Additional Comments**: The FI does not address individual events but provides daily averages of flaring activity.

_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper focuses on the automated identification of coronal holes (CHs) using extreme ultraviolet (EUV) synoptic maps from multiple instruments. The authors use data recorded at three wavelengths (195/193 Å, 171 Å, and 304 Å) to capture the various emissions corresponding to different temperature regimes in the solar atmosphere. Additionally, the study incorporates synoptic magnetic field maps to distinguish true CH regions from filament channels based on their magnetic flux imbalance. The datasets span from 1996 to early 2017 and cover major parts of solar cycles 23 and 24. A key component in the study is the dynamic adjustment of the CH threshold intensity by selecting the optimum image segment in each synoptic map. This method is applied to datasets obtained from SOHO/EIT and SDO/AIA (for EUV imaging) as well as SOHO/MDI and SDO/HMI (for magnetic measurements).

---

## Instrumentation Details

### 1. SOHO/EIT (Extreme Ultraviolet Imaging Telescope)
- **General Comments**:
  - SOHO/EIT is used to obtain synoptic maps of the solar atmosphere in selected EUV wavelengths. The instrument observes in multiple emission lines that include the Fe XII (195 Å), Fe IX–X (171 Å), and He II (304 Å), providing temperature diagnostics from ≈6×10⁴ K to 3×10⁶ K.
  - The study utilizes two separate datasets from SOHO/EIT: one produced by the Stanford Solar Observatories Group and another by the Space Weather Lab at George Mason University.
  - The data undergo preprocessing (binning, scaling, and intensity homogenization) in order to construct maps in 1°×1° heliographic resolution.

- **Supporting Quote**:  
  "Synoptic maps based on the data from SOHO/EIT (Delaboudinière et al., 1995) give a view of the solar atmosphere in four different wavelengths in 1996-2010... The synoptic maps for CR 1911 (1996 June 28) - CR 2042 (2006 April 10) are based on calibrated data... Another set of EIT/EUV synoptic maps for the same wavelengths, covering CR 2058 (2007 June 21) - CR 2102 (2010 October 03) are provided by Space Weather Lab at George Mason University."

#### Data Collection Period 1: EIT-1 Period
- **Time Range**: CR 1911 (June 28, 1996) – CR 2055 (March 31, 2007)
  - **Supporting Quote**:  
    "Synoptic maps based on the data from SOHO/EIT ... constructed by Benevolenskaya, Kosovichev, and Scherrer (2001) from CR 1911 (1996 June 28) to CR 2055 (2007 March 31)..."
- **Wavelength(s)**: 195 Å, 171 Å, and 304 Å
  - **Supporting Quote**:  
    "They [the maps] are obtained at three different wavelengths (195˚ A/193˚ A, 171˚ A and 304˚ A) measured by SOHO/EIT..."
- **Physical Observable**: EUV intensity which maps coronal structures such as active regions, quiet Sun, and coronal holes.
- **Additional Comments**:  
  - The original 1024×1024 images are binned to 512×512 for the Stanford maps and transformed to a Carrington coordinate system.
  - The intensity calibration is maintained over a period (2003–2007) when the distributions are stable.

#### Data Collection Period 2: EIT-2 Period
- **Time Range**: CR 2058 (June 21, 2007) – CR 2102 (October 03, 2010)
  - **Supporting Quote**:  
    "Another set of EIT/EUV synoptic maps for the same wavelengths, covering CR 2058 (2007 June 21) - CR 2102 (2010 October 03) are provided by Space Weather Lab at George Mason University."
- **Wavelength(s)**: 195 Å, 171 Å, and 304 Å (same as EIT-1)
- **Physical Observable**: EUV emissions indicating temperature and density variations used to delineate coronal holes versus active regions.
- **Additional Comments**:
  - The maps in this period have higher resolution (3600×1080 pixels with 0.1°×0.1667° sampling).
  - Some synoptic maps during this period are missing; about 23 of 45 are not available.

---

### 2. SDO/AIA (Atmospheric Imaging Assembly)
- **General Comments**:
  - The SDO/AIA instrument records high-resolution solar EUV images across several wavelengths and is less affected by cosmic rays or solar proton events because SDO is in a geosynchronous orbit.
  - It provides observations analogous to those of SOHO/EIT but with improved spatial resolution and a different sensitivity profile. The AIA data are particularly noted for calibration drifts and sudden shifts (instrument bakeouts) that influence the intensity histograms.
  
- **Supporting Quote**:  
  "Synoptic maps based on the data from SDO/AIA EUVI sensor were obtained for CR 2097 (2010 May 20) - CR 2186 (2017 January 10) from Space Weather Lab at George Mason University (Karna, Hess Webber, and Pesnell, 2014)."
  
#### Data Collection Period:
- **Time Range**: CR 2097 (May 20, 2010) – CR 2186 (January 10, 2017)
  - **Supporting Quote**:  
    "These maps ... cover all longitudes and all measured latitudes at best up to ± 90°... for CR 2097 (2010 May 20) - CR 2186 (2017 January 10)."
- **Wavelength(s)**: 193 Å, 171 Å, and 304 Å
  - **Supporting Quote**:  
    "SDO/AIA EUV wavelengths are listed in Table 1. For AIA observations in 193˚ A, the measurements are primarily from the Fe XII (1.6×10^6 K) emission..."
- **Physical Observable**: EUV intensity that reveals coronal structures. In the 193 Å channel, additional emission from Fe XXIV (formation temperature of about 10×10^6 K) is present.
- **Additional Comments**:
  - The resolution of the SDO/AIA synoptic maps is 3600×1080 pixels.
  - Instrument degradation and calibration drifts (e.g., sudden jumps in intensity distributions) are noted issues that the study mitigates by constructing a composite CH map from the three wavelengths.

---

### 3. SOHO/MDI (Michelson Doppler Imager)
- **General Comments**:
  - SOHO/MDI provides synoptic maps of the radial magnetic field over the solar disk.
  - It is used in the paper to identify magnetic properties of CH regions and to differentiate coronal holes from filament channels based on the relative magnetic flux imbalance.
  
- **Supporting Quote**:  
  "Synoptic maps of both SOHO/MDI and SDO/HMI were obtained from the Stanford University ... The SOHO/MDI maps have a resolution of 3600×1080 ... and also incorporate a polar field interpolation."
  
#### Data Collection Period:
- **Time Range**: CR 1911 (June 28, 1996) – CR 2102 (October 03, 2010)
  - **Supporting Quote**:  
    "SOHO/MDI ... available for the same period as the SOHO/EIT maps, from CR 1911 (1996 June 28) to CR 2102 (2010 October 03)."
- **Physical Observable**: Radial magnetic field measurements that indicate magnetic flux and polarity.
- **Additional Comments**:
  - The maps are expressed in equally spaced longitude and sine latitude.
  - A polar field interpolation is applied to fill data gaps in the polar regions.

---

### 4. SDO/HMI (Helioseismic and Magnetic Imager)
- **General Comments**:
  - SDO/HMI is used to obtain synoptic maps of the photospheric radial magnetic field.
  - It complements SOHO/MDI and provides magnetic measurements during the later period corresponding to the SDO/AIA dataset.
  
- **Supporting Quote**:  
  "Synoptic maps of both SOHO/MDI and SDO/HMI were obtained ... (3600×1440, respectively)... with the SDO/HMI maps used to study the magnetic field properties during the same time period as the AIA EUV observations."
  
#### Data Collection Period:
- **Time Range**: CR 2097 (May 20, 2010) – CR 2186 (January 10, 2017)
  - **Supporting Quote**:  
    "SDO/HMI ... data are available from CR 2097 (2010 May 20) to CR 2186 (2017 January 10)."
- **Physical Observable**: The measured radial (line-of-sight corrected) photospheric magnetic field.
- **Additional Comments**:
  - The resolution of the HMI maps is 3600×1440 pixels.
  - Unlike the MDI maps, HMI synoptic maps include only the directly measured regions without polar field filling.

---

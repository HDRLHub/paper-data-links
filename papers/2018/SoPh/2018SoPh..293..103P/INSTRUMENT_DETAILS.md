_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: This paper describes an innovative onboard automated algorithm for detecting coronal mass ejections (CMEs) using the Visible Emission Line Coronagraph (VELC) onboard India’s ADITYA-L1 mission. The study explains the synthesis of coronal images, the simulation of CMEs with varying speeds, intensities, and morphologies, and the detailed working of the algorithm based on intensity and area thresholding. In order to validate the algorithm, the authors apply it to data from existing space‐ and ground‐based coronagraphs (notably STEREO/SECCHI COR-1A and K-Cor) as well as to simulated VELC images. The paper also reviews other historical and upcoming instruments (e.g., LASCO on SOHO, ASPIICS on PROBA-3, and METIS on Solar Orbiter) which have contributed to our understanding of CMEs over various observation periods.

---

## Instrumentation Details

### 1. Visible Emission Line Coronagraph (VELC) on board ADITYA‑L1
- **General Comments**:
  - VELC is a key payload of India’s first space mission, ADITYA‑L1, designed to study the dynamics of the inner coronal mass ejections.
  - It is configured to capture high-resolution (≈2.51 arcsec pixel⁻¹) white‑light images of the corona over a field of view from 1.05 R⊙ to 3 R⊙.
  - The instrument uses a 10 Å passband centered at 5000 Å and is capable of high‑cadence observations (1 image per second) with onboard processing to reduce telemetry.
  
- **Supporting Quote**:
  - “Visible Emission Line Coronagraph (VELC) is one of the seven payloads in ADITYA-L1 mission scheduled to be launched around 2020. One of the primary objectives of the VELC is to study the dynamics of coronal mass ejections (CMEs) in the inner corona. This will be accomplished by taking high resolution (≈2.51 arcsec pixel−1) images of corona from 1.05 R⊙– 3 R⊙ at high cadence of 1 s in 10 ˚A passband centered at 5000 ˚A.”

- #### Data Collection Period 1: Continuous Daily Coronagraph Observations
  - **Time Range**: Although no explicit UT start and end times are provided, the paper indicates that VELC is expected to operate continuously (e.g., generating ~8640 images in 24 hours).
    - *Supporting Quote*: “…considering 24 hours of operation of the instrument a total of 8640 images (24 × 60 × 6) will be generated each day.”
  - **Wavelength(s)**: 5000 Å (10 Å wide passband)
    - *Supporting Quote*: “…images of corona with high resolution (≈2.51 arcsec pixel−1) at wavelength of 5000 ˚A…”
  - **Physical Observable**: White‑light coronal brightness used to study the structure and dynamics of CMEs.
    - *Supporting Quote*: “…to capture dynamic coronal features such as CMEs…”
  - **Additional Comments**: The detector is a CMOS device set with an exposure time of 100 ms (to avoid saturation) and uses onboard frame summing and binning to build the coronal signal.

---

### 2. STEREO/SECCHI COR‑1A
- **General Comments**:
  - STEREO COR‑1A is a space‑based white‑light coronagraph that provides images with a field of view similar to VELC.
  - It acquires polarized brightness images in triplets at angles of 0°, 120°, and 240° to derive total brightness (tB) images which are subsequently used for CME detection validation.
  
- **Supporting Quote**:
  - “STEREO COR-1A polarized brightness images are acquired in triplets with polarization angles of 0◦, 120◦ and 240◦… and every triplet has difference in time of 5 minutes.”
  
- #### Data Collection Period 1: High‑Jitter Observations
  - **Time Range**: Specific observation dates provided include, for example, 2013‑10‑26, 2013‑10‑27, and 2013‑10‑28 (with each date representing a full day of observations where image acquisition follows the instrument’s cadence).
    - *Supporting Quote*: “Images from dates 2013-10-26, 2013-10-27, 2013-10-28… which contain high jitters…”
  - **Wavelength(s)**: White‑light (derived from polarized brightness at multiple polarization angles)
    - *Supporting Quote*: “…combined to derive the total brightness (tB) image.”
  - **Physical Observable**: Total white‑light coronal intensity used to identify and track CMEs.
  - **Additional Comments**: Other high‑jitter dates mentioned are 2011‑05‑14, 2011‑05‑15, 2011‑09‑22, 2012‑04‑17, and 2012‑04‑19.

- #### Data Collection Period 2: Low‑Jitter Observations
  - **Time Range**: Data were also selected from dates such as 2010‑11‑10, 2010‑11‑11, 2010‑11‑12, 2011‑08‑02, 2011‑08‑03, 2011‑08‑04, 2012‑06‑13, 2012‑06‑14, and 2012‑06‑15.
    - *Supporting Quote*: “Images from dates 2010-11-10, 2010-11-11, 2010-11-12, 2011-08-02, 2011-08-03, 2011-08-04, 2012-06-13, 2012-06-14, 2012-06-15 were selected for low jitters…”
  - **Wavelength(s)**: White‑light (total brightness images computed from the polarization triplets)
  - **Physical Observable**: Variation of coronal brightness to detect transient events such as CMEs.
  - **Additional Comments**: Exposure times are typically ≈1.7 s per image with a detector size of 512×512 pixels.

---

### 3. K‑Cor (Mauna Loa Solar Observatory)
- **General Comments**:
  - K‑Cor is a ground‑based coronagraph operating from the Mauna Loa Solar Observatory that shares a similar field of view as VELC (from 1.05 R⊙ to 3 R⊙).
  - The instrument suffers from atmospheric effects that introduce significant scattered light, affecting CME detection.
  
- **Supporting Quote**:
  - “The K-Cor telescope … is a coronagraph with FOV same as that of VELC starting from 1.05 R⊙to 3 R⊙. K-Cor takes images of corona with dimension of 1024×1024 and cadence of 15 s.”
  
- #### Data Collection Period 1: Example Day of CME Observations
  - **Time Range**: For instance, data from 2016‑01‑01 (encompassing a full day’s observations; although the paper does not specify exact UT start/end times, the entirety of the day’s captured images is used for algorithm testing).
    - *Supporting Quote*: “Figure 8a shows an example of good CME event captured by K-cor on 2016-01-01…”
  - **Wavelength(s)**: White‑light continuum.
  - **Physical Observable**: White‑light coronal images used to visually identify CMEs; these observations are challenged by atmospheric scattered intensity.
  - **Additional Comments**: Other dates studied include 2014‑06‑26, 2016‑02‑09, 2015‑05‑05, 2014‑04‑03, 2014‑05‑07, and 2014‑05‑28, as detailed in Table 2 of the paper.

---

### 4. LASCO Instruments on board SOHO and Historical Coronagraphs
- **General Comments**:
  - The LASCO suite (including C1, C2, and C3) onboard SOHO has been fundamental to CME studies. LASCO C2 and C3 have provided nearly continuous data since their launch in 1995, while LASCO C1 (with a unique FOV of 1.1 R⊙ to 3 R⊙) operated for about two years after its launch.
  - In addition to LASCO, several historical instruments such as the white‑light coronagraph on OSO‑7 (first CME observations in 1971), Skylab’s coronagraph, Solwind, Solar Maximum Mission, and Spartan 201 have contributed extensive CME catalogs.
  
- **Supporting Quote**:
  - “The first observation of CMEs from space was in 1971 … by a white light coronagraph … Later several other coronagraphs were sent to space… First statistical survey of CMEs was done with data obtained from coronagraph onboard Skylab… White light coronagraph with FOV from 1.5 R⊙to 6 R⊙and spatial resolution 10 arcsec, onboard Solar Maximum Mission… LASCO C2 and C3 onboard Solar and Heliospheric Observatory (SOHO) launched in 1995… The only coronagraph to have FOV closest to solar limb was LASCO C1 (1.1 R⊙to 3 R⊙) which stopped its operation two years after its launch in 1998.”
  
- #### Data Collection Periods:
  - **LASCO C1**:
    - **Time Range**: Operated for approximately two years post‑launch (exact dates not provided; operational period roughly in the late 1990s until its cessation around 1998–2000).
  - **LASCO C2 and C3**:
    - **Time Range**: Launched in 1995 and have provided continuous observations spanning over two solar cycles.
  - **Historical Missions (OSO‑7, Skylab, Solwind, Solar Maximum Mission, Spartan 201)**:
    - **Time Ranges**: 
      - OSO‑7: CME observation initiated in 1971.
      - Skylab: Data recorded during its operational period starting in the early 1970s (e.g., 1974).
      - Solwind and Solar Maximum Mission: Operated around 1980.
      - Spartan 201: Operated from April 1993 to November 1998.
  
- **Wavelength(s)**: Primarily white‑light; details on specific wavelengths are not provided.
- **Physical Observable**: White‑light coronal brightness and CME structures.
- **Additional Comments**: These instruments serve as the historical reference points against which modern observations and algorithms are compared.

---

### 5. ASPIICS on PROBA‑3
- **General Comments**:
  - ASPIICS is an externally occulted coronagraph onboard the PROBA‑3 mission, designed to observe the solar corona with a field of view from approximately 1.08 R⊙ to 3 R⊙.
  - Its FOV is noted to be very similar to that of VELC, and it is expected to be launched around the same time as ADITYA‑L1.
  
- **Supporting Quote**:
  - “Association de Satellites pour l'Imagerie et l'Interferomtrie de la Couronne Solaire (ASPIICS) onboard PROBA-3 … having FOV from 1.08⊙to 3⊙ similar to VELC might be launched around the same time of VELC.”
  
- #### Data Collection Period 1: Planned Operations
  - **Time Range**: Specific observation start/end times are not provided; the instrument is expected to operate in a manner analogous to VELC, capturing continuous white‑light coronal images.
  - **Wavelength(s)**: White‑light observational band (details on passband not provided).
  - **Physical Observable**: White‑light coronal structure for CME studies.
  - **Additional Comments**: Being an upcoming instrument parallel to VELC, its data characteristics are anticipated rather than already established.

---

### 6. METIS on Solar Orbiter
- **General Comments**:
  - METIS (Multi‑Element Telescope for Imaging and Spectroscopy) onboard Solar Orbiter is another advanced coronagraph instrument designed for imaging and spectroscopic investigation of CMEs.
  - An onboard automated CME detection algorithm, similar in concept to that presented for VELC, has been developed for METIS.
  
- **Supporting Quote**:
  - “Among the upcoming solar missions, an automated CMEs detection has been developed by Bemporad et al. (2014) for CMEs detection in Multi Element Telescope for Imaging and Spectroscopy (METIS) onboard Solar Orbiter.”
  
- #### Data Collection Period 1: Planned / Ongoing Observations
  - **Time Range**: The paper does not specify exact operational dates or times for METIS; it is mentioned in the context of future missions and algorithm development.
  - **Wavelength(s)**: METIS acquires white‑light images (with additional spectroscopic and spectro‑polarimetric capabilities), although specific passbands are not detailed.
  - **Physical Observable**: White‑light coronal brightness along with spectroscopic observables for CME tracking.
  - **Additional Comments**: METIS complements VELC by providing multi‑element imaging capabilities and serves as a benchmark for onboard algorithms in different mission environments.

---

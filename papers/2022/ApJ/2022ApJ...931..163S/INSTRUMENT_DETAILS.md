_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper addresses the problem of predicting solar flares by distinguishing between flare-imminent active regions, which produce M- or X-class flares within 24 hours, and quiet active regions, which do not produce any flares within ±24 hours. The study utilizes data from two solar cycles, Solar Cycle 23 and 24, using two data products: SMARP and SHARP. These data products are derived from observations by the Michelson Doppler Imager (MDI) aboard the Solar and Heliospheric Observatory (SoHO) and the Helioseismic and Magnetic Imager (HMI) aboard the Solar Dynamics Observatory (SDO), respectively. The study employs deep learning algorithms, specifically CNN and LSTM, to train and evaluate flare prediction models. The paper also explores the potential of combining these models using ensemble learning techniques and interprets the CNN predictions using visual attribution methods.

## Instrumentation Details

### Helioseismic and Magnetic Imager (HMI) on board Solar Dynamics Observatory (SDO)
- **General Comments**:
   - HMI provides full-disk observations of the solar surface, capturing line-of-sight magnetograms and summary parameters of active regions. It is part of the SHARP data product, which covers much of Solar Cycle 24.
- **Supporting Quote**: "The SHARP database is derived from full-disk observations of the Helioseismic and Magnetic Imager (HMI, Schou et al. 2012) aboard the Solar Dynamics Observatory (SDO)..."

#### Data Collection Period 1: Observations of Solar Cycle 24
- **Time Range**: May 1, 2010 – December 1, 2020
   - **Supporting Quote**: "We query... SHARP records from 2010 May 1 to 2020 December 1, both at a cadence of 96 minutes."
- **Wavelength(s)**: Photospheric line-of-sight magnetic field
   - **Supporting Quote**: "For images, we use photospheric line-of-sight magnetic field maps, or magnetograms, from the two data products."
- **Physical Observable**: Line-of-sight magnetic field
   - **Supporting Quote**: "HMI’s measurement of the solar surface magnetic field is only restricted to the line-of-sight component..."
- **Additional Comments**: SHARP data is used for training and evaluating deep learning models for flare prediction.

### Michelson Doppler Imager (MDI) on board Solar and Heliospheric Observatory (SoHO)
- **General Comments**:
   - MDI provides observations of the solar surface, capturing line-of-sight magnetograms with lower spatial resolution and signal-to-noise ratio compared to HMI. It is part of the SMARP data product, which covers Solar Cycle 23.
- **Supporting Quote**: "The SMARP database was derived from the Michelson Doppler Imager (MDI, Scherrer et al. 1995) aboard the Solar and Heliospheric Observatory (SoHO)..."

#### Data Collection Period 1: Observations of Solar Cycle 23
- **Time Range**: April 23, 1996 – October 28, 2010
   - **Supporting Quote**: "We query SMARP records from 1996 April 23 to 2010 October 28..."
- **Wavelength(s)**: Photospheric line-of-sight magnetic field
   - **Supporting Quote**: "For images, we use photospheric line-of-sight magnetic field maps, or magnetograms, from the two data products."
- **Physical Observable**: Line-of-sight magnetic field
   - **Supporting Quote**: "MDI’s measurement of the solar surface magnetic field is only restricted to the line-of-sight component..."
- **Additional Comments**: SMARP data is used to extend the SHARP database backward to include more flaring events from a stronger solar cycle.

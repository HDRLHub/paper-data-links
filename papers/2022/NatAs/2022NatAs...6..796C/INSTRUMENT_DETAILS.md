_This commentary was initially drafted by an AI model. Please use with caution_

# Scientific Observation Instrumentation Form

## Summary of the Paper
- **Content Summary**: The paper discusses the use of convolutional neural networks (CNNs) to improve the labeling of solar flux evolution videos, specifically focusing on the emergence of bipolar magnetic regions (BMRs). The study leverages videos from the Solar and Heliospheric Observatory's Michelson Doppler Imager (SoHO/MDI) to train and refine a deep learning model. The iterative process of training and manual verification aims to reduce human intervention in labeling by 50%. The paper also explores the model's ability to detect the time of BMR emergence by masking video frames and analyzing changes in CNN inference.

## Instrumentation Details

### Michelson Doppler Imager (MDI) on board Solar and Heliospheric Observatory (SoHO)
- **General Comments**:
   - The MDI instrument on SoHO is used to capture line-of-sight (LoS) magnetic patches on the solar surface. These observations are crucial for creating videos that are used to train the CNN for detecting BMR emergence.
- **Supporting Quote**: "We use 96-minute cadence videos of SoHO/MDI Line-of-Sight (LoS) magnetic patches (15◦ × 15◦ in Carrington grid) (Figure 1) labelled for BMR ‘emergence’ (i.e. BMRs that clearly emerge within the visible solar disk) or BMR ‘non-emergence’ (i.e. BMRs that rotate into view)."

#### Data Collection Period 1: Training and Validation Set
- **Time Range**: January 1996 – October 2011
   - **Supporting Quote**: "We divide our data into a training+validation set (BMR observations within the first 10 months of every year between 1996 and 2011; Figure 2) and a test set (BMR observations on the last two months of every year between 1996 and 2011; Figure 2)."
- **Wavelength(s)**: Not explicitly mentioned
- **Physical Observable**: Line-of-Sight (LoS) magnetic field
   - **Supporting Quote**: "We use 96-minute cadence videos of SoHO/MDI Line-of-Sight (LoS) magnetic patches (15◦ × 15◦ in Carrington grid)..."
- **Additional Comments**: The training and validation set is used to train the CNN weights and optimize hyper-parameters.

#### Data Collection Period 2: Test Set
- **Time Range**: November 1996 – December 2011
   - **Supporting Quote**: "We divide our data into a training+validation set... and a test set (BMR observations on the last two months of every year between 1996 and 2011; Figure 2)."
- **Wavelength(s)**: Not explicitly mentioned
- **Physical Observable**: Line-of-Sight (LoS) magnetic field
   - **Supporting Quote**: "We use 96-minute cadence videos of SoHO/MDI Line-of-Sight (LoS) magnetic patches (15◦ × 15◦ in Carrington grid)..."
- **Additional Comments**: The test set is used to evaluate the performance of the CNN under pseudo-operational conditions.

---

This form captures the details of the MDI instrument on SoHO, including its role in the study, the time ranges for data collection, and the physical observables measured.

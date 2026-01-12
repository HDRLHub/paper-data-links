# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
SunPy VSO Query Script
Instrument: SOHO/UVCS (OVI Detector)
Data: O VI 103.2–103.7 nm resonance doublet
Time Range: 1996-01-01 to 2002-12-31
"""
import astropy.units as u
from sunpy.net import Fido, attrs as a

def main():
    # Define the data source: SOHO
    source = a.Source('SOHO')
    
    # Define the instrument: UVCS
    instrument = a.Instrument('UVCS')
    
    # Define the detector channel for O VI (1032–1037 Å)
    detector = a.Detector('OVI')
    
    # Define the time range matching off-limb coronal hole studies (1996–2002)
    time_range = a.Time('1996-01-01', '2002-12-31')
    
    # Define the wavelength window for the O VI doublet (1032 Å to 1037 Å)
    wavelength_range = a.Wavelength(1032 * u.Angstrom, 1037 * u.Angstrom)
    
    # Perform the VSO search
    results = Fido.search(source, instrument, detector, time_range, wavelength_range)
    
    # Print the search results summary
    print(results)
    
    # Uncomment the following line to download the data
    # downloaded_files = Fido.fetch(results)

if __name__ == '__main__':
    main()

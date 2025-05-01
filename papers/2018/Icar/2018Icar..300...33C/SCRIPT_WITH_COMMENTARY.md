# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script queries the Virtual Solar Observatory (VSO) for SOHO/SWAN data,
specifically targeting hydrogen Lyman‑α observations as used in the paper.
We query data for various comet apparitions observed by SWAN.
The basic required parameters for each query are the time range and the instrument.
Additional attributes such as source and wavelength are provided to reflect the VSO interface.
Note: The actual fetch commands are commented out.
"""

from sunpy.net import Fido, attrs
from astropy import units as u

def query_swan_data(time_start, time_end, comet_name):
    """
    Query VSO for SOHO/SWAN data within a given time range for a specific comet event.
    
    Parameters:
      time_start (str): Start time in ISO format.
      time_end (str): End time in ISO format.
      comet_name (str): Name/description of the comet observation.
    
    Returns:
      search_result: The query result from Fido.search.
    """
    print(f"Querying SOHO/SWAN data for {comet_name} from {time_start} to {time_end}")
    query_result = Fido.search(
        attrs.Time(time_start, time_end),
        attrs.Source('SOHO'),
        attrs.Instrument('SWAN'),
        # The wavelength for Hydrogen Lyman-alpha as per the VSO interface is 1215.6 Å.
        attrs.Wavelength(1215.6 * u.Angstrom, 1215.6 * u.Angstrom)
    )
    print(query_result)
    # To download the data, uncomment the following fetch command:
    # data = Fido.fetch(query_result)
    print("\n" + "="*80 + "\n")
    return query_result


if __name__ == '__main__':
    # Comet C/2012 K1 (PanSTARRS)
    query_swan_data("2014-04-22", "2014-12-06", "Comet C/2012 K1 (PanSTARRS)")
    
    # Comet C/2013 US10 (Catalina)
    query_swan_data("2015-06-30", "2016-02-18", "Comet C/2013 US10 (Catalina)")
    
    # Comet C/2013 V5 (Oukaimeden)
    query_swan_data("2014-08-19", "2014-10-07", "Comet C/2013 V5 (Oukaimeden)")
    
    # Comet C/2013 R1 (Lovejoy)
    query_swan_data("2013-10-13", "2014-03-14", "Comet C/2013 R1 (Lovejoy)")
    
    # Comet C/2014 E2 (Jacques)
    query_swan_data("2014-04-03", "2014-10-19", "Comet C/2014 E2 (Jacques)")
    
    # Comet C/2014 Q2 (Lovejoy)
    query_swan_data("2014-11-28", "2015-06-28", "Comet C/2014 Q2 (Lovejoy)")
    
    # Comet C/2015 G2 (MASTER)
    query_swan_data("2015-04-07", "2015-06-26", "Comet C/2015 G2 (MASTER)")
    
    # Comet C/2014 Q1 (PanSTARRS)
    query_swan_data("2015-05-20", "2015-08-10", "Comet C/2014 Q1 (PanSTARRS)")
    
    # Comet C/2013 X1 (PanSTARRS)
    query_swan_data("2016-01-01", "2016-06-21", "Comet C/2013 X1 (PanSTARRS)")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script constructs two Sunpy VSO queries based on the available interface and the context.
One query targets SDO/HMI data that covers the period relevant for helioseismic near-surface
velocity measurements (2010 August to ~7 years duration). The other query targets historical
SOHO/MDI data as a reference for earlier helioseismic observations.
"""

# Import necessary modules from sunpy.net
from sunpy.net import Fido, attrs as a

# -------------------------------
# Query for SDO/HMI data
# -------------------------------
# According to the context, the HMI data are used for measuring the near-surface torsional oscillation velocities.
# The HMI observations are available from August 2010. We choose a time range from 2010-08-01 to 2017-07-31
# (approximately 7 years). Note: The VSO interface confirms SDO/HMI is available from 2010/03/29 to present.
time_hmi = a.Time("2010-08-01", "2017-07-31")
# Query for SDO data with the HMI instrument from the Virtual Solar Observatory
query_hmi = Fido.search(time_hmi, a.Source("SDO"), a.Instrument("HMI"))

# Print the HMI query results
print("SDO/HMI Query Results:")
print(query_hmi)

# To actually download the data, uncomment the following line:
# files_hmi = Fido.fetch(query_hmi)

# -------------------------------
# Query for SOHO/MDI data
# -------------------------------
# Although the primary analysis in the paper is based on ring diagram analysis from GONG and HMI, the
# historical SOHO/MDI observations are referenced as the initial helioseismic detection of solar flows.
# We use a time range available from the VSO interface. In this example, we choose the available data from
# a representative period: 1996-03-03 to 2011-04-12.
time_mdi = a.Time("1996-03-03", "2011-04-12")
# Query for SOHO data with the MDI instrument from the Virtual Solar Observatory
query_mdi = Fido.search(time_mdi, a.Source("SOHO"), a.Instrument("MDI"))

# Print the MDI query results
print("SOHO/MDI Query Results:")
print(query_mdi)

# To actually download the data, uncomment the following line:
# files_mdi = Fido.fetch(query_mdi)

if __name__ == '__main__':
    # This block ensures that the script can be run as a standalone program.
    print("Queries constructed successfully. Check printed results for details on matching observations.")

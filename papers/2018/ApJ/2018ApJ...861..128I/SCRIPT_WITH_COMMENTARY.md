# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO client to query for SDO/HMI data corresponding to the SHARPs data product.
The study described in the context uses SHARPs data from SDO/HMI spanning from 01 January 2010 to 31 January 2018.
Only the time range and the instrument are explicitly specified as required by the context.
Note: The DONKI and GOES databases are not available in the VSO interface, so we only query SDO/HMI.
"""

# Import necessary modules from SunPy and astropy
from sunpy.net import Fido, attrs as a
import astropy.units as u

# Define the time range for the query from the paper: 01 January 2010 to 31 January 2018.
start_time = '2010-01-01'
end_time = '2018-01-31'

# Since the context describes SHARPs data from SDO/HMI, we query for data from the HMI instrument.
# There are multiple physical observables in the VSO interface (for example, "Stokes_parameters",
# "vector_magnetic_field", "LOS_magnetic_field"). For SHARPs, the vector magnetic field data derived from
# disambiguated Stokes measurements is typically used. Here, we use the 'HMI' instrument specification.
query_result = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument('HMI'),
    a.Source('SDO')
)

# Print out the query results to see the available datasets.
print("Query Results for SDO/HMI from {} to {}:".format(start_time, end_time))
print(query_result)

# The following line would download the data if uncommented.
# files = Fido.fetch(query_result)

if __name__ == '__main__':
    # Entry point for running the query.
    # The printed output will show the resources available for the given query.
    pass

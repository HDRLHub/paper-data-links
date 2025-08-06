# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net
from sunpy.net import Fido
from sunpy.net import attrs as a
import astropy.units as u

# Define the time range for the observations: April 1, 2009 to July 31, 2009
# This period covers the microflare observations analyzed in the study.
time_start = "2009-04-01T00:00:00"
time_end = "2009-07-31T23:59:59"

# Build the query for SOHO/MDI line-of-sight magnetograms
# We request Level-1.8 MDI data in the LOS_magnetic_field observable,
# which provides the photospheric line-of-sight magnetic field required
# to compute field strength and magnetic flux for the microflare regions.
query = Fido.search(
    a.Time(time_start, time_end),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Detector("MDI"),
    a.Physobs("LOS_magnetic_field")
)

# Print the query results: a summary of files available over the specified period.
print(query)

# Uncomment the following line to download the data once you have reviewed the search results.
# files = Fido.fetch(query)

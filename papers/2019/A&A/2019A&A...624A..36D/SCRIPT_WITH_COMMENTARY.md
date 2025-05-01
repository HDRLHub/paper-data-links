# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script demonstrates how to use SunPy's VSO interface to query solar data,
based on our study benchmarking observed versus predicted solar EUV irradiances.
We create two explicit queries using the VSO:
    
  1. In-flight SDO/EVE observations from 2010 May 16.
  2. SOHO CDS (GIS detector) observations from 2008 September 22.

Note:
- The VSO interface provided contains SDO/EVE data (with a start time of 2010/04/30) and 
  SOHO CDS data (with available time range starting 1996/01/19).
- The only required values in our queries are the time range and the instrument.
- The Fido.fetch commands are included as comments so that the script only prints query results.
"""

from sunpy.net import Fido, attrs as a

# Query 1: SDO/EVE in-flight observations on 2010 May 16.
# This instrument provides daily solar EUV irradiance measurements.
sdo_eve_time = a.Time("2010-05-16", "2010-05-16T23:59:59")
sdo_eve_instrument = a.Instrument("EVE")
sdo_eve_source = a.Source("SDO")

# Construct the query for SDO/EVE data.
query_eve = Fido.search(sdo_eve_time, sdo_eve_source, sdo_eve_instrument)
print("Query Results for SDO/EVE observations on 2010 May 16:")
print(query_eve)
# To download the data, use the following command (commented out):
# eve_files = Fido.fetch(query_eve)

# Query 2: SOHO CDS observations on 2008 September 22.
# Although the CDS instrument in the VSO interface is listed with the GIS detector,
# we use it here to represent quiet Sun measurements.
soho_cds_time = a.Time("2008-09-22", "2008-09-22T23:59:59")
soho_cds_instrument = a.Instrument("CDS")
soho_source = a.Source("SOHO")

# Construct the query for SOHO CDS data.
query_cds = Fido.search(soho_cds_time, soho_source, soho_cds_instrument)
print("\nQuery Results for SOHO CDS (GIS) observations on 2008 September 22:")
print(query_cds)
# To download the data, use the following command (commented out):
# cds_files = Fido.fetch(query_cds)

if __name__ == "__main__":
    pass

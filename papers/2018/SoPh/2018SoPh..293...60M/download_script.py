# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses SunPy's VSO interface to query solar data
relevant to the CME study described in the paper. In particular,
we query data from:
  1. RHESSI – to obtain high-energy flare observations.
  2. SDO/HMI – for vector magnetic field measurements of active regions.
  3. SOHO LASCO – coronagraph observations (using the C2 detector).

The queries are set over a time window corresponding to the March 5, 2012 event,
which is referenced in the context as associated with a GOES X1.1 flare.
Note: Data download (Fido.fetch) commands are provided as comments.
"""

from sunpy.net import Fido, attrs as a

# Define the time window for the query (e.g. around the 2012-03-05 flare event).
start_time = "2012-03-05T00:00:00"
end_time = "2012-03-05T03:00:00"

# 1. Query RHESSI data
#    This instrument provides high-energy observations in hard X-rays.
query_rhessi = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("RHESSI"),
    a.Source("RHESSI")
)
print("RHESSI query results:")
print(query_rhessi)

# Uncomment the next line to fetch RHESSI data files
# rhessi_files = Fido.fetch(query_rhessi)

# 2. Query SDO/HMI data for vector magnetic field measurements
#    HMI provides modern observations of photospheric magnetic fields in the Fe I 6173 Å line.
#    We use the 'vector_magnetic_field' physical observable.
query_hmi = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("HMI"),
    a.Physobs("vector_magnetic_field")
)
print("\nSDO/HMI query results (vector magnetic field):")
print(query_hmi)

# Uncomment the next line to fetch SDO/HMI data files
# hmi_files = Fido.fetch(query_hmi)

# 3. Query SOHO LASCO data using the C2 detector
#    LASCO/C2 provides continuum white-light observations of the corona,
#    useful for tracking CME brightness and morphology.
query_lasco = Fido.search(
    a.Time(start_time, end_time),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSOHO LASCO (C2) query results:")
print(query_lasco)

# Uncomment the next line to fetch SOHO LASCO data files
# lasco_files = Fido.fetch(query_lasco)

if __name__ == "__main__":
    print("\nQueries completed. Review the printed query results for details.")

# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
"""
This script uses Sunpy's VSO client to query solar observational data related
to SEP events described in the paper. In particular, we query for data from three instruments:

1. GOES-16/SUVI:
   - Captures high-cadence EUV images.
   - Here we query a time period associated with the onset of the X8.2 flare on 10 September 2017.
   - Query time range: 2017-09-10 15:00:00 to 2017-09-10 16:30:00.

2. SDO/HMI:
   - Observes white-light and helioseismic signatures associated with the X9.3 flare on 6 September 2017.
   - Query time range: 2017-09-06 11:30:00 to 2017-09-06 12:30:00.

3. SOHO/LASCO:
   - Provides coronagraph images to study CME kinematics.
   - Here we query data around the CME observation on 6 September 2017 (around 12:24 UT).
   - Query time range: 2017-09-06 12:00:00 to 2017-09-06 13:00:00.

Note:
- The queries include only the required parameters: time range and instrument.
- The Fido.fetch commands are provided as comments so you can execute them if desired.
"""

from sunpy.net import Fido, attrs as a

def query_goes16_suvi():
    # Query GOES-16/SUVI data for the X8.2 flare on 10 September 2017
    time_start = "2017-09-10T15:00:00"
    time_end   = "2017-09-10T16:30:00"
    # GOES-16 is specified as the source and SUVI as the instrument, using the VSO interface information.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source("GOES16"),
        a.Instrument("SUVI")
    )
    print("GOES-16/SUVI Query Result:")
    print(query_result)
    # Uncomment the following line to fetch the data:
    # files = Fido.fetch(query_result)
    
def query_sdo_hmi():
    # Query SDO/HMI data corresponding to the X9.3 flare peak on 6 September 2017.
    time_start = "2017-09-06T11:30:00"
    time_end   = "2017-09-06T12:30:00"
    # SDO is specified as the source and HMI as the instrument.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source("SDO"),
        a.Instrument("HMI")
    )
    print("\nSDO/HMI Query Result:")
    print(query_result)
    # Uncomment the following line to fetch the data:
    # files = Fido.fetch(query_result)
    
def query_soho_lasco():
    # Query SOHO/LASCO data to examine CME observations around 6 September 2017.
    time_start = "2017-09-06T12:00:00"
    time_end   = "2017-09-06T13:00:00"
    # SOHO is the source and LASCO is the instrument.
    query_result = Fido.search(
        a.Time(time_start, time_end),
        a.Source("SOHO"),
        a.Instrument("LASCO")
    )
    print("\nSOHO/LASCO Query Result:")
    print(query_result)
    # Uncomment the following line to fetch the data:
    # files = Fido.fetch(query_result)

def main():
    # Run all queries and print the results
    query_goes16_suvi()
    query_sdo_hmi()
    query_soho_lasco()

if __name__ == "__main__":
    main()

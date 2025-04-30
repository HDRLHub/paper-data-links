# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import astropy.units as u
from sunpy.net import Fido, attrs as a

# Define the time ranges for the data collection periods
time_ranges = {
    "GONG_Cycle_23": ("1996-01-14", "2006-12-22"),
    "GONG_Cycle_24": ("2008-12-12", "2019-05-24"),
    "MDI_Cycle_23": ("1999-02-03", "2008-12-11"),
    "MDI_Cycle_24": ("2009-12-07", "2019-08-04"),
    "HMI_Cycle_23": ("1999-02-03", "2008-12-11"),  # Combined with MDI data
    "HMI_Cycle_24": ("2009-12-07", "2019-08-04"),  # Combined with MDI data
}

# Define the instruments
instruments = {
    "GONG": "GONG",
    "MDI": "MDI",
    "HMI": "HMI",
}

# Query for GONG data for Cycle 23
gong_cycle_23_query = Fido.search(
    a.Time(time_ranges["GONG_Cycle_23"][0], time_ranges["GONG_Cycle_23"][1]),
    a.Instrument(instruments["GONG"])
)
print("GONG Cycle 23 Query Results:")
print(gong_cycle_23_query)
# Uncomment the following line to fetch the data
# gong_cycle_23_download = Fido.fetch(gong_cycle_23_query)

# Query for GONG data for Cycle 24
gong_cycle_24_query = Fido.search(
    a.Time(time_ranges["GONG_Cycle_24"][0], time_ranges["GONG_Cycle_24"][1]),
    a.Instrument(instruments["GONG"])
)
print("GONG Cycle 24 Query Results:")
print(gong_cycle_24_query)
# Uncomment the following line to fetch the data
# gong_cycle_24_download = Fido.fetch(gong_cycle_24_query)

# Query for MDI data for Cycle 23
mdi_cycle_23_query = Fido.search(
    a.Time(time_ranges["MDI_Cycle_23"][0], time_ranges["MDI_Cycle_23"][1]),
    a.Instrument(instruments["MDI"])
)
print("MDI Cycle 23 Query Results:")
print(mdi_cycle_23_query)
# Uncomment the following line to fetch the data
# mdi_cycle_23_download = Fido.fetch(mdi_cycle_23_query)

# Query for MDI data for Cycle 24
mdi_cycle_24_query = Fido.search(
    a.Time(time_ranges["MDI_Cycle_24"][0], time_ranges["MDI_Cycle_24"][1]),
    a.Instrument(instruments["MDI"])
)
print("MDI Cycle 24 Query Results:")
print(mdi_cycle_24_query)
# Uncomment the following line to fetch the data
# mdi_cycle_24_download = Fido.fetch(mdi_cycle_24_query)

# Query for HMI data for Cycle 23 (combined with MDI data)
hmi_cycle_23_query = Fido.search(
    a.Time(time_ranges["HMI_Cycle_23"][0], time_ranges["HMI_Cycle_23"][1]),
    a.Instrument(instruments["HMI"])
)
print("HMI Cycle 23 Query Results:")
print(hmi_cycle_23_query)
# Uncomment the following line to fetch the data
# hmi_cycle_23_download = Fido.fetch(hmi_cycle_23_query)

# Query for HMI data for Cycle 24 (combined with MDI data)
hmi_cycle_24_query = Fido.search(
    a.Time(time_ranges["HMI_Cycle_24"][0], time_ranges["HMI_Cycle_24"][1]),
    a.Instrument(instruments["HMI"])
)
print("HMI Cycle 24 Query Results:")
print(hmi_cycle_24_query)
# Uncomment the following line to fetch the data
# hmi_cycle_24_download = Fido.fetch(hmi_cycle_24_query)
```

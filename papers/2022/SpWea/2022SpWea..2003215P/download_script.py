# This script, including code comments, was initially drafted by an AI model. Please use with caution.

# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from sunpy.time import TimeRange
import astropy.units as u

# Define the time ranges and instruments based on the context provided
time_ranges = {
    "AIA": TimeRange("2018-08-20T07:30", "2018-08-20T08:30"),
    "LASCO": TimeRange("2018-08-20T10:24", "2018-08-20T21:48"),
    "HI": TimeRange("2018-08-20T15:29", "2018-08-21T06:09"),
    "MFI": TimeRange("2018-08-24T02:25", "2018-08-27T00:00"),
    "SWIA": TimeRange("2018-08-25T09:45", "2018-08-30T00:00"),
    "MAG": TimeRange("2018-08-25T09:45", "2018-08-30T00:00"),
    "SWE": TimeRange("2018-08-24T02:25", "2018-08-27T00:00"),
    "EPAM": TimeRange("2018-08-24T02:25", "2018-08-27T00:00"),
    "CRaTER": TimeRange("2018-08-24T02:25", "2018-08-27T00:00"),
    "NMDB": TimeRange("2018-08-24T02:25", "2018-08-27T00:00"),
    "ASPERA-3": TimeRange("2018-08-25T09:45", "2018-08-30T00:00"),
    "SEP": TimeRange("2018-08-25T09:45", "2018-08-30T00:00"),
    "RAD": TimeRange("2018-08-25T09:45", "2018-08-30T00:00")
}

# Define the instruments and their attributes
instruments = {
    "AIA": {"source": "SDO", "instrument": "AIA", "wavelength": [193, 94, 131]},
    "LASCO": {"source": "SOHO", "instrument": "LASCO", "detector": "C2"},
    "HI": {"source": "STEREO_A", "instrument": "SECCHI", "detector": "HI1"},
    "MFI": {"source": "Wind", "instrument": "MFI"},
    "SWIA": {"source": "MAVEN", "instrument": "SWIA"},
    "MAG": {"source": "MAVEN", "instrument": "MAG"},
    "SWE": {"source": "Wind", "instrument": "SWE"},
    "EPAM": {"source": "ACE", "instrument": "EPAM"},
    "CRaTER": {"source": "LRO", "instrument": "CRaTER"},
    "NMDB": {"source": "NMDB", "instrument": "NMDB"},
    "ASPERA-3": {"source": "MEX", "instrument": "ASPERA-3"},
    "SEP": {"source": "MAVEN", "instrument": "SEP"},
    "RAD": {"source": "MSL", "instrument": "RAD"}
}

# Perform the queries
for inst, attrs in instruments.items():
    time_range = time_ranges[inst]
    query = Fido.search(
        a.Time(time_range.start, time_range.end),
        a.Instrument(attrs["instrument"]),
        a.Source(attrs["source"]),
        *(a.Wavelength(wl * u.Angstrom) for wl in attrs.get("wavelength", [])),
        *(a.Detector(attrs["detector"]) for det in attrs.get("detector", []))
    )
    print(f"Query results for {inst}:")
    print(query)
    # Uncomment the following line to fetch the data
    # files = Fido.fetch(query)

# Note: Be aware of potential pagination issues when fetching large datasets.

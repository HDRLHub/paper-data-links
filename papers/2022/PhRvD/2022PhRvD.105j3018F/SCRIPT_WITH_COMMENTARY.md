# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
# Import necessary modules from SunPy
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Context:
# The paper proposes a gravitational wave (GW) detection concept using asteroids in the inner Solar System as test masses (TMs).
# We need data from the CELIAS/MTOF Proton Monitor and VIRGO instrument on board SOHO.

# Reasoning:
# Let's think step by step in order to produce the script. We need to:
# 1. Query data from the CELIAS/MTOF Proton Monitor for solar wind proton density and velocity.
# 2. Query data from the VIRGO instrument for total solar irradiance (TSI) during solar maximum and minimum periods.

# Script:

# Query for CELIAS/MTOF Proton Monitor data
# Time Range: 1996 – 2021
# Instrument: CELIAS
# Detector: MTOF
# Physical Observable: proton density and velocity
celias_query = Fido.search(
    a.Time('1996-01-01', '2021-12-31'),
    a.Instrument('CELIAS'),
    a.Detector('MTOF')
)
print("CELIAS/MTOF Proton Monitor Query Results:")
print(celias_query)
# Uncomment the following line to fetch the data
# celias_data = Fido.fetch(celias_query)

# Query for VIRGO instrument data during solar maximum
# Time Range: October 2000 – February 2002
# Instrument: VIRGO
# Physical Observable: total solar irradiance (TSI)
virgo_max_query = Fido.search(
    a.Time('2000-10-01', '2002-02-28'),
    a.Instrument('VIRGO')
)
print("VIRGO Instrument Query Results (Solar Maximum):")
print(virgo_max_query)
# Uncomment the following line to fetch the data
# virgo_max_data = Fido.fetch(virgo_max_query)

# Query for VIRGO instrument data during solar minimum
# Time Range: February 1996 – August 1997
# Instrument: VIRGO
# Physical Observable: total solar irradiance (TSI)
virgo_min_query = Fido.search(
    a.Time('1996-02-01', '1997-08-31'),
    a.Instrument('VIRGO')
)
print("VIRGO Instrument Query Results (Solar Minimum):")
print(virgo_min_query)
# Uncomment the following line to fetch the data
# virgo_min_data = Fido.fetch(virgo_min_query)
```

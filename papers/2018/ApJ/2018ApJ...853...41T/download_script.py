# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net as net
from sunpy.net import attrs as a
from astropy.time import Time
import astropy.units as u

# --------------------------------------------------------------------------------------------------
# Example Event 1: X17 Flare on 2003-10-28
#   - Hα data from ISOON (used for the 2003 October 28 X17 event)
#   - Pre-flare LOS magnetogram from SOHO/MDI
# --------------------------------------------------------------------------------------------------

# Flare start and end times for the ISOON event (from Table 2; here illustrative)
flare_start_isoon = Time("2003-10-28T11:10:00")
flare_end_isoon   = Time("2003-10-28T11:24:00")

# Define Hα filtergram window: 5 minutes before flare start to 5 minutes after flare end
ha_start = flare_start_isoon - 5 * u.min
ha_end   = flare_end_isoon   + 5 * u.min

# Query ISOON Hα filtergrams (physobs=intensity)
ha_query = net.Fido.search(
    a.Time(ha_start, ha_end),
    a.Source("ISOON"),
    a.Instrument("ISOON"),
    a.Physobs("intensity")
)
print("ISOON H-alpha query result:")
print(ha_query)

# To download the ISOON data, uncomment the following line:
# net.Fido.fetch(ha_query)

# Pre-flare magnetogram time: 1 minute before flare start
mdi_time = flare_start_isoon - 1 * u.min

# Query SOHO/MDI LOS magnetic field magnetogram
mdi_query = net.Fido.search(
    a.Time(mdi_time, mdi_time),
    a.Source("SOHO"),
    a.Instrument("MDI"),
    a.Physobs("LOS_magnetic_field")
)
print("SOHO/MDI LOS magnetogram query result:")
print(mdi_query)

# To download the MDI magnetogram, uncomment the following line:
# net.Fido.fetch(mdi_query)


# --------------------------------------------------------------------------------------------------
# Example Event 2: Flare after 2010-05-01 (e.g. 2012-07-12)
#   - Hα data from KSO HA2
#   - Pre-flare LOS magnetogram from SDO/HMI
# --------------------------------------------------------------------------------------------------

# Flare start and end times for the KSO event (from Table 2; here illustrative)
flare_start_kso = Time("2012-07-12T16:45:00")
flare_end_kso   = Time("2012-07-12T17:00:00")

# Define Hα filtergram window: 5 minutes before flare start to 5 minutes after flare end
kso_ha_start = flare_start_kso - 5 * u.min
kso_ha_end   = flare_end_kso   + 5 * u.min

# Query KSO HA2 Hα filtergrams (physobs=intensity)
kso_query = net.Fido.search(
    a.Time(kso_ha_start, kso_ha_end),
    a.Source("KSO"),
    a.Instrument("HA2"),
    a.Physobs("intensity")
)
print("KSO HA2 H-alpha query result:")
print(kso_query)

# To download the KSO HA2 data, uncomment the following line:
# net.Fido.fetch(kso_query)

# Pre-flare magnetogram time: 1 minute before flare start
hmi_time = flare_start_kso - 1 * u.min

# Query SDO/HMI LOS magnetic field magnetogram
hmi_query = net.Fido.search(
    a.Time(hmi_time, hmi_time),
    a.Source("SDO"),
    a.Instrument("HMI"),
    a.Physobs("LOS_magnetic_field")
)
print("SDO/HMI LOS magnetogram query result:")
print(hmi_query)

# To download the HMI magnetogram, uncomment the following line:
# net.Fido.fetch(hmi_query)

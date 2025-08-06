# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net as snt
from sunpy.net import Fido, attrs as a
import astropy.units as u

# -------------------------------------------------------------------
# 1. HMI Doppler Velocity Data (Sunquake detection window)
# Time Range: 2013-02-17 11:59 UT – 2013-02-17 19:58 UT
# Physical Observable: LOS_velocity
# -------------------------------------------------------------------
hmi_doppler_time = a.Time('2013-02-17 11:59', '2013-02-17 19:58')
hmi_doppler_inst = a.Instrument('HMI')
hmi_doppler_phys = a.Physobs('LOS_velocity')

hmi_doppler_query = Fido.search(
    hmi_doppler_time,
    hmi_doppler_inst,
    hmi_doppler_phys
)
print("HMI Doppler Query Results:")
print(hmi_doppler_query)

# To download:
# files_hmi_doppler = Fido.fetch(hmi_doppler_query)

# -------------------------------------------------------------------
# 2. HMI Continuum Intensity Data (Sunquake detection window)
# Time Range: 2013-02-17 11:59 UT – 2013-02-17 19:58 UT
# Physical Observable: intensity (photospheric continuum)
# -------------------------------------------------------------------
hmi_cont_time = a.Time('2013-02-17 11:59', '2013-02-17 19:58')
hmi_cont_inst = a.Instrument('HMI')
hmi_cont_phys = a.Physobs('intensity')

hmi_cont_query = Fido.search(
    hmi_cont_time,
    hmi_cont_inst,
    hmi_cont_phys
)
print("\nHMI Continuum Intensity Query Results:")
print(hmi_cont_query)

# To download:
# files_hmi_cont = Fido.fetch(hmi_cont_query)

# -------------------------------------------------------------------
# 3. HMI Line-of-Sight Magnetic Field Data (Sunquake detection window)
# Time Range: 2013-02-17 11:59 UT – 2013-02-17 19:58 UT
# Physical Observable: LOS_magnetic_field
# -------------------------------------------------------------------
hmi_los_time = a.Time('2013-02-17 11:59', '2013-02-17 19:58')
hmi_los_inst = a.Instrument('HMI')
hmi_los_phys = a.Physobs('LOS_magnetic_field')

hmi_los_query = Fido.search(
    hmi_los_time,
    hmi_los_inst,
    hmi_los_phys
)
print("\nHMI LOS Magnetic Field Query Results:")
print(hmi_los_query)

# To download:
# files_hmi_los = Fido.fetch(hmi_los_query)

# -------------------------------------------------------------------
# 4. HMI Vector Magnetic Field Snapshot for NLFFF Extrapolation
# Time: 2013-02-17 14:36 UT (single snapshot)
# Physical Observable: vector_magnetic_field
# -------------------------------------------------------------------
hmi_vec_time = a.Time('2013-02-17 14:36', '2013-02-17 14:36')
hmi_vec_inst = a.Instrument('HMI')
hmi_vec_phys = a.Physobs('vector_magnetic_field')

hmi_vec_query = Fido.search(
    hmi_vec_time,
    hmi_vec_inst,
    hmi_vec_phys
)
print("\nHMI Vector Magnetic Field Query Results:")
print(hmi_vec_query)

# To download:
# files_hmi_vec = Fido.fetch(hmi_vec_query)

# -------------------------------------------------------------------
# 5. AIA EUV and UV Imaging Data (Flare and Filament Evolution)
# Time Range: 2013-02-17 15:24 UT – 2013-02-17 15:51 UT
# Wavelengths: 304 Å, 171 Å, 193 Å, 211 Å, 335 Å, 1700 Å
# Physical Observable: intensity
# -------------------------------------------------------------------
aia_time = a.Time('2013-02-17 15:24', '2013-02-17 15:51')
aia_inst = a.Instrument('AIA')
aia_phys = a.Physobs('intensity')

# Query for each wavelength channel separately
aia_waves = [304, 171, 193, 211, 335, 1700]  # in Angstrom

aia_queries = {}
for wave in aia_waves:
    key = f"AIA_{wave}A"
    aia_queries[key] = Fido.search(
        aia_time,
        aia_inst,
        aia_phys,
        a.Wavelength(wave * u.angstrom)
    )
    print(f"\n{key} Query Results:")
    print(aia_queries[key])

# To download:
# for key, query in aia_queries.items():
#     files = Fido.fetch(query)

# -------------------------------------------------------------------
# 6. RHESSI Hard X-ray Data (Flare Energy Estimation)
# Time Range: 2013-02-17 15:46 UT – 2013-02-17 15:52 UT
# Physical Observable: intensity
# -------------------------------------------------------------------
rhessi_time = a.Time('2013-02-17 15:46', '2013-02-17 15:52')
rhessi_inst = a.Instrument('RHESSI')

rhessi_query = Fido.search(
    rhessi_time,
    rhessi_inst
)
print("\nRHESSI Query Results:")
print(rhessi_query)

# To download:
# files_rhessi = Fido.fetch(rhessi_query)

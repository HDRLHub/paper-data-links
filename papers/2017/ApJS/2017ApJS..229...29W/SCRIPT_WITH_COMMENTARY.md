# This script, including code comments, was initially drafted by an AI model. Please use with caution.

import sunpy.net Fido
import sunpy.net.attrs as a

# Define the overall time range for CME observations (2008-01-01 to 2012-07-12)
time_range = a.Time("2008-01-01", "2012-07-12")

# 1. Query STEREO-A SECCHI COR1 white-light images
query_st_a_cor1 = Fido.search(
    time_range,
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("STEREO-A COR1 query results:")
print(query_st_a_cor1)
# Fido.fetch(query_st_a_cor1)

# 2. Query STEREO-A SECCHI COR2 white-light images
query_st_a_cor2 = Fido.search(
    time_range,
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nSTEREO-A COR2 query results:")
print(query_st_a_cor2)
# Fido.fetch(query_st_a_cor2)

# 3. Query STEREO-A SECCHI HI1 white-light images
query_st_a_hi1 = Fido.search(
    time_range,
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("HI1")
)
print("\nSTEREO-A HI1 query results:")
print(query_st_a_hi1)
# Fido.fetch(query_st_a_hi1)

# 4. Query STEREO-A SECCHI HI2 white-light images
query_st_a_hi2 = Fido.search(
    time_range,
    a.Source("STEREO_A"),
    a.Instrument("SECCHI"),
    a.Detector("HI2")
)
print("\nSTEREO-A HI2 query results:")
print(query_st_a_hi2)
# Fido.fetch(query_st_a_hi2)

# 5. Query STEREO-B SECCHI COR1 white-light images
query_st_b_cor1 = Fido.search(
    time_range,
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR1")
)
print("\nSTEREO-B COR1 query results:")
print(query_st_b_cor1)
# Fido.fetch(query_st_b_cor1)

# 6. Query STEREO-B SECCHI COR2 white-light images
query_st_b_cor2 = Fido.search(
    time_range,
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("COR2")
)
print("\nSTEREO-B COR2 query results:")
print(query_st_b_cor2)
# Fido.fetch(query_st_b_cor2)

# 7. Query STEREO-B SECCHI HI1 white-light images
query_st_b_hi1 = Fido.search(
    time_range,
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("HI1")
)
print("\nSTEREO-B HI1 query results:")
print(query_st_b_hi1)
# Fido.fetch(query_st_b_hi1)

# 8. Query STEREO-B SECCHI HI2 white-light images
query_st_b_hi2 = Fido.search(
    time_range,
    a.Source("STEREO_B"),
    a.Instrument("SECCHI"),
    a.Detector("HI2")
)
print("\nSTEREO-B HI2 query results:")
print(query_st_b_hi2)
# Fido.fetch(query_st_b_hi2)

# 9. Query SOHO LASCO C2 white-light coronagraph images
query_soho_c2 = Fido.search(
    time_range,
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C2")
)
print("\nSOHO LASCO C2 query results:")
print(query_soho_c2)
# Fido.fetch(query_soho_c2)

# 10. Query SOHO LASCO C3 white-light coronagraph images
query_soho_c3 = Fido.search(
    time_range,
    a.Source("SOHO"),
    a.Instrument("LASCO"),
    a.Detector("C3")
)
print("\nSOHO LASCO C3 query results:")
print(query_soho_c3)
# Fido.fetch(query_soho_c3)

# End of script

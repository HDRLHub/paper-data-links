# This script, including code comments, was initially drafted by an AI model. Please use with caution.

#!/usr/bin/env python3
import sunpy
from sunpy.net import Fido, attrs as a

# This script queries SOHO GOLF and SOHO VIRGO/SPM data for specified time windows
# corresponding to flare-study epochs in February 2011 and a solar-minimum epoch in April 2007.
# Query results are printed. Fido.fetch commands are provided but commented out.

# 1. GOLF data: 11–17 February 2011, 8-hour windows each day
query_golf_20110211 = Fido.search(
    a.Time('2011-02-11T09:00', '2011-02-11T17:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-11 09:00-17:00 UT:", query_golf_20110211)

query_golf_20110212 = Fido.search(
    a.Time('2011-02-12T08:00', '2011-02-12T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-12 08:00-16:00 UT:", query_golf_20110212)

query_golf_20110213 = Fido.search(
    a.Time('2011-02-13T12:00', '2011-02-13T20:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-13 12:00-20:00 UT:", query_golf_20110213)

query_golf_20110214 = Fido.search(
    a.Time('2011-02-14T12:00', '2011-02-14T20:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-14 12:00-20:00 UT:", query_golf_20110214)

query_golf_20110215 = Fido.search(
    a.Time('2011-02-15T00:00', '2011-02-15T08:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-15 00:00-08:00 UT:", query_golf_20110215)

query_golf_20110216 = Fido.search(
    a.Time('2011-02-16T06:00', '2011-02-16T14:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-16 06:00-14:00 UT:", query_golf_20110216)

query_golf_20110217 = Fido.search(
    a.Time('2011-02-17T08:00', '2011-02-17T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2011-02-17 08:00-16:00 UT:", query_golf_20110217)

# 2. VIRGO/SPM (red channel at 862 nm) data: 11–17 February 2011, same 8-hour windows
query_virgo_20110211 = Fido.search(
    a.Time('2011-02-11T09:00', '2011-02-11T17:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-11 09:00-17:00 UT:", query_virgo_20110211)

query_virgo_20110212 = Fido.search(
    a.Time('2011-02-12T08:00', '2011-02-12T16:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-12 08:00-16:00 UT:", query_virgo_20110212)

query_virgo_20110213 = Fido.search(
    a.Time('2011-02-13T12:00', '2011-02-13T20:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-13 12:00-20:00 UT:", query_virgo_20110213)

query_virgo_20110214 = Fido.search(
    a.Time('2011-02-14T12:00', '2011-02-14T20:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-14 12:00-20:00 UT:", query_virgo_20110214)

query_virgo_20110215 = Fido.search(
    a.Time('2011-02-15T00:00', '2011-02-15T08:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-15 00:00-08:00 UT:", query_virgo_20110215)

query_virgo_20110216 = Fido.search(
    a.Time('2011-02-16T06:00', '2011-02-16T14:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-16 06:00-14:00 UT:", query_virgo_20110216)

query_virgo_20110217 = Fido.search(
    a.Time('2011-02-17T08:00', '2011-02-17T16:00'),
    a.Source('SOHO'),
    a.Instrument('VIRGO'),
    a.Detector('SPM')
)
print("VIRGO/SPM 2011-02-17 08:00-16:00 UT:", query_virgo_20110217)

# 3. GOLF data: 19–23 April 2007 (solar-minimum null-test), 08:00–16:00 UT each day
query_golf_20070419 = Fido.search(
    a.Time('2007-04-19T08:00', '2007-04-19T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2007-04-19 08:00-16:00 UT:", query_golf_20070419)

query_golf_20070420 = Fido.search(
    a.Time('2007-04-20T08:00', '2007-04-20T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2007-04-20 08:00-16:00 UT:", query_golf_20070420)

query_golf_20070421 = Fido.search(
    a.Time('2007-04-21T08:00', '2007-04-21T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2007-04-21 08:00-16:00 UT:", query_golf_20070421)

query_golf_20070422 = Fido.search(
    a.Time('2007-04-22T08:00', '2007-04-22T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2007-04-22 08:00-16:00 UT:", query_golf_20070422)

query_golf_20070423 = Fido.search(
    a.Time('2007-04-23T08:00', '2007-04-23T16:00'),
    a.Source('SOHO'),
    a.Instrument('GOLF'),
    a.Detector('Fsmain')
)
print("GOLF 2007-04-23 08:00-16:00 UT:", query_golf_20070423)

# Uncomment the following lines to actually download the data:
# files_golf_20110211 = Fido.fetch(query_golf_20110211)
# files_virgo_20110211 = Fido.fetch(query_virgo_20110211)
# ... and so on for each query variable above.

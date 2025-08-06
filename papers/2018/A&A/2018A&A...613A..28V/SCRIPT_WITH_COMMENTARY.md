# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
#!/usr/bin/env python3
"""
Script to query Jovian electron measurements from VSO using Sunpy.
Instruments and time ranges are based on specific flyby and observational
periods as described in the context.
"""

from sunpy.net import Fido, attrs as a
import astropy.units as u

def main():
    # Query 1: Pioneer 10 CPI measurements on 11 May 1973 (7–17 MeV electron channel)
    pioneer_time = a.Time('1973-05-11 00:00', '1973-05-11 23:59')
    pioneer_instrument = a.Instrument('CPI')
    pioneer_source = a.Source('PIONEER 10')

    print("Querying Pioneer 10 CPI data for 11 May 1973...")
    pioneer_query = Fido.search(pioneer_time, pioneer_instrument, pioneer_source)
    print(pioneer_query)
    # To download data, uncomment the next line:
    # pioneer_files = Fido.fetch(pioneer_query)

    # Query 2: Ulysses COSPIN-KET during first Jupiter encounter (February 1992)
    ulysses_time = a.Time('1992-02-01 00:00', '1992-02-28 23:59')
    ulysses_instrument = a.Instrument('COSPIN-KET')
    ulysses_source = a.Source('Ulysses')

    print("\nQuerying Ulysses COSPIN-KET data for February 1992 (Jupiter encounter)...")
    ulysses_query = Fido.search(ulysses_time, ulysses_instrument, ulysses_source)
    print(ulysses_query)
    # To download data, uncomment the next line:
    # ulysses_files = Fido.fetch(ulysses_query)

    # Query 3: ISEE 3 Chicago Electron Spectrometer in connected intervals (1978–1984)
    isee_source = a.Source('ISEE 3')
    isee_instrument = a.Instrument('Chicago Electron Spectrometer')

    # Interval 1: 1978-11-04 to 1979-04-10
    print("\nQuerying ISEE 3 Chicago data for 1978-11-04 to 1979-04-10...")
    isee_q1 = Fido.search(a.Time('1978-11-04', '1979-04-10'),
                         isee_source, isee_instrument)
    print(isee_q1)
    # To download data, uncomment:
    # isee_files_1 = Fido.fetch(isee_q1)

    # Interval 2: 1979-09-07 to 1980-04-09
    print("\nQuerying ISEE 3 Chicago data for 1979-09-07 to 1980-04-09...")
    isee_q2 = Fido.search(a.Time('1979-09-07', '1980-04-09'),
                         isee_source, isee_instrument)
    print(isee_q2)
    # isee_files_2 = Fido.fetch(isee_q2)

    # Interval 3: 1980-10-26 to 1981-04-20
    print("\nQuerying ISEE 3 Chicago data for 1980-10-26 to 1981-04-20...")
    isee_q3 = Fido.search(a.Time('1980-10-26', '1981-04-20'),
                         isee_source, isee_instrument)
    print(isee_q3)
    # isee_files_3 = Fido.fetch(isee_q3)

    # Interval 4: 1981-10-27 to 1982-06-19
    print("\nQuerying ISEE 3 Chicago data for 1981-10-27 to 1982-06-19...")
    isee_q4 = Fido.search(a.Time('1981-10-27', '1982-06-19'),
                         isee_source, isee_instrument)
    print(isee_q4)
    # isee_files_4 = Fido.fetch(isee_q4)

    # Interval 5: 1982-11-28 to 1983-05-20
    print("\nQuerying ISEE 3 Chicago data for 1982-11-28 to 1983-05-20...")
    isee_q5 = Fido.search(a.Time('1982-11-28', '1983-05-20'),
                         isee_source, isee_instrument)
    print(isee_q5)
    # isee_files_5 = Fido.fetch(isee_q5)

    # Interval 6: 1983-12-06 to 1984-07-18
    print("\nQuerying ISEE 3 Chicago data for 1983-12-06 to 1984-07-18...")
    isee_q6 = Fido.search(a.Time('1983-12-06', '1984-07-18'),
                         isee_source, isee_instrument)
    print(isee_q6)
    # isee_files_6 = Fido.fetch(isee_q6)

if __name__ == "__main__":
    main()
```

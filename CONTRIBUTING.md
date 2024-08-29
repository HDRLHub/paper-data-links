---
layout: default
title: Contributing
---

# Contributing to Paper Data Links

We welcome contributions to Paper Data Links! Here are some guidelines to help you get started.

## Expected Structure

Contributed materials should follow the expected directory structure and file requirements:

- **Directory Structure**: Use the format `papers/year/journal_abbrev/bibcode` (e.g., `papers/2023/ApJ/2023ApJ...943...70S`).
- **Required Files**:
    - `INSTRUMENT_DETAILS.md`: A natural language description of the data sources used.
    - `download_script.py`: The script to download the data.
    - `README.md`: A YAML front matter file containing metadata and paper information.
- **Other Files**:
    - Other files (e.g., `RATIONALE.md`, `SCRIPT_WITH_COMMENTS.md`) are not required. These files are artifacts of our automated pipeline and do not require correction.

Example structure:
```
papers/2023/ApJ/2023ApJ...943...70S/  
│  
├── INSTRUMENT_DETAILS.md  
├── download_script.py  
├── README.md 
```

## Pull Request Actions

We categorize the actions one can take with a new PR as follows:
- **Accept**: If the materials meet the required criteria, merge the PR.
- **Leave**: If the materials have potential but need further work, provide appropriate labels and comments.
- **Reject**: If the paper related to the material is not relevant (ex. is not in heliophysics, does not use VSO data, etc), reject the PR.


## Guidelines for Acceptance

### Instrument Details

- A natural language description of the data sources used.
- Must align with the `download_script.py` but focus more on how the data were used in the context of the study.
- Should provide an overview of each instrument, including its purpose and relevance to the study.
- Must explain how the data from each instrument was utilized in the analysis or findings of the paper.

- **Completeness**: 
  - The document should cover all instruments used in the `download_script.py`.
  - It should describe each instrument's role and the type of data it provides.

- **Accuracy**: 
  - The descriptions must accurately reflect the instruments and their functionalities.
  - Any technical terms should be used correctly.

- **Clarity**: 
  - The explanations should be clear and understandable, avoiding unnecessary jargon.
  - Should be well-organized and logically structured.

- **Alignment with Script**: 
  - The descriptions in `INSTRUMENT_DETAILS.md` must be consistent with the parameters and data sources specified in `download_script.py`.

### Download Script

1. **Required Parameters:**
    - **Time Ranges**: Must be correctly specified.
    - **Instruments**: Must be correctly specified.

2. **Optional Parameters:**
    - **Physical Observables, Wavelengths, Cadences**:
        - It's acceptable if these are omitted.
        - It’s NOT acceptable if they are supplied but incorrect.

3. **Handling Broad Time Ranges:**
    - If the script does not reliably run due to broad time ranges, include a comment in the code explaining why results are unlikely to be returned.
    - Example comment:
    ```
    # WARNING: BROAD TIME RANGE
    # This query may not return results due to fetching too many files.
    # Consider using a shorter time range (e.g., a day or a week) to see results from providers.
    ```

4. **Review Papers:**
    - Generally, ignore scripts for review papers unless they produce a correct script without extensive errors.

5. **Observation Gaps:**
    - Count as correct if the gaps are not mentioned.
    - Need not be accounted for, but nice to have.

- **Commenting in Code:**
    - Provide visible comments or warnings next to time-ranges and other parameters that are likely to result in a script which returns no results.
    - Example: `# Check VSO Health Report for latest assessment on connectivity. https://docs.virtualsolar.org/wiki/VSOHealthReport`

### README.md

The README.md file should contain YAML front matter with the following required keys:

```yaml
---
layout: paper
title: [Paper Title]
bibcode: [NASA/ADS Bibcode]
authors:
  - [Author 1]
  - [Author 2]
  # ... more authors
vso_source_keys:
  [Source Key 1]: [Source Name 1]
  [Source Key 2]: [Source Name 2]
  # ... more sources
vso_instrument_keys:
  [Instrument Key 1]: [Instrument Name 1]
  [Instrument Key 2]: [Instrument Name 2]
  # ... more instrumentsA
year: [Year of Publication]
journal_abbrev: [Journal Abbreviation, (bibstem)]
---
```

All of these keys are required. Ensure that the information is accurate and matches the paper and the data sources used. Also, carefully note that the file MUST start and end with `---`.  

Available VSO sources can be found [here](https://sdac.virtualsolar.org/cgi/show_details?keyword=SOURCE).  
Available VSO instruments can be found [here](https://sdac.virtualsolar.org/cgi/show_details?keyword=INSTRUMENT).  

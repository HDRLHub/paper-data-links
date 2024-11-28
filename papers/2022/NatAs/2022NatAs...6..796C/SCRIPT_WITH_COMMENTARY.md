# This script, including code comments, was initially drafted by an AI model. Please use with caution.

```python
import sunpy.net
from sunpy.net import Fido, attrs as a

# Define the instrument and time ranges based on the context
instrument = a.Instrument('mdi')
time_range_training_validation = a.Time('1996-01-01', '2011-10-31')
time_range_test = a.Time('1996-11-01', '2011-12-31')

# Query for the training and validation set
print("Querying for Training and Validation Set:")
query_training_validation = Fido.search(time_range_training_validation, instrument)
print(query_training_validation)
# Uncomment the following line to fetch the data
# Fido.fetch(query_training_validation)

# Query for the test set
print("Querying for Test Set:")
query_test = Fido.search(time_range_test, instrument)
print(query_test)
# Uncomment the following line to fetch the data
# Fido.fetch(query_test)
```

### Explanation
- **Imports**: We import the necessary modules from Sunpy.
- **Define Parameters**: We define the instrument (`mdi`) and the two time ranges for the training/validation set and the test set.
- **Query for Training and Validation Set**: We use `Fido.search` to query the data for the training and validation set and print the results.
- **Query for Test Set**: Similarly, we query the data for the test set and print the results.
- **Fetch Commands**: The `Fido.fetch` commands are commented out as per the directive.

This script is explicit, well-commented, and directly reflects the data used in the context provided.

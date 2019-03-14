# Fastpandavro
Converts avro file to pandas dataframe in parallel


## Installation Instruction
- Downlowd the repository and Extract to any location
- Go to the folder and run following command
```python setup.py install```

## How to convert Avro file to Pandas dataframe
```
import fastpandavro as fpa
import pandas as pd
df = fpa.avro_to_pandas(fname="test/sample.avro")
print(df.shape)
```

## How to write pandas dataframe to avro file
```
fpa.pandas_to_avro(df, "sample_output.avro", schema_file="test/schema.avsc")
```




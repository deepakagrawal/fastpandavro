# AvroToPandas
Converts avro file to pandas dataframe in parallel


## Installation Instruction
- Downlowd the repository and Extract to any location
- Go to the folder and run following command
```python setup.py install```

## How to convert Avro file to Pandas dataframe
```
import AvroToPandas as atp
import pandas as pd
df = atp.avro_to_pandas(fname="test/sample.avro")
print(df.shape)
```

## How to write pandas dataframe to avro file
```
atp.pandas_to_avro(df, "output.avro", reader_schema="schema")





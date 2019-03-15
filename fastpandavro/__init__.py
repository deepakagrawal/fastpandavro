import itertools
import json
from multiprocessing import cpu_count

from fastavro import writer, block_reader, parse_schema
from joblib import Parallel, delayed
from pandas import DataFrame


def process_block(i):
    return [record for record in i]


def avro_to_pandas(fname, reader_schema=None, num_cores=None):
    """    Converts Avro file to pandas dataframe using parallel processing.
    :param fname: path of avro file to be converted
    :param reader_schema: if schema of avro file is available (optional)
    :param num_cores: Number of processors to use (optional). By default uses all processors available
    :return: Pandas dataframe
    """
    if num_cores is None:
        num_cores = cpu_count()
    with open(fname, 'rb') as fo:
        avro_reader = block_reader(fo, reader_schema)
        results = Parallel(n_jobs=num_cores)(delayed(process_block)(i) for i in avro_reader)
    results = list(itertools.chain.from_iterable(results))
    return DataFrame(results)


def pandas_to_avro(df, fname, schema_file):
    """
    Converts pandas dataframe to avro file
    :param df: Pandas dataframe
    :param fname: path where avro file will be saved
    :param schema_file: schema of the avro file
    :return: Nothing to return
    """
    with open(schema_file) as schema:
        reader_schema = json.load(schema)
    with open(fname, 'wb') as out:
        writer(out, parse_schema(reader_schema), df.to_dict('records'))

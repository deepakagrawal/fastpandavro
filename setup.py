import setuptools

with open("README.md", "r") as fh:
      long_description = fh.read()

setuptools.setup(name='fastpandavro',
                 version='1.1',
                 description='Parallel conversion of Avro file to Pandas dataframe and conversion of pandas dataframe to avro file',
                 url='https://github.com/deepakagrawal/fastpandavro',
                 author='Deepak Agrawal',
                 long_description= long_description,
                 author_email='agrawal.deepankur@gmail.com',
                 packages=setuptools.find_packages(),
                 zip_safe=False,
                 download_url='https://github.com/deepakagrawal/fastpandavro/archive/v1.1.tar.gz',
                 classifiers=[
                       "Programming Language :: Python :: 3",
                       "License :: OSI Approved :: MIT License",
                       "Operating System :: OS Independent",
                 ],
                 python_requires = '>=3.6',
                 install_requires=['fastavro', 'joblib'])

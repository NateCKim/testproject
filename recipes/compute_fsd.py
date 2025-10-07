# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
yy = dataiku.Dataset("yy")
yy_df = yy.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

fsd_df = yy_df # For this sample code, simply copy input to output


# Write recipe outputs
fsd = dataiku.Dataset("fsd")
fsd.write_with_schema(fsd_df)

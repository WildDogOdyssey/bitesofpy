import pandas as pd
from functools import lru_cache


XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = _make_df(XYZ)
    df['Dollar Flux'] = df['12/31/20'] - df['12/31/19']
    df['Percentage'] = df['Dollar Flux'] / df['12/31/19']

    return [tuple(df.iloc[row, :]) for row in range(df.shape[0])]


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    return [line for line in calculate_flux(XYZ)
                     if all([abs(line[-2]) > THRESHOLDS[0], abs(line[-1]) > THRESHOLDS[1]])]

@lru_cache()
def _make_df(XYZ: str):
    """Helper function to convert string to data frame and cache for
    better retrieval
    """
    return pd.read_csv(XYZ)

# print(_make_df(XYZ))
# print(calculate_flux(XYZ))
# print(identify_flux(XYZ))
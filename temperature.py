# This module processes the input file given its filename.
import pandas as pd
def readData(filename):
    """
    Gather data from the input file.
    Use a data structure that will help you analyze and report the data.
    """
    #defining gobal variable (dataframe) to access it outside this function
    global dataframe
    #storing full CSV file into a dataframe(data structure)
    dataframe = pd.read_csv(filename)
    #type casting temperature column of dataframe to numeric data and ignoring '***' values
    dataframe['Temperature'] = pd.to_numeric(dataframe['Temperature'], errors='coerce')
    return dataframe

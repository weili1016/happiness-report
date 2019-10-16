import pandas as pd
import numpy as np
happinessDF = pd.read_csv("world-happiness-report-2019.csv")
print(happinessDF)
print(happinessDF.info())
colNameDict = {'Country(region)':'Country',
                'SD of Ladder':'SD_ladder',
               'Positive affect':'Positive_affect',
               'Negative affect':'Negative_affect',
               'Social support':'Social_support',
               'Log of GDP\nper capita':'Log_of_GDP',
               'Healthy life\nexpectancy':'Healthy_life'}
happinessDF.rename(columns=colNameDict,inplace=True)
print(happinessDF.head())
happinessDF.isnull().sum().sort_values(ascending=False)
happinessDF_new = happinessDF.dropna(axis=0,how='any',thresh=None,subset=None,inplace=False)
print(happinessDF_new)

happinessDF_new.to_csv('new-happiness-2019.csv')
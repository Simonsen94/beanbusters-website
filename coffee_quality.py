# 1. import data tools to manipulate and visualize the data
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
# 2. import Machine Learning tools
from sklearn import svm
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#-------------------------------------- Data understanding & collection -----------------------------------------------------

# 3. Pulling data from Github and storing in a variable
url = 'https://github.com/jldbc/coffee-quality-database/raw/master/data/arabica_data_cleaned.csv' 

# 4. Creating dataframe and reading csv file from 0 column
dfraw = pd.read_csv(url, index_col=0)

dfclean = dfraw[['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Balance', 'Total.Cup.Points']].copy()

#---------------------------------------- Data pre-processing & analysis -----------------------------------------------------

# Defining what is great, decent and poor coffee in 3 bins with respective labels.

# coffee >= 85 is great, coffee >= 82 & <85, coffee < 82 is poor
bins = [-1, 82, 85, 100]
labels = ['poor', 'decent', 'great']
dfclean['greatCoffee'] = pd.cut(dfclean['Total.Cup.Points'], bins = bins, labels = labels)
dfclean = dfclean.drop(columns=['Total.Cup.Points'])
dfclean['greatCoffee'].unique()

# testing if coffee's are divided properly in bins based on labels.
dfclean['greatCoffee'].value_counts()

# replacing previous labels of 'great', 'decent' and 'poor' coffee with 0, 1 & 2.
encoder = LabelEncoder()
dfclean['greatCoffee'] = encoder.fit_transform(dfclean['greatCoffee'])

# Converting df to csv format and storing locally
dfclean.to_csv('C:/Users/soere/OneDrive/Documents/Visual Studio 2017/files/coffee_project/coffeeQualityFile.csv')
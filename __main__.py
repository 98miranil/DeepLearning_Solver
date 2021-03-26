#Imports
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

#Other python files
sys.path.insert(1, r"C:\MSI\projectes\Python\MachineLearning\DeepLearning_Solver\lib")
import standarize

#MAIN PROGRAM
"""
----------------------------------------------------------------
"""

"""
GET THE DATASET and prepare it
TO SUBTITUTE
path = input("Enter the path of the dataset: \n")
filename = input("Enter the name of the dataset: \n")
#Load the dataset
dataset = pd.read_csv(path + filename, sep = ",", header=None) #TENIR EN COMPTE A PREGUNTAR TOTS AQUESTS PARÀMETRES
"""
dataset = pd.read_csv(r"C:\MSI\projectes\Python\MachineLearning\NeuralNetwork\pima-indians-diabetes.data.csv", sep = ",", header=None)
X = dataset.iloc[:,0:(len(dataset.columns)-1)]
y = dataset.iloc[:,(len(dataset.columns)-1):(len(dataset.columns))]
#Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

"""
SCALAR DECISION
"""
scalar_decision = input("Do you want to scale the data [Y/N]? \n")
if(scalar_decision == "Y"):
    X_train, X_test = standarize.scale_data(X_train,X_test)



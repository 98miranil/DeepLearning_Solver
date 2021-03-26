#Scalar the data

from sklearn.preprocessing import StandardScaler

def scale_data(X_train, X_test):
    # Define the scaler 
    scaler = StandardScaler().fit(X_train)

    # Scale the train set
    X_train = scaler.transform(X_train)

    # Scale the test set
    X_test = scaler.transform(X_test)

    return X_train, X_test
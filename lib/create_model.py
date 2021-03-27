#Create the model

from keras.models import Sequential
from keras.layers import Dense

def define_manual_model(attributes): #ATTRIBUTES IS THE LENGHT OF COLUMNS-1, WE DONT WANT THE OUTPUT
    model = Sequential()
    num_layers = input("How many layers do you want (INCLUDING ENTRANCE LAYER)? \n")
    for i in range(int(num_layers)-1):
        if i == 0:
            nodes = int(input(f"How many nodes do you want on the layer {i+1} (FIRST HIDDEN LAYER)? \n"))
            activation_func = input(f"Which activation function do you want on layer {i+1} (relu, sigmoid, tanh)? \n")
            model.add(Dense(nodes, activation = activation_func, input_dim=attributes))
        elif i == (int(num_layers)-2):
            nodes = int(input(f"How many nodes do you want on the output layer? \n"))
            activation_func = input(f"Which activation function do you want on the output (linear, sigmoid, softmax)? \n")
            model.add(Dense(nodes, activation = activation_func))
        else:
            nodes = int(input(f"How many nodes do you want on the layer {i+1}? \n"))
            activation_func = input(f"Which activation function do you want on layer {i+1} (relu, sigmoid, tanh)? \n")
            model.add(Dense(nodes, activation = activation_func))
    return model

def read_model(model):
    print("\n\n")
    model.summary()
    print("\n\n")

def compile_manual_model(model):
    print("Which loss function do you want to use: \n 1. Mean Squared Error \n 2. Mean Squared Logarithmic Error \n 3. Mean Absolute Error \n-------------------------------------\n 4. Binary Cross-Entropy \n 5. Hinge \n 6. Squared Hinge \n-------------------------------------\n 7. Categorical Cross-Entropy \n 8. Sparse Categorical Cross-Entropy \n 9. Kullback Leibler Divergence")
    lf = int(input())
    if lf == 1:
        lf = "mean_squared_error"
    elif lf == 2:
        lf = "mean_squared_logarithmic_error"
    elif lf == 3:
        lf = "mean_absolute_error"
    elif lf == 4:
        lf = "binary_crossentropy"
    elif lf == 5:
        lf = "hinge"
    elif lf == 6:
        lf = "squared_hinge"
    elif lf == 7:
        lf = "categorical_crossentropy"
    elif lf == 8:
        lf = "sparse_categorical_crossentropy"
    else:
        lf = "kullback_leibler_divergence"
    
    opt = input("Which optimizer do you want to use (SGD, adam)? \n")

    model.compile(loss=lf,
              optimizer=opt,
              metrics=['accuracy'])

def fit_model(model, X_train, y_train):
    epochs = int(input("How many epochs do you want? \n"))
    batch = int(input("Which batch size do you want? \n"))
    model.fit(X_train, y_train,epochs=epochs, batch_size=batch, verbose=0)

def save_model(model):
    name_model = input("Name of the model saved: ")
    model.save(name_model+".h5")
    print("Model saved to disk")




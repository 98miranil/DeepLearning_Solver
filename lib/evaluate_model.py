#EVALUATION OF THE MODEL

def evaluate_model(model, X_test, y_test):
    _, score = model.evaluate(X_test, y_test, verbose = 0)
    print(score)

def predict_model(model, X):
    y = model.predict(X)
    print(y)

def predict_class_model(model, X):
    y = model.predict_classes(X)
    print(y)
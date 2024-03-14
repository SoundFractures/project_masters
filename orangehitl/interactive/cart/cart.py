from sklearn.tree import DecisionTreeClassifier


def train_cart_model(X, y):
    """
    Trains a CART (Classification and Regression Trees) model using the input data and target labels.

    Parameters:
    - X (array-like): Input features (training data).
    - y (array-like): Target labels.

    Returns:
    - model: Trained CART model.
    """
    # Initialize the CART classifier
    cart_model = DecisionTreeClassifier()

    # Train the model
    cart_model.fit(X, y)

    return cart_model

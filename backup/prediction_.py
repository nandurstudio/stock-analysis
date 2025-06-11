def predict_stock_price(data):
    """
    Predict stock prices using a simple linear regression model.
    
    Parameters:
    data (DataFrame): A pandas DataFrame containing stock data with 'Date' and 'Close' columns.

    Returns:
    DataFrame: A DataFrame with predicted stock prices.
    """
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    import pandas as pd

    # Prepare the data
    data['Date'] = pd.to_datetime(data['Date'])
    data['Date'] = data['Date'].map(pd.Timestamp.timestamp)
    X = data[['Date']]
    y = data['Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Create a DataFrame for the results
    results = pd.DataFrame({'Date': X_test['Date'], 'Predicted_Close': predictions})
    results['Date'] = pd.to_datetime(results['Date'], unit='s')

    return results.sort_values('Date')
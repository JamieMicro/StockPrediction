# StockPrediction
Project that uses a Neural Network developed with TensorFlow to predict stocks 

This model is trained to predict bullish stock price movements of 1% or greater. So the idea is that if the model predicts a "1" or true, the stock price should increase by at least 1% the following day.


DataCaptureHistorical.py - Downloads historical market data used for training the model

DataCaptureDaily.py - Downloads daily market data for making predictions

TrainModelAndPredict.py - Trains the model and makes predictions
